from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from config_db import Base

class Artists(Base):
    __tablename__ = 'artists'

    ArtistId = Column(Integer, primary_key=True, index=True)
    Name = Column(String)

class Albums(Base):
    __tablename__ = 'albums'

    AlbumId = Column(Integer, primary_key=True, index=True)
    Title = Column(String)
    ArtistId = Column(ForeignKey("artists.id"))

class Songs(Base):
    __tablename__ = 'tracks'
    TrackId = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    AlbumId = Column(ForeignKey("albums.id"))
    MediaTypeId = Column(ForeignKey("media_types.id"))
    GenreId = Column(ForeignKey("genre.id"))
    Composer = Column(String)
    Milliseconds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(Numeric)