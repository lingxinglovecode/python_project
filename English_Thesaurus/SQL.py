'''
从网络数据库读取字典资源对特定单词的定义进行查询
实现功能列表：
[√] 读取到数据库中的字典资源
[√] 查询特定单词
[√] 如果没有查询到单词对最相近词进行提示
'''
import mysql.connector
from difflib import get_close_matches
con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

cursor = con.cursor()
word = input("Please type your word: ")
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'"%word)
results = cursor.fetchall()
if not results:
    query = cursor.execute("SELECT Expression FROM Dictionary ")
    wordbook = cursor.fetchall()
    wordbook_list = wordbook[:]
    for i in range(len(wordbook)):
        wordbook_list[i] = wordbook[i][0]
    closest_word = get_close_matches(word,wordbook_list)[0]
    confirm = input("Did you mean the word %s:"%closest_word+"y or n? ")
    if confirm.lower() == 'y':
        query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % closest_word)
        results = cursor.fetchall()
if results:
    for result in results:
        print(result[1])
else:
    print("Sorry,we didnt find the word.")