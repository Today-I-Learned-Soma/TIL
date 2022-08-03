# CORS? ( Cross-Origin-Resource-Sharing )

> 프로토콜, 도메인, 포트번호가 다른 외부 사이트에 데이터 요청을 했을 때, 보안상의 이유로 브라우저에서 HTTP 요청을 제한하는 것

## 필요한 이유

모든 곳에서 데이터를 요청할 수 있게 되면 다른 사이트를 흉내내어
기존 사이트와 동일하게 로그인을 하게 만들고, 로그인했던 세션을 탈취하여
악의적으로 정보를 추출하거나 다른 사람의 정보를 입력하는 등 ( XSS, XSRF )
공격을 할 수 있기 때문에 서버에서 동의를 한 경우에만 요청을 수락하고
동의하지 않으면 브라우저에서 거절한다.

## 동작

1. Simple requests
   HTTP method가 다음 중 하나이면서

- GET
- HEAD
- POST
  자동으로 설정되는 헤더는 제외하고, 설정할 수 있는 다음 헤더들만 변경하면서
- Accept
- Accept-Language
- Content-Language
  Content-type이 다음과 같은 경우
- application/x-www-form-urlencoded
- multipart/form-data
- text/plain

2. preflight
   Origin헤더에 현재 요청하는 origin과, Access-Control-Request-Method헤더에 요청하는 HTTP method와 Access-Control-Request-Headers요청 시 사용할 헤더를 OPTIONS 메서드로 서버에 요청한다. ( 이때 내용물은 없고 헤더만 전송 )
   브라우저가 서버에서 응답한 헤더가 유효한 요청인지 확인한 후
   유효하지 않은 요청이면 요청 중단되고 에러 발생.
   유효한 요청이라면 원래 보내려던 요청의 리소스를 응답받는다.
