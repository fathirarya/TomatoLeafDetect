from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
app.secret_key = 'supersecretkey'

# Load the Keras model
model = load_model('tomato_model_vgg16_25-06.h5')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def predict_image(filepath):
    # Load and preprocess the image
    img = image.load_img(filepath, target_size=(224, 224))  # Adjust the target size to match your model input
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize the image data

    # Make predictions
    prediction = model.predict(img_array)
    # Convert the predictions to a human-readable format
    labels_dir = "tomato_fix/train"
    class_labels = sorted(os.listdir(labels_dir))
    predicted_class = class_labels[np.argmax(prediction)]
    return predicted_class

@app.route('/api/predict', methods=['POST'])
def api_predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        prediction_result = predict_image(filepath)
        return jsonify({'filename': filename, 'prediction': prediction_result}), 200
    else:
        return jsonify({'error': 'Allowed file types are png, jpg, jpeg, gif'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)