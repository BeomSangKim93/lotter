print("hello 로또")

from random import *
from math import *

MAXLOTTERNUM = 6    #1등 로또 맞아야하는 개수
bool_reLotter = True #로또번호가 적합하지 확인하는 인자


cntThree = 0        #3개 맞은개수
cntFour = 0         #4개 맞은개수
cntFive = 0         #5개 맞은개수

cnt_rount = 0           #회전수
int_rand = [0, 0, 0, 0, 0 ,0]  #로또 번호 입력
sort_rand = [0, 0, 0, 0, 0 ,0]  #로또 번호 큰수부터 작은수로 소팅//숫자가 뒤에서 맞는경우의 수를 생각함
lotter_num = [1, 2, 5, 10, 30, 40]
intRdnum = 0    #rand번호
cntLotter = 0  #동일한 숫자개수, 회전마다 초기화
bool_end = True    #롯또당첨이면 False
intEqnum = 0     #랜덤숫자가 같은지 체크할때 사용
bool_rand = True  #랜덤숫자 발생 끝


#########입력된 로또 숫자가 적합한지 체크함수

def CheckLotterNum(lotter_num, bool_reLotter):
    #첫번째 로또번호 체크
    if lotter_num[0] > 0 and lotter_num[0] <= 45 and lotter_num[0] != lotter_num[1] and lotter_num[0] != lotter_num[2] and lotter_num[0] != lotter_num[3] and lotter_num[0] != lotter_num[4] and lotter_num[0] != lotter_num[5] :
        bool_reLotter = False
    else :
        print("로또번호에 적합하지 않습니다. 로또 번호를 입력해주세요 동일하지 않은 1 ~ 45 사이의 숫자입니다")
        return bool_reLotter

    #두번째 로또번호 체크
    if lotter_num[1] > 0 and lotter_num[1] <= 45 and lotter_num[1] != lotter_num[0] and lotter_num[1] != lotter_num[2] and lotter_num[1] != lotter_num[3] and lotter_num[1] != lotter_num[4] and lotter_num[1] != lotter_num[5] :
        bool_reLotter = False
    else: 
        bool_reLotter = True
        print("로또번호에 적합하지 않습니다. 로또 번호를 입력해주세요 동일하지 않은 1 ~ 45 사이의 숫자입니다")
        return bool_reLotter
    
    #세번째 로또번호 체크
    if lotter_num[2] > 0 and lotter_num[2] <= 45 and lotter_num[2] != lotter_num[1] and lotter_num[2] != lotter_num[0] and lotter_num[2] != lotter_num[3] and lotter_num[2] != lotter_num[4] and lotter_num[2] != lotter_num[5] :
        bool_reLotter = False
    else: 
        bool_reLotter = True
        print("로또번호에 적합하지 않습니다. 로또 번호를 입력해주세요 동일하지 않은 1 ~ 45 사이의 숫자입니다")
        return bool_reLotter
    
    #네번째 로또번호 체크
    if lotter_num[3] > 0 and lotter_num[3] <= 45 and lotter_num[3] != lotter_num[1] and lotter_num[3] != lotter_num[2] and lotter_num[3] != lotter_num[0] and lotter_num[3] != lotter_num[4] and lotter_num[3] != lotter_num[5] :
        bool_reLotter = False
    else: 
        bool_reLotter = True
        print("로또번호에 적합하지 않습니다. 로또 번호를 입력해주세요 동일하지 않은 1 ~ 45 사이의 숫자입니다")
        return bool_reLotter
    
    #다섯번째 로또번호 체크
    if lotter_num[4] > 0 and lotter_num[4] <= 45 and lotter_num[4] != lotter_num[1] and lotter_num[4] != lotter_num[2] and lotter_num[4] != lotter_num[3] and lotter_num[4] != lotter_num[0] and lotter_num[4] != lotter_num[5] :
        bool_reLotter = False
    else: 
        bool_reLotter = True
        print("로또번호에 적합하지 않습니다. 로또 번호를 입력해주세요 동일하지 않은 1 ~ 45 사이의 숫자입니다")
        return bool_reLotter
    
    #여섯번째 로또번호 체크
    if lotter_num[5] > 0 and lotter_num[5] <= 45 and lotter_num[5] != lotter_num[1] and lotter_num[5] != lotter_num[2] and lotter_num[5] != lotter_num[3] and lotter_num[5] != lotter_num[4] and lotter_num[5] != lotter_num[0] :
        bool_reLotter = False
    else: 
        bool_reLotter = True
        print("로또번호에 적합하지 않습니다. 로또 번호를 입력해주세요 동일하지 않은 1 ~ 45 사이의 숫자입니다")

    return bool_reLotter



###########로또번호 입력받기
print("이번 회차 로또 번호를 입력해주세요 1 ~ 45 사이의 숫자입니다")
while(bool_reLotter) :
    lotter_num[0] = eval(input("1번째 로또 숫자는(1~45) = "))
    lotter_num[1] = int(input("2번째 로또 숫자는(1~45) = "))
    lotter_num[2] = eval(input("3번째 로또 숫자는(1~45) = "))
    lotter_num[3] = eval(input("4번째 로또 숫자는(1~45) = "))
    lotter_num[4] = eval(input("5번째 로또 숫자는(1~45) = "))
    lotter_num[5] = eval(input("6번째 로또 숫자는(1~45) = "))

    bool_reLotter = CheckLotterNum(lotter_num, bool_reLotter)



print("이번회차 로또번호는 {0} {1} {2} {3} {4} {5}".format(lotter_num[0],lotter_num[1],lotter_num[2],lotter_num[3],lotter_num[4],lotter_num[5]))
    

#########랜덤 번호 발생해서 로또 번호 맞는지 확인
while (bool_end):
    
    # 랜덤숫자 초기화
    int_rand[0] = 0
    int_rand[1] = 0
    int_rand[2] = 0
    int_rand[3] = 0
    int_rand[4] = 0
    int_rand[5] = 0

    #랜덤 숫자 위치 초기화
    intRdnum = 0 
    intEqnum = 0

    #랜덤숫자 발생 루틴
    while (bool_rand) :
        int_rand[intRdnum] = randint(1,45) #랜덤숫자 발생
        
        for intEqnum in range(intRdnum) :
            if int_rand[intEqnum]==int_rand[intRdnum]: #이전것들과 같은지 체크
                intRdnum -= 1
                break

        intRdnum += 1   #랜덤다음번 랜덤 숫자로 넘어가기
        if intRdnum >= 6 : #랜덤숫자가 6개발생했으면 중지
            bool_rand = False
    
    #랜덤 발생진행 위치 초기화
    bool_rand = True

    #랜덤 숫자 출력
 #   print(str(cnt_rount)+" 번째 롯또숫자는 = "+str(int_rand[0])+" "+str(int_rand[1])+" "+str(int_rand[2])+" "+str(int_rand[3])+" "+str(int_rand[4])+" "+str(int_rand[5])+" ")
    
    #작은 수에서 큰수로 소팅
    sort_rand[0] = int_rand[0]
    sort_rand[1] = int_rand[1]
    sort_rand[2] = int_rand[2]
    sort_rand[3] = int_rand[3]
    sort_rand[4] = int_rand[4]
    sort_rand[5] = int_rand[5]
    sort_rand.sort()

    for intRdnum in range(0,6) :

        #1번째 로또번호 맞는지 체크
        if sort_rand[intRdnum] == lotter_num[0] : 
            cntLotter += 1
        #    print(str(intRdnum+1)+"번째 숫자 맞음 " + str(sort_rand[intRdnum]))
                    
        #2번째 로또번호 맞는지 체크
        if sort_rand[intRdnum] == lotter_num[1] : 
            cntLotter += 1
        #    print(str(intRdnum+1)+"번째 숫자 맞음 " + str(sort_rand[intRdnum]))
                    
        #3번째 로또번호 맞는지 체크
        if sort_rand[intRdnum] == lotter_num[2] : 
            cntLotter += 1
        #    print(str(intRdnum+1)+"번째 숫자 맞음 " + str(sort_rand[intRdnum]))
                    
        #4번째 로또번호 맞는지 체크
        if sort_rand[intRdnum] == lotter_num[3] : 
            cntLotter += 1
        #    print(str(intRdnum+1)+"번째 숫자 맞음 " + str(sort_rand[intRdnum]))
                    
        #5번째 로또번호 맞는지 체크
        if sort_rand[intRdnum] == lotter_num[4] : 
            cntLotter += 1
        #    print(str(intRdnum+1)+"번째 숫자 맞음 " + str(sort_rand[intRdnum]))
            
        #6번째 로또번호 맞는지 체크
        if sort_rand[intRdnum] == lotter_num[5] : 
            cntLotter += 1
        #    print(str(intRdnum+1)+"번째 숫자 맞음 " + str(sort_rand[intRdnum]))
                
    #맞은 개수 추가
    if cntLotter == 3 : cntThree += 1
    if cntLotter == 4 : cntFour  += 1
    if cntLotter == 5 : #5개 맞으면 출력
        cntFive += 1
        print("{0:<10,} 번째 5개 맞음, 로또숫자는 = ".format(cnt_rount+1),end=" ")
        print(str(int_rand[0])+" "+str(int_rand[1])+" "+str(int_rand[2])+" "+str(int_rand[3])+" "+str(int_rand[4])+" "+str(int_rand[5])+" ")


    #롯또 맞은 개수 체크
    if cntLotter >= MAXLOTTERNUM :
        bool_end = False

    cnt_rount += 1      #로또뽑기 발생개수 추가
    cntLotter = 0       #롯또 맞은 개수 초기화
    
#   print("진행상황 프린트")
    if (cnt_rount%2)  == 0 : print("/",end="\x08")
    if (cnt_rount%2)  == 1 : print("\\",end="\x08")
        


#########  마무리 정리 프린트
print("\n 전체회전수는 {0:<10,}".format(cnt_rount))
print("로또숫자는 = "+str(int_rand[0])+" "+str(int_rand[1])+" "+str(int_rand[2])+" "+str(int_rand[3])+" "+str(int_rand[4])+" "+str(int_rand[5])+" ")
print("번호 3개 맞은 개수는 {0:<10,}".format(cntThree))
print("번호 4개 맞은 개수는 {0:<10,}".format(cntFour))
print("번호 5개 맞은 개수는 {0:<10,}".format(cntFive))
