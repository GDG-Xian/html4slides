html4slides
===========

It's a tool for converting text files into html files(slides)

INSTALL
===========

`sudo python setup.py install`

COMMAND
===========

html4slides provides a cli named `givemeslides`, you can use it convert your markdown file into slides.

arguments:

    --markup:
        Which markup languge you want to use, default is Markdown
    --parser:
        Which html slides you wanna use, options can be `HTML5Slides`, `Deck` and `RevealJS`
    --file:
        Your text file
    --theme:
        Haven't implemented yet, used for slides to choose a theme
    --title:
        Input title for your slides
