from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Configuration can be added here
    app.config['SECRET_KEY'] = 'your_secret_key'
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app