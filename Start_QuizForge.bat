
@echo off
cd /d "E:\Mini Project\quizforge-mcq-generator"

call .venv\Scripts\activate.bat

start "" http://localhost:8501

streamlit run app.py

pause
