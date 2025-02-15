from src.prompt_templates import (
    youtube_script_prompt,
    youtube_description_prompt,
    readme_file_prompt,
    blog_1_prompt,
    blog_2_prompt,
    architecture_prompt,
    demo_video_prompt
)
import json

def process_data(project_details, youtube_link, github_link, blog_link, screenshot_details, architecture_details):

    result = {
        'youtube_script_prompt': get_youtube_script_prompt(project_details, screenshot_details, architecture_details),
        'youtube_description_prompt': get_youtube_description_prompt(project_details, github_link, blog_link),
        'readme_file_prompt': get_readme_file_prompt(project_details, github_link, blog_link) + "\n\n" + get_demo_prompt(screenshot_details) + "\n\n" + get_architecture_prompt(architecture_details),
        'blog_1_prompt': get_blog_1_prompt(project_details, youtube_link, github_link, blog_link, screenshot_details, architecture_details),
        'blog_2_prompt': get_blog_2_prompt(project_details, screenshot_details),
        'architecture_prompt': get_final_architecture_prompt(project_details, architecture_details),
        'demo_video_prompt': demo_video_prompt + project_details
    }

    # for key, value in result.items():
    #     result[key] = invoke_llm([{"role": "user", "content": value}])
    
    return result

def get_blog_2_prompt(project_details, screenshot_details):
    if screenshot_details != []:
        return blog_2_prompt + f"Project details: {project_details}\n\n" + get_demo_prompt(screenshot_details)
    return "No demo details provided"

def get_final_architecture_prompt(project_details, architecture_details):
    if archiecture_exists(architecture_details):
        return architecture_prompt + f"Project details: {project_details}\n\n" + get_architecture_prompt(architecture_details)
    return "No architecture details provided"

def get_youtube_script_prompt(project_details, screenshot_details, architecture_details):
    return (
        youtube_script_prompt 
        + project_details
    )


def get_youtube_description_prompt(project_details, github_link, blog_link):
    return (
        youtube_description_prompt
        + project_details
        + f"\n\n- GitHub link: {github_link}"
        + f"\n\n- Blog article link: {blog_link}"
    )


def get_readme_file_prompt(project_details, github_link, blog_link):
    return (
        readme_file_prompt
        + project_details
        + f"\n\n- GitHub link: {github_link}"
        + f"\n\n- Blog article link: {blog_link}"
    )


def get_blog_1_prompt(project_details, youtube_link, github_link, blog_link, screenshot_details, architecture_details):   
    return (
        blog_1_prompt
        + project_details
        + f"\n\n- YouTube link: {youtube_link}"
        + f"\n\n- GitHub link: {github_link}"
        + f"\n\n- Blog article link: {blog_link}"
        + "\n\n" + get_demo_prompt(screenshot_details)
        # + "\n\n" + architecture_details
    )


def get_demo_prompt(screenshot_details):
    screenshots = [
        {"name": screenshot.get("file_name", "No file name provided"), 
         "description": screenshot.get("description", "No description provided")}
        for screenshot in screenshot_details
    ]
    demo_json = {"screenshots": screenshots}
    return f"```json\n{json.dumps(demo_json, indent=4)}\n```"

def archiecture_exists(architecture_details):
    if architecture_details:
        architecture = architecture_details[0]
        return architecture.get("description", "No description provided") != "No description provided"
    else:
        return False

def get_architecture_prompt(architecture_details):
    if architecture_details:
        architecture = architecture_details[0]
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

import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.environ.get('TOKEN')
HOST = os.environ.get('HOST')
client = OpenAI(
    api_key = TOKEN,
    base_url = f"{HOST}/serving-endpoints"
)
LLM_PARAMS = {
  "temperature" : 0.2,
  "model"  : os.environ.get('MODEL')
}

def invoke_llm( messages):

    llm_params = LLM_PARAMS
    llm_params.update({"messages": messages, "stream": False})

    chat_completion = client.chat.completions.create(**llm_params)

    return chat_completion.choices[0].message.content

def invoke_llm_stream( messages):

    llm_params = LLM_PARAMS
    llm_params.update({"messages": messages, "stream": True})

    chat_completion = client.chat.completions.create(**llm_params)

    for chunk in chat_completion:
        content = chunk.choices[0].delta.content
        if content:
            yield content