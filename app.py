from flask import Flask, request, jsonify
import os
from model_utils import detector

app = Flask(__name__)

@app.route('/detect', methods=['POST'])
def detect():
    # Check if the file part is in the request
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
   
    # Ensure that a file is uploaded
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    try:
        # Save the file temporarily
        temp_path = "temp_image.jpg"
        file.save(temp_path)
       
        # Run detection
        results = detector.detect(temp_path)
       
        # Clean up
        os.remove(temp_path)
       
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
