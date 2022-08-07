from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from dependencies import get_album_repo, get_db, get_artist_repo, get_song_repo
from repositories.music_repositories import AlbumRepo, ArtistRepo, SongRepo
from schemas.music_schemas import AlbumInDB, ArtistInDB, SongInDB

router = APIRouter(
    prefix="",
    tags=["Music Store"]
)

# Endpoint /music-store/api/v1/singers/: Retorna lista de artistas
@router.get("/singers/", status_code=status.HTTP_200_OK)
async def get_all_singers(
    db: Session = Depends(get_db),
    repo: ArtistRepo = Depends(get_artist_repo)
) -> List[ArtistInDB]:
    return await repo.get_all_singers(db=db)

# Endpoint /music-store/api/v1/singers/ID/: Retorna albumes de un artista
@router.get("/singers/{id}/", status_code=status.HTTP_200_OK)
async def get_singer_albums(
    id: int,
    db: Session = Depends(get_db),
    repo: AlbumRepo = Depends(get_album_repo)
) -> List[AlbumInDB]:
    return await repo.get_singer_albums(db=db, id=id)

# Endpoint /music-store/api/v1/albums/ID/: Retorna canciones de un album
@router.get("/albums/{id}/", status_code=status.HTTP_200_OK)
async def get_album_songs(
    id: int,
    db: Session = Depends(get_db),
    repo: SongRepo = Depends(get_song_repo)
) -> List[SongInDB]:
    return await repo.get_album_songs(db=db, id=id)

# Endpoint /music-store/api/v1/singer/ID/: Retorna canciones de un artista
@router.get("/singer/{id}/", status_code=status.HTTP_200_OK)
async def get_singer_songs(
    id: int,
    db: Session = Depends(get_db),
    repo: SongRepo = Depends(get_song_repo)
) -> List[SongInDB]:
    return await repo.get_singer_songs(db=db, id=id)

# Endpoint /music-store/api/v1/song/ID/: Retorna datos de una cancion
@router.get("/song/{id}/", status_code=status.HTTP_200_OK)
async def get_song(
    id: int,
    db: Session = Depends(get_db),
    repo: SongRepo = Depends(get_song_repo)
) -> SongInDB:
    return await repo.get_song(id=id, db=db)