### 1일차 요약

- vpc를 만들 때는 이름이랑 ip주소 범위를 cidr표기법으로 준다.
    - 그럼 기본 라우팅 테이블이 생긴다.
- vpc를 나누어서 쓰기 위해서 서브넷을 쓴다.
- 서브넷을 만들면 vpc의 주소 범위를 그대로 가져온다.
- 인터넷과 통신하기 위한 서브넷은 퍼블릭 서브넷이다.
    - 인터넷 게이트웨이를 만든다.
        - id가 생성된다.
- 그냥 만든 서브넷(default)는 프라이빗 서브넷이다.
- `퍼블릭 서브넷` 안에 NAT 게이트 웨이를 만든다.
    - 아웃바운드 규칙은 NAT게이트웨이를 거쳐 인터넷 게이트웨이를 거쳐 나간다.
- NACL은 상태 비저장이다
    - 들어오고 나가고를 다 체크해야 한다.
- security group은 리소스에 걸리는 가상방화벽
    - 상태 저장 → 들어올때만 체크한다.

- Service Scope
    1. global 서비스
    2. region 서비스
        1. VPC 외부
            1. s3
        2. VPC 내부
            1. ELB
    3. 가용영역(AZ) 내부
        1. EC2, EBS

## 4. 컴퓨팅

![AMI-EC2-02.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7269f641-9481-469d-88d1-ab96bad2b648/AMI-EC2-02.png)

- AMI는 OS를 선택하는 것이다.
- EBS
    - storage서버는 네트워크로 연결된다.
    - stop 했다가 start하면 다른쪽에 저장된다.
    - 비휘발성
    - EBS Optimized
        - EBS쪽의 네트워크를 강화시켰다.
- Instance store
    - 어떤 HW에 존재하는 physical한 storage
    - 휘발성
    - physical하게 연결되어 있다.
- Launch Template
    - Auto Scaling에서 사용
    - 사용자 부하가 발생하면 같은 형태의 서버를 자동으로 구동시키게 하기 위함
- busting기능
    - 최대 크래딧을 저장해 두었다가 부하가 급증하면 해당 크래딧을 사용한다.
- Image Builder
    - 이미지 생성해주는 솔루션
- 태그
    - 리소스를 만들면 꼭 태그를 만들어라
    - 리소스 관리는 태그로 이루어지기 때문이다.

- 배치그룹
    - 클러스터 배치그룹
        - 동일한 가용영역
    - 분산형 배치그룹
        - 다른 가용영역에 들어가있는다
    - 파티션 배치그룹
        - 각각의 역할을 하는 것을 파티션으로 묶을 수 있다.

## Lambda

- 서버리스 컴퓨팅
    - 서버를 관리하지 않는다.
    - 확장성
        - 사용자가 많으면 자동적으로 늘려준다.
    - 고가용성
- 메모리를 작게 잡으면 CPU도 작게 잡힌다
    - 메모리 설정에 따라 CPU의 사이즈가 달라진다.
- api 방식으로 구동
    - 클라이언트 app에서 바로 api를 호출할 수 있다.
    
- 람다 실습

[https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/lambda-examples.html](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/lambda-examples.html)

## DB 서비스

Aurora

- 클라우드를 위해 구축된 MySQL 및 PostgreSQL 호환 관계형 DB

DynamoDB

- 완전관리형
- 서버리스
    - 관리할 서버가 없음
    - 규모에 따른 성능
- NoSQL AWS DB 서비스
- 균등하게 저장이 되도록 파티션키를 잘 잡아야 한다.
- 

# 스토리지

---

## S3

- 객체 스토리지 솔루션
    - 객체는 파일과 파일을 기술하는 모든 메타데이터로 구성된다.
- 리전에 저장된다
- 한 리전 내의 모든 가용영역에 저장되서 하나가 날라가더라도 복구 가능하다
- 버켓의 이름은 글로벌하게 유일해야 한다.
- 미디어 데이터를 저장할 때 쓰인다
- 정적데이터(HTML , 정적 웹사이트) 같은 것들을 넣는다.
- 종류
    - inteliigent-tiering : 뭘 해야할지 잘 모르겠을 때 이걸 사용
        - 파일의 개수가 매우 많을 경우 비용이 더 증가할 수 있다.
- 대부분의 AWS 시스템들이 이벤트를 발생시킬 수 있다.
- 무제한으로 저장 가능
    - 한 파일 당 5TB가 MAX이다
        - 큰 파일을 올려야 할 때 멀티 파트 업로드를 사용한다.
- 비용 요소
    - 다른 리전 또는 인터넷으로 전송
    - PUT, COPY, POST, GET요청일때
- 비용X
    - 동일한 리전 내에서 전송할 경우
- 사용사례
    - Write Once, Read Only

## EFS

- 파일 서버
- 큰 사이즈를 설정할 수록 성능이 좋아진다.

## 모니터링

---

### Amazon CloudWatch

- 지표 및 로그를 거의 실시간으로 수집한다.
- 모니터링 데이터를 한 위치에서 액세스한다.
- 경보를 생성하고 알림을 전송
- 규칙에 따라 리소스 용량 변경을 시작
- 대시 보드를 생성하고 볼 수 있다.
- Amazon CloudWatch Logs
    - 로그 데이터들을 스트림으로 모아서 그룹핑해서 필터링 후 분석가능

### 로드밸런서

- 정기적으로 HTTP Request를 던져서 살아있는지를 확인 → ping을 통해
- 살아있음 → Healthy
- 고가용성을 제공
- 자동으로 트래픽을 여러 대상에 분산시킨다.
- ALB
    - L7 스위치
    - 경로기반 라우팅이 가능
- NLB
    - L4 스위치
    - 고정 IP 주소

## 자동화

---

### AWS Elastic Beanstalk

- 인프라를 자동으로 만들어줌
- 사용자는 코드만 올리면 사용가능함
- app을 자동으로 스케일 업/다운 가능

[웹 서버 환경](https://docs.aws.amazon.com/ko_kr/elasticbeanstalk/latest/dg/concepts-webserver.html)

- 웹서버 환경
    - autoscaling으로 구성되어 있다.
- 작업자 환경
    - SQS서비스를 사용

### CloudFormation

- 아키텍처 템플릿을 생성
    - JSON이나 YAML으로 생성
    - 실제 코드로 취급됨
        - github
        - codecommit 버전
- 아키텍처 스택
    - 논리적인 모습
- 드리프트 감지기능
- 장애 발생 시 서비스를 마지막 양호한 상태로 롤백

[템플릿 구조]

[https://docs.aws.amazon.com/ko_kr/AWSCloudFormation/latest/UserGuide/template-anatomy.html](https://docs.aws.amazon.com/ko_kr/AWSCloudFormation/latest/UserGuide/template-anatomy.html)

→ 디자이너형태로도 볼 수 있다.

→ 샘플 솔루션도 존재한다.

[AWS 솔루션 라이브러리](https://aws.amazon.com/ko/solutions/)

[Quick Starts - Amazon Web Services(AWS)](https://aws.amazon.com/ko/quickstart/?solutions-all.sort-by=item.additionalFields.sortDate&solutions-all.sort-order=desc&awsf.filter-tech-category=*all&awsf.filter-industry=*all&awsf.filter-content-type=*all)