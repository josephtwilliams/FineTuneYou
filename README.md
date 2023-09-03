FineTuneYou
===========

Overview
--------

`FineTuneYou` is a project designed to fine-tune language models based on personalized text documents, such as resumes and custom questions. Leveraging the capabilities of GPT-3.5-turbo, this project allows users to generate questions based on their resume, fine-tune a language model, and utilize it for various tasks.

Features
--------

-   PDF to Text: Convert your resume from PDF format to a text file.
-   Question Generation: Generate custom questions based on your resume.
-   Fine-Tuning: Fine-tune a language model using your generated questions and resume.
-   Embedding Generation: Create embeddings for fast and efficient querying.
-   Question Answering: Utilize the fine-tuned model for Q&A tasks based on your resume.

Requirements
------------

-   Python 3.11
-   OpenAI GPT-3.5-turbo API key
-   Various Python packages such as `openai`, `dotenv`, etc.

Installation
------------

1.  Clone the Repository

    bashCopy code

    `git clone https://github.com/josephtwilliams/FineTuneYou.git`

2.  Install Required Python Packages

    bashCopy code

    `pip install -r requirements.txt`

3.  Set Up Your OpenAI API Key Create a `.env` file in the root directory and add the following line:

    bashCopy code

    `OPENAI_API_KEY=your-api-key`

Usage
-----

### Step 1: Upload Resume and Fill Out Questions

-   Upload your resume into the root directory, replacing `resume_example.pdf`.
-   Fill out additional questions in the `questions.json` file. You are free to add your own questions as well.

### Step 2: Run the Notebook

Open and run all the cells in the `FineTuneYou.ipynb` notebook.

### Step 3: Check Results

After successfully running the notebook, you can check the results of the fine-tuning and question-answering tasks.

Resetting the Project
---------------------

To reset the project and remove all generated files except for essential ones like `inappropriate_questions.txt` and `questions.json`, you can use the `reset_project()` Python function.

pythonCopy code

`from reset_script import reset_project
reset_project()`

License
-------

MIT