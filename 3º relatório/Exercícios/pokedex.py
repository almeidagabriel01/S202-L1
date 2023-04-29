from database import Database
from helper.writeAJson import writeAJson

class Pokedex:
    def __init__(self, db_name, collection_name):
        self.db = Database(db_name, collection_name)
    
    def get_pokemons_by_type(self, types):
      pokemons = self.db.collection.find({"type": {"$in": types}})
      writeAJson(pokemons, "pokemons_by_type")
      count = self.db.collection.count_documents({"type": {"$in": types}})
      print(f"Saved {count} pokemons by type {types}")
        
    def get_pokemons_by_name_or_id(self, name_or_id):
        pokemons = self.db.collection.find({ "$or": [{"name": name_or_id}, {"id": name_or_id}]})
        writeAJson(pokemons, "pokemons_by_name_or_id.json")
        count = self.db.collection.count_documents({ "$or": [{"name": name_or_id}, {"id": name_or_id}]})
        print(f"Saved {count} pokemons by name or id {name_or_id}")
    
    def get_pokemons_by_weakness(self, weaknesses):
        pokemons = self.db.collection.find({ "weaknesses": {"$in": weaknesses} })
        writeAJson(pokemons, "pokemons_by_weakness.json")
        count = self.db.collection.count_documents({ "weaknesses": {"$in": weaknesses} })
        print(f"Saved {count} pokemons by weakness {weaknesses}")
    
    def get_pokemons_by_type_and_weakness(self, type, weaknesses):
        pokemons = self.db.collection.find({ "type": type, "weaknesses": {"$in": weaknesses} })
        writeAJson(pokemons, "pokemons_by_type_and_weakness.json")
        count = self.db.collection.count_documents({ "type": type, "weaknesses": {"$in": weaknesses} })
        print(f"Saved {count} pokemons by type {type} and weakness {weaknesses}")
    
    def get_pokemons_by_candy(self, candy_amount):
        pokemons = self.db.collection.find({ "candy_count": {"$lte": candy_amount} })
        writeAJson(pokemons, "pokemons_by_candy.json")
        count = self.db.collection.count_documents({ "candy_count": {"$lte": candy_amount} })
        print(f"Saved {count} pokemons by candy amount {candy_amount}")