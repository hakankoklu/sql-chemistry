from random import randint, choice
import datetime

import yaml


def get_static_data():
    try:
        Loader = yaml.CSafeLoader
    except AttributeError:
        Loader = yaml.SafeLoader
    filename = 'sample_data.yaml'
    with open(filename, 'rb') as yaml_stream:
        data = yaml.load(yaml_stream, Loader=Loader)
    return data


def get_dob(start, end):
    day_limits = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = randint(start, end)
    month = randint(1, 12)
    day = randint(1, day_limits[month - 1])
    return datetime.date(year, month, day)


def get_random_timestamp(start, end):
    seconds = randint(0, int((end - start).total_seconds()))
    return start + datetime.timedelta(0, seconds)


def get_start_end(start_range, end_range):
    return get_random_timestamp(*start_range), get_random_timestamp(*end_range)


def get_sessions(start, end, session_num_range, session_fill):
    session_num = randint(*session_num_range)
    total_time = int((end - start).total_seconds())
    total_work_time = int(total_time * session_fill)
    ave = total_work_time // session_num
    session_lengths = [randint(ave // 2, 2 * ave) for _ in range(session_num)]
    ave_interval = total_time // session_num

    session_starts = [ave_interval // 2 + ave_interval * ind + randint(-1 * ses_len // 2,
                                                                       ses_len // 2)
                      for ind, ses_len in enumerate(session_lengths)]
    return [(start + datetime.timedelta(seconds=ses_start),
             start + datetime.timedelta(seconds=ses_start + ses_len))
            for ses_start, ses_len in zip(session_starts, session_lengths)]


def get_finished(chance):
    return randint(1, 100) <= chance


def get_people(num):
    return list(set([randint(1, 100) for _ in range(num)]))


def get_people_in_range(rrange):
    return get_people(randint(*rrange))


def get_writer_sessions(session_count, writers):
    return [choice(writers) for _ in range(session_count)]


def run_query(stmt, engine):
    with engine.begin() as conn:
        result = conn.execute(stmt)
    return result.fetchall()
