from random import randint

import datetime
from sqlalchemy import create_engine, select, func
from sqlalchemy.engine.url import URL

import settings
import utils
import tables

engine = create_engine(URL(**settings.DATABASE))
tables.create_all(engine)

data = utils.get_static_data()

with engine.begin() as conn:
    for book in data['books']:
        ins = tables.Book.insert().values(title=book)
        conn.execute(ins)

ins = tables.Person.insert()
values = []
for person in data['persons']:
    dob = utils.get_dob(1980, 2010)
    values.append({'name': person, 'date_of_birth': dob})

with engine.begin() as conn:
    conn.execute(ins, values)

ins = tables.Write.insert()
with engine.begin() as conn:
    for ind, _ in enumerate(data['books']):
        writers = utils.get_people_in_range([5, 10])
        writing_start_end = utils.get_start_end([datetime.datetime(2015, 1, 1),
                                                 datetime.datetime(2015, 6, 30)],
                                                [datetime.datetime(2017, 7, 1),
                                                 datetime.datetime(2017, 12, 31)])
        seshes = utils.get_sessions(writing_start_end[0], writing_start_end[1], [30, 50], 0.25)
        writer_sessions = utils.get_writer_sessions(len(seshes), writers)
        values = []
        for sesh, writer in zip(seshes, writer_sessions):
            values.append({'book_id': ind + 1, 'person_id': writer, 'start_time': sesh[0],
                           'end_time': sesh[1], 'finished': False})
        values[-1]['finished'] = utils.get_finished(90)
        conn.execute(ins, values)

s = select([tables.Write.c.book_id, func.min(tables.Write.c.end_time)])\
    .group_by(tables.Write.c.book_id)
with engine.begin() as conn:
    books_available = conn.execute(s).fetchall()

ins = tables.Read.insert()
with engine.begin() as conn:
    for b_id, finish_time in books_available:
        readers = utils.get_people_in_range([20, 100])
        for reader in readers:
            reading_start = utils.get_random_timestamp(finish_time,
                                                       finish_time + datetime.timedelta(days=1000))
            reading_time = randint(7, 60)
            reading_end = reading_start + datetime.timedelta(days=reading_time)
            seshes = utils.get_sessions(reading_start, reading_end, [10, 50], 0.1)
            values = []
            for sesh in seshes:
                values.append({'book_id': b_id, 'person_id': reader, 'start_time': sesh[0],
                               'end_time': sesh[1], 'finished': False})
            values[-1]['finished'] = utils.get_finished(95)
            conn.execute(ins, values)
