import random

n= random.choice(["노트북","냉장고","핸드폰"])
k= random.choice(["노트북","냉장고","핸드폰"])
for i in range(1):
    guess=input("노트북,냉장고,핸드폰 중에서 하나를 입력하세요?")
    if guess==n:
        print("당첨입니다.")
        print("☆ 내가 선택한 상품은==>:",guess)
        print("★ 컴퓨터가 보낸 상품은==>:",n)
        break
    else:
        print("-------------꽝-------------")
        print("☆ 내가 선택한 상품은==>:",guess)
        print("★ 컴퓨터가 보낸 상품은==>:",n)
    for j in range(1):
        guess=input("노트북,냉장고,핸드폰 중에서 하나를 입력하세요?")
        if guess==k:
            print("당첨입니다.")
            print("☆ 내가 선택한 상품은==>:",guess)
            print("★ 컴퓨터가 보낸 상품은==>:",k)
            break
        else:
            print("-------------꽝-------------")
            print("☆ 내가 선택한 상품은==>:",guess)
            print("★ 컴퓨터가 보낸 상품은==>:",k)
        if j==0:
            print("2번의 기회가 끝나 게임을 종료합니다.")
        
        
