from flask import Flask, render_template, flash, session, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired
from helpers.steam_wishlist import scrap_wishlist

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'


class SteamidForm(FlaskForm):
    steam_id = IntegerField('SteamID', validators=[DataRequired()])
    submit = SubmitField('Scan')


@app.route('/', methods=['GET', 'POST'])
def scan_steam():
    form = SteamidForm()
    if form.validate_on_submit():
        session['steam_id'] = request.form['steam_id']
        return redirect(url_for('wishlist_to_text'))
    return render_template('steamid.html', form=form)


@app.route('/wishlist')
def wishlist_to_text():
    games = scrap_wishlist(session['steam_id'])
    if not games:
        flash('Was not able to scan wishlist', 'danger')
    else:
        flash('Wishlist is scanned', 'success')
    return render_template('wishlist.html', games=games)


if __name__ == '__main__':
    app.run()