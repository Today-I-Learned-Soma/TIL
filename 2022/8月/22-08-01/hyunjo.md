# 갑자기 궁금해진 Axios

> 맨날 사용은 하는데 자세히 알아본적은 없는 Axios

## 정의

node.js와 브라우저를 위한 Promise 기반 HTTP 클라이언트

## 특징

- 브라우저를 위해 XMLHttpRequests 생성
- node.js를 위해 http 요청 생성
- Promise API를 지원
- 요청 및 응답 인터셉트
- 요청 및 응답 데이터 변환
- 요청 취소
- JSON 데이터 자동 변환
- XSRF를 막기위한 클라이언트 사이드 지원

## 설치

```shell
$ npm install axios
```

## fetch와의 비교

> axios는...

- 설치를 필요로 한다
- CSRF(사이트 간 요청 위조) 보호를 해준다
- data 속성을 사용한다
- object 형태를 포함한다
- 자동으로 JSON 데이터 형식으로 변환된다
- 요청 취소, 타임아웃이 가능하다
- HTTP 요청을 가로챌 수 있다

=> 간단한 경우에는 fetch 사용해도 되지만 axios를 사용하는 것이 확장성, 보안성에 유리하다.

## 커스텀 axios

```javascript
const instance = axios.create({
  baseURL: "https://some-domain.com/api/",
  timeout: 1000,
  headers: { "X-Custom-Header": "foobar" },
});
```

## mock API

[REQRES](https://reqres.in/?fbclid=IwAR0hhe_cxVwzJHgrT6siWRQloSODOwDd2QQVlmpob3N0a6SyJXiYSVXd12U) 사용하여 mocking 가능
