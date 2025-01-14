from prompt_templates import (
    youtube_script_prompt,
    youtube_description_prompt,
    readme_file_prompt,
    overview_prompt,
    demo_prompt,
    architecture_prompt,
    installation_prompt,
    future_works_prompt,
    conclusion_prompt
)

def process_data(project_details, youtube_link, github_link, blog_link, screenshot_details, architecture_details):
    result = {
        'youtube_script_prompt': get_youtube_script_prompt(project_details),
        'youtube_description_prompt': get_youtube_description_prompt(project_details, github_link, blog_link),
        'readme_file_prompt': get_readme_file_prompt(project_details, github_link, blog_link),
        'overview_prompt': get_overview_prompt(project_details, youtube_link, github_link, blog_link),
        'demo_prompt': get_demo_prompt(screenshot_details),
        'architecture_prompt': get_architecture_prompt(architecture_details),
    }
    return result



def get_youtube_script_prompt(project_details):
    return youtube_script_prompt + project_details

def get_youtube_description_prompt(project_details, github_link, blog_link):
    return youtube_description_prompt + project_details + github_link + blog_link

def get_readme_file_prompt(project_details, github_link, blog_link):
    return readme_file_prompt + project_details + github_link + blog_link

def get_overview_prompt(project_details, youtube_link, github_link, blog_link):
    return overview_prompt + project_details + youtube_link + github_link + blog_link

def get_demo_prompt(screenshot_details):
    return demo_prompt + screenshot_details

def get_architecture_prompt(architecture_details):
    return architecture_prompt + architecture_details
