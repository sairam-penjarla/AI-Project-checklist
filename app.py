import os
from flask import Flask, render_template, request, jsonify, send_file
from PIL import Image
from src.thumbnail_handler import ThumbnailHandler  # Import the ThumbnailHandler class
from src.utils import process_data

app = Flask(__name__)

# Initialize ThumbnailHandler
mockup_folder = "static/thumbnails"
output_folder = "./output_thumbnail"
chrome_coordinates = (316, 231)
safari_coordinates = (316, 205)
chrome_width = 1288
safari_width = 1288

thumbnail_handler = ThumbnailHandler(mockup_folder, output_folder, chrome_coordinates, safari_coordinates, chrome_width, safari_width)

chrome_coordinates = (316, 100)
safari_coordinates = (316, 100)
thumbnail_handler_arch = ThumbnailHandler(mockup_folder, output_folder, chrome_coordinates, safari_coordinates, chrome_width, safari_width)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/submit-project', methods=['POST'])
def submit_project():
    try:
        # Extract basic project details
        project_details = request.form.get('project_details', '')
        youtube_link = request.form.get('youtube_link', '<PASTE LINK HERE>')
        github_link = request.form.get('github_link', '<PASTE LINK HERE>')
        blog_link = request.form.get('blog_link', '<PASTE LINK HERE>')

        # Process screenshot details
        screenshot_details = []
        index = 1
        while True:
            # Extract file name and description for each screenshot
            screenshot_file_name = request.form.get(f'screenshot_file_{index}')
            screenshot_description = request.form.get(f'screenshot_desc_{index}')
            
            if not screenshot_file_name and not screenshot_description:
                break  # Stop processing if no more screenshots are found
            
            screenshot_details.append({
                "file_name": screenshot_file_name,
                "description": screenshot_description
            })
            index += 1

        # Process architecture details
        architecture_details = []
        index = 1
        while True:
            # Extract file name and description for each architecture diagram
            architecture_file_name = request.form.get(f'architecture_file_{index}')
            architecture_description = request.form.get(f'architecture_desc_{index}')
            
            if not architecture_file_name and not architecture_description:
                break  # Stop processing if no more architecture diagrams are found
            
            architecture_details.append({
                "file_name": architecture_file_name,
                "description": architecture_description
            })
            index += 1

        result = process_data(
            project_details,
            youtube_link,
            github_link,
            blog_link,
            screenshot_details,
            architecture_details
        )

        # Return result as JSON
        return jsonify(result=result), 200
    except Exception as e:
        # Handle errors gracefully
        return jsonify({'error': str(e)}), 500



@app.route('/generate_thumbnail', methods=['POST'])
def generate_thumbnail():
    if 'screenshot' not in request.files:
        return jsonify({'error': 'No screenshot file provided.'}), 400

    screenshot_file = request.files['screenshot']

    try:
        # Open the uploaded screenshot
        screenshot_image = Image.open(screenshot_file).convert("RGBA")
        # Generate the thumbnail using ThumbnailHandler
        output_path, error = thumbnail_handler.process_screenshot(screenshot_image)

        if error:
            return jsonify({'error': error}), 500

        # Send the generated image back to the client
        return send_file(output_path, mimetype='image/png')

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/generate_thumbnail_arch', methods=['POST'])
def generate_thumbnail_arch():
    if 'screenshot' not in request.files:
        return jsonify({'error': 'No screenshot file provided.'}), 400

    screenshot_file = request.files['screenshot']

    try:
        # Open the uploaded screenshot
        screenshot_image = Image.open(screenshot_file).convert("RGBA")
        # Generate the thumbnail using ThumbnailHandler
        output_path, error = thumbnail_handler_arch.process_screenshot(screenshot_image)

        if error:
            return jsonify({'error': error}), 500

        # Send the generated image back to the client
        return send_file(output_path, mimetype='image/png')

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
