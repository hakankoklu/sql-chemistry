from sqlalchemy import create_engine, select, func
from sqlalchemy.engine.url import URL

import settings
import tables
import utils

engine = create_engine(URL(**settings.DATABASE))


def get_all_persons_in_town_sa_core():
    stmt = select([tables.Person])
    return utils.run_query(stmt, engine)


def get_all_persons_names_in_town_sa_core():
    stmt = select([tables.Person.c.name])
    return utils.run_query(stmt, engine)


def get_youngest_persons_dob():
    stmt = select([func.min(tables.Person.c.date_of_birth)])
    return utils.run_query(stmt, engine)


def get_youngest_persons_name():
    min_age = select([func.min(tables.Person.c.date_of_birth).label('date_of_birth')])\
        .alias('some_alias')
    stmt = select([tables.Person.c.name]).select_from(
        tables.Person.join(min_age, tables.Person.c.date_of_birth == min_age.c.date_of_birth)
    )
    return utils.run_query(stmt, engine)


def get_youngest_persons_name2():
    ordered_age = select(
        [tables.Person.c.name,
         func.row_number().over(order_by=tables.Person.c.date_of_birth).label('row_no')])\
        .alias('some_alias')
    stmt = select([ordered_age.c.name]).where(ordered_age.c.row_no == 1)
    return utils.run_query(stmt, engine)
