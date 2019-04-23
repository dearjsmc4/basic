def fibo(n):
    #초기값 설정
    #0,1이 있어야 0(첫번째)+1(두번째) 해서 세번째 값이 나오니까.
    #전전수와 전수를 더해서 이번수가 나온다.
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibo(n-2)+fibo(n-1)

for i in range(1,11):
    print(fibo(i), end="   ")
