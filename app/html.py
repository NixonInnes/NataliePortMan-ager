import json

from app.utils.misc import get_unique_name
import bootlets.html as html
import bootlets.boots as boots


class Title(boots.Boot):
    _class = "d-sm-flex align-items-center justify-content-between mb-4"

    def build(self):
        return html.Div(**self.get_kwargs())(
            html.H(*self.args, class_="h3 mb-0 text-gray-800", size=1)
        )


class DropdownCard(boots.Boot):
    defaults = {"title": "Dropdown Card Example", "footer": None, "menu_items": []}

    def build(self):
        id = get_unique_name()
        header = html.Div(
            class_="card-header py-3 d-flex flex-row"
            "align-items-center justify-content-between"
        )(
            html.H(size=6, class_="m-0 font-weight-bold text-primary")(
                self.get("title")
            ),
            html.Div(class_="dropdown no-arrow")(
                html.A(
                    class_="dropdown-toggle",
                    href="#",
                    role="button",
                    id=id,
                    **{
                        "data-bs-toggle": "dropdown",
                        "aria-haspopup": "true",
                        "aria-expanded": "false",
                    }
                )(html.I(class_="fas fa-ellipsis-v fa-sm fa-fw text-gray-400")),
                html.Div(
                    class_="dropdown-menu dropdown-menu-right shadow animated--fade-in",
                    **{"aria-labelledby": id}
                )(*self.get("menu_items")),
            ),
        )

        card = html.Div(class_="card shadow mb-4")(
            header, html.Div(class_="card-body")(*self.args)
        )

        if self.get("footer") is not None:
            card = card(*card.args, html.Div(class_="card-footer")(self.get("footer")))

        return card


class TableCard(boots.Boot):
    def __init__(self, items, title=""):
        self.items = items
        self.title = title

    def build(self):
        if len(self.items) > 0:
            headers = self.items[0].public
            rows = [i.public_list for i in self.items]
        else:
            headers = []
            rows = []

        table = boots.Table(_headers=headers, _rows=rows)

        return DropdownCard(table, title=self.title)


class TVMarketWidget(boots.Boot):
    def __init__(self, name, symbols):
        self.name = name
        self.symbols = symbols

    def build(self):
        opts = {
            "width": "100%",
            "height": min(550, 50 + len(self.symbols) * 50),
            "symbolsGroups": [
                {
                    "name": self.name,
                    "originalName": self.name,
                    "symbols": [
                        {"name": symbol["name"], "displayName": symbol["displayName"]}
                        for symbol in self.symbols
                    ],
                }
            ],
            "showSymbolLogo": True,
            "colorTheme": "light",
            "isTransparent": False,
            "locale": "en",
        }

        return html.Div(class_="tradingview-widget-container")(
            html.Div(class_="tradingview-widget-container__widget"),
            html.Script(
                type="text/javascript",
                src="https://s3.tradingview.com/external-embedding/embed-widget-market-quotes.js",
                _async=True,
            )(json.dumps(opts)),
        )
