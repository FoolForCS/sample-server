import os
import psycopg2
from contextlib import contextmanager

from quart import Quart

from samples import blueprint as samples_blueprint

def create_app():
    app = Quart(__name__)
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

    @app.before_first_request
    async def create_db():
        # Use a config.py file for managing all settings centrally
        app.conn = psycopg2.connect("host=localhost dbname=postgres user=newuser password=password")
        
    app.register_blueprint(samples_blueprint)

    return app

if __name__ == '__main__':
    create_app().run()