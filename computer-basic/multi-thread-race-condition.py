import threading

# 공유자원
# 모든 스레드에서 접근 가능한 자원
# 대표적으로 지역변수

g_num = 0
# lock 개체를 만든다
lock = threading.Lock()

def thread_main():
    global g_num
    # 크리티컬 세션. 공유자원에 접근한 후 수정/변경 하려는 코드. 임계영역.
    # 공유자원을 먼저 점유한 애가 릴리즈를 할 때까지 다른 스레드들이 기다리도록.
    lock.acquire()
    for _ in range(100000):
        g_num+=1
    lock.release()

threads=[]

for _ in range(50):
    th=threading.Thread(target=thread_main)
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()

print(g_num)