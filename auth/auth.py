from initialize import app
from views import auth_api



app.register_blueprint(auth_api)

if __name__ == '__main__':

    app.run(host="0.0.0.0", debug=False, port=5005)