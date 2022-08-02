## 오늘 배운 것

---

## 빌더 패턴

- 정보들을 모두 받은 뒤에 객체를 생성한다.
    - 데이터의 무결성을 보장할 수 있다.

### IntelliJ 단축키

- command + shift + T : 테스트 코드 작성

## JAVA Enum 타입

---

### 예제

```java
public enum Rank {
	THREE(3, 4000), --> match : 3, money : 4000
	FOUR(4, 10000),
	FIVE(5, 30000);
	
	private final int match;
	private final int money;
	private int count;

	Rank(int match, int money) {
		this.match = match;
		this.money = money;
	}
```

- Default 생성자는 private → 따라서 임의대로 객체를 생성할 수 없음.

### 특징

- 서로 다른 Enum타입 비교 시 컴파일 에러를 발생시킨다.
- 데이터의 그룹화에 용이
    
    ```java
    public enum Address {
    	SEOUL("서울",Arrays.asList("강남","서대문","마포")
    	
    	private final String city;
    	private final String distinct;
    
    	Address(String city, List<String> distinct) {
    		this.city = city;
    		this.distinct = distinct;
    	}
    }
    ```
    
- 함수 추가 가능
    
    ```java
    enum VehicleType {
    	BUS(1500) {
    		@Override
    		int calculateAmount(int person) {
    			return person * fee;
    		}
    	},
    	AIRPLAIN(300000) {
    		@Override
    		int calculateAmount(int person) {
    			int additionalFee = 30000;
    			return person * fee + additionalFee * person;
    		}
    	}, // Enum 상수끼리는 ,로 연결
    	TAXI(30000) {
    		@Override
    		int calculateAmount(int person) {
    			return fee;
    		}
    	}; // 꼭 세미콜론 찍어주기!
    
    	protected int fee;
    
    	VehicleType(int fee) {
    		this.fee = fee;
    	}
    
    	abstract int calculateAmount(int person);
    }
    	
    ```
    

## 다양한 Read 방식

- **Dirty Read**
    - **다른 트랜잭션에 의해 수정됬지만 아직 커밋되지 않은 데이터를 읽는 것**
    - 잘못된 값을 가지고 로직 처리 가능
- Non-Repeatable Read
    - 한 트랜잭션 내에서 같은 row를 두번 읽음 → 중간에 값이 변경/삭제되서 결과가 다르게 나타남
- Phantom Read
    - 한 트랜잭션 내에서 같은 쿼리 두번 수행 → 없던 레코드가 두번째 쿼리에서 나타남

### @Transactional 어노테이션

- 선언적 트랜잭션
- 메소드, 클래스, 인터페이스 위에 추가하여 사용 가능
- 자동으로 commit / rollback을 처리해줌
- 옵션
    - isolation
        - 일관성 없는 데이터 허용 수준을 설정
        - Default
        - READ_UNCOMMITED
            
            커밋되지 않은 데이터에 대해 읽기 허용 → Dirty Read / Non-Repeatable Read / Phantom Read발생
            
        - READ_COMMITED
            
            커밋된 데이터에 대해 읽기 허용 → Non-Repeatable Read / Phantom Read발생
            
        - REPEATEABLE_READ
            
            동일 필드에 다중 접근 시 → 동일한 결과 보장 → Phantom Read발생
            
            shared lock이 걸리게 됨 → 수정 불가능
            
        - SERIALIZABLE
            
            
    - propagation
        - 
    - noRollbackFor
    - rollbackFor
    - timeout
    - readOnly

## 오늘 느낀 것

---

- 스터디 매우 알차다.. 그동안 나는 배우고자 하는 열정은 있었지만 왜 이걸 배워야 하고 왜 이걸 써야하는지에 대해서는 생각해보지 않고 누군가의 의견에 따라 이리저리 흔들리고 있었다는 걸 뼈져리게 느끼게 된 순간이었다
- 그래서 앞으로 프로젝트에서 무언가를 도입하고 공부할 때 `이걸 왜 쓰지?` 라는 생각을 바탕으로 공부할 것 같다!
- 누가 옆에서 아무리 좋아보이는걸 하고 있어도 내 뚝심으로 밀고가기!
- 이리저리 흔들리지 말고 계획 세운대로 실천하자~

## 내일 할 일

---

- 여성간담회
- 매물 리스트 crud완성
- 매물 상세페이지 crud완성
- s3업로드 기능 구현
- 비용 청구하기 → 미리캔버스