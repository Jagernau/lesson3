from flask import Blueprint, request, render_template

main_blueprint = Blueprint('main_blueprint', __name__)

@main_blueprint.route("/")
def page_index():
    return render_template("index.html")

@main_blueprint.route("/search")
def page_tag():
    s = request.args['s']
    return f'Вы ввели {s}'

