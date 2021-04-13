from pydantic import BaseModel
from typing import Optional, List


class user (BaseModel):    
    id: Optional[str] = None
    nome: str
    telefone: str
    meus_podutos: List[Produtos]
    minhas_vendas: List[Pedido]
    meus_pedidos: List[Pedido]


class Produto(BaseModel):
    usuario: Usuario
    id: Optional[str] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
  
  
  
class Pedido(BaseModel):
    id: Optional[str] = None
    usuario = Usuario
    produto = Produto
    quantidade = int
    entrega: boll = True
    endereco: str 
    observacoes: Optional[str] = "Sem observações"


    