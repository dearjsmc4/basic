li = [1,2,3,4,5,6,9,10,14,16,20,21]
target = 3

def binary_search(target, li):
    start = 0
    end = len(li) - 1
    while start <= end: 
        # start 가 end 보다 커지면 이미 찾고자하는 값을 못 찾은 상태니까 while문 중지
        # 범위가 줄어들다보면 start 와 end 가 같아질 수는 있음
        mid = (start + end) // 2
        if li[mid] == target:
            return mid
        elif li[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return None

idx = binary_search(target, li)
print(idx)