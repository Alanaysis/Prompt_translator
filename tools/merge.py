#!/usr/bin/env python3
"""
vibe-glossary merge — Obsidian 合并工具

功能:
  generate  - 从 terms.json 生成 Obsidian 兼容的 markdown 文件（含 wiki-links）
  map       - 生成跨领域映射文档
  inject    - 将术语注入到项目文档中（添加 wiki-link）

用法:
  python merge.py generate                         # 生成 Obsidian 文件到 output/
  python merge.py map product software-engineering  # 生成跨领域映射
  python merge.py inject /path/to/project           # 注入到项目文档
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
DOMAINS_DIR = ROOT / "domains"
OUTPUT_DIR = ROOT / "output"


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


def term_to_filename(term_name: str) -> str:
    """将术语名转为文件名"""
    # 保留字母、数字、中文，空格转连字符
    filename = re.sub(r'[^\w一-鿿-]', '-', term_name)
    filename = re.sub(r'-+', '-', filename).strip('-')
    return filename


def generate_obsidian_files(all_terms: dict[str, list[dict]], output_dir: Path):
    """为每个术语生成独立的 Obsidian markdown 文件"""
    output_dir.mkdir(parents=True, exist_ok=True)

    # 收集所有术语名用于 wiki-link 匹配
    all_term_names = set()
    for terms in all_terms.values():
        for t in terms:
            all_term_names.add(t["term"])
            for alias in t.get("aliases", []):
                all_term_names.add(alias)

    for domain_name, terms in all_terms.items():
        domain_dir = output_dir / domain_name
        domain_dir.mkdir(parents=True, exist_ok=True)

        for term_data in terms:
            term_name = term_data["term"]
            filename = term_to_filename(term_name) + ".md"
            filepath = domain_dir / filename

            # 生成 markdown 内容
            content = generate_term_markdown(term_data, domain_name, all_term_names, all_terms)
            filepath.write_text(content, encoding="utf-8")

        # 生成领域索引
        index_path = domain_dir / "_index.md"
        index_content = generate_domain_index(domain_name, terms)
        index_path.write_text(index_content, encoding="utf-8")

    # 生成总索引
    main_index = output_dir / "_index.md"
    main_index.write_text(generate_main_index(all_terms), encoding="utf-8")

    print(f"生成完成: {output_dir}")
    for domain_name, terms in all_terms.items():
        print(f"  {domain_name}: {len(terms)} 个术语")


def generate_term_markdown(term_data: dict, domain: str, all_names: set, all_terms: dict) -> str:
    """为单个术语生成 Obsidian 兼容的 markdown"""
    term = term_data["term"]
    aliases = term_data.get("aliases", [])
    definition = term_data.get("definition", {})
    related = term_data.get("related", [])
    cross_domain = term_data.get("cross_domain", {})
    examples = term_data.get("examples", [])
    hints = term_data.get("model_hints", {})

    lines = []

    # Frontmatter
    lines.append("---")
    lines.append(f"term: \"{term}\"")
    lines.append(f"domain: {domain}")
    if aliases:
        lines.append(f"aliases: {json.dumps(aliases, ensure_ascii=False)}")
    lines.append(f"tags: [glossary, {domain}]")
    lines.append("---")
    lines.append("")

    # 标题
    lines.append(f"# {term}")
    lines.append("")

    # 别名
    if aliases:
        lines.append(f"**别名**: {', '.join(aliases)}")
        lines.append("")

    # 定义
    if definition.get("zh"):
        lines.append(f"## 定义")
        lines.append("")
        lines.append(f"**中文**: {definition['zh']}")
        lines.append("")
    if definition.get("en"):
        lines.append(f"**English**: {definition['en']}")
        lines.append("")

    # 提示
    if hints.get("prompt_fragment"):
        lines.append(f"> 💡 **Agent 提示**: {hints['prompt_fragment']}")
        lines.append("")

    # 示例
    if examples:
        lines.append("## 示例")
        lines.append("")
        for ex in examples:
            lines.append(f"- \"{ex['context']}\"")
            lines.append(f"  → {ex['meaning']}")
            lines.append("")

    # 关联术语（wiki-links）
    if related:
        lines.append("## 关联术语")
        lines.append("")
        for rel in related:
            # 尝试找到对应的文件名
            link = find_wiki_link(rel, all_terms)
            lines.append(f"- {link}")
        lines.append("")

    # 跨领域映射
    if cross_domain:
        lines.append("## 跨领域映射")
        lines.append("")
        for target_domain, mappings in cross_domain.items():
            lines.append(f"### → {target_domain}")
            lines.append("")
            for m in mappings:
                target_term = m["term"]
                note = m.get("note", "")
                link = find_wiki_link(target_term, all_terms)
                lines.append(f"- {link}")
                if note:
                    lines.append(f"  📌 {note}")
            lines.append("")

    return "\n".join(lines)


def find_wiki_link(term_name: str, all_terms: dict) -> str:
    """为术语生成 wiki-link"""
    # 在所有领域中查找
    for domain_name, terms in all_terms.items():
        for t in terms:
            if t["term"] == term_name:
                filename = term_to_filename(term_name)
                return f"[[{domain_name}/{filename}|{term_name}]]"
            # 检查别名
            if term_name in t.get("aliases", []):
                filename = term_to_filename(t["term"])
                return f"[[{domain_name}/{filename}|{term_name}]]"

    # 找不到，返回纯文本
    return term_name


def generate_domain_index(domain_name: str, terms: list[dict]) -> str:
    """生成领域索引文件"""
    lines = []
    lines.append("---")
    lines.append(f"domain: {domain_name}")
    lines.append("tags: [glossary, index]")
    lines.append("---")
    lines.append("")
    lines.append(f"# {domain_name} 术语索引")
    lines.append("")
    lines.append(f"共 {len(terms)} 个术语")
    lines.append("")

    # 按首字母分组
    sorted_terms = sorted(terms, key=lambda t: t["term"])
    for t in sorted_terms:
        term = t["term"]
        zh = t["definition"].get("zh", "")[:50]
        filename = term_to_filename(term)
        lines.append(f"- [[{filename}|{term}]] — {zh}")

    return "\n".join(lines)


def generate_main_index(all_terms: dict[str, list[dict]]) -> str:
    """生成总索引"""
    lines = []
    lines.append("---")
    lines.append("tags: [glossary, index, main]")
    lines.append("---")
    lines.append("")
    lines.append("# Prompt_translator 术语知识库")
    lines.append("")

    total = sum(len(terms) for terms in all_terms.values())
    lines.append(f"共 {len(all_terms)} 个领域，{total} 个术语")
    lines.append("")

    for domain_name, terms in all_terms.items():
        lines.append(f"## [[{domain_name}/_index|{domain_name}]]")
        lines.append("")
        lines.append(f"{len(terms)} 个术语")
        lines.append("")

    return "\n".join(lines)


def generate_cross_domain_map(source_domain: str, target_domain: str,
                               all_terms: dict[str, list[dict]], output_dir: Path):
    """生成跨领域映射文档"""
    output_dir.mkdir(parents=True, exist_ok=True)

    source_terms = all_terms.get(source_domain, [])
    target_terms = all_terms.get(target_domain, [])
    target_dict = {t["term"]: t for t in target_terms}

    lines = []
    lines.append("---")
    lines.append(f"source: {source_domain}")
    lines.append(f"target: {target_domain}")
    lines.append("tags: [glossary, mapping]")
    lines.append("---")
    lines.append("")
    lines.append(f"# {source_domain} → {target_domain}")
    lines.append("")
    lines.append("跨领域术语映射关系")
    lines.append("")

    mapped = 0
    unmapped = 0

    for src in source_terms:
        cross_domain = src.get("cross_domain", {})
        if target_domain in cross_domain:
            mappings = cross_domain[target_domain]
            for m in mappings:
                target_name = m["term"]
                note = m.get("note", "")
                target_filename = term_to_filename(target_name)
                src_filename = term_to_filename(src["term"])

                lines.append(f"## [[{source_domain}/{src_filename}|{src['term']}]] → [[{target_domain}/{target_filename}|{target_name}]]")
                lines.append("")
                if note:
                    lines.append(f"📌 {note}")
                    lines.append("")

                # 源术语定义
                src_zh = src["definition"].get("zh", "")
                if src_zh:
                    lines.append(f"**{src['term']}**: {src_zh}")
                    lines.append("")

                # 目标术语定义
                if target_name in target_dict:
                    tgt = target_dict[target_name]
                    tgt_zh = tgt["definition"].get("zh", "")
                    if tgt_zh:
                        lines.append(f"**{target_name}**: {tgt_zh}")
                        lines.append("")

                mapped += 1
        else:
            unmapped += 1

    lines.append("---")
    lines.append("")
    lines.append(f"已映射: {mapped} | 未映射: {unmapped}")

    filepath = output_dir / f"{source_domain}_to_{target_domain}.md"
    filepath.write_text("\n".join(lines), encoding="utf-8")
    print(f"生成映射文档: {filepath}")


def inject_wiki_links(project_path: str, all_terms: dict[str, list[dict]]):
    """将术语注入到项目文档中（添加 wiki-link）"""
    project = Path(project_path)
    if not project.exists():
        print(f"错误: 路径不存在 {project_path}", file=sys.stderr)
        sys.exit(1)

    # 收集所有术语和别名，去重并按长度降序排列
    term_map = {}  # alias_lower -> (term_name, domain, filename)
    for domain_name, terms in all_terms.items():
        for t in terms:
            filename = term_to_filename(t["term"])
            entry = (t["term"], domain_name, filename)
            # 主术语优先
            if t["term"].lower() not in term_map:
                term_map[t["term"].lower()] = entry
            for alias in t.get("aliases", []):
                key = alias.lower()
                # 更长的别名优先（避免子串匹配问题）
                if key not in term_map or len(alias) > len(term_map[key][0]):
                    term_map[key] = entry

    # 按长度降序排序，优先匹配更长的术语
    sorted_terms = sorted(term_map.items(), key=lambda x: -len(x[0]))

    # 扫描项目中的 markdown 文件
    md_files = list(project.rglob("*.md"))
    modified_count = 0

    for md_file in md_files:
        # 跳过 glossary 自己的文件
        if "vibe-glossary" in str(md_file) or "Prompt_translator" in str(md_file):
            continue

        content = md_file.read_text(encoding="utf-8")
        original = content

        # 先标记所有已替换的区域，避免嵌套替换
        # 使用占位符策略：先替换最长的术语，再用占位符保护
        replaced_ranges = []  # (start, end) 已替换的范围

        for alias_lower, (term_name, domain, filename) in sorted_terms:
            # 对中文不做 word boundary 检查
            if any('一' <= c <= '鿿' for c in alias_lower):
                pattern = re.escape(alias_lower)
            else:
                pattern = r'\b' + re.escape(alias_lower) + r'\b'

            for match in re.finditer(pattern, content, re.IGNORECASE):
                start, end = match.start(), match.end()

                # 检查是否与已替换区域重叠
                overlaps = any(start < re_end and end > re_start
                              for re_start, re_end in replaced_ranges)
                if overlaps:
                    continue

                matched_text = match.group(0)
                link = f"[{matched_text}](./glossary/{domain}/{filename}.md)"

                # 替换
                content = content[:start] + link + content[end:]
                replaced_ranges.append((start, start + len(link)))

                # 由于内容长度变了，需要重新计算后续范围的偏移
                offset = len(link) - (end - start)
                replaced_ranges = [(s + offset if s > start else s,
                                   e + offset if e > start else e)
                                  for s, e in replaced_ranges]
                break  # 每个术语只替换一次

        if content != original:
            md_file.write_text(content, encoding="utf-8")
            modified_count += 1
            print(f"  修改: {md_file}")

    print(f"\n扫描完成: {len(md_files)} 个文件，修改了 {modified_count} 个")


def main():
    parser = argparse.ArgumentParser(
        description="vibe-glossary Obsidian 合并工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python merge.py generate
  python merge.py map product software-engineering
  python merge.py inject /path/to/project
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="子命令")

    # generate 子命令
    gen_parser = subparsers.add_parser("generate", help="生成 Obsidian 兼容文件")
    gen_parser.add_argument("--output", default=str(OUTPUT_DIR), help="输出目录")

    # map 子命令
    map_parser = subparsers.add_parser("map", help="生成跨领域映射文档")
    map_parser.add_argument("source", help="源领域")
    map_parser.add_argument("target", help="目标领域")
    map_parser.add_argument("--output", default=str(OUTPUT_DIR / "mappings"), help="输出目录")

    # inject 子命令
    inject_parser = subparsers.add_parser("inject", help="将术语注入到项目文档")
    inject_parser.add_argument("project", help="项目路径")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    all_terms = load_all_terms()

    if args.command == "generate":
        generate_obsidian_files(all_terms, Path(args.output))
    elif args.command == "map":
        if args.source not in all_terms:
            print(f"错误: 源领域 '{args.source}' 不存在", file=sys.stderr)
            sys.exit(1)
        if args.target not in all_terms:
            print(f"错误: 目标领域 '{args.target}' 不存在", file=sys.stderr)
            sys.exit(1)
        generate_cross_domain_map(args.source, args.target, all_terms, Path(args.output))
    elif args.command == "inject":
        inject_wiki_links(args.project, all_terms)


if __name__ == "__main__":
    main()
