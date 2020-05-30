from src.routes import mod as api_routes
from flask import Flask

app = Flask(__name__)

app.register_blueprint(api_routes, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)

