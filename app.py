import os
import csv
import streamlit as st
from qna_bot import QnAChatbot, quality_score
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("API key not found. Please set it in the .env file.")

genai.configure(api_key=api_key)

pathname = "dataset/SPOTIFY_REVIEWS.csv"
MAX_ROWS = 1000

def extract_csv(pathname, max_rows=MAX_ROWS, encoding='utf-8'):
    parts = []
    with open(pathname, "r", newline="", encoding=encoding) as csvfile:
        csv_reader = csv.reader(csvfile)
        for index, row in enumerate(csv_reader):
            parts.append(" ".join(row))
            if index >= max_rows: break
    return parts

data_parts = extract_csv(pathname)

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

qna_bot = QnAChatbot(model, data_parts)

st.set_page_config(page_title="Spotify Review Q&A Chatbot", layout="wide")
st.title("Spotify Review Q&A Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

def display_chat():
    for message in st.session_state.history:
        if message["role"] == "user":
            st.markdown(f'<div style="background-color:#5B7B5B;border-radius:10px;padding:10px;margin:10px 0;text-align:right;color:#FFF;">{message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div style="background-color:#FFD966;border-radius:10px;padding:10px;margin:10px 0;text-align:left;color:#000;">{message["content"]}</div>', unsafe_allow_html=True)

def handle_query(query):
    if query:
        st.session_state.history.append({"role": "user", "content": query})
        response = qna_bot.ask_question(query)
        # score = quality_score(query, response)
        # st.session_state.history.append({"role": "assistant", "content": f"{response}\n\n*Quality Score: {score:.2f}*"})
        st.session_state.history.append({"role": "assistant", "content": f"{response}"})
        display_chat()

query = st.text_input("Enter your question:", key="input")
if st.button("Send"):
    handle_query(query)

example_questions = [
    "What are the specific features or aspects that users appreciate the most in our application?",
    "In comparison to our application, which music streaming platform are users most likely to compare ours with?",
    "What are the primary reasons users express dissatisfaction with Spotify?",
    "Can you identify emerging trends or patterns in recent user reviews that may impact our product strategy?"
]

st.sidebar.title("Example Questions")
for q in example_questions:
    if st.sidebar.button(q):
        handle_query(q)