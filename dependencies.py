from tokenize import Single
from typing import final
from config_db import SessionLocal
from repositories.music_repositories import AlbumRepo, ArtistRepo, SongRepo

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_artist_repo():
    return ArtistRepo()

def get_album_repo():
    return AlbumRepo()

def get_song_repo():
    return SongRepo()