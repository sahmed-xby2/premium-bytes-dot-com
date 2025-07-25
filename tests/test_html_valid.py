import glob
from html.parser import HTMLParser

def test_html_files_parse():
    parser = HTMLParser()
    for path in glob.glob('docs/*.html'):
        with open(path, encoding='utf-8') as f:
            data = f.read()
        parser.feed(data)
