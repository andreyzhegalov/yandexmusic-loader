import sys
import os
from yandex_music_loader import YandexMusicLoader
import argparse

TOKEN = os.environ.get('TOKEN')


def __get_id(args):
    id = args.id
    if (id == None):
        raise ValueError('please, set --id argument')
    return id


def __get_title(args):
    title = args.title
    if (title == None):
        raise ValueError('please, set --title argument')
    return title


def main() -> int:
    parser = argparse.ArgumentParser(description='Скачивание треков ... ')
    parser.add_argument(
        'source', type=str, choices=['favourite', 'track', 'album', 'playlist'], help='источник. варианты')
    parser.add_argument(
        '--id', type=int, dest='id', help='идентификатор для трека или альбома')
    parser.add_argument(
        '--title', type=str, dest='title', help='название playlist')
    args = parser.parse_args()

    music_loader = YandexMusicLoader(TOKEN)

    source = args.source
    if (source == 'track'):
        id = __get_id(args)
        music_loader.load_by_track_ids([id])
    elif (source == 'album'):
        id = __get_id(args)
        music_loader.load_album(id)
    elif (source == 'favourite'):
        music_loader.load_my_favourite()
    elif (source == 'playlist'):
        title = __get_title(args)
        music_loader.load_user_playlist(title)
    else:
        raise ValueError

    return 0


if __name__ == '__main__':
    sys.exit(main())
