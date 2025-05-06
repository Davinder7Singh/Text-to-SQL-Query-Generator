# Text-to-SQL-Query-Generator
This project simplifies the process of writing SQL queries by allowing users to input English questions. It leverages the Google Gemini API to generate appropriate SQL queries based on the context provided. The application is built with Streamlit for an interactive interface and utilizes SQLite for database interaction.

# Key Features
Text-to-SQL Translation: Converts user questions into SQL queries.
Dynamic Data Retrieval: Queries and fetches data from a sample EMPLOYEE database.
User-Friendly Interface: Built with Streamlit for easy interaction.
Secure API Handling: Uses python-dotenv for managing sensitive credentials.
Randomized Data: Generates 100 random employee records for testing.

# Tech Stack
Language: Python
Framework: Streamlit
Database: SQLite
API: Google Gemini
Libraries: pandas, dotenv, sqlite3

# How It Works
Users input English questions about employee records.
The application translates the query into SQL using Google Gemini API.
The SQL query is executed on the SQLite database.
Results are displayed in a Streamlit interactive data table.

## 📦 Database Schema (EMPLOYEE Table)

| **Column**    | **Type**    | **Description**                                   |
|---------------|------------|---------------------------------------------------|
| **ID**        | INTEGER     | Unique identifier for each employee               |
| **NAME**      | TEXT        | Employee's name                                   |
| **DEPARTMENT**| TEXT        | Department where the employee works               |
| **SALARY**    | INTEGER     | Employee's salary                                 |


#Streamlit interface
![p33](https://github.com/user-attachments/assets/8c4f4458-2557-4375-b927-0670db845690)

