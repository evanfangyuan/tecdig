#!/usr/bin/env python3
"""生成每日科技简报 HTML"""
import re
from pathlib import Path

# 读取 markdown 内容
md_path = Path("/home/admin/.openclaw/workspace/archive/tech-news-digest/daily-2026-03-24.md")
md_content = md_path.read_text(encoding='utf-8')

# 简单转换 markdown 到 HTML
html_content = md_content
# 标题
html_content = html_content.replace("# ", "<h1>").replace("\n", "</h1>\n", 1)
# 二级标题
html_content = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html_content, flags=re.MULTILINE)
# 三级标题
html_content = re.sub(r'^### (\d+)\. (.+)$', r'<h3>\1. \2</h3>', html_content, flags=re.MULTILINE)
# 粗体
html_content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html_content)
# 链接
html_content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html_content)
# 列表项
html_content = re.sub(r'^- (.+)$', r'<li>\1</li>', html_content, flags=re.MULTILINE)
# 表格处理
html_content = re.sub(r'\|(.+)\|', lambda m: '<td>' + m.group(1).strip().split('|')[-1] + '</td>', html_content)
# 换行
html_content = html_content.replace("\n\n", "</p><p>")
html_content = html_content.replace("\n", "<br>")

# 构建完整 HTML
full_html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>科技芯声 | 2026-03-24</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Microsoft YaHei', sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
            color: #333;
            line-height: 1.8;
        }}
        h1 {{ color: #1a1a1a; border-bottom: 3px solid #0066cc; padding-bottom: 10px; }}
        h2 {{ color: #0066cc; margin-top: 30px; }}
        h3 {{ color: #333; }}
        a {{ color: #0066cc; }}
        li {{ margin: 8px 0; }}
    </style>
</head>
<body>
{html_content}
</body>
</html>'''

# 写入文件
output_path = Path("/home/admin/.openclaw/workspace/tecdig/digest-20260324.html")
output_path.write_text(full_html, encoding='utf-8')
print(f"Generated: {output_path}")

# 同时写入 index.html
index_path = Path("/home/admin/.openclaw/workspace/tecdig/index.html")
index_path.write_text(full_html, encoding='utf-8')
print(f"Updated: {index_path}")
