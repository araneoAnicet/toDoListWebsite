from src.models import  sql_db
from src.api.routes import api_blueprint
from src.admin.routes import admin, admin_blueprint
from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config['SECRET_KEY'] = 'some_secret_key'

with app.app_context():
    admin.init_app(app)
    sql_db.init_app(app)

app.register_blueprint(api_blueprint, url_prefix='/api')
app.register_blueprint(admin_blueprint)

if __name__ == '__main__':
    app.run(debug=True)

