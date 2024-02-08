from sqlalchemy import create_engine

'''Create an engine that acts a central connection to a database server.
Supply the following parameters for psql:
    username:password@host:port/dbname
'''
engine = create_engine('postgresql+psycopg2://cmmasaba:postgres@localhost:5432/postgres_tutorial', echo=True, future=True)