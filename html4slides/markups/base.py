#-*-coding:utf-8-*-

class BaseMarkup(object):
    """
    """
    html_content = None

    def __init__(self, content):
        self.content = content

    def prepare(self):
        pass

    def markup(self):
        pass

    def finish(self):
        pass
