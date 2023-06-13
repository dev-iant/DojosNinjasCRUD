from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
# model the class after the friend table from our database
class Dojo:
    def __init__( self , data ):
        self.iddojo = data['iddojo']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
        self.ninjas = []
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def save(cls, data):
        query = """INSERT INTO dojos (name, created_at, updated_at) 
        VALUES (%(name)s, NOW(), NOW());"""
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data) 
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM dojos WHERE iddojo = %(iddojo)s"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
    
    @classmethod
    def get_one(cls,iddojo):
        query = "SELECT * FROM dojos WHERE iddojo = %(iddojo)s"
        data = {'iddojo': iddojo}
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return cls(result[0])
    
    @classmethod
    def update(cls,data):
        query = "UPDATE dojos SET name=%(name)s, updated_at=NOW();"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
    
    @classmethod
    def join(cls, data):
        query = """
        SELECT *
        FROM dojos
        LEFT JOIN ninjas
        ON dojos.iddojo = ninjas.dojo_iddojo
        WHERE ninjas.dojo_iddojo = %(iddojo)s;"""
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        dojo = cls(results[0])
        for row in results:
            student_data = {
                "idninja": row["idninja"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "age": row["age"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"],
                "dojo_iddojo": row["dojo_iddojo"]
            }
            dojo.ninjas.append(ninja.Ninja(student_data))
        return dojo