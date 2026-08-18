from fastapi import FastAPI, Query

from produto.produto_database import ProdutosDAO
from produto.produto_model import Produto
from produto.produto_service import ProdutoService

app = FastAPI()

produtoDao = ProdutosDAO()

@app.get("/produtos")
async def buscar_nome_produtos(self,nome: str = Query(default=None)):
    produto_service = ProdutoService
    produtos = produto_service.buscar_nome_produtos(nome)
    return produtos
@app.get("/preco")
async def buscar_preco_produtos(preco: float = Query(...)):
    produtos = produtoDao.buscar_por_preco(preco)
    return produtos

@app.get("/categoria")
async def buscar_categoria_produtos(categoria: str = Query(...)):
    produtos = produtoDao.buscar_por_categoria(categoria)
    return produtos

@app.post("/")
async def criar_produto(produto: Produto):
    produto.nome = produto.nome.upper()
    produto.categoria = produto.categoria.upper()
    produto.descricao = produto.descricao.upper()
    produto_id = produtoDao.criar_produto(produto)
    return {"message": f"{produto_id}"}
