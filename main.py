import os
from flask import (Flask, render_template,
                   flash, session, request,
                   redirect, url_for)
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import NumberRange
from helpers.steam_wishlist import scrap_wishlist

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'secret_key'


class SteamidForm(FlaskForm):
    steam_id = IntegerField(
        'SteamID',
        validators=[NumberRange(message='Only numbers allowed')])
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
        return redirect(url_for('scan_steam'))
    else:
        flash('Wishlist is scanned', 'success')
    return render_template('wishlist.html', games=games)


if __name__ == '__main__':
    app.run()
