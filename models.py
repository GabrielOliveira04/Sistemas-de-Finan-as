from sqlmodel import SQLModel, Field, create_engine, Relationship
from enum import Enum
from datetime import date



class Bancos(Enum):
    NUBANK = 'Nubank'
    SANTANDER = 'Santander'
    INTER = 'Inter'



class Status (Enum):
    ATIVO = 'Ativo'
    INATIVO = 'Inativo'


class Conta(SQLModel, table = True):
    id: int = Field(primary_key=True)
    valor: float
    banco: Bancos = Field(default= Bancos.NUBANK)
    status: Status = Field(default=Status.ATIVO)    
    

sqlite_file_name = 'database.db'
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)
 
 
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)    
    


class Tipos(Enum):
    ENTRADA = 'Entrada'
    SAIDA = 'Saida'

class Historico(SQLModel, table = True):
    id:int=Field(primary_key=True)
    conta_id: int=Field(foreign_key="conta.id")
    conta: Conta= Relationship()
    tipo: Tipos = Field(default=Tipos.ENTRADA)
    valor: float
    data: date








if __name__ == "__main__":  
    create_db_and_tables()     