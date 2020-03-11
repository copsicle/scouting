#!/usr/bin/env python
__author__ = "Gonen Cohen"
import psycopg2 as psql
from Objects import *
from datetime import datetime as dt
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT as AC
from getpass import getpass


def connect_to_database(name, user, password, host="127.0.0.1", port="5432"):
    """
    Connect to a Postgres database
    :param name: Name of the database
    :param user: PostgreSQL user
    :param password: Database users password
    :param host: Database address
    :param port: The port Postgres is running in
    All of the above are strings
    :return: Database connection
    """
    return psql.connect(f"dbname={name} user={user} password={password} host={host} port={port}")


def create_new_database(name, user, password):  # , scname
    """
    Creates the working database if it doesn't exist already
    The database is created by logging into the default database 'postgres' and creating through there
    :param name: Desired database name
    :param user: Desired owner of said database (user must exist already)
    :param password: Password of the user (user must have a password, the default 'postgres' account does not)
    :return: Database connection
    """
    with connect_to_database("postgres", user, password) as dab, dab.cursor() as curs:
        dab.set_isolation_level(AC)
        curs.execute(f"CREATE DATABASE {name} OWNER {user};")
    # with connect_to_database(name, user, password) as dab, dab.cursor() as curs:
    #     create_schema(curs, scname, user)
    return connect_to_database(name, user, password)


def check_database(dbname, user, password):  # , scname
    """
    Check if the desired database exists already and if not calls create_new_database()
    getpass() asks to input the user password safely
    :param dbname: Desired database name
    :param user: Desired owner of database
    :param password: Password of the database owner
    :return: Database connection
    """
    if password == "":
        password = getpass("Input Postgres password: ")
    try:
        # with connect_to_database(dbname, user, passw) as dab, dab.cursor() as curs:
        #    create_schema(curs, scname, user)
        return connect_to_database(dbname, user, password)
    except psql.OperationalError:
        print(f"{dbname} doesn't exist, creating a new database")
        return create_new_database(dbname, user, password)  # , scname


def create_schema(curs, name, user):
    """
    Create a new database schema (basically a directory for tables), used for sorting by year and competition
    :param curs: Database cursor
    :param name: Desired schema username
    :param user: Desired schema owner
    """
    curs.execute(f"CREATE SCHEMA IF NOT EXISTS {name} AUTHORIZATION {user};")


def translate_to_schema(name, year=dt.now().year):
    """
    Generates a name for a schema, every schema is a competition for a specific season
    :param name: The name of the competition you want the schema for
    :param year: The desired year of the schema
    :return: Schema name
    """
    dic = {
        "ISR District 1": "ISRD1",
        "ISR District 2": "ISRD2",
        "ISR District 3": "ISRD3",
        "ISR District 4": "ISRD4",
        "ISR District Championship": "ISRDCMP",
        "Detroit Championship": "DETCMP",
        "Houston Championship": "HOCMP",
        "Test Competition": "TEST",
        "Templates": "TEMP"
        }
    if name in dic.keys():
        return dic[name] + "_" + str(year)


def translate_to_table(gametype, gameid):
    """
    Generates a name for a table, every table is a specific game in a type of game
    :param gametype: The type of the game
    :param gameid: The number of the game
    :return: Table name
    """
    dic = {
        "Practice": "PRTC",
        "Qualification": "QUAL",
        "Playoff": "PLYF",
        "Test": "TEST",
        "Template": "TEMP"
    }
    if type in dic.keys():
        return dic[gametype] + "_" + str(gameid)


def get_template_list(year):
    """
    Gets all columns and types required for a table template of a specific year
    :param year: The year of the season you want (int)
    :return: Dictionary where the key is the name of the column and the value is the type (both strings)
    """
    template_list = {}
    # Get EventWrapper parameters
    for params in inspect.signature(EventWrapper).parameters:
        if params and params not in template_list.keys():
            if params not in EventWrapper.datatypes.keys(): continue
            template_list.update({params: EventWrapper.datatypes[params]})
    # Get all parameters from a specific season
    for season in Seasons:
        if season.year == year:
            for mem, ber in inspect.getmembers(season, inspect.isclass):
                if params := inspect.signature(ber).parameters:
                    for par in params:
                        if par not in template_list.keys():
                            if par not in ber.datatypes.keys(): continue
                            template_list.update({par: ber.datatypes[par]})
    return template_list


def create_template(year, templist, cu, user, name="templates"):
    create_schema(cu, name, user)
    query = f"CREATE TABLE {name}.TEMP_{year}("
    for i, l in templist.items():
        query += f"{i} {l.upper()},"
    query = query[:-1]
    query += ");"
    print(query)
    return query


if __name__ == "__main__":
    with check_database("scouting", "gonen", "4590") as db, db.cursor() as cur:
        try:
            db.autocommit = True
            create_template(2020, get_template_list(2020), cur, "gonen")
        except Exception as e:
            print(e)
