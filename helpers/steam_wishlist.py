import requests
import argparse


# use https://steamidfinder.com/ to get steamid from username
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--steam-id",
                        dest='steam_id',
                        help="Provide your steam ID")
    return parser.parse_args()


def scrap_wishlist(steamid):
    page_number = 0
    games_list = []

    while True:
        page = requests.get(
            f'https://store.steampowered.com/wishlist/profiles/{steamid}/wishlistdata/?p={page_number}'
        ).json()

        if len(page) < 2:
            break

        games_list.extend(value['name'] for value in page.values())

        page_number += 1

    return sorted(games_list)


if __name__ == '__main__':
    arguments = get_arguments()
    for game in scrap_wishlist(arguments.steam_id):
        print(game)