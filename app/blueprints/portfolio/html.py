import bootlets.html as html
import bootlets.boots as boots

from app.html import DropdownCard, TVMarketWidget


def fmt_num(num):
    return f"{num:,.5f}"[:5]


class PortfolioCard(boots.Boot):
    def __init__(self, portfolio, create_asset_form):
        self.portfolio = portfolio
        self.create_asset_form = create_asset_form

    def build(self):
        symbols = [
            {
                "name": asset.symbol.ticker,
                "displayName": f"{asset.symbol.ticker} ({fmt_num(asset.volume)} @ {fmt_num(asset.price)}) [{fmt_num(asset.cost)}]",
            }
            for asset in self.portfolio.assets
        ]
        content = TVMarketWidget(self.portfolio.name, symbols)
        modal = boots.Modal(boots.QuickForm(self.create_asset_form), title="Add Asset")
        add_asset_button = boots.ModalButton(_id=modal.get("_id"), _text="Add asset")

        return DropdownCard(
            html.Container(content.build(), modal.build()),
            title=self.portfolio.name,
            footer=add_asset_button.build(),
        )
