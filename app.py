from flask import Flask

from main.main import main_blueprint


app = Flask(__name__)

app.register_blueprint(main_blueprint)


app.run()
