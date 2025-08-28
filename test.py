import readerlast

with open("test_data.txt", "r") as f:
    data = eval(f.read())

correct = 0
not_answer = 0
i = 0
emo_count = {}

for text in data:
    predict = readerlast.main_app(text)
    if len(predict)==6:
        not_answer += 1
        continue
    if predict[0] == data[text]:
        correct += 1
    if data[text] in emo_count:
        emo_count[data[text]] += 1
    else:
        emo_count[data[text]] = 1
    print(f"{i} : Emo = {data[text]}, Predict = {predict[0]}")
    i += 1

accuracy = (correct/len(data))*100
print(f"Sampels : {len(data)}, Correct Predicts : {correct}")
print(f"Accuracy : {accuracy}")
if not not_answer:
    print(f"Not Answerd : {not_answer}")
for x in emo_count:
    print(f"{x}:{emo_count[x]}")