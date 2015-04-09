from flask import Flask, render_template
from flask_outdated_browser import OutdatedBrowser

def create_app():

    app = Flask(__name__)
    OutdatedBrowser(app)
    app.config['OUTDATED_BROWSER_AJAX'] = True

    @app.route("/")
    def index():

        return render_template("index.html")


    return app

if __name__ == '__main__':
    create_app().run(debug=True)