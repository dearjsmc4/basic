
import random

def merge(li, start, end):
    pass

def merge_sort(li, start, end):
    pass




if __name__=="__main__":
    while True:
        num_data=int(input('데이터 개수(종료:0):'))
        if not num_data:
            break
        data=[random.randint(1, 100) for _ in range(num_data)]
        print(data)
        quick_sort(data, 0, len(data)-1)
        print(data)