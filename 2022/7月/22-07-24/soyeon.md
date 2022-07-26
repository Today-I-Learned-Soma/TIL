## CloudFront

- AWS에서 제공하는 CDN 서비스
- 사용자가 CloudFront의 콘텐츠를 요청할 경우 요청이 가까운 엣지 로케이션으로 라우팅된다.
    - 이때 캐시 사본이 있으면 해당 사본을 사용자에게 전송한다.
- 콘텐츠 종류
    - Download Distribution
        - HTTP 프로토콜을 이용해서 다운로드할 수 있는 일반적인 이미지 혹은 정적 파일을 제공받을 수 있다.
- S3와의 연동
    - 정적 콘텐츠를 대규모로 저장, 보호, 전송이 가능하다.

## S3

- 파일을 버킷에 `무제한으로 저장`하고 가져올 수 있도록 설계됨
- 스토리지 공간을 계획하여 특정 크기를 할당할 필요가 없다.
- 파일이 저장되는 서버를 관리하거나 패치할 필요가 없다
    - 콘텐츠를 저장 및 가져오기만 하면된다.
    

### graphDb(Neo4j)

- relation형식으로 되어 있어서 내 친구가 좋아하는 게시물이 나한테 뜨게 함
- 유사하다고 판단되는 단어들을 기준으로 검색이 되도록
    - word to vector

### s3

- 엔드포인트 URL이 빠진다.
- 다운로드, 업로드 스트림이 생긴다.
- 파일서버로 보면 된다.
- 일회용 권한을 줄 수 있고

cloudfront

- 많은 부하가 발생해도 처리가능하다.

elb

- proxy가 가능하다.
- scaling을 해도 다 받아낸다.

## Embedded 타입

- 복합 값 타입
    - 새로운 값 타입을 직접 정의해서 사용하는 JPA의 방법
    - 데이터들의 응집력을 향상시킨다.
- 사용방법
    - @Embeddable : 값 타입을 정의하는 곳에 표시
    - @Embedded : 값 타입을 사용하는 곳에 표시
    

## 파라미터 종류

1. @NoArgsConstructor : 파라미터가 없는 기본 생성자를 생성
2. @AllArgsConstructor : 모든 필드 값을 파라미터로 받는 생성자를 생성
3. @RequiredArgsConstructor : final, @NotNull인 필드값만 파라미터로 받는 생성자를 생성

## 값 타입 컬렉션

- 값 타입을 하나 이상 저장하기 위함
- 컬렉션에 보관 후 @ElementCollection, @CollectionTable 어노테이션을 사용하면 된다.

```java
@ElementCollection
@CollectionTable(name = "FAVORITE_FOODS", joinColumns = @JoinColumn(name = "MEMBER_ID"))
@Column(name="FOOD_NAME")
private Set<**String**> favoriteFoods = new HashSet<String>();
```

```java
@ElementCollection
@CollectionTable(mame = "ADDRESS", joinColumns = @JoinColumn(name = "MEMBER_ID"))
private List<**Address**> addressHistory = new ArrayList<Address>();
```

[임베디드 타입의 컬럼을 두 개 이상 정의하고 싶다면]

```java
@Embedded Address homeAddress;
@Embedded Address companyAddress;
--> 컬럼명 중복
```

```java
@Embedded Address homeAddress;
@Embedded
@AttributeOverrides({
	@AttributeOverride(name="city", column=@Column(name = "COMPANY_CITY")),
	@AttributeOverride(name="street", column=@Column(name = "COMPANY_STREET")),
	@AttributeOverride(name="zipcode", column=@Column(name = "COMPANY_ZIPCODE"))
})
Address companyAddress;
```

## 상속관계 매핑

- RDB에서는 상속 개념이 따로 있지 않음
    - 객체의 상속 구조와 DB의 슈퍼타입-서브타입 관계를 매핑하는 것
1. 각각의 테이블로 변환<`조인전략`>
    - 엔티티 각각을 모두 테이블로 만듦
    - 자식 테이블이 부모 테이블의 기본키를 받아 기본키 + 외래키로 사용하는 전략
    - 어노테이션
        - @Inheritance(strategy = InheritanceType.JOINED)
            - 상속매핑은 부모 클래스에 Inheritance어노테이션이 필요함
        - @DiscriminatorColumn
            - 부모 클래스에 `구분 컬럼을 지정`
        - @DiscriminatorValue(”S”)
            - `구분 컬럼에 입력할 값`을 지정
            - “S”라고 지정하면 부모 클래스인 Food의 DTYPE에 S가 저장됨
2. 단일 테이블 전략
    - 테이블을 하나만 사용하는 전략
    - 한 테이블 내에 부모값과 자식값을 모두 저장하는 방식
        - 자식 엔티티의 컬럼값이 Null값이 될 수도 있음
3. 구현 클래스마다 테이블 전략
    - 각각의 테이블을 만드는 전략
    - 추천하지 않는 전략
    

## VPC(Virtual Private Cloud)

- AWS의 리소스들이 위치할 네트워크 망
- 복수의 AZ가 걸친 형태로 생성가능
- 물리적으로는 다른 곳에 위치하지만 같은 사설 IP 대역에 위치하게 만들어 `리소스들끼리 통신할 수 있도록 만드는 기술`

## Subnet

- VPC의 영역 안에서 `망을 더 나누는 행위`
- 단일 AZ에 위치
- 종류
    - Public Subnet
        - `외부에서 접근이 가능`한 네트워크 영역
        - 인터넷 게이트 웨이로 향하는 라우팅테이블이 존재해야 함
        - 해당 서브넷에 위치한 리소스들은 공인 IP를 가질 수 있다.
    - Private Subnet
        - 외부에서 `다이렉트로 접근이 불가능`한 네트워크 영역
        - 해당 서브넷에 위치한 리소스들은 외부와의 연결이 불가능
            - NAT 게이트웨이를 통해 `내부에서 외부로만 접근`이 가능하도록 만듦
            - 외부
                - VPC 영역이 다른 것
                - 같은 VPC 내부의 경우 private IP로 접근 가능
        - 사용 이유
            - 리소스들을 안전하게 관리하기 위함

### L4 스위치

- 부하 분산 처리
- Protocol들의 헤더를 분석 → 부하 분산을 실시
- 필요한 이유
    - 서버가 자꾸 늘어났을 때 부하 분산 처리를 자동화 시키기 위함 → ‘로드밸런싱’
- 모든 요청을 L4 스위치가 받기 때문에 각각 서버가 가진 공인 IP는 사라지고 오직 L4스위치만 공인 IP를 받게 됨
    - 따라서 서버들은 사설(private) IP를 부여받고 L4는 private, public IP를 가지게 됨

### NAT(Network Address Translation)이란

- 네트워크 망을 이동하면서 라우터와 같은 장비를 통해 출발지 or 목적지 ip가 변화하는 것을 의미

## 프로젝트 서버정리

- ALB : Lambda를 대상으로 로드밸런싱
- `**ELB**` : 부하분산, 헬스 체크, SSL 암복호화
    - 사용자는 `**DNS 이름**`을 통해 ELB에 접속 가능
        - 요청을 대상그룹에 전달 → 대상그룹의 EC2가 요청을 처리
    - `리스너`
        - 외부 요청을 받아들임
        - 서비스 포트를 보유
        - 다수의 리스너 존재가능
        - 로드밸런서에 접근 == 리스너의 포트에 접근
    - `대상그룹`(target group)
        - 리스너가 전달한 요청을 분산/전달할 리소스의 집합
        - `헬스 체크`를 통해 끊임없이 상태를 확인받음
        - 서비스 포트를 보유
    - `보안그룹`
        - 네트워크 인터페이스에 적용
        - ELB도 네트워크 인터페이스를 가지므로 보안그룹 가질 수 있음
        - 사용자가 전달하는 요청을 처리하기 위해서는 해당 요청의 포트를 보안그룹에서 열어둬야 한다
    - 종류
        - ALB
            - HTTP의 헤더 정보를 이용해 부하분산을 실시
            - SSL암호화/복호화 대신 진행
        - NLB
            - HTTP 헤더를 이용한 부하 분산이 불가
    - VPC내 에서 하나의 형태로 존재
    - `로드밸런서 노드`
        - 다수의 네트워크 인터페이스
        - 실질적으로 사용자의 요청을 받아들인 뒤 부하분산 대상들에게 요청을 나누어주는 역할
        - AZ마다 하나씩 존재
        - 공인/사설 IP를 모두 가짐
            - VPC 외부의 사용자들이 ELB로 작업요청 가능
    - 과정 총정리
    
    ```
    1. 사용자가 로드밸런서에 접근하기 위해 아마존의 DNS서버(Route 53)에 로드 밸런서ㅢ 도메인 해석을 요청
    2. 이마존의 DNS t서버가 로드 밸런서 노드 IP리스트를 사용자에게 전달
    3. 사용자는 IP중 하나를 선택하여 로드밸런서에 접근
    4. 사용자는 로드밸런서의 리스너에 접근 -> 리스너는 해당 요청을 적절한 대상그룹으로 전달
    5. 리스너로부터 전달받은 요청을 EC2가 처리한 후 다시 사용자에게 반환 
    ```
    - AutoScaling : 일정 시간 내 일정 조건을 충족하면 EC2를 추가/삭제

### ALB

---

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/943f4c53-bbdc-4dc0-b485-dae4305edaf3/Untitled.png)

- 구성요소
    - 규칙
        - HTTP 헤더에 담긴 정보를 해석 → 어떤 대상그룹에 전달할 지 판단
- 특징
    - HTTP를 활용한 라우팅(부하분산)
        - 요청헤더와 일반헤더를 활용하여 사용자의 상태정보나 디바이스 정보를 서버에게 전달가능
        - HTTP 요청 메서드
            - 요청 메서드를 기준으로 규칙을 생성
    - 로드 밸런싱
        - 라운드 로빈으로 요청을 EC2인스턴스에 순서대로 할당 → 요청이 고르게 분산
    - SSL 탑재 가능
        - L4스위치가 사용자와의 `암호화 통신`
            - 서비스 포트의 프로토콜을 443으로 변경
        - L4스위치와 서버는 `평문통신`
            - EC2 인스턴스들의 포트를 80으로 설정
        - 사전작업
            - Route 53을 통해 도메인 발급
            - ACM(AWS Certificate Manager) - SSL 인증서 발급 서비스를 통해 인증서를 발급받음
    - 프록시 서버역할
        - 프록시 서버
            - 클라이언트가 자신을 통해 다른 네트워크 서비스에 간접적으로 접속할 수 있게끔 하는 컴퓨터 시스템
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/abae554e-caae-4601-82cd-1ce6ef4556a3/Untitled.png)
    
    [과정 요약]
    
    ```
    1. 사용자와 ALB의 3 way handshake 
    2. ALB와 EC2인스턴스의 3 way handshake
    3. 사용자가 요청을 ALB에게 전달하면 ALB가 EC2 인스턴스에게 전달
    ```
    

## Reference

---

[AWS Application Load Balancer 쉽게 이해하기 #1](https://aws-hyoh.tistory.com/134)

## 오늘 느낀점

---

- 김동현 멘토님을 오랜만에 뵜는데.. 저번에 ERD설계를 열심히 한것에 비해서 이번 2주동안은 별로 한게 없어서 나한테 실망하신게 보였다. 팀원들은 더더욱 열심히 해줘서 나도 그거에 맞춰서 해야 할말 있을 것 같구!
- 그래서 이번주 내로 API 서버 다 완성할 계획이다 무조건 할꺼임 + 아키텍쳐 설계도 끝내고 EC2랑 ALB까지 연동할것이다
- 다들 열심히 하는만큼 나도 열심히 하자ㅏㅏ → 열심히 하면 다 됨! 자존감 높이기
- 하나 하다가 하나 더 하고싶은거 있으면 잠시 적어두고 하던거 마무리하고 하기 → 너무 정신없이 이것저것하니까 더 뭐했는지 모르는 것 같다.

## 내일 목표

---

- [ ]  AWS 설계 검증
- [ ]  AWS 팀 계정 받기
- [ ]  S3랑 람다 연결 
- [ ]  도메인 CRUD 완성 후 테스트