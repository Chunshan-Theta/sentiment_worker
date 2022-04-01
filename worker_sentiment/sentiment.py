from transformers import AutoTokenizer, AutoModelForSequenceClassification
# tokenizer = AutoTokenizer.from_pretrained("techthiyanes/chinese_sentiment")
# model = AutoModelForSequenceClassification.from_pretrained("techthiyanes/chinese_sentiment")
tokenizer = AutoTokenizer.from_pretrained("rohanrajpal/bert-base-multilingual-codemixed-cased-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("rohanrajpal/bert-base-multilingual-codemixed-cased-sentiment")


def senti(text):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)["logits"][0].tolist()
    # return [(outputs[0]+outputs[1])/2,outputs[2],(outputs[3]+outputs[4])/2]
    return outputs


def senti_vec(text):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)["logits"][0].tolist()
    score = ((outputs[2] - outputs[0]) / 3.5 + 1) / 2 * 0.85
    return score if 0 < score < 1 else float(int(score))

def senti_level(text):
    # result = senti(text) #negative, neutral, positive
    # max_index = result.index(max(result))
    # if max_index == 0:
    #     return 0
    # if max_index == 1:
    #     return 0.5
    # if max_index == 2:
    #     return 1
    negative, neutral, positive = senti(text)
    if positive < -0.5:
        return 0
    if positive < 0:
        return 0.5
    if positive > 0:
        return 1



print(senti_level("你可以去死嗎"))
print(senti_level("你這個離經叛道的傢伙"))
print(senti_level("這個食物真的太好吃了"))
# print("-")
# print(senti_vec("你可以去死嗎"))
# print(senti_vec("你這個離經叛道的傢伙"))
# print(senti_vec("這個食物真的太好吃了"))
# print("-")
# print(senti_vec("違憲"))
# print(senti_vec("犯不着"))
# print(senti_vec("惡人先告狀"))