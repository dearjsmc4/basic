### 자바스크립트 메소드

#### window 객체 : 브라우저를 제어하는 객체.
- window.open() – 새창 열기  
- window.close() – 현재창닫기  
- window.print() – 현재 창을 프린트할 수 있는 창이 뜬다.  
- confirm(“확인문구”) – 확인이나 취소를 반환하는 알림창인데. 취소는 false, 확인은 true 가 반환된다.  
    보통 변수 = confirm() 형태로 많이 쓴다.  
- prompt(“질문”, “기본값”) – 입력받기.
- window.innerHeight – 창의 높이  
- window.innerWidth – 창의 너비  
- window.pageX(Y)Offset – 스크롤된 수치  
- window.resizeTo(w,h) / window.resizeBy(w,h)   
- window.scrollTo(x,y) – 지정한 위치로 스크롤 움직이기  
- window.scrollBy(x,y) – 현재위치에서 얼마나 움직일지 설정(위나 왼쪽으로가면 마이너스)  

**타이머 만들기**  
`interval = window.setInterval(function() {console.log(1);}, 1000);` – 1초에 한번씩 1을 출력  
`window.clearInterval(interval);` – 멈추기  

- 창을 전체너비로 띄울 때 쓰는 방법  
    - screen.width / screen.height – 전체 화면 너비/높이  
- screen.availHeight / screen.availWidth  – 가려지거나 침범할 수 없는 영역은 빼고 계산해서 보여준다.  
    실제 이용 가능한 영역.

- history.length – 쌓여있는 페이지 개수  
- history.back() – 뒤로가기 (링크를 거는 것과 다르다. 링크를 걸면 히스토리가 쌓인지만  
히스토리백으로 걸면 히스토리가 안 쌓이고 페이지를 새로 로드할 필요가 없다. 스크롤 위치까지 그대로.)  
- history.forward() – 다음 페이지로.  
- history.go(숫자) – 플러스/마이너스로 페이지 이동  

#### Navigator  
정보를 이용, 고객 분석에 사용한다.  
- navigator.platform – 운영체제 종류 읽기  
- navigator.userAgent – 브라우저 종류 읽기  
- navigator.language – 언어 종류 읽기  
- navigator.geolocation.getCurrentPosition(function(position){console.log(position.coords.latitude,   position.coords.longitude);}) – 내 위치 읽기 (권한 요청 창이 뜸)  

#### location  
페이지 이동할 때 많이 쓰인다.  
- location.href – 현재 페이지 주소 읽기  
- location.protocol – 어떤 메소드로 접근했는지 확인.  
- location.host – 도메인주소  
- location.pathname – 경로  
`"/C:/Users/user/Desktop/%EA%B3%B5%EB%B6%80/0314.html"`
- location.search – 쿼리스트링  
- location.hash – anchor 값  
- location.reload()  - 페이지 새로고침  
- location.replace(“주소”) – 히스토리를 쌓지 않고 페이지 이동  
- location.href = “주소” – 히스토리를 쌓으며 이동  


### JQuery  
JQuery 에서 이벤트를 사용하기  
`$(요소).eventName(실행할 함수);`
- .show(), .hide(), .toggle() – 요소를 보이거나 숨긴다.  
- .addClass(‘클래스이름’), .removeClass(‘클래스이름’), .toggleClass(‘클래스이름’)  
: 클래스 이름을 추가/삭제 하는 역할  

**중요**
- $(요소).html(), .text() – 내부 값 읽기. (html 은 태그까지 다 보여주고, text 는 텍스트만 보여줌)  
- $(요소).html(값), .text(값) – 내부 값 변경 . 아예 값을 변경한다.  
- $(요소).html($(요소).html()+”추가값”) – 값을 추가한다.  
- $('#test_ul').append("<li>추가</li>") – 닫는 태그 직전에 리스트 추가.  
- $('#test_ul').prepend("<li>추가</li>") – 여는 태그 직후에 리스트 추가.  
- $(‘요소’).remove ()– 삭제한다. 돔객체에서 아예 지우는 것.  
- $('요소').remove (‘selector’) – 해당 요소의 자식 노드 중 셀렉터에 해당하는 자식을 삭제  

#### css변경
- $('요소').css(‘display’, ‘block’); - 디스플레이를 블록으로 바꾼다.  
- $('요소').css({‘display’ : ‘block’, ‘color’:’red’}); - 여러속성을 바꾸고 싶을 때는 중괄호로 담아준다.  


