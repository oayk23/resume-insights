# resume-insights
Resume analysing tool with the power of Google Gemma 3.

## What is the purpose of this repository.
This repository is a resume analysing app. The goal is let users analyse and get insights about their resume by the power of Generative AI.It supports multilingual prompts tested in both English and Turkish.

## Installation

1.  Get `google/gemma-3-4b-it` model from [HuggingFace](https://huggingface.co/google/gemma-3-4b-it). To get the model:
- Login or sign up huggingface.
- Get access to model.
-  Click **Files and Versions** on the model card.
-  Download all the model files appears on the screen.

2. Install [poppler](https://poppler.freedesktop.org/) and add to path.
3. Then clone this repository via `git clone https://github.com/oayk23/resume-insights` on the terminal.
4. Create a folder named `model` in the repository.
5. After this open a terminal in the repository directory and type `pip install -r requirements.txt`.

Repo is ready!

## Usage
Basicly run `python app.py` on the terminal and click on the link that shows which url gradio started the app.

## Example

![example](https://github.com/oayk23/resume-insights/blob/main/example.jpg?raw=true)

## Limitations 
The package and work has some limitations,like generated text not shown in the textbox. It shown on a Markdown for prettify the model's outputs.
Some of the limitations about gemma 3. Like strong but limited image understanding etc.
