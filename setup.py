import os
from pathlib import Path

def create_folders_and_files():
    # Folder and file structure
    structure = {
        "app.py": "from flask import Flask, render_template, request\nfrom utils import process_data\napp = Flask(__name__)\n\n@app.route('/', methods=['GET', 'POST'])\ndef index():\n    if request.method == 'POST':\n        project_details = request.form['project_details']\n        architecture_desc = request.form['architecture_desc']\n        # Process files\n        uploaded_files = request.files.getlist('screenshots')\n        architecture_image = request.files['architecture_image']\n        # Gather descriptions\n        screenshot_descs = request.form.getlist('screenshot_desc')\n\n        # Generate the dictionary\n        result = process_data(project_details, uploaded_files, screenshot_descs, architecture_image, architecture_desc)\n        return render_template('index.html', result=result)\n    return render_template('index.html', result=None)\n\nif __name__ == '__main__':\n    app.run(debug=True)\n",
        "utils.py": "def process_data(project_details, uploaded_files, screenshot_descs, architecture_image, architecture_desc):\n    result = {\n        'YouTube_video_script': f'Script based on: {project_details}',\n        'YouTube_video_description': f'Description based on: {project_details}',\n        'readme_file': f'README content based on: {project_details}',\n        'blog_article': f'Blog based on: {project_details}'\n    }\n    return result\n",
        "prompt_templates.py": "# Placeholder for prompt templates\n",
        ".env": "# Environment variables\nFLASK_ENV=development\nSECRET_KEY=supersecretkey\n",
        "config/config.yaml": "settings:\n  debug: true\n",
        "templates/index.html": """<!DOCTYPE html>\n<html>\n<head>\n    <title>Project Submission</title>\n</head>\n<body>\n    <div style="display: flex;">\n        <div style="width: 50%; padding: 10px;">\n            <form method="POST" enctype="multipart/form-data">\n                <h3>Project Details</h3>\n                <textarea name="project_details" rows="4" cols="50" placeholder="Enter project details"></textarea><br><br>\n\n                <h3>Screenshots</h3>\n                <input type="file" name="screenshots" multiple><br><br>\n                <textarea name="screenshot_desc" rows="2" cols="50" placeholder="Describe each screenshot"></textarea><br><br>\n\n                <h3>Architecture Diagram</h3>\n                <input type="file" name="architecture_image"><br><br>\n                <textarea name="architecture_desc" rows="4" cols="50" placeholder="Describe the architecture diagram"></textarea><br><br>\n\n                <button type="submit">Generate</button>\n            </form>\n        </div>\n        <div style="width: 50%; padding: 10px;">\n            {% if result %}\n                <h3>Generated Outputs</h3>\n                <p><strong>YouTube Video Script:</strong> {{ result['YouTube_video_script'] }}</p>\n                <p><strong>YouTube Video Description:</strong> {{ result['YouTube_video_description'] }}</p>\n                <p><strong>README File:</strong> {{ result['readme_file'] }}</p>\n                <p><strong>Blog Article:</strong> {{ result['blog_article'] }}</p>\n            {% endif %}\n        </div>\n    </div>\n</body>\n</html>\n""",
        "static/": None,
        "static/js/": None,
        "static/images/": None,
        "logs/__init__.py": "import logging\n\nlogging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')\nlogger = logging.getLogger(__name__)\n"
    }

    for path, content in structure.items():
        if path.endswith('/'):
            os.makedirs(path, exist_ok=True)
        else:
            folder = os.path.dirname(path)
            if folder:
                os.makedirs(folder, exist_ok=True)
            with open(path, 'w') as f:
                if content:
                    f.write(content)
    print("Setup complete. All files and folders have been created.")

if __name__ == "__main__":
    create_folders_and_files()
