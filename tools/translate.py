#!/usr/bin/env python3
"""
vibe-glossary translate — 跨领域术语翻译工具

核心功能：将一个领域视角的描述，翻译成另一个领域的术语体系。

用法:
    python translate.py --from product --to software-engineering "先做 MVP 验证痛点，用 AB 测试看转化率"
    python translate.py --from software-engineering --to product "需要解耦，加个熔断和限流"
    python translate.py --from product --to natural-language "用户留存太低，需要优化新手引导"
"""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
DOMAINS_DIR = ROOT / "domains"
CONFIG_DIR = ROOT / "config"


def load_terms(domain: str) -> dict[str, dict]:
    """加载指定领域的所有术语，返回 {term_name: term_data} 的字典"""
    terms_file = DOMAINS_DIR / domain / "terms.json"
    if not terms_file.exists():
        print(f"错误: 领域 '{domain}' 不存在 ({terms_file})", file=sys.stderr)
        sys.exit(1)
    with open(terms_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    result = {}
    for t in data.get("terms", []):
        result[t["term"]] = t
    return result


def load_all_terms() -> dict[str, dict[str, dict]]:
    """加载所有领域的术语"""
    all_terms = {}
    for domain_dir in DOMAINS_DIR.iterdir():
        if domain_dir.is_dir():
            terms_file = domain_dir / "terms.json"
            if terms_file.exists():
                with open(terms_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                domain_terms = {}
                for t in data.get("terms", []):
                    domain_terms[t["term"]] = t
                all_terms[domain_dir.name] = domain_terms
    return all_terms


def load_primary_domain() -> dict:
    config_file = CONFIG_DIR / "primary-domain.json"
    if config_file.exists():
        with open(config_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"primary": "software-engineering", "fallback": "natural-language"}


def build_search_index(terms: dict[str, dict]) -> list[tuple[str, str, int]]:
    """构建搜索索引：(关键词, 术语名, 关键词长度)，按长度降序"""
    index = []
    for term_name, term_data in terms.items():
        index.append((term_name, term_name, len(term_name)))
        for alias in term_data.get("aliases", []):
            index.append((alias, term_name, len(alias)))
    index.sort(key=lambda x: -x[2])
    return index


def match_terms(text: str, terms: dict[str, dict]) -> list[dict]:
    """在文本中匹配术语，返回匹配结果"""
    index = build_search_index(terms)
    results = []
    used_ranges = []

    for keyword, term_name, kw_len in index:
        search_text = text.lower()
        keyword_lower = keyword.lower()
        pos = 0
        while True:
            idx = search_text.find(keyword_lower, pos)
            if idx == -1:
                break
            end = idx + kw_len

            overlaps = any(idx < ue and end > us for us, ue in used_ranges)
            if not overlaps:
                results.append({
                    "term_name": term_name,
                    "term_data": terms[term_name],
                    "matched_text": text[idx:end],
                    "start": idx,
                    "end": end,
                })
                used_ranges.append((idx, end))

            pos = idx + 1

    results.sort(key=lambda r: r["start"])
    return results


def find_target_mapping(source_term: dict, target_terms: dict[str, dict],
                        target_domain: str) -> list[dict] | None:
    """
    为源领域术语找到目标领域的对应术语。
    优先通过 cross_domain 字段显式映射，其次通过 related 字段模糊匹配。
    返回: [{"term": term_data, "note": "映射说明"}, ...] 或 None
    """
    # 方法1: 通过 cross_domain 显式映射（最可靠）
    cross_domain = source_term.get("cross_domain", {})
    if target_domain in cross_domain:
        mappings = cross_domain[target_domain]
        result = []
        for m in mappings:
            term_name = m["term"]
            if term_name in target_terms:
                result.append({
                    "term": target_terms[term_name],
                    "note": m.get("note", ""),
                })
        if result:
            return result

    # 方法2: 通过 related 字段匹配（模糊）
    related = source_term.get("related", [])
    result = []
    seen = set()

    for rel in related:
        rel_name = rel.split("/")[-1] if "/" in rel else rel
        # 精确匹配
        if rel_name in target_terms and rel_name not in seen:
            seen.add(rel_name)
            result.append({"term": target_terms[rel_name], "note": ""})
        else:
            # 别名匹配
            for target_name, target_data in target_terms.items():
                aliases = [a.lower() for a in target_data.get("aliases", [])]
                if (rel_name.lower() in aliases or rel_name.lower() == target_name.lower()) and target_name not in seen:
                    seen.add(target_name)
                    result.append({"term": target_data, "note": ""})
                    break

    return result if result else None


def cross_domain_translate(text: str, source_domain: str, target_domain: str) -> dict:
    """
    跨领域翻译。

    返回:
    {
        "translated": "翻译后的句子",
        "mappings": [{"source": ..., "target": ..., "original": ...}, ...],
        "unmapped": ["未找到映射的术语", ...]
    }
    """
    all_terms = load_all_terms()

    if source_domain not in all_terms:
        print(f"错误: 源领域 '{source_domain}' 不存在", file=sys.stderr)
        sys.exit(1)
    if target_domain not in all_terms:
        print(f"错误: 目标领域 '{target_domain}' 不存在", file=sys.stderr)
        sys.exit(1)

    source_terms = all_terms[source_domain]
    target_terms = all_terms[target_domain]

    # 在文本中匹配源领域术语
    matches = match_terms(text, source_terms)

    # 为每个匹配找目标领域映射
    mappings = []
    unmapped = []
    for m in matches:
        source_name = m["term_name"]
        source_data = m["term_data"]
        target_mapping = find_target_mapping(source_data, target_terms, target_domain)

        if target_mapping:
            # 取第一个映射作为主要替换
            primary = target_mapping[0]
            mappings.append({
                "source": source_data,
                "target": primary["term"],
                "target_note": primary.get("note", ""),
                "all_targets": target_mapping,  # 保留所有映射
                "original": m["matched_text"],
                "start": m["start"],
                "end": m["end"],
            })
        else:
            unmapped.append(source_name)

    # 构建翻译后的句子
    translated = _build_translated_sentence(text, mappings)

    return {
        "translated": translated,
        "mappings": mappings,
        "unmapped": unmapped,
    }


def _build_translated_sentence(text: str, mappings: list[dict]) -> str:
    """用目标领域术语替换源领域术语，构建翻译后的句子"""
    if not mappings:
        return text

    result = []
    last_end = 0

    for m in mappings:
        start, end = m["start"], m["end"]
        result.append(text[last_end:start])

        # 用目标术语替换
        target_name = m["target"]["term"]
        result.append(target_name)
        last_end = end

    result.append(text[last_end:])
    return "".join(result)


def format_output(text: str, source_domain: str, target_domain: str, result: dict) -> str:
    """格式化翻译输出"""
    lines = []

    lines.append(f"{'═' * 50}")
    lines.append(f"  {source_domain} → {target_domain}")
    lines.append(f"{'═' * 50}")
    lines.append("")
    lines.append(f"原文: {text}")
    lines.append(f"翻译: {result['translated']}")
    lines.append("")

    if result["mappings"]:
        lines.append("─── 术语映射 ───")
        for m in result["mappings"]:
            src = m["source"]
            tgt = m["target"]
            note = m.get("target_note", "")
            all_targets = m.get("all_targets", [])

            lines.append(f"  {src['term']}  →  {tgt['term']}")

            # 映射说明
            if note:
                lines.append(f"    📌 {note}")

            # 源术语解释（一句话）
            src_zh = src["definition"].get("zh", "")
            if src_zh:
                lines.append(f"    [{src_zh}]")

            # 目标术语解释
            tgt_zh = tgt["definition"].get("zh", "")
            tgt_en = tgt["definition"].get("en", "")
            if tgt_zh:
                lines.append(f"    → {tgt_zh}")

            # 提示
            hint = tgt.get("model_hints", {}).get("prompt_fragment", "")
            if hint:
                lines.append(f"    💡 {hint}")

            # 如果有多个映射，显示其他选项
            if len(all_targets) > 1:
                others = [t["term"]["term"] for t in all_targets[1:]]
                lines.append(f"    也可映射为: {', '.join(others)}")

            lines.append("")

    if result["unmapped"]:
        lines.append("─── 未找到映射 ───")
        for name in result["unmapped"]:
            lines.append(f"  ⚠ {name} — 在 {target_domain} 中没有直接对应")
        lines.append("")

    return "\n".join(lines)


def interactive_mode():
    """交互模式"""
    print("╔══════════════════════════════════════════════╗")
    print("║   vibe-glossary 跨领域翻译模式              ║")
    print("║   输入 'quit' 退出                          ║")
    print("╚══════════════════════════════════════════════╝")
    print()

    config = load_primary_domain()
    primary = config.get("primary", "software-engineering")
    fallback = config.get("fallback", "natural-language")

    print(f"默认: {primary} → {fallback}")
    print(f"提示: /from product /to engineering 可切换方向")
    print()

    source = primary
    target = fallback

    while True:
        try:
            text = input("📝 ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n再见！")
            break

        if text.lower() in ("quit", "exit", "q"):
            print("再见！")
            break

        if text.startswith("/from"):
            parts = text.split()
            if len(parts) >= 2:
                source = parts[1]
                print(f"  源领域: {source}")
            continue

        if text.startswith("/to"):
            parts = text.split()
            if len(parts) >= 2:
                target = parts[1]
                print(f"  目标领域: {target}")
            continue

        if not text:
            continue

        result = cross_domain_translate(text, source, target)
        print()
        print(format_output(text, source, target, result))
        print("─" * 50)


def main():
    parser = argparse.ArgumentParser(
        description="vibe-glossary 跨领域术语翻译工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python translate.py --from product --to software-engineering "先做 MVP 验证痛点"
  python translate.py --from software-engineering --to product "需要解耦，加个熔断"
  python translate.py --from product --to natural-language "用户留存太低"
  python translate.py --interactive
        """
    )
    parser.add_argument("text", nargs="?", help="要翻译的文本")
    parser.add_argument("--from", dest="source", help="源领域")
    parser.add_argument("--to", dest="target", help="目标领域")
    parser.add_argument("--interactive", "-i", action="store_true", help="交互模式")
    parser.add_argument("--list-domains", action="store_true", help="列出所有可用领域")
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
        for term_name, term_data in terms.items():
            aliases = ", ".join(term_data.get("aliases", []))
            print(f"  {term_name}")
            if aliases:
                print(f"    别名: {aliases}")
            print(f"    定义: {term_data['definition'].get('zh', term_data['definition'].get('en', ''))}")
            related = term_data.get("related", [])
            if related:
                print(f"    关联: {', '.join(related)}")
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

    result = cross_domain_translate(args.text, source, target)
    print(format_output(args.text, source, target, result))


if __name__ == "__main__":
    main()
