from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
import numpy as np

app = Flask(__name__)
CORS(app)


@app.route('/transpose', methods=["POST"])
def homepage():
    data = request.json
    result = None
    error = ""
    try:
        mat = data["matrix"]
        mat = np.array(mat)
        result = mat.T.tolist()
        error = ""
    except KeyError as e:
        error = "Key %s not found" % (str(e))
        pass
    except Exception as e:
        error = str(e)
        pass
    return jsonify({"result": result, "error": error})


app.run()
