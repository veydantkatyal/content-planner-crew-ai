# AI Content Planner with CrewAI

## Overview
This project is a simple AI-powered content planning tool that leverages **CrewAI** to generate blog outlines based on user input. The web application is built using **Streamlit**, making it easy to interact with the AI agent through a user-friendly interface.

## Features
- Accepts user input for a blog topic.
- Uses an AI-powered agent (CrewAI) to generate structured blog outlines.
- Displays the generated outline in the web app.
- Simple and interactive interface built with Streamlit.

## Prerequisites
Before running the application, ensure you have the following installed:

- Python 3.8+
- Pip package manager

## Installation
Clone the repository and install the required dependencies:

```bash
git clone https://github.com/veydantkatyal/content-planner-crew-ai.git
cd content-planner-crew-ai

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

pip install -r requirements.txt
```

## Dependencies
The project requires the following Python packages:

```bash
pip install streamlit crewai litellm dotenv
```

## Usage
Run the Streamlit web application:

```bash
streamlit run app.py
```

Once the application is running, follow these steps:
1. Enter a topic for the blog.
2. Click the **"Generate Blog Outline"** button.
3. The AI agent will process the input and generate an outline.
4. The structured blog outline will be displayed on the UI.

## Project Structure
```
content-planner-crew-ai/
│── app.py              # Streamlit web app
│── content-planner-crewai.ipynb    # jupyter notebook
│── README.md           # Project documentation
```

## License
This project is open-source and available under the [MIT License](https://github.com/veydantkatyal/content-planner-crew-ai/blob/main/LICENSE).
