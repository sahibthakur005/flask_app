from flask import Flask, request, jsonify
import base64
import rembg
import numpy as np
from PIL import Image
from io import BytesIO
app = Flask(__name__)

@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'message': 'No file part in the request'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    # Convert image file to byte array
    # using rembg
    #input_image = Image.open(file)
    #input_array = np.array(input_image)
    #output_array = rembg.remove(input_array)
    #output_image = Image.fromarray(output_array)
    #buffered = BytesIO()
    #output_image.save(buffered, format='JPEG')
    #img_str_bytes = base64.b64encode(buffered.getvalue())
    





    input_array = file.read()
    output_array = rembg.remove(input_array)

    img_str_bytes = base64.b64encode(output_array)
    image_byte_array = img_str_bytes.decode("utf-8")


    # Construct the response with message and byte array
    response_data = {
        'message': 'Image uploaded successfully as byte array',
        'image_byte_array': image_byte_array if image_byte_array else None
    }

    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 
