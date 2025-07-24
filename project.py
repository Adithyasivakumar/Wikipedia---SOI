import wikipedia
import re
from langdetect import detect
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag

# ===================================================================
# FINAL FIX: Forcing NLTK to find the data in your home directory.
# This line explicitly adds the correct path for NLTK to search.
nltk.data.path.append('/home/adithya/nltk_data')
# ===================================================================


def run_nlp_project():
    print("Starting the program...")
    raw_text = ""

    try:
        random_page_title = wikipedia.random(pages=1)
        print(f"✅ Step 1: Found a random page -> '{random_page_title}'")
        page = wikipedia.page(random_page_title, auto_suggest=False, redirect=True)
        raw_text = page.content
        print("   - Successfully fetched the page content.")

    except wikipedia.exceptions.DisambiguationError as e:
        print(f"   - ⚠️ This is a disambiguation page. Automatically choosing: '{e.options[0]}'")
        try:
            page = wikipedia.page(e.options[0], auto_suggest=False, redirect=True)
            raw_text = page.content
            print("   - Successfully fetched the new page content.")
        except Exception as new_e:
             print(f"❌ An error occurred trying to fetch the disambiguation option: {new_e}")
             return

    except Exception as e:
        print(f"❌ An error occurred: {e}.")
        return

    if not raw_text:
        print("Could not retrieve any text to process. Stopping.")
        return

    # 2. DETECT THE LANGUAGE
    language = detect(raw_text)
    print(f"✅ Step 2: Detected Language -> {language}")

    # 3. SEGMENT INTO SENTENCES
    text_for_sentencing = raw_text.replace('\n', ' ')
    sentences = sent_tokenize(text_for_sentencing)
    print(f"✅ Step 3: Segmented text into {len(sentences)} sentences.")
    
    first_real_sentence = ""
    for s in sentences:
        if len(s.strip()) > 10:
            first_real_sentence = s
            break
    
    if not first_real_sentence:
        print("Could not find a valid sentence to process.")
        return

    print(f"\n--- Now processing the first full sentence ---")
    print(f"'{first_real_sentence}'")
    
    # 4. TOKENIZE THE SENTENCE INTO WORDS
    words = word_tokenize(first_real_sentence)
    print(f"\n✅ Step 4: Tokenized the sentence into {len(words)} words.")
    print(words)

    # 5. APPLY PART-OF-SPEECH (POS) TAGGING
    tagged_words = pos_tag(words)
    print(f"\n✅ Step 5: Applied POS tags to each word.")
    print(tagged_words)


if __name__ == "__main__":
    run_nlp_project()