from sqlalchemy import Column, Integer, String
from .database import Base

class Dorama(Base):
    __tablename__ = "doramas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    genero = Column(String)
    episodios = Column(Integer)
    status = Column(String)  # Ex: "Assistindo", "Concluído", etc.


