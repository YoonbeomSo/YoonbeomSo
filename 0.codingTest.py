# #입출력과 사칙연산

# print("HelloWorld")

# print("강한친구 대한육군\n강한친구 대한육군")

# print("\\    /\\\n )  ( \')\n(  /  )\n \\(__)|")

# print("|\\_/|\n|q p|   /}\n( 0 )\"\"\"\\\n|\"^\"`    |\n||_/=\\\\__|")

# A, B = map(int,input().split())
# print(A+B)

# A, B = map(int,input().split())
# print(A-B)

# A, B = map(int,input().split())
# print(A*B)

# A, B = map(float,input().split())
# print(A/B)

# A,B = map(int,input().split())
# print(A+B)
# print(A-B)
# print(A*B)
# print(A//B)
# print(A%B)

# A, B, C = map(int,input().split())
# print((A+B)%C)
# print(((A%C)+(B%C))%C)
# print((A*B)%C)
# print(((A%C)*(B%C))%C)

# A=int(input())
# B=int(input())

# print(A*(B%10))
# print(A*(B//10%10))
# print(A*(B//100))
# print(A*B)









# #if문

# #1330 두 수 비교하기
# A,B=map(int,input().split())
# if A>B:
#     print(">")
# elif A<B:
#     print("<")
# else:
#     print("==")

# #9498 시험 성적
# A=int(input())

# if 100>=A>=90:
#     print('A')
# elif 90>A>=80:
#     print('B')
# elif 80>A>=70:
#     print('C')
# elif 70>A>=60:
#     print('D')
# else:
#     print("F")


# #2753 윤년
# A=int(input())

# if  A%4==0 and A%100!=0 or A%400==0:
#     print("1")
# else:
#     print("0")


# #14681번 사분면 고르기
# x=int(input())
# y=int(input())

# if x>0 and y>0:
#     print("1")
# elif x<0 and y>0:
#     print("2")
# elif x<0 and y<0:
#     print("3")
# elif x>0 and y<0:
#     print("4")


# #2884 알람시계
# a, b = map(int,input().split())

# if a>0 and b-45 < 0:
#     print(a-1, b-45+60)
# elif a==0 and b-45<0:
#     print(a+23, b-45+60)
# else:
#     print(a, b-45)










# #for문

# #2739번 구구단
# N = int(input())
# for i in range(1,10):
#     print(N,"*",i,"=",N*i)

# #10950번 A+B-3

# N =int(input())

# for i in range(N):
#     a, b = map(int,input().split())
#     print(a+b)

# #8393번 합

# N = int(input())
# sum = 0

# for i in range(1,N+1):
#     sum += i
# print(sum)

# #15552번 빠른A+B
# import sys

# N = int(input())
# for i in range(N):
#     A, B = map(int, sys.stdin.readline().split())
#     print(A+B)

# #2741번 N찍기
# N = int(input())
# for i in range(1,N+1):
#     print(i)
    
# # 2742번 기찍N
# N = int(input())
# for i in range(N,0,-1):
#     print(i)

# # 11021 A+B -7
# N = int(input())
# for i in range(1,N+1):
#     a, b = map(int,input().split())
#     print(f"Case #{i}:", a+b) 
    
# # 11022 A+B -8
# N = int(input())
# for i in range(1,N+1):
#     a, b = map(int, input().split())
#     print(f"Case #{i}: {a} + {b} =",a+b)

# #2438 별찍기 -1
# N = int(input())
# for i in range(1,N+1):
#     print("*"*i)
    
# #2439 별찍기 -2
# N = int(input())
# for i in range(1,N+1):
#     print(" "*(N-i) + "*"*i)


# #10871 x보다 작은 수
# N, X = map(int,input().split())
# A = list(map(int,input().split()))
# for i in range(N):
#     if A[i]<X:
#         print(A[i],end="")







# #while문
# #10952번 A+B -5
# while True:
#     a, b = map(int, input().split())
#     if a == 0 and b == 0:
#         break
#     print(a+b)
    
# #10951번  A+B -4
# while True:
#     try:
#         a, b = map(int, input().split())
#         print (a+b)
#     except:
#         break

# #1110번 더하기 사이클
# n=int(input())
# num=n
# su=0
# while True:
#     a = num//10
#     b = num%10
#     c = (a+b) %10
#     num = b*10 + c 
#     su+=1
#     if n == num:
#         print(su)
#         break








# #1차원 배열

# # 10818번 최소, 최대
# N=int(input())
# numbers = list(map(int,input().split()))
# maxa=numbers[0]
# mina=numbers[0]
# for i in numbers :
#     if i > maxa :
#         maxa = i
#     elif i < mina:
#         mina = i
# print(mina, maxa)

# # 2562번 최대값
# su=[]
# for i in range(0,9):
#     su.append(int(input()))
# maxa=su[0]
# for i in su:
#     if i > maxa:
#         maxa = i
# #maxa=max(su)
# print(maxa)
# print(su.index(maxa)+1)

# #2577번 숫자의 개수
# A = int(input())
# B = int(input())
# C = int(input())
# result=list(str(A*B*C))
# for i in range(10):
#     print(result.count(str(i)))

# #3052번 나머지
# li=[]
# for i in range(10):
#     li.append((int(input()))%42)
# sli = set(li)
# print(len(sli))

# #1546번 평균
# ea = int(input())
# li = list(map(int,input().split()))
# li2 =[]
# maxa=li[0]
# for i in li:
#     if i > maxa:
#         maxa=i      
# for i in li:
#     li2.append(((i/maxa)*100))
# print(int(sum(li2))/ea)  

# #8958번 OX퀴즈
# ea = int(input())
# for i in range(ea):
#     data = input()
#     score = 0
#     point = 1
#     for i in data:
#         if i == "O":
#             score+=point
#             point+=1
#         else:
#             point = 1
#     print(score)


# #4344번 평균은 넘겠지

# nea = int(input())
# for i in range(nea):
#     score = list(map(int,input().split()))
#     average = sum(score[1:])/score[0]
#     su = 0
#     for j in score[1:]:
#         if j > average:
#             su += 1
#     re = su/score[0]*100
#     print(f"{re:.3f}%")



#함수

##15596번 정수 N개의 합

# def solve(a):
#     su = 0
#     for i in a:
#         su += i
#     return su

# #4673번 셀프넘버

# numbers = set(range(1,10000))
# remove_set = set()
# for i in numbers:
#     for j in str(i):
#         i += int(j)
#     remove_set.add(i)

# self_numbers = numbers - remove_set
# for i in (sorted(self_numbers)):
#     print(i)

# 1065번 한수

n = int(input())
result=[]
for i in range(1,n+1):
    li=[]
    if i<100:
        result.append(i)
    else :
        for j in str(i):
            li.append(int(j))       
        a = li[0]-li[1] 
        b = li[1]-li[2]
        if a == b :
            result.append(i)
print(len(result))

# print("Windows Upload")
# print("20211230")



