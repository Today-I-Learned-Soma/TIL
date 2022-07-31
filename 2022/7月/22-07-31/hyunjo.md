# 네트워크: VPC 3

## Private Subnet의 종류

- with NAT
- without NAT: protected와 같이 완전히 닫힌 상태 = internal
  - ex) RDS, Elastic cache등 관리형 데이터베이스 서버는 외부에서 접근할 필요도 없고 밖으로 인터넷을 통해서 나갈 이유가 없다

## Three-tier 아키텍쳐

- public network subnet
  - 사실 여기만 public이면 됨
  - 로드밸런서 등
- private application
  - stateless
  - api server
- private data
  - DB

## 용도에 따른 서브넷 종류

- app-subnet
  - 실제 비즈니스 로직
- data-subnet
  - 데이터 저장하는 애들
  1. managed - 관리형 데이터 서비스(rds, elastic cache, dynamo DB)
  2. self - 직접 ec2위에 구축해서 운영하는 서버들(mySQL, elastic search cluster,…)
- network-subnet
  - 네트워크 장비들(gateway, load balancer, proxy)
  1. private: 내부 네트워크 장비들
  2. public: 밖에서 들어오는 트래픽 받을 gateway, loadbalancer 등…

## Subnet Group

- vpc 상에서는 존재하지 않는 개념
- RDS, red shift등을 접하게 되면 등장
- az1번에 이 서브넷 사용하겠다 이런식으로 매핑 가능
- 고가용성을 위해서 선택되어있는 여러 az에 분배해서 하나가 fail over되더라도 사용 가능하게 만들어줌
- 같은 목적끼리 그룹핑해서 쓰는것이 서브넷 그룹이다.

## Network ACLS vs Security groups

- Subnet에 진입하고 그 후에 장비로 찾아가므로 NACL이 SG보다 먼저 적용된다.
- 라우팅 테이블을 보고 허용이 되었는지 보고 후에 NACL을 보고 서브넷간의 관계에서 문제가 없다고 하면 SG를 본다 → 다 허용되면 통신 가능!

### Network ACLS

- 서브넷과 연결됨
- stateless
- NACL:subnet=1:n
- rule number 작을 수록 우선순위 높음
- 어떤 rule에 맞음 → 라우팅 시킴, 안 맞음 → 다음 룰로 넘어감
- type(traffic type), protocol, port range, destination 등을 지정해서 allow, deny 지정할 수 있음

### Security groups

- 인스턴스와 연결됨(EC2, Load Balancer)
- stateful
- SG:instance = m:n (1 instance 당 SG default로 최대 다섯개 가질 수 있고 더 가지려면 따로 요청해야 하지만 네트워크 성능이 저하될 수 있다.)
- 우선순위 없음
- SSH, TCP, 22 로 사용하면 편하지만 보안에 취약함
- 이 보안 그룹을 가지는 장비들끼리는 서로 통신이 가능하다!

## stateful vs stateless

- 장바구니는 1번, 결제 요청은 3번으로 갔을 때 문제가 없다 → stateless, 문제가 있다 → stateful
- redis등의 임시 메모리 캐시에 저장하기 or 아예 stateless하게 만들기(jwt 사용과 같은 느낌)
- api server는 stateless해야 한다
  - 복제본이 많아지더라도 수평확장이 가능함, 부하분산이 확실하다(헤비유저 and 경량유저)
  - 그게 아니면 sticky session: load balancer가 client를 식별해서 같은 대상은 같은 서버에만 요청보내도록(client ip, user id 등을 사용할 수 있다.)

## NACL과 SG에서의 stateless, stateful?

- 보안그룹은 stateful하다
  - 들어올때 허용해줬으면 나갈때도 허용해주기
  - 나갈때 허용해줬으면 들어올때도 허용해주기
  - 외부에서 안쪽으로 먼저 trigger한 애들 - inbound rules
  - 내가 먼저 요청보낸쪽 - outbound rule 포함
- NACL은 stateless하다
  - 나가는 traffic은 모두 나가는 트래픽이고 들어오는건 다 들어오는 트래픽이다.
  - UDP면 그냥 가는데 TCP 3-way handshake 과정에서 이루어지지 않을 것
