from flask import Flask
import models
from resources.users import users_api


app = Flask(__name__)
app.register_blueprint(users_api, url_prefix = '/api/v1')


@app.route('/')
def index():
    return("This Web App is Under Development, Please Visit http://github.com/vetronus/simple-user-api")

if __name__ == '__main__':
    models.initialize()
    app.run(debug=True)
