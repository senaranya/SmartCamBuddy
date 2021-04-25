from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
import os

from smarcambuddy.exposure import Exposure

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
ma = Marshmallow(app)

# TODO:
#  Add exposure APIs
#  Install on Raspi
#  Test with Android app


# GET exposure
@app.route('/current_exposure', methods=['GET'])
def get_current_exposure():
    return jsonify(Exposure.get_current_exposure())

# PUT exposure

# Run server
if __name__ == '__main__':
    app.run(debug=True)
