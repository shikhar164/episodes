#!/usr/bin/python3
"""."""
import json
from pytvdbapi import api
DB_OB = api.TVDB('B43FF87DE395DF56')
EPI_JSON = {}


def get_episodes_json(show_name):
    """."""
    result = DB_OB.search(show_name, 'en')
    show = result[0]
    no_of_seasons = len(show)
    for index in range(1, no_of_seasons):
        EPI_JSON[show_name.title() + ' Season ' + str(index)] = []
    for index in range(1, no_of_seasons):
        season = show[index]
        no_of_episodes = len(season)
        for ep_index in range(1, no_of_episodes + 1):
            episode = season[ep_index]
            s_number = season.season_number
            e_number = episode.EpisodeNumber
            if s_number < 10:
                s_number = '0' + str(s_number)
            if e_number < 10:
                e_number = '0' + str(e_number)
            EPI_JSON[show_name.title() + ' Season ' + str(season.season_number)].append(
                'S' + str(s_number) + 'E' +
                str(e_number) + ' ' + str(episode.EpisodeName))
    with open(show_name.title() + '_episodes.json', 'w+') as jsonfile:
        jsonfile.write(json.dumps(EPI_JSON, indent=4))


if __name__ == '__main__':
    SHOW_NAME = input('Enter the show name: ')
    get_episodes_json(SHOW_NAME)
