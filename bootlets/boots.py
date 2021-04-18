from flask_bootstrap import is_hidden_field_filter

from .funcs import list_to_str, try_draw
from . import html


class Boot:
    defaults = {}
    _class = ""

    def __init__(self, *args, **kwargs) -> None:
        self.args = args
        self.kwargs = kwargs

    def __call__(self, *args, **kwargs):
        args = args if args else self.args
        kwargs = {**self.kwargs, **kwargs}
        return self.__class__(*args, **kwargs)

    def get(self, key, *args, **kwargs):
        return {**self.defaults, **self.kwargs}.get(key, *args, **kwargs)

    def get_class(self) -> str:
        s = ""
        if self._class:
            s += self._class
        optionals = self.build_classes()
        if optionals:
            s += " " + optionals
        if "class_" in self.kwargs:
            extra = list_to_str(self.kwargs["class_"])
            if extra:
                s += " " + extra
        return s

    def get_kwargs(self) -> dict:
        kwargs = {}
        for key, value in {**self.defaults, **self.kwargs}.items():
            if key.startswith("_"):
                continue
            if key == "class_":
                value = self.get_class()
            else:
                key = key.replace("_", "-")
                value = list_to_str(value)

            if key == "for_":
                key = "for"
            kwargs[key] = value
        if "class_" not in kwargs:
            c = self.get_class()
            if c:
                kwargs["class_"] = c
        return kwargs

    def build_classes(self) -> str:
        return ""

    def build(self):
        return html.Div(*self.args, **self.get_kwargs())

    def draw(self) -> str:
        return try_draw(self.build())


class Alert(Boot):
    _class = "alert"
    defaults = {"_context": "primary", "role": "alert"}

    def build_classes(self):
        return f'alert-{self.get("_context")}'

    def build(self):
        return html.Div(*self.args, **self.get_kwargs())


class AlertHeading(Boot):
    _class = "alert-heading"
    defaults = {
        "_size": 4,
    }

    def build(self):
        return html.H(*self.args, **self.get_kwargs())


class AlertDismissButton(Boot):
    _class = "close"
    defaults = {"type": "button", "data-dismiss": "alert", "aria-label": "Close"}

    def build(self):
        return html.Button(
            html.Span("&times;", aria_hidden="true"), **self.get_kwargs()
        )


class Badge(Boot):
    _class = "badge"
    defaults = {"_context": "primary"}

    def get_class(self):
        return f'{self._class} badge-{self.get("_context")}'

    def build(self):
        return html.Span(*self.args, **self.get_kwargs())


class BadgePill(Badge):
    _class = "badge badge-pill"


class LinkBadge(Boot):
    _class = "badge"
    defaults = {
        "_context": "primary",
        "href": "#",
    }

    def build_class(self):
        return f'badge-{self.get("_context")}'

    def build(self):
        return html.A(*self.args, **self.get_kwargs())


class BreadcrumbItem(Boot):
    _class = "breadcrumb-item"
    defaults = {"_active": False}

    def build_classes(self):
        if self.get("_active"):
            return "active"
        return ""

    def build(self):
        return html.Li(*self.args, **self.get_kwargs())


class Breadcrumb(Boot):
    _class = "breadcrumb"
    Li = BreadcrumbItem
    Ol = html.Ol
    Nav = html.Nav(aria_label="breadcrumb")

    def build(self):
        items = []
        for arg in self.args[:-1]:
            items.append(self.Li(arg))
        items.append(self.Li(self.args[-1], _active=True, aria_current="page"))
        return self.Nav(self.Ol(*items, **self.get_kwargs()))


class Button(Boot):
    defaults = {
        "_context": "primary",
        "_size": "md",
        "_outline": False,
        "_block": False,
        "_disabled": False,
        "type": "button",
    }

    sizes = {"sm": "btn-sm", "md": "", "lg": "btn-lg"}

    def get_class(self):
        s = "btn"
        size_class = self.sizes.get(self.get("_size"))
        if size_class:
            s += " " + size_class
        s += " btn-"
        if self.get("_outline"):
            s += "outline-"
        s += self.get("_context")
        if self.get("_block"):
            s += " btn-block"
        if self.get("_disabled"):
            s += " disabled"
        return s

    def build(self):
        return html.Button(*self.args, **self.get_kwargs())


class ButtonGroup(Boot):
    defaults = {
        "_vertical": False,
        "role": "group",
        "size": "md",
        "aria-label": "myButtonGroup",
    }

    sizes = {"sm": "btn-group-sm", "md": "", "lg": "btn-group-lg"}

    def get_class(self):
        s = "btn-group"
        if self.get("_vertical"):
            s += "-vertical"
        size_class = self.sizes.get(self.get("_size"))
        if size_class:
            s += " " + size_class
        return s


class Card(Boot):
    _class = "card"


class CardBody(Boot):
    _class = "card-body"


class CardHeader(Boot):
    _class = "card-header"


class CardFooter(Boot):
    _class = "card-footer"


class CardTitle(Boot):
    _class = "card-title"
    defaults = {"_size": 5}

    def build(self):
        return html.H(*self.args, **self.get_kwargs())


class CardText(Boot):
    _class = "card-text"

    def build(self):
        return html.P(*self.args, **self.get_kwargs())


class CardImage(Boot):
    defaults = {
        "_location": "top",
        "src": "#",
        "alt": "myCardImage",
    }

    def build_class(self):
        return f'card-img-{self.get("location")}'

    def build(self):
        return html.Img(**self.get_kwargs())


class ListGroup(Boot):
    _class = "list-group"
    Li = html.Li(class_="list-group-item")
    defaults = {"_flush": False}

    def build_class(self):
        s = ""
        if self.get("_flush"):
            s += " list-group-flush"
        return s

    def build(self):
        return html.Ul(*[self.Li(arg) for arg in self.args], **self.get_kwargs())


class Accordian(Boot):
    _class = "accordian"
    defaults = {"id": "myAccordian"}


class Dropdown(Boot):
    _class = "dropdown"


class DropdownItem(Boot):
    _class = "dropdown-item"
    defaults = {
        "href": "#",
    }

    def build(self):
        return html.A(*self.args, **self.get_kwargs())


class DropdownMenu(Boot):
    _class = "dropdown-menu"
    defaults = {
        "aria-labelledby": "myDropdownMenu",
    }


class DropdownDivider(Boot):
    _class = "dropdown-divider"


class DropdownButton(Boot):
    _class = "btn"
    defaults = {
        "_context": "primary",
        "data-toggle": "dropdown",
        "aria-haspopup": "true",
        "aria-expanded": "false",
    }

    def build_class(self):
        return "btn-" + self.get("_context") + "dropdown-toggle"

    def build(self):
        return html.Button(*self.args, **self.get_kwargs())


class Table(Boot):
    _class = "table table-hover"

    defaults = {
        "_headers": [],
        "_rows": [],
        "_hover": True,
    }

    def build(self):
        headers = html.THead(
            html.Tr(*[html.Th(i, scope="col") for i in self.get("_headers")])
        )
        rows = html.TBody(
            *[html.Tr(*[html.Td(i) for i in row]) for row in self.get("_rows")]
        )

        return html.Table(headers, rows, **self.get_kwargs())


class FormField(Boot):
    defaults = {
        "_form_type": "basic",
        "_columns": ("lg", 2, 10),
        "_button_map": {},
    }

    def build(self):
        field = self.args[0]

        if field.type == "SubmitField":
            btn_cls = self.get("_button_map").get(field.name, "primary")
            return field(**{"class": f"btn btn-{btn_cls}"})
            # return html.Button(class_=f'btn btn-{btn_cls}')

        elif field.type == "RadioField":
            return html.Container(
                *[html.Div(class_="form-check")(item(), item.label()) for item in field]
            )

        elif field.type == "FormField":
            return html.FieldSet()(
                html.Legend()(field.label),
                *[
                    FormField(
                        item,
                        _form_type=self.get("_form_type"),
                        _columns=self.get("_columns"),
                        _button_map=self.get("_button_map"),
                    )
                    for item in field
                    if not is_hidden_field_filter(item)
                ],
            )

        else:
            return html.Div(class_="form-group")(field.label(), field())


class QuickForm(Boot):
    defaults = {
        "_action": "",
        "_method": "post",
        "_extra_classes": None,
        "_role": "form",
        "_form_type": "basic",
        "_columns": ("lg", 2, 10),
        "_enctype": None,
        "_button_map": {},
        "_id": "",
        "_novalidate": False,
        "_render_kw": {},
    }

    def build(self):
        form = self.args[0]
        return html.Form(
            html.Container(
                *[
                    FormField(
                        field,
                        _form_type=self.get("_form_type"),
                        _columns=self.get("_columns"),
                        _button_map=self.get("_button_map"),
                    )
                    for field in form
                ]
            )
        )


class Modal(Boot):
    defaults = {"_id": "modal_id", "_title": "Modal", "_tabindex": -1}

    def build(self):
        return html.Div(
            class_="modal fade",
            id=f'Modal_{self.get("_id")}',
            tabindex=self.get("_tabindex"),
            role="dialog",
            aria_labelledby=f'ModalLabel_{self.get("_id")}',
            aria_hidden="true",
        )(
            html.Div(class_="modal-dialog modal-dialog-centered", role="document")(
                html.Div(class_="modal-content")(
                    html.Div(class_="modal-header")(
                        html.H(
                            size=5,
                            class_="modal-title",
                            id=f'ModalLabel-{self.get("_id")}',
                        )(self.get("_title")),
                        html.Button(
                            type="button",
                            class_="close",
                            data_bs_dismiss="modal",
                            aria_label="Close",
                        )(html.Span(aria_hidden="true")("&times;")),
                    ),
                    html.Div(class_="modal-body")(*self.args),
                    self.get_footer(),
                )
            )
        )

    def get_footer(self):
        if self.get("_footer"):
            return html.Div(class_="modal-footer")(self.get("_footer"))
        return ""


class ModalButton(Boot):
    defaults = {
        "_id": "modal_id",
        "_text": "Submit",
        "_context": "primary",
    }

    def build(self):
        return html.Button(
            type="button",
            class_=f'btn btn-{self.get("_context")}',
            data_bs_toggle="modal",
            data_bs_target=f'#Modal_{self.get("_id")}',
        )(self.get("_text"))


class ModalLink(Boot):
    defaults = {
        "_id": "modal_id",
        "_context": "primary",
    }

    def build(self):
        return html.A(
            type="button",
            data_toggle="modal",
            data_target=f'#Modal_{self.get("_id")}',
            **self.get_kwargs(),
        )(*self.args)
