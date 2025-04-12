from flask import Flask
from flask_cors import CORS
from routes.predict import predict_route

app = Flask(__name__)
CORS(app)

# Register blueprint
app.register_blueprint(predict_route, url_prefix='/predict')



if __name__ == '__main__':
    app.run(port=5000, debug=True)

