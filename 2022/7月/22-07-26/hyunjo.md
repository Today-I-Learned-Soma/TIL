# 네트워크: VPC 2

## Route Table

- 라우팅 테이블은 컴퓨터 네트워크에서 목적지 주소를 목적지에 도달하기 위한 네트워크 노선으로 변환시키는 목적으로 사용된다.
- Router Table: Subnet = 1:N
  - 여러 서브넷이 같은 규칙을 이용할 수 있다.
- 0.0.0.0/0 → 전체 IP 주소 (목적지가 무엇이든 다 어디로 보낸다)

## Ec2서버를 올려보자

- 어떤 az에 있는 서브넷에 Ec2서버를 올린다고 해보자
- 여기에는 VPC내부에 속하는 private IP를 줄 수 있다.
- 이때 internet gateway가 연결되어있기 때문에 public ip(공인 IP)도 줄 수 있어야 한다.
- 인트라넷 네부 서브넷끼리는 private IP로 통신할 수 있고, 인터넷상에서는 public IP로 호출할 수 있다.
- 정해지지 않은 ip로 사용해도 되긴 하지만 추후에 인터넷에 연결될 수 있을 때 문제가 발생할 수 있다.
- 각각의 서브넷이 public ip를 가지면 공격자 입장에서 이득임
- 또한 private ip를 사용하는 이유는 public ip를 아끼기 위한 것이기도 함(공인 ip도 비싼 자원임)
- 정말 외부 노출이 필요한 서버들만 공인 ip를 갖도록 하는 것이 좋다.
  -> 따라서 서브넷의 용도를 나누어 놓아야 한다!

## 서브넷(Subnet)

> Private subnet & Public subnet

- Public subnet은 public ip를 가질 수 있는 subnet
- 그렇다면 외부에서 접근하는 게이트에서 정확히 어느 서브넷으로 갈지 알아야 한다.
  -> NAT Gateway가 필요하다!

## NAT Gateway (Network Address Translation)

- (ex) 공유기 등
- 인터넷 선 계약은 하나만 하고 기기 여러대가 인터넷을 사용할 수 있다.
- 이때 밖에서는 공인 IP가 하나인데, 돌아올 때는 누가 보낸 요청인지 맞춰서 응답해주어야 한다.
- 위의 역할을 하는 것이 NAT Gateway!
- Ingress traffic은 차단, Egress traffic은 허용한다
- 위 말인 즉슨, 안에서는 요청을 보낼 수 없지만, 밖에서는 먼저 찌를 수 없다는 뜻이다.
- 따라서 NAT Gateway는 private IP -> public IP로 번역해주는 역할인 경우가 많고, private -> private 번역도 가능하다.
- VPC안에 속하는 컴포넌트이므로 public subnet에 생성해야 한다.
- private IP를 가짐
- NAT Gateway : subnet = 1:1 ⇒ NAT Gateway : AZ = 1:1
