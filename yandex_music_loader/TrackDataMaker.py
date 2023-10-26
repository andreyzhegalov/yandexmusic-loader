from yandex_music import Client
from yandex_music_loader.TrackInfo import TrackInfo


class TrackDataMaker:
    __client = None

    def __init__(self, client: Client):
        self.__client = client

    def make_track_info(self, track_ids: list) -> TrackInfo:
        track_infos = self.__client.tracks(track_ids)
        result = []
        for info in track_infos:
            t = TrackInfo()
            t.id = info.id
            t.title = self.__make_title(info)
            t.artist = self.__make_artist(info)
            result.append(t)

        return result

    def __make_artist(self, info):
        if (len(info.artists) == 0):
            return "undefined"
        return info.artists[0].name

    def __make_title(self, info):
        if (info.title == None):
            return "undefined"
        return info.title
