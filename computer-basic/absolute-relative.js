/* 절대 비교 기법 --> 함수
a-b(Math.abs(a-b)) 가 내가 생각해둔 범위(1e-10)보다 작다면 a,b 를 같은 것으로 생각하겠다.
e : 지수를 뜻하는 exponent 의 줄임말
1e-10 =  1 * 10^-10 
단점 : 추상화가 깨지고(내부 구현을 직접 바꾼다는 것(10을 바꿔야지))
재사용성이 안 좋음 */

function is_equal(a,b){
    return Math.abs(a-b) <= 1e-10
}

function main(){
    var a = 0.3;
    var b = 0.1 * 3;

    if(is_equal(a,b)){
        console.log("the same");
    }
    else{
        console.log("not the same");
    }
}

// -------------------------------------------------------------------- 

/* 상대 비교 기법 */

function is_equal2(a, b, allowed=0){
    var diff = Math.abs(a-b);
    return diff <= Math.max(Math.abs(a), Math.abs(b)) * Number.EPSILON * Math.pow(2, allowed)
}

function main2(){

    sum = 0;

    for(var i = 0; i < 100; i++){
        sum += 0.01;
    }

    if(is_equal2(sum, 1.0, 2)){
        console.log("the same");
    }
    else{
        console.log("not the same");
    }
   
}