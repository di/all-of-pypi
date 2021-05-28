import html.parser
import urllib.request

from setuptools import setup


class SimpleParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.project_names = []
        self.in_href = False

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.in_href = True

    def handle_endtag(self, tag):
        if tag == "a":
            self.in_href = False

    def handle_data(self, data):
        if self.in_href:
            self.project_names.append(data)


s = urllib.request.urlopen("https://pypi.org/simple/").read().decode()
p = SimpleParser()
p.feed(s)

setup(
    name="all-of-pypi",
    version="0a0",
    description="All of PyPI",
    long_description="This project installs all of PyPI.",
    long_description_content_type="text/markdown",
    url="https://pypi.org",
    author="Dustin Ingram",
    author_email="di@python.org",
    install_requires=p.project_names,
)
