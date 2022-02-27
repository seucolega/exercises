"""
Markdown on Exercism's Python Track
"""

import re


def parse_inline_symbol(text: str, md_symbol: str, html_symbol) -> str:
    match = re.match(f'(.*){md_symbol}(.*){md_symbol}(.*)', text)

    if match:
        return match.group(1) + f'<{html_symbol}>' + match.group(2) \
               + f'</{html_symbol}>' + match.group(3)

    return text


def parse_inline_text(text: str) -> str:
    inline_symbols = {'__': 'strong', '_': 'em'}

    for md_symbol, html_symbol in inline_symbols.items():
        text = parse_inline_symbol(text, md_symbol, html_symbol)

    return text


def parse(markdown: str):
    html = ''
    in_list = False
    markdown = markdown.splitlines()
    markdown.append('')

    for line in markdown:
        if line.startswith('#'):
            header = len(line.split()[0])
            if header < 7:
                line = f'<h{header}>' + line[header + 1:] + f'</h{header}>'

        line = parse_inline_text(line)

        if line.startswith('* '):
            line = '<li>' + line[2:] + '</li>'

            if not in_list:
                in_list = True
                line = '<ul>' + line

            html += line

            continue

        if line and not re.match('<h|<ul|<p|<li', line):
            line = '<p>' + line + '</p>'

        if in_list:
            in_list = False
            line = '</ul>' + line

        html += line

    return html
