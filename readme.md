# Django Blog Application with NLP Title Suggestions

## Overview

This project is a Django-based blog application that allows users to create blog posts. It integrates Natural Language Processing (NLP) to suggest titles based on the content of the posts using the `transformers` library.

## Features
- Automatic title suggestions based on the content using NLP.
- API endpoint for fetching title suggestions in JSON format.

## Technologies Used

- Django
- Python
- Transformers library (Hugging Face)
- NLTK for natural language processing
- Bootstrap for frontend styling

## Installation

### Steps to Install

1. **Clone the repository:**

   ```bash
   git clone https://github.com/saketjaiswal746/title_suggestion.git
   cd title_suggestion

2. **Create virtual Environment:**

python -m venv venv
venv\Scripts\activate

3. **Install the required package**

pip install -r requirements.txt

4. **Set up the database:**

Run the following commands to apply migrations and create a database:

python manage.py makemigrations
python manage.py migrate

5. **Run the development server**

python manage.py runserver


## Usage

 # Creating a Blog Post:

Navigate to the blog creation page.
Enter the content of your blog post.
Upon submission, suggested titles will be displayed based on the content.

You can access the application at http://127.0.0.1:8000/blog/create/


## API for Title Suggestions:

- You can also use the API endpoint to get title suggestions.

- Send a POST request to http://127.0.0.1:8000/blog/api/suggest-titles/ 

- with the following JSON body:
 {
     "content": "Your blog content here."
 }
- The response will contain suggested titles in JSON format.

