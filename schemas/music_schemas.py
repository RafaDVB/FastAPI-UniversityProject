from typing import Text
from pydantic import BaseModel

class ArtistBase(BaseModel):
    name: Text

class AlbumBase(BaseModel):
    title: Text

class SongBase(BaseModel):
    name: Text
    composer: Text
    milliseconds: int
    bytes: int
    unitprice: float

# Obtener artista
class ArtistInDB(ArtistBase):
    id: int
    name: Text

# Obtener album
class AlbumInDB(AlbumBase):
    id: int
    title: Text
    artistid: int

# Obtener cancion
class SongInDB(SongBase):
    id: int
    name: Text
    albumid: int
    mediatypeid: int
    genreid: int
    composer: Text
    milliseconds: int
    bytes: int
    unitprice: float