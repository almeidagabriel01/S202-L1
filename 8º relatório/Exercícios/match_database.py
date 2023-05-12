class MatchDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, id, name):
        query = "CREATE (:Player {id: $id, name: $name})"
        parameters = {"id": id, "name": name}
        self.db.execute_query(query, parameters)

    def create_match(self, id, result):
        query = "CREATE (:Match {id: $id, result: $result})"
        parameters = {"id": id, "result": result}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_matches(self, id):
        query = "MATCH (p:Player)<-[:POSSUI]-(m:Match) WHERE m.id = $id RETURN p.name AS name, m.result AS match_result"
        parameters = {"id": id}
        results = self.db.execute_query(query, parameters)
        return [(result["name"], result["match_result"]) for result in results]
    
    def get_player_matches(self, player_name):
        query = "MATCH (p:Player)<-[:POSSUI]-(m:Match) WHERE p.name = $player_name RETURN m.result AS match_result"
        parameters = {"player_name": player_name}
        results = self.db.execute_query(query, parameters)
        return [(result["match_result"]) for result in results]

    def update_player(self, old_name, new_name):
        query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)
        
    def update_match(self, id, new_result):
        query = "MATCH (m:Match {id: $id}) SET m.result = $new_result"
        parameters = {"id": id, "new_result": new_result}
        self.db.execute_query(query, parameters)
    
    def insert_match_player(self, match_id, player_names):
        query = "MATCH (m:Match {id: $match_id}) MATCH (p:Player) WHERE p.name IN $player_names CREATE (m)-[:POSSUI]->(p)"
        parameters = {"match_id": match_id, "player_names": player_names}
        self.db.execute_query(query, parameters)

    def delete_player(self, name):
        query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
    
    def delete_match(self, id):
        query = "MATCH (m:Match {id: $id})-[:POSSUI]->(p:Player) DETACH DELETE m"
        parameters = {"id": id}
        self.db.execute_query(query, parameters)