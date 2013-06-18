#-*-coding:utf-8-*-
import sys
from markdown import markdown


def check_args(args):
    markup_name = "%sMarkup" % (args.markup or 'Markdown')
    markup_class = get_class("markups.%s.%s" % (markup_name.lower(), markup_name))


def get_class(class_name):
    d = class_name.rfind('.')
    classname = class_name[d+1:]
    m = __import__(class_name[:d], globals(), locals(), [classname])
    return getattr(m, classname)


def get_markup_names(name):
    markup_name = "%sMarkup" % (name or 'Markdown')
    return markup_name, "markups.%s.%s" % (markup_name.lower(), markup_name)


def get_markup_class(name):
    markup_name, markup_class_name = get_markup_names(name)
    return get_class(markup_class_name)


def get_parser_names(name):
    parser_name = "%sParser" % (name or 'Deck')
    return parser_name, "parsers.%s.%s" % (parser_name.lower(), parser_name)


def get_parser_class(name):
    parser_name, parser_class_name = get_parser_names(name)
    return get_class(parser_class_name)


def get_file_contents(filename):
    try:
        f = open(filename, 'r')
        contents = f.read()
        f.close()
    except Exception, e:
        print "Please check %s" % filename
        sys.exit(1)
    return contents


def show_slides(args):
    contents = get_file_contents(args.file)

    markup_class = get_markup_class(args.markup)
    markup = markup_class(contents)
    markup.prepare()
    markup.markup()
    markup.finish()

    parser_class = get_parser_class(args.parser)
    parser = parser_class(args.title, markup.html_content)
    parser.prepare()
    parser.parse()
    parser.finish()

    print parser.html_content
