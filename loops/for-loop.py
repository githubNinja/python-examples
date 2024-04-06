'''scores =  [99, 65, 45, 89, 23,57,90, 72]
for score in scores:
  if score < 70:
      print("score is::", score, "::It's fail")
  if score == 70 and score <=80:
        print("score is::", score, "SCORE is :C")
  if score >=80 and score <=90:
        print("score is::", score, "Score is :B")
  if score >90:
        print("score is::", score, "Score is :A")
        '''

scores = [99, 65, 45, 89, 23, 57, 90, 72]
length = len(scores)
i = 0
while i < length:
    if scores[i] < length:
        print("score is::", scores, "::It's fail")
    elif scores[i] == 70 and scores[i] <= 80:
        print("score is::", scores, "SCORE is :C")
    elif 80 <= scores[i] <= 90:
        print("score is::", scores, "Score is :B")
    elif scores[i] > 90:
        print("score is::", scores, "Score is :A")

    i = i + 1
