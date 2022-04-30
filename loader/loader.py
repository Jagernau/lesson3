from flask import Blueprint, request, render_template, send_from_directory
import functions

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates', static_folder='static')

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


@loader_blueprint.route("/post", methods=["GET", "POST"])
def page_post_form():
    return render_template("post_form.html")


@loader_blueprint.route("/upload", methods=["POST"])
def page_post_upload():

    picture = request.files.get("picture")
    filename = picture.filename    
    picture.save(f"./uploads/{filename}")

    post_text = request.form["content"]

    return render_template("post_uploaded.html",pic=f"./uploads/{filename}", text=post_text)


@loader_blueprint.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)
