# TomatoLeafDetect

## Overview

TomatoLeafDetect is a machine learning-based application for detecting diseases in tomato leaves. This project uses image classification techniques to identify various diseases affecting tomato plants, helping farmers and gardeners quickly diagnose plant health issues.

## Features

- **Disease Detection**: Identifies various tomato leaf diseases from images
- **User-friendly Interface**: Easy-to-use application for uploading and analyzing leaf images
- **Fast Results**: Quick processing and classification of uploaded images
- **High Accuracy**: Trained model with high precision in disease identification

## Technologies Used

- TensorFlow/Keras for model development
- Python for backend processing
- Image processing libraries (OpenCV, PIL)
- Flask for API development (if applicable)

## Installation

```bash
# Clone the repository
git clone https://github.com/fathirarya/TomatoLeafDetect.git

# Navigate to the project directory
cd TomatoLeafDetect

# Install required dependencies
pip install -r requirements.txt
```

## Usage

1. Prepare your tomato leaf image for analysis
2. Run the application:
   ```bash
   python app.py
   ```
3. Upload the leaf image through the interface
4. View the detection results and disease classification

## Model Information

The disease detection model was trained on a comprehensive dataset of tomato leaf images with various disease conditions including:
- Early Blight
- Late Blight
- Bacterial Spot
- Target Spot
- Mosaic Virus
- Yellow Leaf Curl Virus
- Healthy leaves

The model architecture uses convolutional neural networks (CNN) optimized for plant disease detection.

## Project Structure

```
TomatoLeafDetect/
├── app.py                 # Main application file
├── models/                # Contains trained model files
├── data/                  # Data processing scripts and utilities
├── static/                # Static files for web interface (if applicable)
├── templates/             # HTML templates (if applicable)
├── utils/                 # Utility functions
├── requirements.txt       # Required Python packages
└── README.md              # Project documentation
```

## Contributing

Contributions to improve TomatoLeafDetect are welcome! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

- Developer: Fathir Arya
- GitHub: [fathirarya](https://github.com/fathirarya)

## Acknowledgements

- Plant Village Dataset for training images
- TensorFlow and Keras communities
- Contributors and supporters of the project
