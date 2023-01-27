# connect to postgresql
from datetime import *
from flask import Flask, send_from_directory, request, jsonify
from dataclasses import dataclass
import psycopg2
import configparser
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

config = configparser.ConfigParser()
config.read('config.ini')
db_config = config['postgresql']

app = Flask(__name__, static_folder='./dist', static_url_path='')

# Host=localhost;Port=5432;Database=playground;User ID=postgres;Password='password'
app.config['SQLALCHEMY_DATABASE_URI'] = db_config['SQLALCHEMY_DATABASE_URI']

api = Api(app)
db = SQLAlchemy(app)


@dataclass
class FreightRate(db.Model):
    # specify schema and table name
    __tablename__ = 'freightrate'
    __table_args__ = {'schema': 'vue_202'}

    pk: int
    start_date: date

    pk = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime, nullable=False)


def all_rows():
    return FreightRate.query.all()


def connect():
    conn = None
    try:
        config = configparser.ConfigParser()
        config.read('config.ini')
        conn_str = db_config["connection_string"]
        print('Connecting to the PostgreSQL database...')
        print(conn_str)

        # split the connection string into arguments
        conn = psycopg2.connect(conn_str)
        cur = conn.cursor()
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)

        # query the freightrate table in the vue_202 schema
        cur.execute("SELECT * FROM vue_202.freightrate")
        results = cur.fetchall()
        cur.close()

        # print the results
        print(results)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return conn


conn = connect()
conn.close()

with app.app_context():
    db.create_all()
    print(all_rows())
