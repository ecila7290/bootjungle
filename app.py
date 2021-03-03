import config

from flask import Flask
from flask_cors import CORS
from sqlalchemy import create_engine

from model import ProgramDao
from service import ProgramService
from view import ProgramView


class Service:
    pass

def create_app(test_config=None):
    app=Flask(__name__)
    CORS(app)

    if test_config is None:
        app.config.from_pyfile('config.py')
    else:
        app.config.update(test_config)

    database=create_engine(app.config['DB_URL'], encoding='utf-8', max_overflow=0)

    program_dao=ProgramDao(database)

    services=Service
    services.program_service=ProgramService(program_dao)

    ProgramView.create_endpoints(app, services)

    return app