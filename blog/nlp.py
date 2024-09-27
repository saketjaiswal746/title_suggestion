from transformers import pipeline
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')
# nltk.download('all')

def suggest_titles(content):
    summarizer = pipeline(
        'summarization',
        model='facebook/bart-large-cnn',
        tokenizer='facebook/bart-large-cnn',
        clean_up_tokenization_spaces=True
    )

    max_input_length = 512
    summary = summarizer(content[:max_input_length], max_length=50, min_length=5, do_sample=False)

    summary_text = summary[0]['summary_text']
    
    shortened_summary = summary_text.split('.')[0] 

    keywords = extract_keywords(content)
    if keywords:
        keyword = keywords[0].capitalize()  
    else:
        keyword = "Insights"

    titles = [
        f"{shortened_summary}",  
        f"Understanding {keyword} in Depth",  
        f"Top Strategies for {keyword} Success" 
    ]

    return list(set(titles))

def extract_keywords(text):

    words = word_tokenize(text.lower())
    
    filtered_words = [word for word in words if word.isalpha() and word not in stopwords.words('english')]
    
    freq_dist = FreqDist(filtered_words)
    
    return [word for word, _ in freq_dist.most_common(5)]  
