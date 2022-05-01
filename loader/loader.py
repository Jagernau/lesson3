from flask import Blueprint, request, render_template, send_from_directory
import functions
import logging

logging.basicConfig(filename="basic.log", level=logging.INFO)

logging.basicConfig(filename="errors.log", level=logging.ERROR)

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates', static_folder='static')



@loader_blueprint.route("/post", methods=["GET", "POST"])
def page_post_form():
    return render_template("post_form.html")


@loader_blueprint.route("/upload", methods=["POST"])
def page_post_upload():

    picture = request.files.get("picture")
    filename = picture.filename
    post_text = request.form["content"]

    if functions.is_filename_allowed(filename):
        try:
            picture.save(f"./uploads/{filename}")
            functions.write_in_json(str(filename), str(post_text))
            logging.info(f"файл {filename} сохраняется")
        except:
            logging.error(f"файл {filename} не сохраняется")
            print("Файл не сохраняется")

        else:

            return render_template("post_uploaded.html",pic=f"./uploads/{filename}", text=post_text)
    
    extension = filename.split(".")[-1]	
    return f"Тип файлов {extension} не поддерживается" 


@loader_blueprint.route("/uploads/<path:path>")
def static_dir(path):

    return send_from_directory("uploads", path)

