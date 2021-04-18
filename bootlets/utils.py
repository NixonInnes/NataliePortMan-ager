from inspect import isclass
from .base import Base
from . import templates


def get_html_tag_map():
    map_ = {}
    for t_name in dir(templates):
        template = getattr(templates, t_name)
        if isclass(template) and issubclass(template, Base):
            map_[template.tag] = template
    return map_

HTML_MAP = get_html_tag_map()