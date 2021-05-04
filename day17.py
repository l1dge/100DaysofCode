import pytest
from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = namedtuple("Game", "title link")


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    feed = feedparser.parse(FEED_URL)
    game_list = ()
    if feed:
        for item in feed["items"]:
            game_list = (*game_list, Game(item["title"], item["link"]))
        return game_list

    else:
        print("Nothing found in feed", FEED_URL)


games = get_games()


def test_assert_number_of_entries():
    assert len(games) == 30


def test_all_list_items_are_namedtuples():
    assert all(isinstance(game, tuple) for game in games)


def test_assert_all_links_contain_store():
    assert all("store.steampowered.com" in game.link for game in games)


def test_title_and_url_first_entry():
    first_game = games[0]
    assert first_game.title == "Midweek Madness - RiME, 33% Off"
    assert first_game.link == "http://store.steampowered.com/news/31695/"


def test_title_and_url_last_entry():
    last_game = games[-1]
    assert last_game.title == "Now Available on Steam - Loco Dojo, 35% off!"
    assert last_game.link == "http://store.steampowered.com/news/31113/"


get_games()

test_assert_number_of_entries()
test_all_list_items_are_namedtuples()
test_assert_all_links_contain_store()
test_title_and_url_first_entry()
test_title_and_url_last_entry()