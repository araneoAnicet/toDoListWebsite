from src.routes import api_blueprint, sql_db
from flask import Flask


app = Flask(__name__)
sql_db.init_app(app)

app.register_blueprint(api_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)

