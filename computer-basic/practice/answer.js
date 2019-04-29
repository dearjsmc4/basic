function fiboLoop(n){
    let left = 0;
    let right = 1;
    for (let i = 1; i < n; i++){
        [left, right] = [right, left+right]
    }
    return left
}


// 클로져

function fiboCloser(){
    var li = [0,1]
    function inner(n){
        if (n>li.length){
            li.push(inner(n-1)+inner(n-2))
        }
        return li[n-1]
    }
    return inner
}

var func = fiboCloser()
console.log(func(4))