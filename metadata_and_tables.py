from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey

from create_engine import engine

metadata = MetaData()

user_table = Table(
    "user_account",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String(30)),
    Column('full name', String),
)

address_table = Table(
    'address',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('userid', ForeignKey('user_account.id'), nullable=False),
    Column('email_address', String, nullable=False),
)