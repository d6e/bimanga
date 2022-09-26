import os
import pathlib

import flask
from flask import Flask, send_file
from markupsafe import escape

app = Flask(__name__)
library = 'manga'


@app.route("/")
def index():
    return flask.render_template('index.html', items=os.listdir(library))


# @app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def get_dir(path):
    path = escape(path)
    return flask.render_template('index.html', path=path, items=os.listdir(pathlib.Path(library, path)))


# @app.route("/<title>")
# def get_page1(title):
#     title = escape(title)
#     return flask.render_template('index.html', name='Languages', items=os.listdir(pathlib.Path(library, title)))


@app.route("/<title>/<lang>")
def get_page2(title, lang):
    title = escape(title)
    lang = escape(lang)
    return flask.render_template('index.html', name='Chapters', path="title/",
                                 items=os.listdir(pathlib.Path(library, title, lang)))


@app.route("/<title>/<lang>/<chapter>")
def get_page3(title, lang, chapter):
    title = escape(title)
    lang = escape(lang)
    chapter = escape(chapter)
    return os.listdir(pathlib.Path(library, title, lang, chapter))


@app.route("/<title>/<lang>/<chapter>/<page>")
def get_page4(title, lang, chapter, page):
    title = escape(title)
    lang = escape(lang)
    chapter = escape(chapter)
    page = escape(page)
    path = pathlib.Path(library, title, lang, chapter, page)
    if not path.exists():
        return 404
    return send_file(path, mimetype='image/gif')


if __name__ == '__main__':
    app.run(debug=True)
