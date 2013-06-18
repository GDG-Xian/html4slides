#-*-coding:utf-8-*-
from markdown import markdown
from base import BaseMarkup

class MarkdownMarkup(BaseMarkup):
    def markup(self):
        self.html_content = markdown(self.content)
