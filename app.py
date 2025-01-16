from flask import Flask, render_template, request
from utils import process_data

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        project_details = request.form.get('project_details', '')
        youtube_link = request.form.get('youtube_link', '<PASTE LINK HERE>')
        github_link = request.form.get('github_link', '<PASTE LINK HERE>')
        blog_link = request.form.get('blog_link', '<PASTE LINK HERE>')

        screenshot_details = process_file_details(
            request.files.getlist('screenshots'),
            request.form.get('screenshot_desc', '')
        )
        architecture_details = process_file_details(
            [request.files.get('architecture_image')],
            request.form.get('architecture_desc', '')
        )

        # Process data using utils
        result = process_data(
            project_details,
            youtube_link,
            github_link,
            blog_link,
            screenshot_details,
            architecture_details
        )

    return render_template('index.html', result=result)


def process_file_details(files, description):
    """
    Combine file names with the description into a single string.
    """
    if not files or not description:
        return ""

    file_names = [file.filename for file in files if file]
    combined_details = f"Files: {', '.join(file_names)} | Description: {description}"
    return combined_details


if __name__ == '__main__':
    app.run(debug=True)
