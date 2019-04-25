import random

def get_middle_idx(li, start, end, mid):
    """
    리스트의 맨 처음 값과 중간 값, 그리고 마지막 값 중에서
    가운데 값이 위치한 인덱스를 반환한다.
    """
    idx_li=[start, end, mid]
    # idx_li.remove(max(idx_li))
    # idx_li.remove(min(idx_li))
    # print(idx_li[0])
    # return idx_li[0]

    if li[idx_li[0]] > li[idx_li[1]]:
        idx_li[0], idx_li[1]=idx_li[1], idx_li[0]
    if li[idx_li[1]] > li[idx_li[2]]:
        idx_li[1], idx_li[2]=idx_li[2], idx_li[1]
    if li[idx_li[0]] > li[idx_li[1]]:
        idx_li[0], idx_li[1]=idx_li[1], idx_li[0]

    return idx_li[1]

def quick_sort(li, start, end):
    if start >= end:
        return

    left = start
    right = end
    mid = (left+right)//2
    mid_idx = get_middle_idx(li, start, end, mid)
    pivot = li[mid]
    li[mid_idx], li[mid] = li[mid], li[mid_idx]


    while left <= right:
        while li[left]<pivot:  
            left += 1

        while li[right]>pivot:
            right -= 1

        if left <= right:
            li[left], li[right] = li[right], li[left]
            left+=1
            right-=1

    quick_sort(li, start, right)
    quick_sort(li, left, end)

if __name__=="__main__":
    while True:
        num_data=int(input('데이터 개수(종료:0):'))
        if not num_data:
            break
        data=[random.randint(1, 100) for _ in range(num_data)]
        print(data)
        quick_sort(data, 0, len(data)-1)
        print(data)