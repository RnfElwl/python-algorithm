word = input()

croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]


for i in croatia:
    word = word.replace(i, "*")
#길이를 아예 1로 줄이니까 그냥 크로아티아랑 알파벳을 합친 갯수가 같아 지네;;
print(len(word))
#난 병따개다
