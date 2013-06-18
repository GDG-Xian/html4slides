#-*-coding:utf-8-*-

class BaseParser(object):
    """
    """
    html_content = None

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def prepare(self):
        pass

    def parse(self):
        pass

    def finish(self):
        pass
