from typing import List

from sqlalchemy.orm import Session
from models.music_model import Albums, Artists, Songs

from schemas.music_schemas import AlbumInDB, ArtistInDB, SongInDB

class ArtistRepo:
    # Obtener todos los artistas
    async def get_all_singers(self, db:Session) -> List[ArtistInDB]:
        singer_list: List[ArtistInDB] = db.query(Artists).all()
        return singer_list

class AlbumRepo:
    # Obtener albums por artista
    async def get_singer_albums(self, *, id:int, db:Session) -> List[AlbumInDB]:
        album_list: List[AlbumInDB] = db.query(Albums).filter(Albums.ArtistId == id).all()
        return album_list

class SongRepo:
    # Obtener canciones de un album
    async def get_album_songs(self, *, id:int, db:Session) -> List[SongInDB]:
        song_list: List[SongInDB] = db.query(Songs).filter(Songs.AlbumId == id).all()
        return song_list

    # Obtener canciones de un artista
    async def get_singer_songs(self, *, id:int, db:Session) -> List[SongInDB]:
        song_list: List[SongInDB] = db.query(Songs, Albums).join(Albums,
            Albums.AlbumId == Songs.AlbumId).filter(Albums.ArtistId == id).all()
        return song_list

    # Obtener cancion
    async def get_song(self, *, id:int, db:Session) -> SongInDB:
        song: SongInDB = db.query(Songs).get(id)
        return song