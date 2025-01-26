youtube_script_prompt = """

### Task

You are a YouTube scriptwriting assistant helping craft a 10-minute, engaging, and structured video for Sairam's data science channel. The script should be fast-paced, strictly business, and no-nonsense.

This project is beneficial for students and freshers who want to land a job by enhancing their portfolios, working employees aiming to upskill for better career opportunities, and even small businesses looking to implement innovative solutions.

The script should include the specified sections and adhere to the formatting rules.

### Sections

1. Introduction
2. Quick Demo
3. Project Overview
4. Architecture Overview
5. Closing Remarks

### Guidelines

The script must:
- Be written in a structured format with appropriate headings (#, ##, ###, etc.).
- Use concise, engaging paragraphs to ensure readability and maintain the audience's attention.
- Be detailed enough to inform but concise enough to retain the viewer's interest.
- Use a casual and conversational tone to make the video engaging.
- separate each and every sub section by a ---
separate each and every sub sub sub sub sub sections like [Opening Hook][Agenda] etc using a ---
- Include expressions (e.g., “See,” “Ok here we go,” “However”) for a natural flow.
- Use continuation lines such as “what we're building today is a little bit more improved version of other projects I've shown on this channel” to indicate there is more to explore on Sairam's channel.
- Add a sense of urgency or FOMO by leveraging trending data science topics.
- if any students, freshers, working employees or small scale business want me to help them on this project, they can feel free to reach out to me.
they can visit my website  where they will find a detailed roadmap for freshers
- End with a strong hook emphasizing Sairam's success in helping freshers land jobs through his projects.

---

#### Section Details

**1. Introduction:**
- Start with a hook: “Hello everybody, this time I brought a new AI project for you…”
- Use continuation lines to emphasize that there are other exciting projects on the channel.
- Highlight how the project adds value to resumes, enhances career prospects, and keeps viewers ahead of trends.
- Explain what tools and tech stack are being used in the project and how each of them benefits students and freshers.
- Include an agenda: Inform the users that the video will first showcase a quick demo of the project, followed by an in-depth explanation of the architecture and project details.
- Briefly explain all the features to build excitement.
- Add urgency by referring to trending topics in data science.

**2. Quick Demo:**
- Provide a quick demo of the project.
- Inform viewers that the project code is available on Sairam's GitHub and that they can visit the blog for a more detailed understanding of the code.
- Motivate students and job seekers with lines like: “If you're looking to take automations further and want some hands-on learning experience, feel free to reach out to me in the comments or on social media.”
- Introduce Sairam with impactful metrics:
  - “I've been a data scientist for XYZ years.”
  - “I've delivered XYZ projects internationally.”
  - “I've worked with XYZ clients globally.”
- Emphasize the actionable data science projects on the channel.
- Mention the website's resources, such as roadmaps and skill-specific topics for freshers.
- Conclude with a hook about Sairam's success in helping freshers land jobs and suggest businesses reach out for project implementation.

**3. Project Overview:**
- Describe the project's purpose and key features in detail.
- Explain the benefits to students, freshers, working employees, and small businesses.
- Emphasize how the project aligns with trending data science skills.

**4. Architecture Overview:**
- Provide a clear and concise explanation of the project's architecture.
- Highlight the technologies used and their relevance.
- Use diagrams or visuals to support the explanation (as needed).

**5. Closing Remarks:**
- Thank the audience for watching.
- Include a call-to-action: “If you've learned something new today, don't forget to hit that like button and comment below—let me know your thoughts or if you have any questions. Also, if you haven't already, subscribe to the channel for more projects like this. Thank you so much for your support, and if you've made it this far, I really appreciate it. Stay tuned for more videos, and as always, happy coding!”
- Close with gratitude: “If you've made it this far into the video, thank you so much for your support. Happy coding!”

---

#### Additional Notes

- Ensure the video script remains engaging and informative.
- Highlight Sairam's online presence and resources:
  - Website: https://psairam9301.wixsite.com/website
  - YouTube: https://www.youtube.com/@sairampenjarla
  - GitHub: https://github.com/sairam-penjarla
  - LinkedIn: https://www.linkedin.com/in/sairam-penjarla-b5041b121/
  - Instagram: https://www.instagram.com/sairam.ipynb/


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
3. In the following section, provide details about the project itself, explaining its purpose and main functionalities. Here's what you've mentioned:
    - The project is a [insert description of the project here].
    - It has features such as [list of key features].
    - You should explain what problem it solves or how it can be used by others.
4. In the final section, include a link to a blog post on your website that explains the project in more detail:

project details:
    
"""

overview_prompt = """
    
### Task

You are a content writer tasked with writing a blog article for a project using the guidelines below. 
This project is very helpful for students and freshers who want to land a job by adding more weight to their portfolio or working employees who want to upskill themselves and land a better job. roe even for small business who would want to implement this solution into their company.

The blog should include the specified sections and adhere to the formatting rules.

### Sections

1. Project Overview
2. About me
3. YouTube Video
4. Use Cases
5. Installation Instructions
6. Future Work
7. Conclusion

### Guidelines

The blog must:
- Be written in proper format with appropriate headings (#, ##, ###, etc.).
- Use concise, engaging paragraphs to ensure readability.
- Be detailed enough to inform but concise enough to retain the reader's interest.
- Separate each section with a ---
- Use a casual conversational tone.
- use continuation lines such as “what we're building today is a little bit more improved version of other projects i've shown on this website” etc so that user will understand that there are more things they need to explore on this website

#### Section Details

- Project Overview:
  - Provide a detailed description of the project, its purpose, and its key features.
  - Highlight the technologies used and the unique benefits the project offers.
  - Highlight how this project will help the readers. that is, students can learn new skills, freshers can add their to portfolio for a job or working employees can add this to their resume for a better job or small businesses can implement this solution into their company.

- About me:
- my name is Sai Ram, a data scientist with expertise in building solutions with expertise in Computer vision and Natural Language Processing. he is currently working on Gen AI projects. Just like this project, you can find more and more projects on his website. link will be in the description. You can follow him on github, linkedin and instagram
- if any students, freshers, working employees or small scale business want me to help them on this project, they can feel free to reach out to me.
they can visit my website  where they will find a detailed roadmap for freshers
- End with a strong hook emphasizing Sairam's success in helping freshers land jobs through his projects.
- Don't forget to tell the users that they can find roadmaps, topics to learn in each skill, detailed plan for learning data science, for free on my website.

    https://psairam9301.wixsite.com/website
    https://www.youtube.com/@sairampenjarla
    https://github.com/sairam-penjarla
    https://www.linkedin.com/in/sairam-penjarla-b5041b121/
    https://www.instagram.com/sairam.ipynb/



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
    1. Cloning the repository (git clone command).
    2. Navigating to the project directory (cd command).
    3. Setting up a virtual environment or Anaconda environment.
        - Include this helpful blog link that will help them understand how to setup virtual environments: [Learn VirtualEnv Basics](https://sairampenjarla.notion.site/Environment-171d56a2fc2780dd9efcd4cef331fa2c).
    4. Installing dependencies using requirements.txt.
    5. Running the project using Python command.

- Future Work:
  - Outline potential improvements or additional features to enhance the project.
  - Explain how this project can me bought to production level

- Conclusion:
  - Summarize the project's impact, usability, and potential.



### Project Details

The content writer should use the provided project details and additional links to create the blog as per the structure outlined above.


"""

demo_prompt = """

### Task

You are a content writer responsible for creating the **Demo Section** of a blog article. Your job is to showcase the features, functionality, and visual elements of the project by writing structured, engaging content based on the provided screenshots and descriptions.

---

### Guidelines

The Demo Section must:
1. **Be Well-Structured**:
   - Use proper headings (#, ##, ###) and subheadings to organize the content logically.
   - Divide the content into clear sections and subsections when necessary.
   
2. **Describe Each Screenshot**:
   - Include a detailed, concise, and engaging description for each screenshot.
   - Provide context for the screenshot: explain what the reader is looking at and how it ties into the project's features or functionality.

3. **Group Related Screenshots**:
   - Group multiple related screenshots under a single section with subsections (if applicable). For example, screenshots of light and dark modes can be grouped under one heading with subheadings for each mode.

4. **Use Placeholders for Images**:
   - Assume the image files are stored in the same directory and include them using markdown syntax: `![Alt Text](filename.png)`.
   
5. **Be Engaging and Informative**:
   - Write in a professional yet approachable tone.
   - Highlight key features or functionalities visible in each screenshot.
   - Connect the visual elements to the project's purpose and benefits for the user.

---

### You Will Receive:
1. **Project Details**:
   - A description of the project, its purpose, and its key features.
   - The tools and technologies used in the project.
   - Any setup or usage instructions relevant to the project.

2. **Screenshot Details**:
   - The names of screenshots (e.g., `home_page.png`, `dashboard.png`).
   - A brief description of what each screenshot represents and any specific details to highlight.

---

### Example Input:

project detail:
This project is an AI-powered email response recommendation system designed to streamline email communication. It suggests automated, context-aware email responses based on the content of incoming emails.
Real-time email analysis to understand context and tone.,
Provides multiple response options for users to choose from.,
Allows users to edit and customize recommended responses.,
Supports multiple email providers like Gmail, Outlook, and Yahoo.,
Utilizes advanced NLP techniques for sentiment and intent analysis.,
Offers light and dark mode for user interface customization.,
Displays a history of recommended responses for auditing purposes.,
Integrated with OpenAI's GPT models and Flask for backend.,
Database managed using PostgreSQL and SQLAlchemy.,
Frontend built with React.js for a responsive and intuitive user experience.,
Email authentication and connection managed via OAuth2.,
Detailed logging and error handling for debugging and analysis.,
Includes a modern repository structure with README, `requirements.txt`, `config.yaml`, and media folder for visual assets.

```json
{
    "screenshots": [
        {
            "name": "email_inbox.png",
            "description": "The main interface displaying the user's email inbox with options for each email."
        },
        {
            "name": "response_recommendations_light.png",
            "description": "Light mode view showing multiple response recommendations for a selected email."
        },
        {
            "name": "response_recommendations_dark.png",
            "description": "Dark mode view showing multiple response recommendations for a selected email."
        },
        {
            "name": "response_editing.png",
            "description": "The editing interface allowing users to customize a selected response."
        },
        {
            "name": "email_history.png",
            "description": "A section displaying a history of email responses, categorized by date and email subject."
        },
        {
            "name": "settings_dark_mode.png",
            "description": "Settings page in dark mode where users can toggle between light and dark modes and manage email provider configurations."
        },
        {
            "name": "settings_light_mode.png",
            "description": "Settings page in light mode with various customization options."
        },
        {
            "name": "analytics_dashboard.png",
            "description": "An analytics dashboard showing metrics such as response time saved, most common response tones, and sentiment analysis over time."
        }
    ]
}
```

---

## Demo Section

### Demo Section:

The following screenshots provide a comprehensive view of the **AI-powered email response recommendation system**, highlighting its features, interface, and functionality.

---

### 1. **User Interface Overview**

#### Inbox View
![Inbox View](email_inbox.png)

This screenshot shows the **main interface**, displaying the user's email inbox. Each email has options for generating recommended responses or opening them for detailed view and customization. The clean and responsive layout ensures seamless navigation.

---

### 2. **Response Recommendations**

#### Light Mode
![Response Recommendations (Light Mode)](response_recommendations_light.png)

Here, we see the **response recommendation interface** in **light mode**, where multiple suggestions are generated for a selected email. Each recommendation is context-aware and aligned with the email's tone and content.

#### Dark Mode
![Response Recommendations (Dark Mode)](response_recommendations_dark.png)

This screenshot displays the **response recommendations** in **dark mode**, showcasing the system's adaptability to different user preferences.

---

### 3. **Customizing Responses**

![Response Editing](response_editing.png)

This image demonstrates the **response editing feature**, where users can modify the recommended responses before sending them. The editor provides a simple and intuitive interface, allowing for fine-tuning of tone and content.

---

### 4. **History and Metrics**

#### Response History
![Response History](email_history.png)

The **response history section** provides users with a chronological view of their past email responses, categorized by date and subject. This feature enables easy auditing and tracking of communication.

#### Analytics Dashboard
![Analytics Dashboard](analytics_dashboard.png)

This screenshot highlights the **analytics dashboard**, which presents key metrics such as:
- Total time saved using recommended responses.
- Most common tones used (e.g., formal, casual, empathetic).
- Sentiment analysis trends over time.

---

### 5. **Settings and Customization**

#### Light Mode
![Settings Light Mode](settings_light_mode.png)

The **settings page in light mode** allows users to configure email provider integrations, toggle between light and dark modes, and customize preferences for response generation.

#### Dark Mode
![Settings Dark Mode](settings_dark_mode.png)

This screenshot shows the **settings page in dark mode**, reflecting the same functionality in a darker aesthetic for user comfort.

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
- details of the project
- The name of the architecture diagram (e.g., `architecture_diagram.png`).
- A brief description of the architecture and its components.

---
### Input:
project details:

Automated Email Response Recommendation System
This project is an AI-driven automated email response recommendation system. The main goal is to assist customer service teams by recommending the most appropriate email response based on the content of incoming customer emails. It utilizes natural language processing (NLP) to analyze email content and suggests responses that are both relevant and personalized. The system also tracks previous recommendations, learning from past interactions to improve future suggestions. The project integrates with popular email platforms like Gmail and Outlook, making it easy for customer service representatives to access and use the recommendations. Additionally, the system is designed to integrate with customer support ticketing systems, enabling automatic logging of responses.

```json
{
    "diagram": "automated_email_response_architecture.png",
    "description": "The architecture diagram for the Automated Email Response Recommendation System illustrates the flow of data and interactions between the user interface, backend services, AI model, and email platforms. The process begins when an email is received by the email client, which triggers the system to analyze the content of the email using NLP. The system processes the email's subject and body to identify the user's intent and sentiment. It then queries the database of pre-written responses, using machine learning algorithms to rank and recommend the most relevant ones. The selected response is displayed to the customer service representative, who can approve it, modify it, or send it as is. If the response is sent, the system logs the interaction for future learning. The architecture also includes integrations with email platforms and ticketing systems. Major components include email parsing, NLP processing, response ranking, database management, and logging. Key services and tools used in the project include Python, Flask, TensorFlow for NLP, PostgreSQL for the database, and third-party email and ticketing system APIs."
}
```

### output

## Architecture Diagram

### Automated Email Response Recommendation System Architecture

The following architecture diagram provides an in-depth look at the components and workflow of the **Automated Email Response Recommendation System**. The system uses multiple technologies and services to automatically analyze incoming emails and recommend appropriate responses for customer service teams.

![Architecture Diagram](media/automated_email_response_architecture.png)

### Detailed Description of the Architecture

#### 1. **Email Platform Integration**
   - The process begins when an email is received by an integrated **email client** (such as Gmail or Outlook). The system automatically detects incoming emails via **IMAP/SMTP protocols**.
   - **Email Parsing**: The email content, including the subject and body, is parsed to extract key data, such as the sender, subject line, and message body. This data is then sent to the backend for processing.

#### 2. **Natural Language Processing (NLP)**
   - The parsed email content is sent to an **NLP model** (powered by **TensorFlow** or **spaCy**) that performs sentiment analysis, intent detection, and entity extraction. This helps understand the customer's needs and the tone of the email.
   - **Intent Detection**: The system identifies the main request or question in the email (e.g., refund request, product inquiry).
   - **Sentiment Analysis**: The model analyzes the emotional tone of the email (positive, negative, neutral), which is used to tailor the response appropriately.

#### 3. **Response Ranking and Recommendation**
   - After processing the email with NLP, the system queries a **database** of pre-written responses, which are stored in **PostgreSQL** or a NoSQL database like **MongoDB**. These responses are categorized by topics and are ranked based on their relevance to the parsed email content.
   - **Machine Learning Model**: The system uses a **ranking algorithm**, such as a decision tree or deep learning model, to select the most relevant responses based on previous interactions and the current email's context.
   - The ranking process ensures that the system suggests responses that are not only accurate but also personalized, improving the overall customer experience.

#### 4. **Display and User Interaction**
   - The ranked response options are displayed to the **customer service representative** through the user interface, developed using **Flask** for the web framework. The representative can either approve a recommended response, modify it, or write a custom response.
   - **Email Customization**: The system allows the representative to adjust the tone and details of the response, providing flexibility while ensuring consistency in communication.

#### 5. **Response Sentiment and Feedback Loop**
   - Once the response is selected and sent to the customer, the system logs the interaction in the **database** for future learning. This feedback loop helps the system improve over time by refining the response recommendations based on past performance.
   - **Logging**: All interactions, including the email content, recommended responses, and customer feedback, are stored in the database for future analysis and model training.

#### 6. **Ticketing System Integration**
   - The system is also integrated with **customer support ticketing systems** like **Zendesk** or **Freshdesk**. Once the email response is sent, a corresponding support ticket is created or updated, allowing customer service representatives to track the progress of customer issues.
   - This integration ensures that responses are logged in the system and that the workflow remains seamless for customer support teams.

#### 7. **Key Components and Services**
   - **NLP Processing**: Powered by **TensorFlow** or **spaCy** for intent recognition, sentiment analysis, and entity extraction.
   - **Email Platform APIs**: Integration with Gmail, Outlook, or other email clients via **IMAP/SMTP**.
   - **Database Management**: **PostgreSQL** or **MongoDB** is used for storing pre-written responses, logs, and interaction history.
   - **Flask Web Application**: The front-end interface for customer service representatives to interact with the system.
   - **Machine Learning Models**: Ranking models such as decision trees, SVM, or neural networks are used to select the best response.

#### 8. **Key Flask Routes**
   - **`/get_email_data`**: Retrieves the email content to be analyzed by the NLP model.
   - **`/process_email`**: Processes the email using NLP and machine learning models to detect intent and rank possible responses.
   - **`/get_recommended_responses`**: Fetches the top-ranked email responses from the database.
   - **`/send_response`**: Sends the selected response to the customer through the email client.
   - **`/log_interaction`**: Logs the customer interaction for future learning and feedback.
   - **`/integrate_ticketing_system`**: Updates the customer support ticket with the interaction details.

By utilizing a combination of **email parsing**, **NLP**, **machine learning**, and **integration with email and ticketing platforms**, the system offers a streamlined and intelligent approach to customer support. It not only assists in responding to emails faster but also ensures that the responses are relevant, personalized, and efficient.

---

### Input:
"""