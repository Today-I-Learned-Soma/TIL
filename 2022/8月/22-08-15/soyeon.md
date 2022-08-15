## 오늘 할일

---

- [x]  블로깅
- [x]  네일아트
- [x]  api 서버 리펙토링

## 블로깅

---

[https://velog.io/@sophia5460/AWS-ALB를-통해-Private-Instance-속-Spring-Boot-웹-서버-접속하기](https://velog.io/@sophia5460/AWS-ALB%EB%A5%BC-%ED%86%B5%ED%95%B4-Private-Instance-%EC%86%8D-Spring-Boot-%EC%9B%B9-%EC%84%9C%EB%B2%84-%EC%A0%91%EC%86%8D%ED%95%98%EA%B8%B0)

## Spring Boot

---

### 연관관계의 주인 = mappedBy를 가지고 있지 않은 쪽

## [ERROR]

- 순환참조 에러
    - 양방향 연관관계일 때 서로를 계속해서 참조하게 되는 에러
    - 방지
        - @JsonIgnore어노테이션 붙이기
            - Json 데이터에 해당 프로퍼티는 null값으로 들어가게 된다.
        - DTO 객체를 통해 꼭 필요한 데이터만 전달하기

## 내일 할 일

---

- [ ]  순환참조 에러 방지
- [ ]  address api 생성
- [ ]  스프링 스터디