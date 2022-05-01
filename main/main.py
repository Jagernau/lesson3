from flask import Blueprint, request, render_template
import functions
import logging

logging.basicConfig(filename="basic.log", level=logging.INFO)

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates', static_folder='static')

@main_blueprint.route("/")
def page_index():
    return render_template("index.html")

@main_blueprint.route("/search")
def page_tag():
    s = request.args['s']
    serch_post = functions.get_post_from_text(s)
    logging.info(f"Искалось {s}")
    
    return render_template("post_list.html", word=s, posts=serch_post)

