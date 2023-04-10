from bs4 import BeautifulSoup
import imgkit
import re
from make_gpt_call import get_content_from_gpt
from split_transcript import split_transcript
from transcript import get_transcript
import random

speaker = "Ezra Klein"
episode = "Episode 3 - Upstream with Erik Torenberg"

def get_top_quotes():
    chunk_size = 750
    transcript = get_transcript()
    transcript_parts = split_transcript(transcript, chunk_size)

    top_quotes = []

    for i in range(4):
        for part in transcript_parts:
            identify_quote_prompt = f'''Below is a transcript. Identify the top quote - at least 25 words, no more than 50 words.\n\n
            {part}
            '''
            quote = get_content_from_gpt(identify_quote_prompt)

            mark_quote_prompt = f'''Below is a quote. Mark the most important phrases in bold using <b>.\n\n
            {quote}
            '''
            quote = get_content_from_gpt(mark_quote_prompt)

            print(quote)
            top_quotes.append(quote)
    
    return top_quotes

def create_quote_image(quote):
    with open('template.html') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

        sentences = re.split('(?<=[.!?]) +', quote)

        quote_elem = soup.find('div', {'id': 'quote'})
        speaker_elem = soup.find('div', {'id': 'speaker'})
        episode_elem = soup.find('div', {'id': 'episode'})
        quote_elem.clear()            
        speaker_elem.clear()            
        episode_elem.clear()            
        for i in range(len(sentences)):
            text = sentences[i]
            if text:
                quote_elem.append(BeautifulSoup(f"<p>{text}</p>", 'html.parser'))
        
        speaker_elem.append(f"{speaker}")
        speaker_elem.append(soup.new_tag('br'))
        episode_elem.append(f"{episode}")

        html = str(soup)

        print(html)

        random_number = random.randint(1, 1000000)

    imgkit.from_string(html, f"quote-{random_number}.png")

top_quotes = get_top_quotes()
for quote in top_quotes:
    create_quote_image(quote)
