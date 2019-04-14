import os

from helpers.steam_wishlist import scrap_wishlist
from flask import abort
from jinja2 import Environment, FileSystemLoader

# Capture our current directory
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Environment(loader=FileSystemLoader(THIS_DIR+"/templates/"))

def handler(request):
    steam_id = request.args.get("steam_id")
    if steam_id:
        games = scrap_wishlist(steam_id)
        return templates.get_template('wishlist.html').render(games=games)

    return templates.get_template('steamid.html').render()