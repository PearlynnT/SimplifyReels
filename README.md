# SimplifyReels

## Project Description

### Inspiration
SimplifyReels was inspired by the spirit of the Wild West—where pioneers carved out a path in uncharted territory, fueled by a desire for freedom and innovation. Just like those early settlers who sought to make their mark on the frontier, today's creators are navigating the vast, fast-paced digital landscape, looking for simpler, more efficient ways to tell their stories.

In the old West, speed, skill, and resourcefulness were key to survival, and that’s exactly what SimplifyReels brings to video creation. Inspired by the grit and determination of those frontier days, our mission is to provide modern-day pioneers—content creators, marketers, and storytellers—with the right tools to capture their audience’s attention without getting bogged down in the technical dust. SimplifyReels rides into town to bring a fresh approach to video production: fast, intuitive, and built for those looking to conquer new horizons with ease.

### What It Does
SimplifyReels takes a piece of text and leverages AI to transform it into short and easy-to-understand reels. The process includes:
1. Summarizing and simplifying the text input using OpenAI API.
2. Extracting key information and generating keywords for a search query.
3. Fetching relevant images using Google Custom Search API with generated keywords.
4. Compiling subtitles and images into a reel using MoviePy.

---

## Setup Instructions

### Step 1: Create and Activate a Python Virtual Environment

To isolate the project dependencies, it's recommended to create a virtual environment.

#### For Windows:
Open a command prompt and run:
```
python -m venv venv
venv\Scripts\activate
```
#### For Linux/MacOS:
Open terminal and run:
```
python3 -m venv venv
source venv/bin/activate
```
After activation, your command prompt should indicate you are in the virtual environment (venv).

### Step 2: Install Required Packages
With the virtual environment active, install the necessary dependencies for the project using pip:
```
pip install streamlit openai moviepy python-dotenv
```
### Step 3: Setting Up Environment Variables
You need to set up an .env file to store API keys, such as your OpenAI API key and Google Custom Search API key. In the root of your project directory, create a file named .env and add the following:
```
OPENAI_API_KEY=your-openai-api-key
GOOGLE_API_KEY=your-google-api-key
GOOGLE_CSE_ID=your-custom-search-engine-id
```
Replace the values with your actual API keys.

### Step 4: Running the Project
In one terminal, run:
```
python3 main.py
```
In anothere terminal, run:
```
streamlit run app.py
```