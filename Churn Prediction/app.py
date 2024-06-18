from flask import Flask, request, jsonify
from src.inference_pipeline import InferencePipeline
from flask_cors import CORS

inference_obj = InferencePipeline()
app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = inference_obj.predict(data)
    return jsonify({
                    "STATUS" : f"{prediction}"
                    })

if __name__ == '__main__':
    app.run(
            host="0.0.0.0", 
            port=5001
            )