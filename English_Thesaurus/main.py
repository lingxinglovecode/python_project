
import json
from difflib import SequenceMatcher
from difflib import get_close_matches
def translate_word(word):
    word = word.lower()
    data = json.load(open('data.json'))

    if word in data:
        return data[word]
    else:
        similar_words = get_close_matches(word,data)
        answer = input("Did you mean the word \""+str(similar_words[0])+"\" Yes or no? ")
        answer = answer.lower()
        if answer in ['right','yes']:
            return data[similar_words[0]]
        return "No defination"


if __name__ == '__main__':
    word = input("Please enter a word:")

    print(translate_word(word))

