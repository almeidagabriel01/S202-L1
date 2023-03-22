from database import Database
from writeAJson import writeAJson

class ProductAnalyzer:
  def __init__(self, db_name, collection_name):
    self.db = Database(db_name, collection_name)
  
  def totalVendas(self):
    # Total de vendas por dia:
    result = self.db.collection.aggregate([
      {"$unwind": "$produtos"},
      {"$group": {"_id": "$data_compra","total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
      {"$sort": {"_id": 1}}
    ])
    writeAJson(result, "Total de vendas por dia")
    
  def produtoMaisVendido(self):
    # Produto mais vendo em todas as compras:
    result = self.db.collection.aggregate([
      {"$unwind": "$produtos"},
      {"$group": {"_id": "$produtos.descricao", "total_vendido": {"$sum": "$produtos.quantidade"}}},
      {"$sort": {"total_vendido": -1}},
      {"$limit": 1}
    ])
    writeAJson(result, "Produto mais vendo em todas as compras")
    
  def clienteMaisGastou(self):
    # Cliente que mais gastou em uma única compra:
    result = self.db.collection.aggregate([
      {"$unwind": "$produtos"},
      {"$group": {"_id": "$cliente_id", "total_gasto": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
      {"$sort": {"total_gasto": -1}},
      {"$limit": 1}
    ])
    writeAJson(result, "Cliente que mais gastou em uma única compra")
    
  def maisDeUmProdutoVendido(self):
    # Produtos com mais de uma unidade vendida:
    result = self.db.collection.aggregate([
      {"$unwind": "$produtos"},
      {"$match": {"produtos.quantidade": {"$gt": 1}}},
      {"$group": {"_id": "$produtos.descricao"}}
    ])
    writeAJson(result, "Produtos com mais de uma unidade vendida")