from database import Database
from MotoristaDAO import MotoristaDAO
from cli import MotoristaCLI

db = Database(database="atividade_avaliativa", collection="Motoristas")
motoristaDAO = MotoristaDAO(database=db)


motoristaCLI = MotoristaCLI(motoristaDAO)
motoristaCLI.run()