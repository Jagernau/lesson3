from json import load, dump, JSONDecodeError
import logging

logging.basicConfig(filename="basic.log", level=logging.INFO)

try:
    with open('posts.json', encoding='utf-8') as f:
        posts = load(f)
except FileNotFoundError:
    print("Файл отсутствует")

except JSONDecodeError:
    print("Файл не удаётся преобразовать")


def get_post_from_text(text):
    """поиск по введенному тексту"""
    result = []

    for i in posts:
        if str(text) in i["content"]:
            result.append(i)
                
    return result


def is_filename_allowed(filename):
    """проверяет является ли имя картинки картинкой"""
    allowed = ['png', 'jpg', 'webp']
    extension = filename.split(".")[-1]

    if extension in allowed:
        logging.info(f"файл {filename} картинка")
        return True
    else:
        logging.info(f"файл {filename} некартинка")
        return False


def write_in_json(pic, text):
    """запись в json"""
    try:
        with open("posts.json", "w") as fp:
            pic = f"./uploads/{pic}"
            cont = posts
            cont.append({"pic": pic, "content": text})
            dump(cont, fp, ensure_ascii=False, indent=4)
    except:
        print("Файл не записывается в json")
