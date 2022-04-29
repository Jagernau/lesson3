from json import load

with open('posts.json', encoding='utf-8') as f:
    posts = load(f)

def get_post_from_text(text):
    """поиск по введенному тексту"""
    result = []

    for i in posts:
        if str(text) in i["content"]:
            result.append(i)
                
    return result

