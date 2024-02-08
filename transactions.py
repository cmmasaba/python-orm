from sqlalchemy import text

from create_engine import engine

'''The Connection is a proxy object that represents a single dbapi connection.
The connection is then used to access the DB and run transactional queries on it.
This returns a Result object that has the results of the query
Alternatively you can use a begin one block that automatically commits successful transactions and rolls back failed ones
with engine.begin() as conn:
    statements
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
    for row in result:
        print(f'{row.age}-year old {row.firstname} {row.secondname}, from {row.city}, {row.state}.') # print the results
    conn.commit() # commit the transaction to the db