# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Ninja:
    def __init__( self , data ):
        self.idninja = data['idninja']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_iddojo = data['dojo_iddojo']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        # Create an empty list to append our instances of friends
        ninjas = []
        # Iterate over the db results and create instances of friends with cls.
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas
    
    @classmethod
    def save(cls, data):
        query = """INSERT INTO ninjas (first_name, last_name, age, dojo_iddojo) 
        VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_iddojo)s);"""
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
    
    @classmethod
    def delete(cls, user_id):
        query = "DELETE FROM ninjas WHERE id = %(id)s"
        data = {"id": user_id}
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return cls(result[0])
    
    @classmethod
    def update(cls,data):
        query = "UPDATE ninjas SET first_name=%(first_name)s, last_name=%(last_name)s, age=%(age)s, updated_at=NOW(), dojo_iddojo=%(dojo)s WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)