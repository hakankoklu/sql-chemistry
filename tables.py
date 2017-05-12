from sqlalchemy import MetaData, Column, Table, Integer, String, Date, ForeignKey, DateTime, Boolean


metadata = MetaData()

book = Table('book', metadata,
             Column('book_id', Integer, primary_key=True, autoincrement=True),
             Column('title', String(50), nullable=False),
             schema='literator')

person = Table('person', metadata,
               Column('person_id', Integer, primary_key=True, autoincrement=True),
               Column('name', String(20), nullable=False),
               Column('date_of_birth', Date, nullable=False),
               schema='literator'
               )

write = Table('write', metadata,
              Column('event_id', Integer, primary_key=True, autoincrement=True),
              Column('book_id', Integer, ForeignKey('literator.book.book_id'), nullable=False),
              Column('person_id', Integer, ForeignKey('literator.person.person_id')),
              Column('start', DateTime, nullable=False),
              Column('end', DateTime, nullable=False),
              Column('finished', Boolean, nullable=False),
              schema='literator')

read = Table('read', metadata,
             Column('event_id', Integer, primary_key=True, autoincrement=True),
             Column('book_id', Integer, ForeignKey('literator.book.book_id'), nullable=False),
             Column('person_id', Integer, ForeignKey('literator.person.person_id')),
             Column('start', DateTime, nullable=False),
             Column('end', DateTime, nullable=False),
             Column('finished', Boolean, nullable=False),
             schema='literator')


def create_all(engine, conn):
    conn.execute('DROP SCHEMA IF EXISTS literator CASCADE;')
    conn.execute('CREATE SCHEMA literator;')
    metadata.create_all(engine)
