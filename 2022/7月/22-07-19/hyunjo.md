# 프론트엔드 코딩 컨벤션

> 권고?? 컨벤션??

- 컨벤션은 선택지가 있고 권고는 선택지가 없다
- 권고는 장단점을 비교할 필요가 없다

## 코딩 컨벤션의 필요성

- 모든 브라우저에서 컨텐츠 손실없이
- 유지보수 (최초 개발자가 아닌 사람도 수정할 수 있도록)
- 일관성있는 코드
- 업무 효율 증가

## 프론트엔드 코딩 컨벤션을 정하기 전에 생각해볼것

- 반응형 (권고) or 적응형: 미디어 태그 사용 여부, js에서의 처리
- 가로모드 지원 (권고): 미디어 태그 사용 여부, js에서의 처리
- 페이지 렌더링 속도 (권고): img width, height을 고정할건지

## 공통적으로 정할 컨벤션

- 폴더 구조 정하기
  - css, js, img로 나눌 것인지, img 폴더 내에 디테일하나 확장자로 나눌것인지 등
- 파일 명명 규칙 정하기
- 들여쓰기 (tab vs 4 space)
- 중괄호 사용 규칙
- 줄 공백 100자까지 (정형화된 모니터 크기 맞춤)

## HTML 작성 컨벤션

- id, class, name에 공통된 컨벤션 규칙을 수립한다.
  - js에서 사용할 때 혼란이 적다.
- id, class, name에 각각의 컨벤션 규칙 수립
  - Css, 마크업 관점에서 유리
- 태그명을 예약어로 생각할 것인지?
- 주석 컨벤션도 있음 (AU, D)
- attribute 순서 정하기(id, class, style)
- title 태그 작성 컨벤션 정하기
  - 페이지마다 중복되면 웹접근성 어긋남(첫번째로 읽힘)
- 허용할 플랫폼 범위 정하기

## CSS 작성 컨벤션

- charset은 반드시 지정하며 HTML의 charset과 일치시키기
- reset css 사용할지 안할지 정하기
  - 장점: 모든 브라우저에서 내가 원하는대로 그려짐
  - 단점: 모든 페이지에서 공통으로 reset.css 사용하면 무조건 request 하나씩 늘어남, 각자 갖게하면 중복 코드 늘어남
- common css 사용 여부
  - 장점: 비슷한거 묶을 수 있음
  - 단점: 위와 같음
- 코드 커버리지: 실제로 사용되고 있나?
  - 개발자도구 code coverage - reload ⇒ 최적화 가능
- 애스터리스크(\*) 사용 여부: 웹 성능에 악영향 미침
- 태그에 스타일 먹이는건 reset code만 가능
- id는 큰 구조에만 먹이는 것이 좋다
- 다중 선택자 사용 범위 정하기 (IE 6.0에서 오류 발생)
- CSS 속성 사용 순서
  - 레이아웃, box, 배경, 폰트, 기타
