cores = [0 , 2, 2, 3]
btn_AP = [1,2,2,1]

acertos = 0

for cor in cores:
    if cor == btn_AP[cor]:
        acertos += 1
print(acertos)
