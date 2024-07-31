import re

title_pattern = r'<title>([^<>]*)<\/title>'
body_pattern = r'<body>.*<\/body>'
body_pattern_2 = r'>([^><]*)<'

html = input()
title = re.findall(title_pattern, html)
title = "".join(title)

body = re.findall(body_pattern, html)
body = "".join(body)
content = re.findall(body_pattern_2, body)

content = ''.join(content)
content = content.replace('\\n', '')



print(f'Title: {title}')
print(f'Content: {content}')