
import random

def merge(li, start, mid, end):
    merged=[]
    # left가 벗어날 경계 : mid, right가 벗어날 경계: end
    left = start
    right = mid+1
    while left <= mid and right <= end:
        if li[left] < li[right]:
            merged.append(li[left])
            left += 1
        else:
            merged.append(li[right])
            right += 1

    while left <= mid:
        merged.append(li[left])
        left += 1
    
    while right <= end:
        merged.append(li[right])
        right += 1
    
    li[start : end+1] = merged

    """
    for idx in range(start, end):
        li[idx] = merged.pop(0)
    """

def merge_sort(li, start, end):
    if start >= end:
        return

    mid = (start+end)//2

    # start가 end와 같아지면 (하나씩 다 쪼개지면) return 하고 다음 함수로 넘어간다.
    merge_sort(li, start, mid)
    merge_sort(li, mid+1, end)

    merge(li, start, mid, end)


if __name__=="__main__":
    while True:
        num_data=int(input('데이터 개수(종료:0):'))
        if not num_data:
            break
        data=[random.randint(1, 100) for _ in range(num_data)]
        print(data)
        merge_sort(data, 0, len(data)-1)
        print(data)