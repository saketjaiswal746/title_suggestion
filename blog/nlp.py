from transformers import pipeline
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('all')

def suggest_titles(content):
    # Load a pre-trained summarization model
    summarizer = pipeline(
        'summarization',
        model='facebook/bart-large-cnn',
        tokenizer='facebook/bart-large-cnn',
        clean_up_tokenization_spaces=True
    )

    # Limit input length to the model's requirements
    max_input_length = 512
    summary = summarizer(content[:max_input_length], max_length=50, min_length=5, do_sample=False)

    # Generate the summary text
    summary_text = summary[0]['summary_text']
    
    # Shorten the summary text for title generation
    shortened_summary = summary_text.split('.')[0]  # Use only the first sentence as a base for title

    # Additional creative titles based on content keywords or summary
    keywords = extract_keywords(content)  # Implement a function to extract keywords
    if keywords:
        keyword = keywords[0].capitalize()  # Use the first keyword in titles
    else:
        keyword = "Insights"

    # Create three distinct suggested titles
    titles = [
        f"{shortened_summary}",  # Use the shortened summary as a simple title
        f"Understanding {keyword} in Depth",  # A more generalized title with a keyword
        f"Top Strategies for {keyword} Success"  # A creative variation
    ]

    # Ensure uniqueness of the titles by removing duplicates
    return list(set(titles))

def extract_keywords(text):
    # Tokenize the text
    words = word_tokenize(text.lower())
    
    # Filter out stop words and non-alphabetic tokens
    filtered_words = [word for word in words if word.isalpha() and word not in stopwords.words('english')]
    
    # Get the frequency distribution of words
    freq_dist = FreqDist(filtered_words)
    
    # Return the most common keywords
    return [word for word, _ in freq_dist.most_common(5)]  # Return top 5 keywords
