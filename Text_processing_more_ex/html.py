title = input()
article_content = input()
comments = []

while True:
    comment = input()

    if comment == 'end of comments':
        break

    comments.append(comment)

print(f'<h1>\n\t{title}\n</h1>')
print(f'<article>\n\t{article_content}\n</article>')
for comment in comments:
    print(f'<div>\n\t{comment}\n</div>')
