youtube_script_prompt = """
    
Task: You are a YouTube scriptwriting assistant helping craft a 10-minute, engaging and structured video for Sairam’s data science channel. the script should be fast pased, strictly business and no nonsence

Specifics (each bullet contains key sections to focus on):

1. Introduction (30 Seconds):
    - start the video by saying “in this video I'll be walking through step bystep how to build …..”
    - use continuation lines such as “what we're building today is a little bit more improved version of other projects i’ve shown on this channel” etc so that user will understand that there are more things they need to explore on this channel
    - Address how the project adds value to resumes, enhances career prospects, and keeps them ahead of trends.
    - explain about all the features very quickly.

1. Quick Demo (2 minutes):
    1. Show a quick demo of the project
    2. here inform the users that the code for this project is available in my github repo and they can visit my blog page to understand the code in more detail.
    3. Add a sense of urgency or FOMO using trending data science topics to make the project feel essential.
    4. lure students and job seekers by saying something like “and if you're looking to take automations a little further and you want some Hands-On learning experience and help then feel free to reach out to me either in the comments, or on my social media”
    5. then talk about who I am and then talk about my website.
        - Use impactful metrics like:
            - “I’ve been a data scientist for XYZ years.”
            - “I’ve delivered XYZ projects internationally.”
            - “I’ve worked with XYZ clients globally.”
        - Highlight that the channel focuses on actionable data science projects.
        - they can visit my website  where they will find a detailed roadmap for freshers
        - End with a strong hook emphasizing Sairam’s success in helping freshers land jobs through his projects.
    6. then lure in companies saying something like "and then if you're sort of a small business or you're looking to have me Implement these systems for you have me build them out for you then please feel free to reach out to me via the comment or my social media or on email or on my website”
2. code walkthrough

Note:

- Create a structured, conversational script with clear voice modulation instructions (e.g., “Pause here,” “Lower voice,” “Stress this point”).
- Use Indian English expressions (e.g., “See,” “Ok here we go,” “However”).
- Break the script into smaller subchapters with:
    - A title and bullet points for on-screen text.
    - Corresponding dialogue for narration.
1. Closing Remarks:
    - Write a thoughtful conclusion thanking the audience.
    - Include a call-to-action: “If you’ve learned something new today, don’t forget to hit that like button and comment below—let me know your thoughts or if you have any questions. Also, if you haven't already, subscribe to the channel for more projects like this. Thank you so much for your support, and if you’ve made it this far, I really appreciate it. Stay tuned for more videos, and as always, happy coding!”
    - Close with something like If you’ve made it this far into the video, thank you so much for your support. happy coding.
    

Youtuber: name: Sai Ram, he is a data scientist with expertise in building solutions with expertise in Computer vision and Natural Language Processing. he is currently working on Gen AI projects. Just like this project, you can find more and more projects on his website. link will be in the description. You can follow him on github, linkedin and instagram

Project details:
"""

youtube_description_prompt = """
        
### Task

Using the project details given to you, fill the given template by writing a hook and a video description. other than that, keep everything else as it is.

exmaple:
hook example: Are you a student, employee, or small business owner looking to enhance your resume, upskill for better career opportunities, or implement AI solutions into your business? This project is perfect for you!

description example: 📘 In this video, we dive deep into creating an AI-powered chatbot integrated with a knowledge base that pulls information directly from PDF documents. Whether you're looking to build a cutting-edge project for your portfolio or implement AI into your business workflow, this is the ideal hands-on project to showcase your skills!


Template:

```
<write a hook here>

<write a description of the video here>

📘 Check out the project repository and blog for more details:  
🔗GitHub repository: https://github.com/sairam-penjarla/pdf-rag-ai-chatbot.git  
🔗Blog post: https://psairam9301.wixsite.com/website/post/building-a-rag-application-part-1

📘 About the Channel:  
↪︎Hi, I'm Sai Ram, a data scientist passionate about teaching AI, Machine Learning, and NLP. I share practical projects, tutorials, and insights to help you build your portfolio, enhance job readiness, and find AI solutions for businesses.

📘 Follow Me on Social Media:

🔗 YouTube: https://www.youtube.com/@sairampenjarla  
🔗 GitHub: https://github.com/sairam-penjarla  
🔗 LinkedIn: https://www.linkedin.com/in/sairam-penjarla-b5041b121/  
🔗 Instagram: https://www.instagram.com/sairam.ipynb

📘 Roadmap for Freshers:  
If you're just starting out, check out the roadmap for freshers. It will guide you through key steps in building a solid foundation in the tech field.
↪︎https://psairam9301.wixsite.com/website/roadmap.


📘 Additional Learning Resources:  
For detailed beginner tutorials on Python, SQL, OpenAI, Deep Learning, and more, visit this page: [Beginner Tutorials and Blogs](https://sairampenjarla.notion.site/171d56a2fc278091bee4c3cb99bbbe30?v=6fb5c52d1a074305adb293b2c026026f).

📘 Timestamps:

0:00 - Introduction

🙏🏼 Thank you so much for using our platform and for watching this video! Don't forget to subscribe and follow along with the tutorial on the channel.  
↪︎ @sairampenjarla  

🙏🏼 If there is anything I missed, or if you have more questions, drop a comment below, and we will respond ASAP! Let me know more tutorial ideas as well!

#DataScience #MachineLearning #AI #ArtificialIntelligence #DeepLearning #DataAnalytics #Coding #SoftwareDevelopment #TechProjects #DataVisualization #DataEngineering #NLP #NaturalLanguageProcessing #Python #OpenSource #TechTutorials #TechSkills #AIProjects #DataScienceProjects #AIForBusiness #TechSolutions #AIChatbot #MLProjects #ML #TechEducation #AICommunity #DataScienceLife #AIResearch #DataScienceLife #AIAlgorithms #TechInnovation #AIApplications #TechWorld
```

### Project details:
"""

readme_file_prompt = """
    
Task: You are an AI assisstant tasked with writing a detailed README.md file for a GitHub project of sairam penjarla. The README.md file should have buttons, instructions, project details, and relevant links.

Specifics:

1. Start the README.md file with four buttons like this:

```jsx
# [![Website](https://img.shields.io/badge/Website-Visit-brightgreen)](https://psairam9301.wixsite.com/website) [![YouTube](https://img.shields.io/badge/YouTube-Subscribe-red)](https://www.youtube.com/@sairampenjarla) [![GitHub](https://img.shields.io/badge/GitHub-Explore-black)](https://github.com/sairam-penjarla) [![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/sairam-penjarla-b5041b121/) [![Instagram](https://img.shields.io/badge/Instagram-Follow-ff69b4)](https://www.instagram.com/sairam.ipynb/)
```
use the same links given above.

2. After the buttons, include a title for the project.
3. In the next section, provide instructions for how to clone the GitHub repository, change directories, and set up the project environment. Include:
    - Instructions for cloning the repository using the `git clone` command.
    - Instructions for navigating to the cloned directory using `cd`.
    - A link to the blog post on your website where you teach how to create a virtual environment (or Anaconda environment): [Link to Blog Post](https://sairampenjarla.notion.site/Environment-171d56a2fc2780dd9efcd4cef331fa2c).
    - Instructions to create a virtual environment or an Anaconda environment.
    - Instructions for installing dependencies using the `requirements.txt` file.
    - Steps for running the project using Python.
3. In the following section, provide details about the project itself, explaining its purpose and main functionalities. Here’s what you’ve mentioned:
    - The project is a [insert description of the project here].
    - It has features such as [list of key features].
    - You should explain what problem it solves or how it can be used by others.
4. In the final section, include a link to a blog post on your website that explains the project in more detail:

project details:
    
"""

overview_prompt = """
    
### Task

You are a content writer tasked with writing a blog article for a project using the guidelines below. 
This project is very helpful for students and freshers who want to land a job by adding more weight to their portfolio or working employees who want to upskill themselves and land a better job.
The blog should include the specified sections and adhere to the formatting rules.

### Sections

1. Project Overview
2. YouTube Video
3. Use Cases
4. Installation Instructions
5. Future Work
6. Conclusion

### Guidelines

The blog must:
- Be written in proper format with appropriate headings (`#`, `##`, `###`, etc.).
- Use concise, engaging paragraphs to ensure readability.
- Be detailed enough to inform but concise enough to retain the reader’s interest.
- Separate each section with a ---

#### Section Details

- Project Overview:
  - Provide a detailed description of the project, its purpose, and its key features.
  - Highlight the technologies used and the unique benefits the project offers.
  - Highlight how this project will help the readers upskill themselves as well as impress the recruiters

- YouTube Video:
  - There is a detailed youtube video as well about this same project on my channel. Encourage the readers to first checkout that video as well before reading the article
  - Include a short introduction to the YouTube video.
  - Provide the video link as a Markdown hyperlink.

- Use Cases:
  - Describe real-world applications of the project.
  - Use structured subheadings and concise paragraphs for each use case.

- Installation Instructions:
  - Provide step-by-step guidance for setting up and running the project.
  - Format commands in Markdown code blocks.
  - Include the following steps:
    1. Cloning the repository (`git clone` command).
    2. Navigating to the project directory (`cd` command).
    3. Setting up a virtual environment or Anaconda environment.
        - Include this helpful blog link that will help them understand how to setup virtual environments: [Learn VirtualEnv Basics](https://sairampenjarla.notion.site/Environment-171d56a2fc2780dd9efcd4cef331fa2c).
    4. Installing dependencies using `requirements.txt`.
    5. Running the project using Python command.

- Future Work:
  - Outline potential improvements or additional features to enhance the project.
  - Explain how this project can me bought to production level

- Conclusion:
  - Summarize the project’s impact, usability, and potential.



### Project Details

The content writer should use the provided project details and additional links to create the blog as per the structure outlined above.


"""

demo_prompt = """
    
### Task

You are a content writer tasked with creating the Demo Section for a blog article. You will be provided with the names of screenshots and their respective details. Your goal is to structure the content clearly and effectively.

---

### Guidelines

The Demo Section should:
- Be written in proper format with appropriate headings (#, ##, ###) and subheadings.
- Use subsections to describe each screenshot in detail.
- Include concise and engaging descriptions of the screenshots.
- Use proper placeholders to include the screenshots. Assume the image files are stored in the same directory.

---

You will receive:
- The names of the screenshots (e.g., `home_page.png`, `dashboard.png`).
- A brief description of what each screenshot represents.


### Example Input

```json
{
  "screenshots": [
    {"name": "home_page.png", "description": "The home page provides navigation to all sections of the application."},
    {"name": "login_page.png", "description": "The login page allows users to securely log in using their credentials."},
    {"name": "profile_page.png", "description": "The profile page displays user information and preferences."}
  ]
}
```
---

### Example Output

## Demo

Below are the key screenshots of the project, showcasing its functionality and features:

### Home Page
`<PASTE IMAGE HERE>`

The Home Page serves as the central hub of the application. It provides users with quick access to the main features, including navigation links and a search bar.

### User Registration
`<PASTE IMAGE HERE>`

This screenshot demonstrates the registration form, allowing new users to sign up with their details, including name, email, and password.

### Dashboard
`<PASTE IMAGE HERE>`

The dashboard displays user-specific data and provides insights through interactive charts and widgets.

### Settings Page
`<PASTE IMAGE HERE>`

The settings page enables users to customize their preferences, update their profiles, and manage notifications.

---

### Input:

"""

architecture_prompt = """
    
### Task

You are a content writer tasked with creating the Architecture Diagram Section for a blog article. You will be provided with the architecture diagram's name and its description. Your goal is to write the section clearly and effectively in Markdown format.

---

### Guidelines

The Architecture Diagram Section should:
- Be written in proper Markdown format with appropriate headings.
- Include a brief description of the architecture diagram, explaining its components and how they interact.
- Use proper Markdown image syntax to display the architecture diagram.

---

You will receive:
- The name of the architecture diagram (e.g., `architecture_diagram.png`).
- A brief description of the architecture and its components.

---
### Input:
```json
{
  "diagram": "architecture_diagram.png",
  "description": "This diagram illustrates the communication flow between the frontend, backend, database, API layer, and external services. The frontend interacts with the backend through the API, while the backend manages data stored in the database and communicates with external services."
}
```

### output

## Architecture Diagram

Below is the architecture diagram of the project, illustrating the various components and their interactions:

`<PASTE IMAGE HERE>`

This diagram represents the overall system architecture, showing the flow of data between various modules. It includes the following components:

- Frontend: The user interface where users interact with the application.
- Backend: The server that processes requests and communicates with the database.
- Database: Stores all the data related to users, content, and configurations.
- API Layer: Facilitates communication between the frontend and backend.
- External Services: Integrates with third-party services like payment gateways or analytics tools.

---

### Input:
"""