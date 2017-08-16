from sqlalchemy import create_engine, select
from sqlalchemy.engine.url import URL

import settings
import utils


engine = create_engine(URL(**settings.DATABASE))


def get_all_persons():
    sql = """
    select *
    from literator.person
    """
    return utils.run_query(sql, engine)


def get_all_persons_names():
    sql = """
    select name
    from literator.person
    """
    return utils.run_query(sql, engine)


def get_youngest_persons_dob():
    sql = """
    select min(date_of_birth)
    from literator.person
    """
    return utils.run_query(sql, engine)


def get_youngest_persons_name():
    sql = """
    with min_age as
    (select min(date_of_birth) as date_of_birth
    from literator.person)
    select name
    from literator.person pp
    inner join min_age
    on pp.date_of_birth = min_age.date_of_birth
    """
    return utils.run_query(sql, engine)


def get_youngest_persons_name2():
    sql = """
        with ordered_age as
        (select name
            , row_number() over (order by date_of_birth asc) as row_no
        from literator.person)
        select name
        from ordered_age
        where row_no = 1
        """
    return utils.run_query(sql, engine)
