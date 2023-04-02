from database import Database
from writeAJson import writeAJson
from bookModel import BookModel
from cli import BookCLI

db = Database(database="relatorio_05", collection="livros")
bookModel = BookModel(database=db)


bookCLI = BookCLI(bookModel)
bookCLI.run()