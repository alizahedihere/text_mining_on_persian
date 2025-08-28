import math

def stopword(row):
    new_row = []
    list_row = row.split(" ")
    for word in list_row:
        if [word] in verbal or [word] in short or [word] in nonverbal:
            continue
        else:
            new_row.append(word)
    new_new_row = ' '.join(new_row)
    return new_new_row

def preprocess(main_data):
    alphabet = ["ا", "ب", "پ", "ت", "ث", "ج", "چ", "ح", "خ", "د", "ذ", "ر", "ز", "ژ", "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف", "ق", "ک", "گ", "ل", "م", "ن", "و", "ه", "ی"," "]
    p_data = []
    emotionals = main_data.pop(0)
    for i_row in range(len(main_data)):
        if main_data[i_row] == ['']:
            continue
        elif len(main_data[i_row]) != 7:
            continue
        text_row = ""
        for char in main_data[i_row][0]:
            if char in alphabet:
                text_row += char
        text_row = list([text_row])
        text_row += main_data[i_row][1:]
        if text_row == '' or text_row == ' ' or len(text_row) < 7:
            continue
        text_row[0] = stopword(text_row[0])
        if text_row[0] == '' or text_row == ' ' or len(text_row) < 7:
            continue
        if text_row[0].isspace():
            continue
        p_data.append(text_row)
    return p_data, emotionals

def tf_idf(corpus, term, rank):
    tf_idf_anger = 0
    tf_idf_fear = 0
    tf_idf_happiness = 0
    tf_idf_hatred = 0
    tf_idf_sadness = 0
    tf_idf_wonder = 0
    term_idf = idf(corpus, term)
    i = 0
    for x in corpus:
        term_tf = tf(x, term)
        if term_tf != 0:
            if int(rank[i][0][0]) > emotion_limit:
                tf_idf_anger += term_tf*term_idf*int(rank[i][0][0])
            if int(rank[i][0][1]) > emotion_limit:
                tf_idf_fear += term_tf*term_idf*int(rank[i][0][1])
            if int(rank[i][0][2]) > emotion_limit:
                tf_idf_happiness += term_tf*term_idf*int(rank[i][0][2])
            if int(rank[i][0][3]) > emotion_limit:
                tf_idf_hatred += term_tf*term_idf*int(rank[i][0][3])
            if int(rank[i][0][4]) > emotion_limit:
                tf_idf_sadness += term_tf*term_idf*int(rank[i][0][4])
            if int(rank[i][0][5]) > emotion_limit:
                tf_idf_wonder += term_tf*term_idf*int(rank[i][0][5])
        i += 1
    return [tf_idf_anger, tf_idf_fear, tf_idf_happiness, tf_idf_hatred, tf_idf_sadness, tf_idf_wonder]

def idf(corpus, term):
    term_df = 0
    for x in corpus:
        term_df += df([x], term)
    if term_df == 0:
        return False
    idf = math.log(len(corpus)/term_df)
    return idf

def cf(docs_list,word):
    i = 0
    j = len(docs_list)
    for x in docs_list:
        i += wd(x, word)
    return round(i/j,2)

def df(docs_list,word):
    i = 0
    for x in docs_list:
        if tf(x, word) > 0:
            i += 1
    return i

def tf(doc, word):
    j = 0.0
    i = 0.0
    for x in doc.split(" "):
        if x == ''or x == ' ':
            continue
        if x == word:
            i += 1
        j += 1
    return round(i/j,2)

def wd(doc, word):
    i = 0
    for x in doc.split(" "):
        if x == '':
            continue
        if x == word:
            i += 1
    return i

with open('dataset.csv', 'r') as file:
    data = [line.strip().split(',') for line in file]
with open('verbal.txt', 'r') as file:
    verbal = [line.strip().split(',') for line in file]
with open('short.txt', 'r') as file:
    short = [line.strip().split(',') for line in file]
with open('nonverbal.txt', 'r') as file:
    nonverbal = [line.strip().split(',') for line in file]

p_data, emotionals = preprocess(data)
print("Preprocess Done!")

unique_words_list = []
text_list = []
emotion_list = []

for row in p_data:
    tmp = []
    text_list.append(row[0])
    tmp.append([row[1]])
    tmp[0].append(row[2])
    tmp[0].append(row[3])
    tmp[0].append(row[4])
    tmp[0].append(row[5])
    tmp[0].append(row[6])
    emotion_list.append(tmp)
    for word in row[0].split(' '):
        if word == '' or word == ' ':
            continue
        if word not in unique_words_list:
            unique_words_list.append(word)

print("spliting Done!")

tf_idf_limit = 3
emotion_limit = 2

anger_rank = {}
fear_rank = {}
happiness_rank = {}
hatred_rank = {}
sadness_rank = {}
wonder_rank = {}
i = 0

for word in unique_words_list:
    t = tf_idf(text_list, word, emotion_list)
    anger_rank[word] = t
    print(i)
    i += 1

with open("tf_idf_word.txt", "w") as f:
    f.write(str(anger_rank))