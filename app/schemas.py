from pydantic import BaseModel

class DoramaBase(BaseModel):
    titulo: str
    genero: str
    episodios: int
    status: str

class DoramaCreate(DoramaBase):
    pass

class DoramaOut(DoramaBase):
    id: int

    class Config:
        orm_mode = True
