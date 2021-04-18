from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from app import db
from app.models import Portfolio, Asset, Symbol
from app.html import Title
from bootlets.boots import QuickForm

from . import portfolio
from .forms import CreatePortfolioForm, CreateAssetForm
from .html import PortfolioCard


@portfolio.route("/<int:id>", methods=["GET", "POST"])
@login_required
def get(id):
    portf = Portfolio.query.get(id)
    if portf is None:
        abort(404)
    create_asset_form = CreateAssetForm()
    content = PortfolioCard(portf, create_asset_form)
    title = Title(portf.name)
    if create_asset_form.validate_on_submit():
        ticker = create_asset_form.symbol.data.upper()
        symbol = Symbol.query.filter_by(ticker=ticker).first()
        if symbol is None:
            symbol = Symbol(ticker=ticker)
            db.session.add(symbol)
        asset = Asset(
            user=current_user,
            portfolio=portf,
            symbol=symbol,
            price=create_asset_form.price.data,
            volume=create_asset_form.volume.data,
        )
        db.session.add(asset)
        db.session.commit()
        flash("Successfully added asset!", "success")
        return redirect(url_for("portfolio.get", id=portf.id))
    return render_template("portfolio/get.html", content=content, title=title)


@portfolio.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = CreatePortfolioForm()
    if form.validate_on_submit():
        portf = Portfolio(user=current_user, name=form.name.data)
        db.session.add(portf)
        db.session.commit()
        flash("Successfully created new portfolio!", "success")
        return redirect(url_for("portfolio.get", id=portf.id))
    return render_template("form.html", form=QuickForm(form), title="New Portfolio")
