import threading

# list 의 모든 요소들에 곱하기 2를 할 때, 스레드를 4개 만들어서 한번에 할수있도록.

n=1000
offset=n//4

def thread_main(li, i):
    # offset=250
    for idx in range(offset*i, offset*(i+1)):
        li[idx]*=2

# 리스트에 1000개의 요소 생성
li=[i for i in range(1,1001)]
# 빈 리스트 생성
threads=[]

# 스레드를 생성
for i in range(4):
    # 스레드 메인 함수에 인자로 li 와 i를 전달
    th=threading.Thread(target=thread_main, args=(li, i))
    # 만들어둔 빈 리스트에 스레드메인 함수의 결과를 추가
    threads.append(th)

# 멀티 스레딩
for th in threads:
    th.start()

# 메인 스레드에서 나머지 스레드들이 모든 실행을 끝날때까지 기다린다
for th in threads:
    th.join()

print(li)

