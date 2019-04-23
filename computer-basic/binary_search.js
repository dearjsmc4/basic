// 파이썬으로 풀었던 바이너리 서치 알고리즘을 JS 로 옮겨보기

li = [1,2,3,4,5,6,9,10,14,16,20,21];
target = 20;

function binary_search(target, li){
    var start = 0;
    var end = li.length-1

    while(start <= end){
    var mid = Math.floor((start + end) / 2)
        if(li[mid] == target){
            return mid;
        }
        else if(li[mid] > target){
            end = mid - 1
        }
        else {
            start = mid + 1
        }
}
}


idx = binary_search(target, li);
console.log(idx);