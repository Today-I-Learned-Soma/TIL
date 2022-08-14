![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a234f319-ce16-4554-8fc4-bdd440fd5824/Untitled.png)

도커단위로 fargate를 

지금은 ec2띄어놓고 나중에 fargate로 바꾸기

## Bastion Instance vs Nat Gateway

---

Nat Gateway

- IP 패킷의 TCP/UDP 포트숫자, 소스 및 목적지의 IP주소 등을 재기록
- 사설 IP를 외부 인터넷과 통신하기 위해 사용
- 사설 네트워크에 속한 여러개의 호스트가 하나의 공인 IP 주소를 사용해서 인터넷에 접속하기 위함
- `private subnet과 public subnet은 같은 vpc내부에 있으면 통신이 가능함`
    - Nat Gateway를 붙이면 public subnet이 외부 인터넷 데이터를 private subnet으로 전달
- 내부에서 외부로의 접속만 가능
    - 외부에서 NAT Gateway를 이용해서 접속하는 것은 불가능

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b7143828-f1ea-4ce3-831f-f155b7f895fb/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/be405098-244c-49ef-b736-b490f0bac632/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ebdae7ca-ca61-42e2-b2c0-bf69d10f5d7e/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a504ba8f-c24d-4af1-b4f9-b57ae5fa1521/Untitled.png)

Bastion server

- 외부에서 Private Subnet과 통신하는 수단

문제점

- 복합키를 이용하여 DB설계를 하려고 하였으나

## JPA N+1 문제 해결

- 연관 관계가 설정된 엔티티를 조회할 경우에 조회된 데이터 갯수(n) 만큼 연관관계의 조회 쿼리가 추가로 발생하여 데이터를 읽어오는 현상

**1. Fetch Join**

JPQL을 사용하여 DB에서 데이터를 가져올 때 처음부터 연관된 데이터까지 같이 가져오게 하는 방법이다. (SQL Join 문을 생각하면 된다. )

# 해야할일

---

지금까지 했던 것들 총 정리→ 이력서 위함(블로깅)

## Reference

---

[[AWS] 📚 VPC 개념 & 사용 - 사설 IP 통신망 [NAT Gateway / Bastion Host]](https://inpa.tistory.com/entry/AWS-%F0%9F%93%9A-VPC-%EA%B0%9C%EB%85%90-%EC%82%AC%EC%9A%A9-%EC%82%AC%EC%84%A4-IP-%ED%86%B5%EC%8B%A0%EB%A7%9D-NAT-Gateway-Bastion-Host#NAT_%EA%B2%8C%EC%9D%B4%ED%8A%B8%EC%9B%A8%EC%9D%B4_(Network_Address_Translation))

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/191fd72d-9c0a-46d8-af32-6eff8c97890c/Untitled.png)

1. Amazon Route53을 통해 도메인 부여받음
2. 실제 서비스는 보안을 위해 Private Subnet안에 넣어두고 Internet gateway를 통해 vpc와 인터넷 간의 통신을 도우며 Nat Gateway를 통해 subnet간의 통신을 돕는다.
3. Application Load Balancer는 서버의 부하분산을 처리하며 SSL인증서를 발급받고, 프록시 서버의 역할을 담당한다.
4. 매물 등록 서비스와 3D 모델 생성 서비스로 분산시켜 사용자가 S3에 2D 도면을 올리면 lambda가 해당 도면을 3D 모델 생성 서비스에 올리고, 해당 서비스는 결과물을 다시 S3에 올리고 DB에 해당 URL을 업데이트 시킨다.
5. DB는 사용자의 세션정보와 위치정보 등을 저장할 레디스 서버와 RDS를 사용할 것이다.

```
[소연]
[JPA N+1 문제]
- 연관 관계가 설정된 엔티티를 조회할 경우에 조회된 데이터 갯수(n) 만큼 연관관계의 조회 쿼리가 추가로 발생하여 데이터를 읽어오는 현상
- 생각지 못한 N개의 쿼리가 추가로 발생하기에 성능이슈가 발생한다.

[해결 방법]
: Fetch Join
- JPQL을 사용해서 DB에서 데이터를 가져올 때 처음부터 연관된 데이터까지 같이 가져오는 방법

[복합키 문제]
- 다양한 entity들을 join시킬 경우 해당 키 값들을 pk로 받아 복합키로 설계할 계획이었지만 이 경우 복합키를 설정해야 하는 어려움 발생
- 복합키의 경우 class를 따로 생성하거나 embedded타입을 따로 설정해야 하기에 서비스단에서 데이터를 가져오기에 매우 복잡한 문제점 발생

[해결방법]
- DB 모델링 시 적절한 pk를 골라 해당 key값이 해당 테이블을 대표할 수 있도록 설정

[Column명 설정 문제]
- Address 도메인 개발 중 '구'를 나타내는 영단어가 'distinct'였기에 쿼리 문법이랑 겹쳐서 잘못된 쿼리문이 생성되는 에러 발생

[해결방법]
- 해당 컬럼명을 다른 것으로 변경

[문제점]
EC2 인스턴스 내부의 톰캣 서버위에 돌아가는 스프링부트 서버는 8080을 열어두고는 ALB를 통해 private subnet안의 인스턴스 연결 시도 중 ALB밖에서는 80포트를 통해 들어오게 하고 ALB와 타겟그룹 간의 통신에도 80포트를 열어두었다. 따라서 EC2 인스턴스에 index.html(아파치 서버)까지는 통신이 가능하였지만 그 뒷단 URL에는 접속이 불가능한 문제점이 발생하였다. 이에 따라 ALB의 보안그룹과 타겟그룹의 리스너를 모두 8080을 열어놓았고, 프라이빗 서브넷 내부의 인스턴스의 보안그룹도 80포트 대신에 8080포트를 열어놓았다. ->그래야 8080으로 들어갈 수 있기 때문이다.
만약에 80포트와 8080포트가 둘다 열려있을 경우 우선순위가 80포트이기 때문에 8080포트 URL로 닿지 않아 404에러가 발생한다.

 문제점 및 해결방안
[문제점] 'Jira'

[해결방안]
http로 alb 도메인 접속 -> 80포트만 열린 alb가 해당 요청을 받음 -> 타겟그룹으로는 8080을 리스너접목시킴 -> private subnet 내부의 인스턴스는 8080포트를 열고 alb의 보안그룹을 ip로 받는다.
그러면 http접속을 통해 아파치 서버 위의 스프링부트 웹서버까지 접속이 가능하다.
```

프로젝트 진행도 파악을 위해 ‘jira’를 사용하였고 스프린트를 2주간격으로 새로 설정하였다.

익숙하지 않았던 툴이었기에 초반에는 백로그를 어느정도 설정해야 하는지 감이 잘 잡히지 않았지만 여러번 진행하다보니 얼마만큼의 양이 적절한 것인지 파악할 수 있었다.

또한 매일 진행하는 ‘데일리 스탠드업'회의를 통해 어제 내가 한일, 오늘 할일, 이슈 등을 공유하면서 서로의 진행도를 파악할 수 있었고 이를 통해 효율적인 스케쥴링이 가능하였다.

매주 진행해야 하는 멘토링 시간도 그동안 진행하다가 발생한 이슈나 어려움등을 멘토링 전에 미리 고민해보고 참여함으로써 알차고 유익한 시간을 보낼 수 있었다.