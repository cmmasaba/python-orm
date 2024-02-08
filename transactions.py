from sqlalchemy import text

from create_engine import engine

'''The Connection is a proxy object that represents a single dbapi connection.
The connection is then used to access the DB and run transactional queries on it.
This returns a Result object that has the results of the query
'''
with engine.connect() as conn:
    conn.execute(
        text("INSERT INTO friend (firstname, secondname, city, state, age) VALUES (:firstname, :secondname, :city, :state, :age)"),
        [
            {"firstname":"John", "secondname":"Doe", "city":"Utawala", "state":"Nairobi", "age":25},
            {"firstname":"Jane", "secondname":"Doe", "city":"Embakasi", "state":"Nairobi", "age":25},
        ]
    )
    result = conn.execute(text("SELECT * FROM friend")) # get results of the query
    print(result.all()) # print the results
    conn.commit() # commit the transaction to the db