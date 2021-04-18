from .base import Base, try_draw
from .decorators import overwrite


###################################################################################################
# Special Tags

class Container(Base):
    funcs = ['get_content']
    defaults = {
        'inline': False
    }
    _block = \
"""
{get_content}
"""
    def get_content(self):
        content = []
        for arg in self.args:
            content.append(try_draw(arg))
        if self.get('inline'):
            joinstr = ' '
        else:
            joinstr = '\n'
        return joinstr.join([str(c) for c in content])


class Comment(Base):
    _block = '<!-- {content} -->'


###################################################################################################
# A


class A(Base):
    defaults = {
        'href': '#'
    }


class Abbr(Base):
    defaults = {
        'title': 'attribute'
    }


class Address(Base):
    pass


class Area(Base):
    defaults = {
        'shape': 'rect',
        'coords': '0,0,0,0',
        'href': '#',
        'alt': 'Area'
    }


class Article(Base):
    pass


class Aside(Base):
    pass


class Audio(Base):
    pass


###################################################################################################
# B

class B(Base):
    pass


class Bdi(Base):
    pass


class Bdo(Base):
    defaults = {
        'dir': 'rtl'
    }


class Blockquote(Base):
    pass


class Body(Base):
    pass


class Br(Base):
    closing = False


class Button(Base):
    defaults = {
        'type': 'button'
    }


###################################################################################################
# C

class Canvas(Base):
    defaults = {
        'id': 'myCanvas'
    }


class Caption(Base):
    pass


class Cite(Base):
    pass


class Code(Base):
    pass


class Col(Base):
    pass


class ColGroup(Base):
    pass


###################################################################################################
# D

class Data(Base):
    defaults = {
        'value': 0
    }


class DataList(Base):
    defaults = {
        'id': 'MyDataList'
    }


class Dd(Base):
    pass


class Del(Base):
    pass


class Details(Base):
    pass


class Dfn(Base):
    pass


class Dialog(Base):
    defaults = {
        '_open': True
    }
    funcs = ['get_open']
    _block = '<{tag}{kwargs}{get_open}>{content}</{tag}>'

    def get_open(self):
        if self.defaults['_open']:
            return ' open'
        return ''


class Div(Base):
    pass


class Dl(Base):
    pass


@overwrite(get_content=('join_content_with', ' '))
class DocType(Base):
    _tag = 'DOCTYPE'
    _block = '<!{tag} {content}>'


class Dt(Base):
    pass


class DlDict(Dl):
    _tag = 'dl'
    TitleClass = Dt
    DescClass = Dd
    defaults = {
        '_title_kwargs': {},
        '_desc_kwargs': {},
    }

    def get_content(self):

        items = []
        for arg in self.args:
            if isinstance(arg, dict):
                for key, value in arg.items():
                    title = self.TitleClass(key, **self.get('_title_kwargs'))
                    desc = self.DescClass(value, **self.get('_desc_kwargs'))
                    items.append(try_draw(title) + try_draw(desc))
            else:
                #raise NotImplementerError()
                # TODO: Raise warning or something better
                continue
        return '\n'.join(items)


###################################################################################################
# E

class Em(Base):
    pass


class Embed(Base):
    defaults = {
        'src': 'default.jpg',
        'width': 100,
        'height': 100
    }


###################################################################################################
# F

class FieldSet(Base):
    pass


class FigCaption(Base):
    pass


class Figure(Base):
    pass


class Footer(Base):
    pass


class Form(Base):
    defaults = {
        'action': '',
        'method': 'POST'
    }


###################################################################################################
# G


###################################################################################################
# H

class H(Base):
    defaults = {'size': 1}
    block = '<{tag}{size}{kwargs}>{content}</{tag}{size}>'


class Head(Base):
    pass


class Header(Base):
    pass


class Hr(Base):
    closing = False


###################################################################################################
# I

class I(Base):
    pass


class IFrame(Base):
    defaults = {
        'src': '#'
    }


class Img(Base):
    defaults = {
        'src': 'default.jpg',
        'height': 100,
        'width': 100,
        'alt': 'default'
    }


class Input(Base):
    defaults = {
        'type': 'text',
        'id': 'myInput',
        'name': 'myInput'
    }


class Ins(Base):
    pass


###################################################################################################
# J


###################################################################################################
# K

class Kbd(Base):
    pass


###################################################################################################
# L

class Label(Base):
    defaults = {
        'for': 'myInput'
    }


class Legend(Base):
    pass


class Li(Base):
    pass


class Link(Base):
    defaults = {
        'rel': 'stylesheet',
        'type': 'text/css',
        'href': 'styles.css'
    }


###################################################################################################
# M

class Main(Base):
    pass


class Map(Base):
    defaults = {
        'name': 'myMap'
    }


class Mark(Base):
    pass


class Meta(Base):
    pass


class Meter(Base):
    defaults = {
        'id': 'myMeter',
        'value': 0
    }


###################################################################################################
# N

class Nav(Base):
    pass


class NoScript(Base):
    pass


###################################################################################################
# O

class Object(Base):
    defaults = {
        'data': None,
        'width': 100,
        'height': 100
    }


class Ol(Base):
    pass


class OlList(Ol):
    _tag = 'ol'
    ItemClass = Li
    defaults = {
        '_item_kwargs': {}
    }

    def get_content(self):
        items = []
        for arg in self.args:
            item = self.ItemClass(arg, **self.get('_item_kwargs'))
            items.append(try_draw(item))
        return '\n'.join(items)


class OptGroup(Base):
    defaults = {
        'label': 'myOptGroup'
    }


class Option(Base):
    defaults = {
        'value': 'value'
    }


class Output(Base):
    defaults = {
        'name': 'myOutput',
        'for': 'myInput'
    }


###################################################################################################
# P

class P(Base):
    pass


class Param(Base):
    closing = False
    defaults = {
        'name': 'myParam',
        'value': 'value',
    }


class Picture(Base):
    pass


class Pre(Base):
    pass


class Progress(Base):
    defaults = {
        'id': 'myProgress',
        'value': 0,
        'max': 100
    }

###################################################################################################
# Q

class Q(Base):
    pass


###################################################################################################
# R

class Rt(Base):
    pass


class Ruby(Base):
    pass


###################################################################################################
# S

class S(Base):
    pass


class Samp(Base):
    pass


class Script(Base):
    pass


class Section(Base):
    pass


class Selection(Base):
    pass


class Small(Base):
    pass


class Source(Base):
    pass


class Span(Base):
    pass


class Strong(Base):
    pass


class Style(Base):
    pass


class Sub(Base):
    pass


class Summary(Base):
    pass


class Sup(Base):
    pass


class Svg(Base):
    pass


###################################################################################################
# T

class Table(Base):
    pass


class TBody(Base):
    pass


class Td(Base):
    pass


class Template(Base):
    pass


class TextArea(Base):
    pass


class TFoot(Base):
    pass


class Th(Base):
    pass


class THead(Base):
    pass


class Time(Base):
    pass


class Title(Base):
    pass


class Tr(Base):
    pass


class Track(Base):
    pass


###################################################################################################
# U

class U(Base):
    pass


class Ul(Base):
    pass


class UlList(Ul):
    ItemClass = Li
    defaults = {
        '_item_kwargs': {}
    }

    def get_content(self):
        items = []
        for arg in self.args:
            item = self.ItemClass(arg, **self.get('_item_kwargs'))
            items.append(try_draw(item))
        return '\n'.join(items)


###################################################################################################
# V


class Var(Base):
    pass


class Video(Base):
    pass


###################################################################################################
# W


class Wbr(Base):
    pass


###################################################################################################
# X


###################################################################################################
# Y


###################################################################################################
# Z

