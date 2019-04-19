# 파이썬 자료형 기초  

- string = "abcde"  
    - string`[2]` = 'c'  
    - string`[2:]` = 'cde' (2번 자리 이상)  
    - string`[:2]` = 'ab' (0번 이상, 2번 미만)  
    - string`[0:1]` = 'a' (0번 째 이상, 1번 미만)  
    - string`[0:2]+"z"+string[3:]` = 'abzde' ( ab + z + de )  
    - string`.replace('c','z')` = 'abzde' (c 를 z 로 바꾸어서 보여줌. 원본이 바뀌지는 않는다.)  


### 문자열 포매팅  
문자열 내의 어떤 값을 삽입하는 방법.  

a = 10  
b = 'abcde'  
- `print("%d, %s" %(a,b))` = 10, abcde  
- `print('숫자는 {0} 문자열은 {1}'.format(a,b))`  
    = 숫자는 10 문자열은 abcde  
- `print(f'숫자는 {} 문자열은 {}')`  
    = 숫자는 10 문자열은 abcde  

a = 0.1234512345  
- `print(f'{a:.3}')` = 0.123 (소수점 뒤의 3자리까지만 자르기)  


### Dictionary  

- dic = {'a':1, 2:'two', 'func':lambda a,b: a+b}
    - dic`['a']` = 1 (a라는 키의 value를 가져오기)  
    - dic`[func](1,2)` = 3 (func 라는 키의 value 인 함수를 실행)  
        lambda: 함수가 위치한 메모리 주소값  
    - dic.`keys()` = dict_keys(['a', 2, 'func']) (dic 의 모든 키값을 가져오기)  
    - dic.`items()` = dict_items([('a', 1), (2, 'two'), ('func', <function <lambda> at 0x05B738E8>)])  
        (key와 value값이 튜플로 묶여서 나옴) -> 튜플인 이유가 있나?  
    - key_list = `list(dic.keys())` = ['a', 2, 'func'] (key만 모아서 리스트로 만들기)  

**list 와 view 객체와의 차이**  
key_view = dic.keys() = dict_keys(['a', 2, 'func'])  
key_list = ['a', 2, 'func']  
일 때,  
`dic[5]='five'` 딕셔너리에 쌍을 추가하면  
key_view = dict_keys(['a', 2, 'func', `5`]) -> 추가되었음  
key_list = ['a', 2, 'func'] -> 추가 되지 않았음  


### Set  
집합 자료형인 세트에서는 중복이 허용되지 않는다.  

s1 = set([1,2,3,4])  
s2 = set([3,4,5,6])  

- `s1|s2` or `s1.union(s2)`= {1,2,3,4,5,6} (합집합)  
- `s1&s2` or `s1.intersection(s2)`= {3,4} (교집합)  
- `s1-s2` or `s1.difference(s2)` = {1,2} (차집합)  
- `s2-s1` or `s2.difference(s1)` = {5,6} (차집합)  
- `s1^s2` or `s1.symmetric_difference(s2)`= {1,2,5,6} (대칭 차집합)  


### True / False  

- **거짓**으로 취급하는 데이터  
    - "" 빈 문자열  
    - [] 빈 리스트  
    - () 빈 튜플  
    - {} 빈 딕셔너리  
    - false  
    - none (JS의 undefined)  
    - 0  

