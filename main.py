import os
import pathlib

import flask
from flask import Flask, send_file
from markupsafe import escape

library = 'manga'
app = Flask(__name__,  static_folder=library)


@app.route("/")
def index():
    return flask.render_template('index.html', items=os.listdir(library))


@app.route("/<title>")
def get_page1(title):
    title = escape(title)
    return flask.render_template('lang.html', path=title, items=os.listdir(pathlib.Path(library, title)))


@app.route("/<title>/<lang>")
def get_page2(title, lang):
    title = escape(title)
    lang = escape(lang)
    path = title + "/" + lang
    return flask.render_template('chapters.html', name='Chapters', path=path,
                                 items=os.listdir(pathlib.Path(library, title, lang)))


@app.route("/<title>/<lang>/<chapter>")
def get_page3(title, lang, chapter):
    title = escape(title)
    lang = escape(lang)
    chapter = escape(chapter)
    path = title + "/" + lang + "/" + chapter
    return flask.render_template('pages.html', name='Chapters', path=path, items=os.listdir(pathlib.Path(library, title, lang, chapter)))


@app.route("/<title>/<lang>/<chapter>/<page>")
def get_page4(title, lang, chapter, page):
    title = escape(title)
    lang = escape(lang)
    chapter = escape(chapter)
    page = escape(page)
    path = f"{library}/{title}/{lang}/{chapter}/{page}"
    return flask.render_template('page.html', image_path=path)
    # return send_file(path, mimetype='image/gif')


if __name__ == '__main__':
    app.run(debug=True)
