#-*-coding:utf-*-
from BeautifulSoup import BeautifulSoup, Tag
from base import BaseParser

DECK_JS = """$(function() {
    // Deck initialization
    $.deck('.slide');
    
    $('#style-themes').change(function() {
        $('#style-theme-link').attr('href', $(this).val());
    });
    
    $('#transition-themes').change(function() {
        $('#transition-theme-link').attr('href', $(this).val());
    });
});
"""

class DeckJSParser(BaseParser):
    def parse(self):
        soup = BeautifulSoup(self.content)

        hsoup = BeautifulSoup()
        html = Tag(hsoup, 'html')
        hsoup.append(html)

        head = Tag(hsoup, 'head')
        title = Tag(hsoup, 'title')
        title.setString(self.title)
        head.append(title)

        link1 = Tag(hsoup, 'link')
        link1['rel'] = 'stylesheet'
        link1['type'] = 'text/css'
        link1['href'] = 'http://imakewebthings.com/deck.js/core/deck.core.css'
        head.append(link1)

        link2 = Tag(hsoup, 'link')
        link2['rel'] = 'stylesheet'
        link2['type'] = 'text/css'
        link2['href'] = 'http://imakewebthings.com/deck.js/themes/style/swiss.css'
        head.append(link2)

        link3 = Tag(hsoup, 'link')
        link3['rel'] = 'stylesheet'
        link3['type'] = 'text/css'
        link3['href'] = 'http://yandex.st/highlightjs/7.3/styles/monokai_sublime.min.css'
        head.append(link3)

        link3 = Tag(hsoup, 'link')
        link3['rel'] = 'stylesheet'
        link3['type'] = 'text/css'
        link3['href'] = 'http://imakewebthings.com/deck.js/themes/transition/fade.css'
        head.append(link3)

        script1 = Tag(hsoup, 'script')
        script1['src'] = 'http://imakewebthings.com/deck.js/jquery-1.7.min.js'
        head.append(script1)

        script2 = Tag(hsoup, 'script')
        script2['src'] = 'http://imakewebthings.com/deck.js/core/deck.core.js'
        head.append(script2)

        script3 = Tag(hsoup, 'script')
        script3['src'] = 'http://yandex.st/highlightjs/7.3/highlight.min.js'
        head.append(script3)

        script3 = Tag(hsoup, 'script')
        script3['type'] = 'text/javascript'
        script3.setString(DECK_JS)
        head.append(script3)

        html.append(head)

        body = Tag(hsoup, 'body')
        body['class'] = 'deck-container'
        elements = []
        elements.append(soup.first())
        elements.extend(soup.first().findNextSiblings())
        section = Tag(hsoup, 'section')
        section['class'] = 'slide'
        body.append(section)
        for element in elements:
            if element.name == 'hr':
                section = Tag(hsoup, 'section')
                section['class'] = 'slide'
                body.append(section)
            else:
                section.append(element)

        html.append(body)

        self.html_content = html

    def finish(self):
        self.html_content = "<!DOCTYPE html>\n\n%s" % self.html_content
