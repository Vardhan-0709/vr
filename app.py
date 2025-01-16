from flask import Flask, request, jsonify
import base64
import io
from PIL import Image
import open3d as o3d

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_image():
    image_data = request.form['image']
    image_data = image_data.split(',')[1]  # Remove base64 prefix
    image_bytes = base64.b64decode(image_data)
    
    image = Image.open(io.BytesIO(image_bytes))
    image.save('captured_image.png')  # Save the image temporarily
    
    # Process image and generate isometric view (replace with actual 3D modeling)
    isometric_image = generate_isometric_view('captured_image.png')

    return jsonify({'isometricView': isometric_image})

def generate_isometric_view(image_path):
    # Placeholder for the actual 3D model processing
    # Here we will just return a dummy image URL
    return 'http://localhost:5000/static/isometric_view.png'

if __name__ == '__main__':
    app.run(debug=True)
