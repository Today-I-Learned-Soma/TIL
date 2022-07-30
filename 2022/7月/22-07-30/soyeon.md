## 오늘 할일

- [ ]  매물 아이디 변경
- [ ]  공통 코드 적용
- [ ]  매물 상세페이지 crud
- [ ]  erd 적용해서 엔티티 정의

## 오늘 배운 것

---

## Swagger Annotation

- @ApiOperation
    - 해당 API에 대한 설명 추가
    - ex) @ApiOperation( value = “개별 API에 대한 소개", notes = “개별 API에 대한 설명")
- @ApiParam
    - 요청 파라미터에 대한 설명 및 필수 여부, 예제 값 설정
    - 매개 변수에 대한 세부정보 추가, 코드에서 읽을 때 값 변경 가능

## ResponseEntity

- httpentity의 자식.
- 결과 데이터와 HTTP 상태 코드를 직접 제어할 수 있는 클래스
- 사용자의 HttpRequest에 대한 응답 데이터가 포함된다.
- 구조
    - HttpStatus
    - HttpHeaders
    - HttpBody
- ex) new ResponseEntity<>(dto, header, HttpStatus.OK) → body, header, status

### 자바 제네릭(Generic)

- 클래스 내부에서 지정하는 것이 아닌 `외부에서 사용자에 의해 지정`되는 것
    - 타입
        - <T> : Type
        - <E> : Element
        - <K> : Key
        - <V> : Value
        - <N> : Number
    
    [타입 정의]
    
    ```java
    public class man <T, T2> {
    	private T name;
    	private T2 age;
    	
    	public T getName() {
    		return name;
    	}
    
    	public T2 getAge() {
    		return age;
    	}
    }
    ```
    
    T : String, T2 : Integer로 지정 → 자유롭게 반환 가능 
    
    [사용]
    
    ```java
    public static void main(String[] args) {
    	man <String, Integer> man1 = new man<>();
    	man1.setName("King");
    	man1.setAge(25);
    }
    
    ```
    

### 와일드 카드

- 제네릭 타입을 매개 값이나 리턴 타입으로 사용할 때 구체적인 타입 대신에 사용
- 코드에서는 ?로 표현된다.
- 종류
    - 제네릭타입<?>
        - 모든 클래스/인터페이스 타입 가능
    - 제네릭타입<? extend 상위 타입>
        - 상위타입과 하위타입 올 수 있다.
    - 제네릭타입<? super 하위 타입>
        - 하위타입과 상위타입이 올 수 있다.

mysql은 json타입으로 박을 수 있다.

media를 json으로 바꿔도 괜찮을 듯