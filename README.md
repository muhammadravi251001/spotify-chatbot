# Q&A Chatbot for Music Streaming Application Reviews
This repository contains the implementation of an AI-powered Q&A chatbot designed to extract actionable insights from a dataset of Google Store reviews for a music streaming application (e.g., Spotify).

## Overview
The project aims to address the management's need for a more efficient solution to analyze and interpret unstructured user reviews. The chatbot utilizes natural language processing techniques to provide insightful responses to various management queries about user preferences, comparisons with competitors, reasons for dissatisfaction, and emerging trends.

## Features
- Integration: Integrates with language models like chatGPT, BERT for natural language understanding and generation.
- Framework: Developed using Python with support for additional tools like Pinecone, Faiss for retrieval-augmented generation.
- UI: Includes a simple user interface built with Streamlit for easy interaction.
- Data Processing: Implements preprocessing and postprocessing methods for efficient data handling and embedding retrieval.
- Quality Scoring: Provides scoring mechanisms to evaluate the quality of generated responses.
- Exception Handling: Addresses edge cases and invalid data inputs for robust performance.

## Repository Structure

Before using Gemini AI by Google, I do much experiments before, like using GPT2, DistilBERT, OpenAI GPT; with utilizing RAG (I use Faiss), and some LangChain experiment(s).
```python
├── dataset/
│   └── SPOTIFY_REVIEWS.csv       # Spotify dataset
├── experiments/                  # All of the experiments before
│   ├── BERT.ipynb
│   ├── BLOOM.ipynb
│   ├── GPT2.ipynb
│   ├── LangChain.ipynb
│   └── OpenAI.ipynb
|   ├── SentenceTransformer_and_DistilBERT.ipynb
├── requirements.txt              # Python dependencies
├── README.md                     # Project overview and documentation
├── LICENSE                       # License information
├── app.py                        # Hosting model & streamlit app
└── qna_bot.py                    # Serve class to support answering logic
```
## How to Use
```bash
git clone https://github.com/muhammadravi251001/spotify-chatbot.git
cd spotify-chatbot
pip install -r requirements.txt
streamlit run app.py
```
Or you can click the link on this Github's repo.