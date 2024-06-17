import streamlit as st
from pandasai.llm.openai import OpenAI    
from dotenv import load_dotenv
from pandasai import SmartDataframe  
import os
import pandas as pd
from pandasai import Agent   
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
PANDASAI_API_KEY = os.getenv('PANDASAI_API_KEY')

st.set_page_config(layout='wide')
st.title("Multi-CSV Chat")

input_csv = st.file_uploader("Upload your csv files", type='csv', accept_multiple_files=True)

if input_csv:

    col1, col2 = st.columns([1,1])

    with col1:
        #select a csv file
        selected_file = st.selectbox("Select a csv file", [file.name for file in input_csv])
        selected_index = [file.name for file in input_csv].index(selected_file)
    
        #load and display
        st.info("csv file uploaded successfully")
        data = pd.read_csv(input_csv[selected_index])
        st.dataframe(data, use_container_width=True)

    with col2:
        #query for analysis
        st.info("Chat below")
        input_text = st.text_input("Enter the query:")

        agent = Agent(data)
 
        if input_text:
            if st.button("Chat with csv"):
                st.info("Your query : " + input_text)
                result = agent.chat(input_text)
                st.success(result)


    
    
    

    
