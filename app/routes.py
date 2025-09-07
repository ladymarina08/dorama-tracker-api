from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import SessionLocal, engine

router = APIRouter()

# Criar as tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)

# Dependência para obter uma sessão de banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Rota inicial
@router.get('/')
def home():
    return {"mensagem": "API dorama funcionando!"}


# Criar dorama
@router.post('/doramas', response_model=schemas.DoramaOut)
def adicionar_dorama(dorama: schemas.DoramaCreate, db: Session = Depends(get_db)):
    novo_dorama = models.Dorama(**dorama.dict())
    db.add(novo_dorama)
    db.commit()
    db.refresh(novo_dorama)
    return novo_dorama


# Listar todos os doramas
@router.get('/doramas', response_model=list[schemas.DoramaOut])
def listar_doramas(db: Session = Depends(get_db)):
    return db.query(models.Dorama).all()


# Buscar dorama por ID
@router.get('/doramas/{dorama_id}', response_model=schemas.DoramaOut)
def buscar_dorama(dorama_id: int, db: Session = Depends(get_db)):
    dorama = db.query(models.Dorama).filter(models.Dorama.id == dorama_id).first()
    if dorama is None:
        raise HTTPException(status_code=404, detail="Dorama não encontrado")
    return dorama


# Atualizar dorama
@router.put('/doramas/{dorama_id}', response_model=schemas.DoramaOut)
def atualizar_dorama(dorama_id: int, dados: schemas.DoramaCreate, db: Session = Depends(get_db)):
    dorama = db.query(models.Dorama).filter(models.Dorama.id == dorama_id).first()
    if dorama is None:
        raise HTTPException(status_code=404, detail="Dorama não encontrado")
    
    for key, value in dados.dict().items():
        setattr(dorama, key, value)
    
    db.commit()
    db.refresh(dorama)
    return dorama


# Deletar dorama
@router.delete('/doramas/{dorama_id}')
def deletar_dorama(dorama_id: int, db: Session = Depends(get_db)):
    dorama = db.query(models.Dorama).filter(models.Dorama.id == dorama_id).first()
    if dorama is None:
        raise HTTPException(status_code=404, detail="Dorama não encontrado")
    
    db.delete(dorama)
    db.commit()
    return {"mensagem": "Dorama deletado com sucesso!"}
