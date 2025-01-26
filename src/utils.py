from src.prompt_templates import (
    youtube_script_prompt,
    youtube_description_prompt,
    readme_file_prompt,
    overview_prompt,
    demo_prompt,
    architecture_prompt
)
import json

def process_data(project_details, youtube_link, github_link, blog_link, screenshot_details, architecture_details):
    # Prepare prompts by processing individual data components
    result = {
        'youtube_script_prompt': get_youtube_script_prompt(project_details, screenshot_details, architecture_details),
        'youtube_description_prompt': get_youtube_description_prompt(project_details, github_link, blog_link),
        'readme_file_prompt': get_readme_file_prompt(project_details, github_link, blog_link) + "\n\n" + get_demo_prompt(screenshot_details) + "\n\n" + get_architecture_prompt(architecture_details),
        'overview_prompt': get_overview_prompt(project_details, youtube_link, github_link, blog_link),
        'demo_prompt': demo_prompt + f"Project details: {project_details}\n\n" + get_demo_prompt(screenshot_details),
        'architecture_prompt': architecture_prompt + f"Project details: {project_details}\n\n" + get_architecture_prompt(architecture_details),
    }
    return result


### `get_youtube_script_prompt`
def get_youtube_script_prompt(project_details, screenshot_details, architecture_details):
    return (
        youtube_script_prompt 
        + project_details 
        + "\n\n ### UI Screenshots\n" 
        + get_demo_prompt(screenshot_details) 
        + "\n\n ### Architecture diagram\n\n" 
        + get_architecture_prompt(architecture_details)
    )


#### `get_youtube_description_prompt`
def get_youtube_description_prompt(project_details, github_link, blog_link):
    return (
        youtube_description_prompt
        + project_details
        + f"\n\n- GitHub link: {github_link}"
        + f"\n\n- Blog article link: {blog_link}"
    )


#### `get_readme_file_prompt`
def get_readme_file_prompt(project_details, github_link, blog_link):
    return (
        readme_file_prompt
        + project_details
        + f"\n\n- GitHub link: {github_link}"
        + f"\n\n- Blog article link: {blog_link}"
    )


#### `get_overview_prompt`
def get_overview_prompt(project_details, youtube_link, github_link, blog_link):
    return (
        overview_prompt
        + project_details
        + f"\n\n- YouTube link: {youtube_link}"
        + f"\n\n- GitHub link: {github_link}"
        + f"\n\n- Blog article link: {blog_link}"
    )


#### `get_demo_prompt`
def get_demo_prompt(screenshot_details):
    screenshots = [
        {"name": screenshot.get("file_name", "No file name provided"), 
         "description": screenshot.get("description", "No description provided")}
        for screenshot in screenshot_details
    ]
    demo_json = {"screenshots": screenshots}
    return f"```json\n{json.dumps(demo_json, indent=4)}\n```"



#### `get_architecture_prompt`
def get_architecture_prompt(architecture_details):
    if architecture_details:
        architecture = architecture_details[0]  # Assuming a single architecture diagram
        diagram_json = {
            "diagram": architecture.get("file_name", "No file name provided"),
            "description": architecture.get("description", "No description provided")
        }
    else:
        diagram_json = {
            "diagram": "No file provided",
            "description": "No description provided"
        }
    return f"```json\n{json.dumps(diagram_json, indent=4)}\n```"
