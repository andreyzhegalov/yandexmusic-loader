from yandex_music import Client
from .TrackDataMaker import TrackDataMaker


class YandexMusicLoader:
    __client = None
    __track_data_maker = None

    def __init__(self, token: str):
        self.__client = Client(token).init()
        self.__track_data_maker = TrackDataMaker(self.__client)

    def load_my_favourite(self) -> None:
        print("loading ...")
        tracks = self.__client.users_likes_tracks()

        track_ids = []
        for track in tracks:
            track_ids.append(track.id)
        self.load_by_track_ids(track_ids)

    def load_album(self, album_id: int):
        album = self.__client.albums_with_tracks(album_id)
        track_ids = []
        for volume in album.volumes:
            if (len(volume) == 0):
                print("album " + album.title + " don't has any volumes")
                return
            for track in volume:
                track_ids.append(track.id)
        self.load_by_track_ids(track_ids)

    def load_user_playlist(self, title: str):
        playlists = self.__client.users_playlists_list()
        kind = None
        for songs in playlists:
            if (songs.title == title):
                kind = songs.kind
        if (kind == None):
            raise KeyError('playlist "' + title + '" dont found')

        playlist = self.__client.users_playlists(kind)
        print('load from "' + playlist.title + '" playlist')
        track_ids = []
        for track in playlist.tracks:
            track_ids.append(track.id)
        self.load_by_track_ids(track_ids)

    def load_by_track_ids(self, track_ids: list):
        track_infos = self.__track_data_maker.make_track_info(track_ids)
        tracks = self.__client.tracks(track_ids)

        for track in tracks:
            track_id = track.id
            track_info = self.__find_track_info(track_id, track_infos)
            file_name = self.__make_track_file_name(track_info)
            print('load ' + file_name)
            track.download("result/" + file_name)

    def __find_track_info(self, track_id, track_infos):
        for track_info in track_infos:
            if (track_info.id == track_id):
                return track_info

    def __make_track_file_name(self, track_info):
        return track_info.artist + "-" + track_info.title + ".mp3"
