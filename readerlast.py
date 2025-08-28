with open("tf_idf_word.txt", "r") as f:
    mydict = eval(f.read())

l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []

def is_in_lst(word, lst):
    for x in lst:
        if x[0] == word:
            return x[1]
    return False

for word, lst in mydict.items():
    if lst[0] > max(lst[1:]):
        l1.append([word, lst[0]])

    elif lst[1] > max(lst[0], lst[2], lst[3], lst[4], lst[5]):
        l2.append([word, lst[1]])

    elif lst[2] > max(lst[0], lst[1], lst[3], lst[4], lst[5]):
        l3.append([word, lst[2]])

    elif lst[3] > max(lst[0], lst[1], lst[2], lst[4], lst[5]):
        l4.append([word, lst[3]])

    elif lst[4] > max(lst[0], lst[1], lst[2], lst[3], lst[5]):
        l5.append([word, lst[4]])

    elif lst[5] > max(lst[0], lst[1], lst[2], lst[3], lst[4]):
        l6.append([word, lst[5]])

def main_app(test_string=False):
    while True:
        if not test_string:
            test_string = input("Enter Text : ")
        anger_rank_predict = 0
        fear_rank_predict = 0
        happiness_rank_predict = 0
        hatred_rank_predict = 0
        sadness_rank_predict = 0
        wonder_rank_predict = 0
        for word in test_string.split(' '):

            anger_status = is_in_lst(word, l1)
            if anger_status:
                anger_rank_predict += anger_status

            fear_status = is_in_lst(word, l2)
            if fear_status:
                fear_rank_predict += fear_status

            happiness_status = is_in_lst(word, l3)
            if happiness_status:
                happiness_rank_predict += happiness_status

            hatred_status = is_in_lst(word, l4)
            if hatred_status:
                hatred_rank_predict += hatred_status

            sadness_status = is_in_lst(word, l5)
            if sadness_status:
                sadness_rank_predict += sadness_status

            wonder_status = is_in_lst(word, l6)
            if wonder_status:
                wonder_rank_predict += wonder_status

        emotion_scores = {'ANGRY': anger_rank_predict, 'FEAR': fear_rank_predict, 'HAPPY': happiness_rank_predict, 'HATE': hatred_rank_predict, 'SAD': sadness_rank_predict, 'SURPRISE': wonder_rank_predict}
        
        max_score = max(emotion_scores.values())
        max_emotion = [emotion for emotion, score in emotion_scores.items() if score == max_score]

        if __name__ == "__main__":
            print("The emotion scores for the string '" + test_string + "' are:")
            for emotion, score in emotion_scores.items():
                print(emotion + ": " + str(score))
            print("The highest score is " + str(max_score) + " and it belongs to the emotion(s): " + ", ".join(max_emotion))
            print("Therefore, the input string is related to the emotion(s): " + ", ".join(max_emotion))
            test_string = False
        else:
            return max_emotion

if __name__ == "__main__":
    main_app()