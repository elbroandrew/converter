from initialize import app
from views import auth_api



app.register_blueprint(auth_api)

if __name__ == '__main__':

    app.run(host="127.0.0.1", debug=True, port=5005)  #TODO: do not forget to turn off for the deploying