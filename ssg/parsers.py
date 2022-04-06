import sys
import shutil
from typing import List
from pathlib import Path
from markdown import markdown
from ssg.content import Content
from docutils.core import publish_parts


class Parser:
    extensions: List[str] = []

    def valid_extension(self, extension):
        return extension in self.extensions

    # TODO: why self and hence not static (all 4 following methods)
    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path):
        with open(path, 'r') as file:
            return file.read()

    def write(self, path: Path, dest: Path, content, ext='.html'):
        full_path = dest / path.with_suffix(ext).name
        with open(full_path, 'w') as file:
            file.write(content)

    # TODO: wanted to write shutil.copy2(src=path, dst=dest/path.relative_to(source))
    def copy(self, path: Path, source: Path, dest: Path):
        shutil.copy2(path, dst=dest / path.relative_to(source))


class ResourceParser(Parser):
    # extensions = ['.jpg', '.png', '.gif', '.css' '.html']
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path: Path, source: Path, dest: Path):
        self.copy(self, path, source, dest)


class MarkdownParser(Parser):

    extensions = ['.md', '.markdown']

    def parse(self, path: Path, source: Path, dest: Path):
        content = Content.load(self.read(path))
        html = markdown(content.body)
        self.write(path=path, dest=dest, content=html)
        sys.stdout.write("\x1b[1;32m{} converted to HTML. Metadata: {}\n".format(path.name, content))


class ReStructuredTextParser(Parser):

    extensions = ['.rst']

    def parse(self, path: Path, source: Path, dest: Path):
        content = Content.load(self.read(path))
        html = publish_parts(content.body, writer_name='html5')
        # TODO: wrote this but got error
        #self.write(path=path, dest=dest, content=html["html_body"])
        self.write(path, dest, html["html_body"])
        sys.stdout.write("\x1b[1;32m{} converted to HTML. Metadata: {}\n".format(path.name, content))
