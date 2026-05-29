#!/usr/bin/env python3
"""
vibe-glossary translate — 领域术语翻译工具

用法:
    python translate.py "你这个后端交互逻辑应该是解耦的"
    python translate.py "我们需要做 MVP 验证" --from product --to software-engineering
    python translate.py "CI/CD 挂了" --lang zh
    python translate.py --interactive
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
DOMAINS_DIR = ROOT / "domains"
CONFIG_DIR = ROOT / "config"


def load_terms(domain: str) -> list[dict]:
    """加载指定领域的所有术语"""
    terms_file = DOMAINS_DIR / domain / "terms.json"
    if not terms_file.exists():
        print(f"错误: 领域 '{domain}' 不存在 ({terms_file})", file=sys.stderr)
        sys.exit(1)
    with open(terms_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("terms", [])


def load_all_terms() -> dict[str, list[dict]]:
    """加载所有领域的术语"""
    all_terms = {}
    for domain_dir in DOMAINS_DIR.iterdir():
        if domain_dir.is_dir():
            terms_file = domain_dir / "terms.json"
            if terms_file.exists():
                with open(terms_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                all_terms[domain_dir.name] = data.get("terms", [])
    return all_terms


def load_primary_domain() -> dict:
    """加载主领域配置"""
    config_file = CONFIG_DIR / "primary-domain.json"
    if config_file.exists():
        with open(config_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"primary": "software-engineering", "fallback": "natural-language"}


def _build_search_index(terms: list[dict]) -> list[tuple[str, dict, int]]:
    """构建搜索索引：(关键词, 术语数据, 关键词长度)，按长度降序排列避免子串误匹配"""
    index = []
    for term_data in terms:
        # 主术语
        index.append((term_data["term"], term_data, len(term_data["term"])))
        # 别名
        for alias in term_data.get("aliases", []):
            index.append((alias, term_data, len(alias)))
    # 按长度降序，优先匹配更长的术语
    index.sort(key=lambda x: -x[2])
    return index


def match_terms_in_text(text: str, terms: list[dict]) -> list[dict]:
    """
    在文本中匹配术语，返回匹配结果列表，每个包含:
    - term_data: 术语数据
    - matched_text: 在原文中匹配到的文本
    - start: 起始位置
    - end: 结束位置
    """
    index = _build_search_index(terms)
    results = []
    used_ranges = []  # 已匹配的范围，避免重叠

    for keyword, term_data, kw_len in index:
        # 在文本中搜索所有出现位置
        search_text = text.lower()
        keyword_lower = keyword.lower()
        pos = 0
        while True:
            idx = search_text.find(keyword_lower, pos)
            if idx == -1:
                break
            end = idx + kw_len

            # 检查是否与已有匹配重叠
            overlaps = False
            for (us, ue) in used_ranges:
                if idx < ue and end > us:
                    overlaps = True
                    break

            if not overlaps:
                results.append({
                    "term_data": term_data,
                    "matched_text": text[idx:end],
                    "start": idx,
                    "end": end,
                })
                used_ranges.append((idx, end))

            pos = idx + 1

    # 按位置排序
    results.sort(key=lambda r: r["start"])
    return results


def get_term_label(term_data: dict, lang: str = "en") -> str:
    """获取术语的翻译标签（用于替换）"""
    if lang == "en":
        return term_data["term"]
    elif lang == "zh":
        return term_data["definition"].get("zh", term_data["term"])
    return term_data["term"]


def build_translated_sentence(text: str, matches: list[dict], target_lang: str) -> str:
    """在整句中将匹配的术语替换为目标语言版本"""
    if not matches:
        return text

    result = []
    last_end = 0

    for m in matches:
        start, end = m["start"], m["end"]
        # 添加匹配前的原文
        result.append(text[last_end:start])
        # 添加翻译后的术语（用 → 标注）
        label = get_term_label(m["term_data"], target_lang)
        result.append(label)
        last_end = end

    # 添加剩余原文
    result.append(text[last_end:])
    return "".join(result)


def build_annotated_sentence(text: str, matches: list[dict], target_lang: str) -> str:
    """构建带注释的翻译句子：原文术语 → 目标语言术语"""
    if not matches:
        return text

    result = []
    last_end = 0

    for m in matches:
        start, end = m["start"], m["end"]
        # 添加匹配前的原文
        result.append(text[last_end:start])
        # 添加带注释的术语
        original = m["matched_text"]
        translated = get_term_label(m["term_data"], target_lang)
        if original.lower() != translated.lower():
            result.append(f"{original} → {translated}")
        else:
            result.append(original)
        last_end = end

    # 添加剩余原文
    result.append(text[last_end:])
    return "".join(result)


def format_translation(text: str, matches: list[dict], source_domain: str,
                       target_domain: str, target_lang: str) -> str:
    """格式化完整的翻译输出"""
    if not matches:
        return f"原文: {text}\n\n⚠️  未在 '{source_domain}' 领域中找到匹配的术语。"

    lines = []

    # 1. 翻译后的句子
    translated = build_translated_sentence(text, matches, target_lang)
    lines.append(f"翻译: {translated}")
    lines.append("")

    # 2. 带注释的版本
    annotated = build_annotated_sentence(text, matches, target_lang)
    lines.append(f"注释: {annotated}")
    lines.append("")

    # 3. 术语详解
    lines.append("─── 术语详解 ───")
    for m in matches:
        td = m["term_data"]
        term = td["term"]
        zh_def = td["definition"].get("zh", "")
        en_def = td["definition"].get("en", "")
        hint = td.get("model_hints", {}).get("prompt_fragment", "")

        lines.append(f"  {term}")
        if zh_def:
            lines.append(f"    中文: {zh_def}")
        if en_def:
            lines.append(f"    英文: {en_def}")
        if hint:
            lines.append(f"    提示: {hint}")

        # 示例
        examples = td.get("examples", [])
        if examples:
            ex = examples[0]
            lines.append(f"    示例: \"{ex['context']}\" → {ex['meaning']}")

        lines.append("")

    return "\n".join(lines)


def translate_text(text: str, source_domain: str, target_domain: str,
                   output_lang: str = "en", all_domains: bool = False) -> str:
    """翻译文本中的术语"""
    if all_domains:
        # 在所有领域中匹配
        all_terms_data = load_all_terms()
        all_matches = []
        seen_terms = set()
        for domain_name, terms in all_terms_data.items():
            matches = match_terms_in_text(text, terms)
            for m in matches:
                term_key = m["term_data"]["term"]
                if term_key not in seen_terms:
                    seen_terms.add(term_key)
                    m["source_domain"] = domain_name
                    all_matches.append(m)
        all_matches.sort(key=lambda r: r["start"])
        return format_translation(text, all_matches, "all", target_domain, output_lang)
    else:
        source_terms = load_terms(source_domain)
        matches = match_terms_in_text(text, source_terms)
        return format_translation(text, matches, source_domain, target_domain, output_lang)


def interactive_mode():
    """交互模式"""
    print("╔══════════════════════════════════════╗")
    print("║   vibe-glossary 交互翻译模式        ║")
    print("║   输入 'quit' 退出                  ║")
    print("╚══════════════════════════════════════╝")
    print()

    config = load_primary_domain()
    primary = config.get("primary", "software-engineering")
    fallback = config.get("fallback", "natural-language")

    print(f"主领域: {primary}  |  Fallback: {fallback}")
    print(f"提示: 输入 /all 可切换为全领域匹配模式")
    print()

    all_domains = False

    while True:
        try:
            text = input("📝 ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n再见！")
            break

        if text.lower() in ("quit", "exit", "q"):
            print("再见！")
            break

        if text == "/all":
            all_domains = not all_domains
            state = "开启" if all_domains else "关闭"
            print(f"  全领域匹配模式: {state}")
            print()
            continue

        if not text:
            continue

        result = translate_text(text, primary, fallback, all_domains=all_domains)
        print()
        print(result)
        print("─" * 50)


def main():
    parser = argparse.ArgumentParser(
        description="vibe-glossary 领域术语翻译工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python translate.py "你这个后端交互逻辑应该是解耦的"
  python translate.py "我们需要做 MVP 验证" --from product
  python translate.py --all "加个缓存优化一下转化率"
  python translate.py --interactive
        """
    )
    parser.add_argument("text", nargs="?", help="要翻译的文本")
    parser.add_argument("--from", dest="source", help="源领域 (默认: primary-domain.json)")
    parser.add_argument("--to", dest="target", help="目标领域 (默认: primary-domain.json)")
    parser.add_argument("--lang", default="en", choices=["en", "zh"],
                        help="目标语言 (默认: en)")
    parser.add_argument("--all", action="store_true",
                        help="在所有领域中匹配术语")
    parser.add_argument("--interactive", "-i", action="store_true",
                        help="交互模式")
    parser.add_argument("--list-domains", action="store_true",
                        help="列出所有可用领域")
    parser.add_argument("--list-terms", help="列出指定领域的所有术语")

    args = parser.parse_args()

    if args.list_domains:
        print("可用领域:")
        for domain_dir in sorted(DOMAINS_DIR.iterdir()):
            if domain_dir.is_dir():
                terms_file = domain_dir / "terms.json"
                if terms_file.exists():
                    with open(terms_file, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    count = len(data.get("terms", []))
                    print(f"  {domain_dir.name} ({count} 个术语)")
        return

    if args.list_terms:
        terms = load_terms(args.list_terms)
        print(f"{args.list_terms} 领域的术语:")
        for term in terms:
            aliases = ", ".join(term.get("aliases", []))
            print(f"  {term['term']}")
            if aliases:
                print(f"    别名: {aliases}")
            print(f"    定义: {term['definition'].get('zh', term['definition'].get('en', ''))}")
            print()
        return

    if args.interactive:
        interactive_mode()
        return

    if not args.text:
        parser.print_help()
        sys.exit(1)

    config = load_primary_domain()
    source = args.source or config.get("primary", "software-engineering")
    target = args.target or config.get("fallback", "natural-language")

    result = translate_text(args.text, source, target, args.lang, args.all)
    print(result)


if __name__ == "__main__":
    main()
