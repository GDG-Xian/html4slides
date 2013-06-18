#-*-coding:utf-*-
from BeautifulSoup import BeautifulSoup, Tag
from base import BaseParser

class HTML5SlidesParser(BaseParser):
    def parse(self):
        soup = BeautifulSoup(self.content)

        hsoup = BeautifulSoup()
        html = Tag(hsoup, 'html')
        hsoup.append(html)

        head = Tag(hsoup, 'head')
        title = Tag(hsoup, 'title')
        title.setString(self.title)
        head.append(title)

        link = Tag(hsoup, 'link')
        link['rel'] = 'stylesheet'
        link['type'] = 'text/css'
        link['href'] = 'http://gdg-xian.github.io/html5slides-markdown/themes/default.css'
        head.append(link)

        script = Tag(hsoup, 'script')
        script['src'] = 'http://gdg-xian.github.io/html5slides-markdown/javascripts/html5slides.js'
        head.append(script)
        html.append(head)

        body = Tag(hsoup, 'body')
        body['style'] = 'display:none'
        section = Tag(hsoup, 'section')
        section['class'] = 'slides layout-regular template-default'
        body.append(section)
        elements = []
        elements.append(soup.first())
        elements.extend(soup.first().findNextSiblings())
        article = Tag(hsoup, 'article')
        section.append(article)
        for element in elements:
            if element.name == 'hr':
                article = Tag(hsoup, 'article')
                section.append(article)
            else:
                article.append(element)

        html.append(body)

        self.html_content = html

    def finish(self):
        self.html_content = "<!DOCTYPE html>\n\n%s" % self.html_content
