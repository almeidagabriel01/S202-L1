from database import Database
from match_database import MatchDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.202.162.218:7687", "neo4j", "hygiene-beam-curves")
db.drop_all()

# Criando uma instância da classe MatchDatabase para interagir com o banco de dados
match_db = MatchDatabase(db)

# Criando players
match_db.create_player(1, "Alice")
match_db.create_player(2, "Bob")
match_db.create_player(3, "Charlie")

# Criando matches
match_db.create_match(1, "Alice wins")
match_db.create_match(2, "Charlie wins")
match_db.create_match(3, "Draw")

# Atualizando o nome de um player
match_db.update_player("Bob", "Pedro")

match_db.insert_match_player(1, ["Alice", "Pedro"])
match_db.insert_match_player(2, ["Alice", "Charlie"])
match_db.insert_match_player(3, ["Pedro", "Charlie"])

# Deletando um player
match_db.delete_player("Alice")

# Atualizando resultado da partida
match_db.update_match(1, "Pedro wins")

# Deletando uma partida
match_db.delete_match(3)

# Imprimindo os players
print("Players:")
print(match_db.get_players())

# Imprimindo uma partida específica
print("Partida:")
print(match_db.get_matches(2))

# Imprimindo histórico de partidas de um jogador
print("Partidas:")
print(match_db.get_player_matches("Pedro"))

# Fechando a conexão com o banco de dados
db.close()