from json import load

with open('posts.json', encoding='utf-8') as f:
    posts = load(f)


def get_post_from_text(text):
    """поиск по хэштэгу"""
    result = []
    for i in posts:
        if text in i["content"].split("#"):
            result.append(i)
    return result

    
