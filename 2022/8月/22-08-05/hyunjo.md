# JavaScript 라이브 코딩 대비하기 #1

> 다음 함수를 구현하세요

```javascript
sum(1)(2)(); /// 3
sum(1)(2)(3)(4)(); // 10
```

### 정답

```javascript
const sum = (num1) => (num2) => num2 ? sum(num1 + num2) : num1;
```

### 해설

> 클로저와 재귀를 이용한 풀이

#### 클로저란?

- 클로저는 함수와 함수가 선언된 어휘적 환경의 조합
- 많은 프로그래밍 언어들은 함수 내 지역 변수를 해당 함수 실행 중에만 접근할 수 있지만 자바스크립트는 특별하다!
- 자바스크립트는 함수를 리턴할 경우, 해당 함수를 리턴하는 외부 함수가 클로저를 형성하기 때문이다.
- 이 클로저는 함수와 함수가 선언된 어휘 환경의 조합이다.
- 클로저가 리턴된 이후에도 외부함수의 변수들에 접근할 수 있다는 의미이다.
- 아래와 같이 활용하면 좋다. (각각 폰트 사이즈를 12,14,16으로 변경하는 함수를 만들고 이를 DOM 요소 onClick event에 연결한다.)

```javascript
function makeSizer(size) {
  return function () {
    document.body.style.fontSize = size + "px";
  };
}

var size12 = makeSizer(12);
var size14 = makeSizer(14);
var size16 = makeSizer(16);
```

```javascript
document.getElementById("size-12").onclick = size12;
document.getElementById("size-14").onclick = size14;
document.getElementById("size-16").onclick = size16;
```
