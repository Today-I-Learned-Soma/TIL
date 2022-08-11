## 오늘 할 일

---

- 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5fdd7b09-7288-4dc6-b21b-5888409fd111/Untitled.png)

완성시키기

- 시간 남으면 API 설계
- intellij에 rds연결

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fbfa2f9b-3491-4d30-8083-0f3f7431c19d/Untitled.png)

## VPC 설정

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/434b178d-87f0-415c-a781-8417697cbf93/Untitled.png)

- 외부에서는 EC2에만 접근 가능. RDS는 EC2를 거쳤을 때만 이용 가능

## NAT란 ( Network Address Translation)

- 포트 숫자와 IP 주소 등을 재기록 → 사설 네트워크에 속한 여러개의 호스트가 하나의 공인 IP주소를 사용하여 인터넷에 접속하기 위함
- 내부망에서는 사설 IP 주소 → 외부와의 통신시에는 NAT를 거쳐 공인 IP로 변환

## @Builder

- 기본적으로 메서드, 생성자에만 붙일 수 있다.
- builder를 사용하지 않을 경우 null값이 들어갈 수도 있다.

## 내일 할 일

---

- 김성헌 멘토님 피드백
    - 서버 재설계 → alb 붙이기
    - aws 파라미터
    - 재설계 대로 aws 구성
- api crud 모두 성공

## 느낀점

---

- 생각보다 개발이 원활하게 진행되고 있는 것 같아서 즐겁다~.~ 빨리 crud 끝내자!