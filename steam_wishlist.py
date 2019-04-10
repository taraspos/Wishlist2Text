import urllib.request
import json


# use https://steamidfinder.com/ to get steamid from username
def scrap_wishlist(steamid):
    page_number = 0
    games_list = []

    while True:
        page = urllib.request.urlopen(
            f'https://store.steampowered.com/wishlist/profiles/{steamid}/wishlistdata/?p={page_number}'
        ).read()
        result = json.loads(page)

        if len(result) == 0:
            break

        for _, value in result.items():
            games_list.append(value['name'])

        page_number += 1

    return games_list


if __name__ == '__main__':
    for game in scrap_wishlist('76561198049351440'):
        print(game)
