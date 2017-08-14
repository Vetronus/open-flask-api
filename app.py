from flask import Flask
import models
import os
from resources.users import users_api


app = Flask(__name__)
app.register_blueprint(users_api, url_prefix = '/api/v1')


@app.route('/')
def index():
    return("This Web App is Under Development, Please Visit http://github.com/vetronus/simple-user-api")

if __name__ == '__main__':
    models.initialize()
    # app.run(debug=True)
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
