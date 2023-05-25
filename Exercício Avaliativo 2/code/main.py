from database import Database
from query import Query
from teacher_crud import TeacherCRUD
from cli import TeacherCLI

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://18.212.11.72:7687", "neo4j", "defense-divider-aviation")

# Criando uma instância da classe Query e  para interagir com o banco de dados
query_db = Query(db)
teacher_db = TeacherCRUD(db)

# Questão 1
print(query_db.renzo())
print(query_db.starts_with_m())
print(query_db.cities())
print(query_db.schools())

# Questão 2
print(query_db.ano_nasc())
print(query_db.population())
print(query_db.cep())
print(query_db.teacher())

# Questão 3
teacherCLI = TeacherCLI(teacher_db)
teacherCLI.run()

# Fechando a conexão com o banco de dados
db.close()