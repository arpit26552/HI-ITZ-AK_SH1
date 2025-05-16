# Notionated-Task-Manager
## About the project
Notionated-Task-Manager is an innovative app designed for students aged 16-25, addressing their struggles with time management and organization in a fast-paced educational environment. By leveraging advanced capabilities of the Pathway LLM app, it helps in keeping track of tasks, allowing users to get input about tasks in natural language for a seamless experience. This not only enhances student productivity but also contributes to improved academic performance while reducing stress associated with overwhelming schedules. This app positions has the potential to make itself as a unique player in the growing EdTech market, fostering high user engagement and retention through dynamic, real-time adjustments and interactive assistance.

## Demo
https://github.com/user-attachments/assets/c4bbf509-177b-4a4c-975a-3a7bc335418a

## Built With
This project was built as a sumbission for the final project in Pathway's 3-Week LLM Building Bootcamp. The tools used for building this app are:

[https://pathway.com/developers/templates/gemini-rag](#feature)  
[https://www.notion.so/integrations/all](#feature)  
[https://streamlit.io/](#feature)

## How it works?
1.Notion API  
Using Notion API , the task management table database created in notion app is extracted as a json file. Then using few functionalities the json file is converted to a csv file with the actual table data and stored in local storage.

2.Multimodal RAG with Gemini  
Multimodal RAG app built with Gemini AI and pathway LLM is used to analyze the stored csv file.

3.Streamlit  
Streamlit is used to built a simple UI to get the notion integration id and table id from the end user, which in connection with Notion API downloads the database as a csv file. After the Multimodal RAG goes through the csv file, we can ask questions through the UI which in turn answers our questions.

# Installation
## 1.Prerequisites  
Docker : [https://www.docker.com/](#feature)
Gemini AI API key : [https://ai.google.dev/gemini-api/docs/api-key](#feature)
## 2. Environment Setup
Create a .env file in the root directory of your project.  
Add the following lines to the .env file, replacing {YOUR_GEMINIAI_KEY} with your actual GEMINI API key:  
`GEMINI_API_KEY={YOUR_GEMINIAI_KEY}`
## 3.Build and run the docker image
`docker build -t imagename . `  
`docker run -v "${PWD}/data:/app/data" -p 8501:8501 imagename `
## 4.Access the application
Open your web browser.  
Navigate to `localhost:8501` to access the application.

# Endusers
Notionated Task Manager is incredibly useful for students as it simplifies the process of managing tasks and schedules. With the ability to interact in natural language, students can easily input their assignments, deadlines, and commitments without needing to navigate complex interfaces. This intuitive communication reduces the cognitive load of organization, allowing students to focus more on their studies.By providing insights into their workload and schedules, the app promotes better time management and reduces stress, ultimately enhancing academic performance and overall well-being.







