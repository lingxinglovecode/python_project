'''
The first project of a dictionary.
Enter the word to see its defination.
'''
import json
from difflib import SequenceMatcher
from difflib import get_close_matches
import mysql.connector
def translate_word(word):
    # word = word.lower()
    # data = json.load(open('data.json'))

    import mysql.connector
    from difflib import get_close_matches
    con = mysql.connector.connect(
        user="ardit700_student",
        password="ardit700_student",
        host="108.167.140.122",
        database="ardit700_pm1database"
    )
    cursor = con.cursor()
    # word = input("Please type your word: ")
    query = cursor.execute("SELECT * FROM Dictionary")
    results = cursor.fetchall()
    data = {}
    for i in range(len(results)):
        data.update({results[i][0]: results[i][1]})


    if word.title() in data:
        return optimize_output(data[word.title()])
    elif word.upper() in data:
        return optimize_output(data[word.upper()])
    elif word in data:
        return optimize_output(data[word])
    elif len(get_close_matches(word,data))>0:
        similar_words = get_close_matches(word,data)
        answer = input("Did you mean the word \""+str(similar_words[0])+"\" instead? ")
        answer = answer.lower()
        if answer in ['right','yes','y']:
            return optimize_output(data[similar_words[0]])
        elif answer in ['n','no']:
            return print("No defination of the word.")
        else:
            return print("We didn't understand what you entry.")
    return print("No defination of the word.")

def optimize_output(answer):
    if len(answer) == 1:
        print("Defination:"+answer[0])
    else:
        for i in range(len(answer)):
            print("Defination {}:".format(i+1)+answer[i])





if __name__ == '__main__':
    while True:
        word = input("Please enter a word:")
        translate_word(word)

