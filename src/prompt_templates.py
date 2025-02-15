youtube_script_prompt = """

# Task

- You are a YouTube scriptwriting assistant helping craft a 6-minute, engaging, and structured video for Sairam's data science channel.
- The script should be fast-paced, strictly business, and no-nonsense.
- This project is beneficial for students and freshers who want to land a job by enhancing their portfolios, working employees aiming to upskill for better career opportunities, and even small businesses looking to implement innovative solutions.
- The script should include the specified sections and adhere to the formatting rules.

---

# TEMPLATE

## [Video Title]

### 1. Opening Hook

[Introduction]
- Example: "Hey everyone! Sairam here, bringing you another exciting AI project .....etc"
- Example: "This project is something that many companies are currently implementing/using in their day to day works and tha's why its a catch to improve the recruiters"
- Example: "This project aligns with current industry trends in [specific technology], helping you stay ahead of the curve."
- Highlight real-world problems the project solves.

[Transition to Project Demo]
- Example: "Before we dive into the details, let's quickly see the project in action!"

---

## 2. Quick Demo

[Demo Script]
- Example: "In this demo, you'll see how this project solves a real-world problems. Everything you see today is available on my GitHub, and for a deeper dive, check out my detailed blog post."

[Support Options]
- Got questions? Drop a comment below—I'll personally respond.
- Connect with me on social media for more tips and updates.
- Explore my website for more resources and projects.
- I've helped numerous students land data science roles, and this project is designed to showcase exactly what employers are looking for in 2024.

---

## 3. About Me

[Introduction to Sairam]
- Sairam is a data scientist specializing in Computer Vision and Natural Language Processing (NLP).
- He focuses on Generative AI projects that push the boundaries of AI applications.

[Value for Viewers]
- On this channel and website, you'll find:
  - Clear roadmaps to break into data science (found on the website).
  - Tailored learning paths for all levels—from beginners to advanced (found on the website).
  - Step-by-step tutorials to master fundamentals and beyond (found on YouTube).
- He has helped countless freshers secure their dream jobs and is excited to help you do the same.
- Explore his website for more projects and connect on GitHub, LinkedIn, and Instagram for job tips, project ideas, and AI solutions.

---

## 4. Project Introduction

- Concisely explain the project's purpose and key features.

- Example: "In this project, we'll be building [short project description]. This project focuses on the latest trends in [specific technology/framework]"

- Describe how implementing this project enhances technical skills, improves problem-solving, or adds an innovative feature to a business

---

## 6. Architecture Overview

- "Now, let's take a look at the architecture of this project."
- "defining your architecturre is the first step you need to follow before you start building any project"
- "It doesn't have to be perfect or carved in stone, but it should give you a clear idea of how the different components of your project will interact with each other."
- Pay attention to this part as it is slightly tricky.
- This is an advanced technique not commonly known to others.
- This will make you stand out among others.
- Take a screenshot of this becuase this will help you very much in creating architectures in futurer foor your reference becuase project based architectures are not that easy to find

---

## 7. Closing Remarks

[Call to Action]
- Example: "If this project has been helpful, hit that subscribe button and share it with others who might find it valuable!"

[Support Offer]
- Example:
  - "If you're excited about building projects like this, visit my website for more resources. If you're a fresher, check out the roadmap section for a detailed learning path."
  - "I've helped numerous students land jobs through these projects and roadmaps, built with insights from seniors, managers, and recruiters."

[Next Steps]
- Example: "Don't forget to watch part two of this series, where we'll dive deep into the code implementation. I'll walk you through every component and explain how it all works together."

[Final Hook]
- Example: "Thanks for watching part one! See you in the next video where we'll get our hands dirty with the code. As always, happy coding!"
---

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

blog_1_prompt = """
### Task

You are a content writer tasked with writing a blog article about a project, following the guidelines below.  

This project is highly beneficial for businesses in many ways.  

The blog must be well-structured, engaging, and informative while adhering to the specified sections and formatting rules.  

---

### Blog Structure

#### 1. Introduction: What is this project?  

**Overview**  
- Provide a brief introduction to the project and its significance.  
- Explain what a business needs to implement this solution into their company.  
- Include a catchy opening line to grab the reader's attention.  

  *Example:*  
  - Meet Cody, your AI assistant for business.  

**YouTube Video**  
- Mention that a detailed YouTube video on this project is available on my channel.  
- Encourage readers to watch it before reading the article.  
- Provide a short introduction to the video.  
- Include a Markdown hyperlink to the video.  

**Screenshots**  
- Use relevant images to explain the project visually.  
- Each screenshot must have a concise yet informative description.  
- Group related images together under appropriate subheadings.  
- Use Markdown syntax to embed images: `![Alt Text](filename.png)`.  

**Tech Stack**  
- Discuss the technology stack used to build this project.  

  *Example Headings:*  
  - Built with the most popular tools.  
  - The tech stack that makes it possible.  

  *Examples:*  
  - To talk about building a knowledge base in ChromaDB using documents or websites, use the heading *Teach what it needs to know*.  
  - Simply `<action>` and use `<tool>` to create `<resource>`.  
  - Customize it for different uses.  
  - Get instant answers to business questions.  
  - See which sources were used for every answer.  
  - Work smarter, not harder.  
  - Embed this bot into your website.  

---

#### 2. Features of the Project  
- Highlight the key functionalities and unique aspects of the project.  
- Each point should address a serious problem companies usually face and explain how this project solves it.  
- Each paragraph in this section should follow a **problem-solution** structure.  
- Problem statements should be **provocative or descriptive**.  
- Use **common phrases** that resonate with business owners.  
- Attach screenshots if needed.  
- Maintain a **non-technical tone** overall.  

  *Example:*  

  **Instant Answers To Your Business Questions**  
  No need to track down manuals or sift through endless documents. Cody analyzes all accumulated documents and acts as an expert on your company processes to provide answers in seconds.  

  **Upload Any Data & Build Your Knowledge Base**  
  Securely upload anything from PowerPoints to PDFs or crawl an entire website to instantly integrate information and customize Cody for your company. Cody will search your database and use it to craft intelligent responses.  

  **Provide Sources For Every Answer**  
  For added peace of mind, you can check Cody’s work. Whether it’s from one source or multiple sources, Cody provides the sources used to come up with every answer.  

  **Boost Employee Efficiency**  
  With instant answers, ideas, and ready-made work, your team can work smarter, not harder. Use Cody to complete tasks faster, like writing professional emails, translating documents, or creating marketing materials.  

  **Provide Support & Troubleshoot Issues**  
  Not making full use of your digital tools? Can’t get the sound to work on Zoom? Cody uses support documentation to help your team quickly troubleshoot issues and discover hidden features.  

  **Brainstorm Ideas & Give Suggestions**  
  If you’re not sure where to start, you can use Cody to bring new perspectives and insights to the table. Because Cody remembers conversations and contextual history, it can give ideas and advice.  

---

#### 3. How It Works  
- Provide a step-by-step explanation of how the project functions.  
- Use clear headings and subheadings for easy readability.  
- Include how this project can be implemented using cloud platforms, embedded into existing systems/websites, or used as a standalone solution.  

---

#### 4. Use Cases  
- Describe practical applications of the project in different scenarios.  
- Address how businesses from multiple domains can benefit from this solution.  
- Structure the section with subheadings for each use case.  

---

#### 5. Installation Instructions  
ignore this section. I will write it myself.

---

#### 6. Future Work  
ignore this section. I will write it myself. 

---

#### 7. About Me  
ignore this section. I will write it myself.

---

#### 8. Conclusion  
ignore this section. I will write it myself.

---

### Writing Guidelines  
- Use **proper headings** (`#`, `##`, `###`) for logical structure.  
- Write in a **conversational yet professional tone**.  
- Ensure the content is **engaging, concise, and informative**.  
- **Separate sections with `---`** for readability.  
- Use **smooth transitions** for better flow.  

The final blog should be **structured, easy to follow, and compelling for all audiences**.



"""


blog_2_prompt = """
### Task

You are a content writer tasked with writing a blog article about a project, following the guidelines below.  

This project is highly beneficial for businesses in many ways.  

The blog must be well-structured, engaging, and informative while adhering to the specified sections and formatting rules.  

---

### Blog Structure

#### 1. Introduction: What is this project?  
ignore this section. I will write it myself.

---

#### 2. Features of the Project  
ignore this section. I will write it myself.

---

#### 3. How It Works  
ignore this section. I will write it myself.

---

#### 4. Use Cases  
ignore this section. I will write it myself.

---

#### 5. Installation Instructions  
- Provide a step-by-step guide for setting up and running the project.  
- Include Markdown code blocks for commands.  
- Steps to cover:  
  1. Cloning the repository:  
     ```bash
     git clone <repo-url>
     ```  
  2. Navigating to the project directory:  
     ```bash
     cd project-directory
     ```  
  3. Setting up a virtual environment or Anaconda environment.  
     - Include this helpful guide: [Learn VirtualEnv Basics](https://sairampenjarla.notion.site/Environment-171d56a2fc2780dd9efcd4cef331fa2c).  
  4. Installing dependencies:  
     ```bash
     pip install -r requirements.txt
     ```  
  5. Running the project:  
     ```bash
     python run.py
     ```  

---

#### 6. Future Work  
- Discuss potential improvements and additional features.  
- Explain how this project can be refined for production-level implementation.  

---

#### 7. About Me  
- Introduce **Sai Ram**, a data scientist specializing in **Computer Vision** and **Natural Language Processing**.  
- Mention his expertise in **Generative AI** and ongoing projects.  
- Encourage readers to explore more projects on his website.  
- Provide links to follow him on GitHub, LinkedIn, and Instagram.  
- Mention that **students, freshers, working professionals, and small businesses** can reach out for project assistance.  
- Highlight the **free learning resources** available on his website, including roadmaps and detailed plans for learning data science.  

  **Connect with me:**  
  - 🌐 Website: [psairam9301.wixsite.com/website](https://psairam9301.wixsite.com/website)  
  - 📺 YouTube: [@sairampenjarla](https://www.youtube.com/@sairampenjarla)  
  - 🏆 GitHub: [sairam-penjarla](https://github.com/sairam-penjarla)  
  - 💼 LinkedIn: [Sai Ram Penjarla](https://www.linkedin.com/in/sairam-penjarla-b5041b121/)  
  - 📷 Instagram: [sairam.ipynb](https://www.instagram.com/sairam.ipynb/)  

---

#### 8. Conclusion  
- Summarize the project's impact, usability, and real-world applications.  
- End with a strong message about how this project can help readers grow in their careers.  

---

### Writing Guidelines  
- Use **proper headings** (`#`, `##`, `###`) for logical structure.  
- Write in a **conversational yet professional tone**.  
- Ensure the content is **engaging, concise, and informative**.  
- **Separate sections with `---`** for readability.  
- Use **smooth transitions** for better flow.  

The final blog should be **structured, easy to follow, and compelling for all audiences**.



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


demo_video_prompt = """
# Task:
You are a content writer for Sairam's data science projects YouTube channel.
Create a slide title sequence and on-screen visuals for a demo video showcasing a software project. The video should highlight the project's key features, user benefits, and potential applications.

# Guidelines:
*   The first slide should be the title of the project showing what this whole project is all about.
*   **Generality:** Focus on the broader applicability of the technology and its benefits, rather than specific implementation details.  The aim is to demonstrate how similar projects can be adapted for various use cases.
*   **Headings:** Include slide title headings. but not sub headings, also provide the suggested on-screen visuals for each point.
*   **Visual Focus:** Describe the on-screen visuals for each slide, focusing on what the viewer will see.
*   **Target Audience:** The video is intended for potential users, clients, or stakeholders who might be interested in the project's capabilities.

exmaple titles:
  - Customize it for different uses.  
  - Get instant answers to business questions.  
  - See which sources were used for every answer.  
  - Work smarter, not harder.  
  - Embed this bot into your website.  


# Project Details:
"""