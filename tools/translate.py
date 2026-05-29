#!/usr/bin/env python3
"""
vibe-glossary translate — 领域术语翻译工具

用法:
    python translate.py "这个接口延迟太高了" --from software-engineering --to natural-language
    python translate.py "我们需要做 MVP 验证" --from product --to software-engineering
    python translate.py "CI/CD 挂了" --lang zh
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

# 项目根目录
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


def find_matching_terms(text: str, terms: list[dict]) -> list[dict]:
    """在文本中匹配术语（精确匹配 term 和 aliases）"""
    matches = []
    text_lower = text.lower()

    for term_data in terms:
        # 检查主术语
        if term_data["term"].lower() in text_lower:
            matches.append(term_data)
            continue

        # 检查别名
        for alias in term_data.get("aliases", []):
            if alias.lower() in text_lower:
                matches.append(term_data)
                break

    return matches


def get_translation(term_data: dict, target_lang: str) -> str:
    """获取术语的翻译"""
    definition = term_data.get("definition", {})
    if target_lang in definition:
        return definition[target_lang]
    # fallback 到英文
    return definition.get("en", term_data["term"])


def get_hint(term_data: dict) -> str:
    """获取术语的模型提示"""
    hints = term_data.get("model_hints", {})
    return hints.get("prompt_fragment", "")


def translate_text(text: str, source_domain: str, target_domain: str, output_lang: str = "en") -> str:
    """翻译文本中的术语"""
    # 加载源领域和目标领域的术语
    source_terms = load_terms(source_domain)
    target_terms = load_terms(target_domain)

    # 在源领域中匹配术语
    matches = find_matching_terms(text, source_terms)

    if not matches:
        return f"未在 '{source_domain}' 领域中找到匹配的术语。\n原文: {text}"

    # 构建翻译结果
    result_parts = []
    result_parts.append(f"原文: {text}")
    result_parts.append(f"领域: {source_domain} → {target_domain}")
    result_parts.append("")

    for match in matches:
        term = match["term"]
        definition_zh = match["definition"].get("zh", "")
        definition_en = match["definition"].get("en", "")
        hint = get_hint(match)

        result_parts.append(f"  术语: {term}")
        if definition_zh:
            result_parts.append(f"  中文: {definition_zh}")
        if definition_en:
            result_parts.append(f"  英文: {definition_en}")
        if hint:
            result_parts.append(f"  提示: {hint}")

        # 查找目标领域中的关联术语
        related = match.get("related", [])
        cross_domain_related = []
        for rel in related:
            for target_term in target_terms:
                if rel.lower() == target_term["term"].lower() or rel in target_term.get("aliases", []):
                    cross_domain_related.append(target_term)
                    break

        if cross_domain_related:
            result_parts.append(f"  关联 ({target_domain}):")
            for related_term in cross_domain_related:
                result_parts.append(f"    - {related_term['term']}: {get_translation(related_term, output_lang)}")

        result_parts.append("")

    return "\n".join(result_parts)


def interactive_mode():
    """交互模式"""
    print("vibe-glossary 交互翻译模式")
    print("输入 'quit' 或 'exit' 退出")
    print()

    config = load_primary_domain()
    primary = config.get("primary", "software-engineering")
    fallback = config.get("fallback", "natural-language")

    print(f"主领域: {primary}")
    print(f"Fallback: {fallback}")
    print()

    while True:
        try:
            text = input("请输入要翻译的内容: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n再见！")
            break

        if text.lower() in ("quit", "exit", "q"):
            print("再见！")
            break

        if not text:
            continue

        # 尝试在主领域中匹配
        result = translate_text(text, primary, fallback)
        print()
        print(result)
        print("-" * 50)


def main():
    parser = argparse.ArgumentParser(
        description="vibe-glossary 领域术语翻译工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python translate.py "这个接口延迟太高了" --from software-engineering --to natural-language
  python translate.py "我们需要做 MVP 验证" --from product --to software-engineering
  python translate.py --interactive
        """
    )
    parser.add_argument("text", nargs="?", help="要翻译的文本")
    parser.add_argument("--from", dest="source", help="源领域 (默认: 使用 primary-domain.json)")
    parser.add_argument("--to", dest="target", help="目标领域 (默认: 使用 primary-domain.json)")
    parser.add_argument("--lang", default="en", choices=["en", "zh"], help="输出语言 (默认: en)")
    parser.add_argument("--interactive", "-i", action="store_true", help="交互模式")
    parser.add_argument("--list-domains", action="store_true", help="列出所有可用领域")
    parser.add_argument("--list-terms", help="列出指定领域的所有术语")

    args = parser.parse_args()

    # 列出领域
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

    # 列出术语
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

    # 交互模式
    if args.interactive:
        interactive_mode()
        return

    # 翻译模式
    if not args.text:
        parser.print_help()
        sys.exit(1)

    config = load_primary_domain()
    source = args.source or config.get("primary", "software-engineering")
    target = args.target or config.get("fallback", "natural-language")

    result = translate_text(args.text, source, target, args.lang)
    print(result)


if __name__ == "__main__":
    main()
