import pandas as pd
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

import streamlit as st
import os
import sqlite3



## Configure Genai Key
#genai.configure(api_key="AIzaSyDmZ8RNp3LidlzpuD86DD-YYXUS50FwYlk")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('models/gemini-1.5-pro-002')
    response=model.generate_content([prompt[0],question])
    return response.text

## Fucntion To retrieve query from the database

def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        # Get column names
        columns = [description[0] for description in cur.description]
        rows = cur.fetchall()
        conn.close()
        # Create DataFrame
        df = pd.DataFrame(rows, columns=columns)
        return df
    except sqlite3.Error as e:
        st.error(f"SQL Error: {e}")
        return pd.DataFrame()



## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name EMPLOYEE and has the following columns - ID, NAME, DEPARTMENT,
    SALARY \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM EMPLOYEE ;
    \nExample 2 - Tell me all the EMPLOYEES in Marketing department, 
    the SQL command will be something like this SELECT * FROM EMPLOYEE 
    where DEPARTMENT="Marketing"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    df = read_sql_query(response, "employee.db")
    st.subheader("The Response is")
    st.dataframe(df)  # Display as an interactive table