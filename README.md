# Q&A Chatbot for Music Streaming Application Reviews
This repository contains the implementation of an AI-powered Q&A chatbot designed to extract actionable insights from a dataset of Google Store reviews for a music streaming application (e.g., Spotify).

## Overview
The project aims to address the management's need for a more efficient solution to analyze and interpret unstructured user reviews. The chatbot utilizes natural language processing techniques to provide insightful responses to various management queries about user preferences, comparisons with competitors, reasons for dissatisfaction, and emerging trends.

You can see the demo video (1 minute length) at [this link](https://youtu.be/nNagb2GXxu8), please use your earphones/headset for a clearer voice.

### Screenshot
![image](https://github.com/muhammadravi251001/spotify-chatbot/assets/78993021/7424c89e-3003-4dee-b230-b52a65dda1ce)

## Features
- Integration: Integrates with language models like chatGPT, BERT for natural language understanding and generation.
- Framework: Developed using Python with support for additional tools like Pinecone, Faiss for retrieval-augmented generation.
- UI: Includes a simple user interface built with Streamlit for easy interaction.
- Data Processing: Implements preprocessing and postprocessing methods for efficient data handling and embedding retrieval.
- Quality Scoring: Provides scoring mechanisms to evaluate the quality of generated responses.
- Exception Handling: Addresses edge cases and invalid data inputs for robust performance.

## Repository Structure

Before using Gemini AI by Google, I do much experiments before, like using GPT2, DistilBERT, OpenAI GPT; with utilizing RAG (I use Faiss), and some LangChain experiment(s). All `.ipynb` files in the `experiments/` folder were created purely as experiments and as drafts. I usually do this to keep track of the milestones of various experiments that need to be conducted. Therefore, these files were not made to be read by others but solely for my own use.

```python
├── dataset/
│   └── SPOTIFY_REVIEWS.csv       # Spotify dataset
├── experiments/                  # All of the experiments before
│   ├── BERT.ipynb
│   ├── BLOOM.ipynb
│   ├── GPT2.ipynb
│   ├── LangChain.ipynb
│   ├── OpenAI.ipynb
|   └── SentenceTransformer_and_DistilBERT.ipynb
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
Or you can click the [link](https://spotify-chatbot.streamlit.app/) on this Github's repo.

## Future Works
One possible continuation is to compare the performance (based on quality scores or similar metrics) of all existing approaches.
