import time
import random

correct=0
count=0

print("순간기억력 테스트")
print()
print("게임을 시작하려면 아무 키나 눌러주세요")
start=input("게임을 그만하려면 exit를 입력하세요: ")

if(start=="exit"):
    print("결과(정답/문제수): %d / %d " % (correct, count))

else:
    for i in range(3, 0, -1):
        print("%d초 뒤 시작합니다.. " % i)
        time.sleep(1)
    print()
    list=[]
    f=open("game_word.txt", "r", encoding="utf-8")
    lines=f.readlines()
    for line in lines:
        temp=line.replace("\n", "")
        list.append(temp)
    while(1):
        x=random.choice(list)
        print(x)
        time.sleep(1.5)
        print("\n"*40)
        print("(게임을 그만하려면 exit를 입력하세요)")
        answer=input("정답은?: ")

        if(answer==x):
            print("정답~")
            correct=correct+1
        else:
            print("오답!")
            
        print()
        count=count+1
        if(answer=="exit"):
            print("결과(정답/문제수): %d / %d " % (correct, count-1))
            break
    f.close()
