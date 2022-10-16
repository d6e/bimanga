import os
import pathlib

html = r"""

<!doctype html>
    <head>
        <meta charset="UTF-8">
        <title>Bilingual Manga</title>
        <style>
        html {{
          max-width: 70ch;
          padding: 3em 1em;
          margin: auto;
          line-height: 1.75;
          font-size: 1.25em;
        }}
        </style>
    </head>
    <body>
        <div id="content">
            <button onclick="location.href='{prev}'" type="button">prev</button>
            <button onclick="location.href=''" type="button">jpn</button>
            <button onclick="location.href='{next}'" type="button">next</button>
            <img src="{current}">
            <button onclick="location.href='{prev}'" type="button">prev</button>
            <button onclick="location.href=''" type="button">jpn</button>
            <button onclick="location.href='{next}'" type="button">next</button>
            <br>
            <form id="form" role="search">
              <input type="search" id="query" name="q"
               placeholder="jisho.org"
               aria-label="Search via jisho.org">
              <button>Search</button>
            </form>
        </div>
    </body>
    <footer>
        <script>
            const f = document.getElementById('form');
            const q = document.getElementById('query');
            const jisho = 'https://jisho.org/search/';

            function submitted(event) {{
              event.preventDefault();
              const url = jisho + q.value;
              const win = window.open(url, '_blank');
              win.focus();
            }}
            f.addEventListener('submit', submitted);
        </script>
    </footer>
</html>
"""


def replace_extension(path, new_extension):
    return path.with_name(path.name.split('.')[0] + new_extension)


def to_html_url(path):
    if path == '':
        return path
    path = pathlib.Path(path)
    path = replace_extension(path, ".html")
    return 'file:///' + path.absolute().as_posix()


def main():
    """ The library file tree is assumed to be <title>/<3-digit language code>/<chapter>/<page>"""
    site = pathlib.Path("site")
    assets = pathlib.Path("manga")
    image_paths = assets.glob("**/*.jpg")
    prev_path = ''
    current_path = ''
    for next_path in image_paths:
        if current_path != '':
            page = site.joinpath(current_path)
            page.parent.mkdir(parents=True, exist_ok=True)
            page = replace_extension(page, ".html")

            current_image = 'file:///' + pathlib.Path(current_path).absolute().as_posix()
            replace_extension(page, ".html")
            with open(page, 'w') as f:
                out = html.format(prev=to_html_url(prev_path), current=current_image, next=to_html_url(next))
                f.write(out)
        prev_path = current_path
        current_path = next_path


if __name__ == '__main__':
    main()
