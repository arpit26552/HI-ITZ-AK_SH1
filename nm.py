import requests
import csv
import streamlit as st
import subprocess
import json

def fetch_notion_data(database_id, api_key):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }
    url = f"https://api.notion.com/v1/databases/{database_id}/query"
    
    results = []
    has_more = True
    cursor = None
    
    while has_more:
        payload = {"start_cursor": cursor} if cursor else {}
        response = requests.post(url, headers=headers, json=payload)
        data = response.json()
        
        results.extend(data.get('results', []))
        has_more = data.get('has_more', False)
        cursor = data.get('next_cursor', None)

    return results

def convert_to_csv(data, output_file):
    if not data:
        print("No data found.")
        return

    # Extract column names
    column_names = ['Tasks','Progress','Submission Date','Milestones','Delivarables','Notes']

    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(column_names)  # Write header

        row_inv=[]

        for entry in data:
            row = []
            for column in column_names:
                if column in entry['properties']:
                    prop = entry['properties'][column]
                    # Handle empty values
                    if 'title' in prop and prop['title']:
                        row.append(prop['title'][0]['text']['content'])
                    elif 'rich_text' in prop and prop['rich_text']:
                        row.append(prop['rich_text'][0]['text']['content'])
                    elif 'number' in prop:
                        row.append(prop['number'])
                    elif 'select' in prop and prop['select']:
                        row.append(prop['select']['name'])
                    elif 'multi_select' in prop:
                        row.append(", ".join([option['name'] for option in prop['multi_select']]))
                    elif 'checkbox' in prop:
                        row.append(prop['checkbox'])
                    elif 'date' in prop and prop['date']:
                        row.append(prop['date']['start'])
                    elif 'url' in prop:
                        row.append(prop['url'])
                    else:
                        row.append("")  # Empty value
                else:
                    row.append("")  # Column not found in entry
            #writer.writerow(row)
            #print(row)
            row_inv.append(row)
       # print(row_inv)

        for i in range(len(row_inv)-1,-1,-1):
            writer.writerow(row_inv[i])

def ask_question(question):
    question_url = "http://0.0.0.0:8000/v1/pw_ai_answer"  # Connect to RAG server on port 6060
    headers = {
        "accept": "/",
        "Content-Type": "application/json",
    }
    data_prompt = {
        "prompt": question
    }
    r = requests.post(question_url,headers=headers, data=json.dumps(data_prompt))
    answer = r.text
    return answer


def question_search():
    search_query = st.text_input("Ask a Question", "")
    print(search_query)

    if search_query:
        st.write(f"Going through your schedule: {search_query}...")
        answer = ask_question(search_query)

        st.write(answer)
    else:
        st.write("You didn't ask anything.")

def ui():
    st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #ADD8E6;  /* Change this to your desired color */
    }
    </style>
    """,
    unsafe_allow_html=True
)
    # Set the title of the app
    st.title("Notionated-Task-Manager")

    # Add a subtitle for clarity
    st.subheader("Please enter your Notion credentials")

    # Input for Notion API token
    notion_api_key = st.text_input("Notion Integration Key:", type="password")

    # Input for Notion Database ID
    notion_database_id = st.text_input("Notion Database ID:")

    # Button to submit
    if st.button("Submit"):
        if notion_api_key and notion_database_id:
            st.success("Credentials added successfully!")
    #print(notion_api_key,notion_database_id)
            NOTION_API_KEY,DATABASE_ID=notion_api_key,notion_database_id
            OUTPUT_FILE = "./data/Tasks.csv"

            data = fetch_notion_data(DATABASE_ID, NOTION_API_KEY)
            convert_to_csv(data, OUTPUT_FILE)    
            
    #Here you can handle the next steps, like storing the values or making API calls.
    else:
        st.error("Please fill in all fields.")

    #question_search()
    search_query = st.text_input("Ask a Question", "")
    print(search_query)

    if search_query:
        
    
    
if __name__ == "__main__":
    process = subprocess.Popen(["python3", "app.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ui()