## 오늘 배운 것

---

### 식별관계

- 부모 테이블의 기본키를 외래키로 받아서 `기본키 + 외래키를 기본키로 사용`하는 관계
- **`복합키 사용`**

### 비식별관계

- 부모 테이블의 기본키를 `외래키로만 사용`하는 관계
- 필수적 비식별 관계
    - 외래키에 NULL허용 X
- 선택적 비식별 관계
    - 외래키에 NULL 허용 O

### 복합키

- JPA에서 영속성 컨텍스트에서 엔티티 보관시 `식별자를 이용해서 구분`
- 식별자가 하나일때는 기본타입으로 구분하지만 여러개일 경우에는 따로 `클래스를 정의해서 사용`해야 함
- 종류
    - @IdClass
        - 관계형 DB에 가까움
        - 조건
            - **`식별자 클래스의 속성명 == 식별자의 속성명`**
            - Serializable 인터페이스를 구현해야 함
            - `기본 생성자` 필요
            - 식별자 클래스는 public
        - 식별자 클래스를 별도로 만들기
        
        ```java
        @Entity
        **@IdClass(ParentId.class)**
        public class Parent {
        	@Id
        	@Column(name = "PARENT_ID1")
        	private String id1;
        
        	@Id
        	@Column(name = "PARENT_ID2")
        	private String id2;
        
        }
        ```
        
        [식별자 클래스]
        
        ```java
        public class ParentId implements Serializable {
        	private String id1;
        	private String id2;
        
        	public ParentId() {}
        
        	public ParentId(String id1, String id2) {
        		this.id1 = id1;
        		this.id2 = id2;
        	}
        
        	@Override
        	public boolean equals(Object o) {...}
        
        	@Override
        	public int hashCode() {...}
        }
        ```
        
        [사용방법]
        
        ```java
        Parent parent = new Parent();
        parent.setId1("myId1");
        parent.setId2("myId2");
        parent.setName("parentName");
        em.persist(parent);
        ```
        
        [검색] → 복합키로 검색해야 한다.
        
        ```java
        ParentId parentId = new ParentId("myId1" , "myId2");
        Parent parent = em.find(Parent.class, parentId);
        ```
        
        [자식클래스]
        
        ```java
        @Entity
        public class Child {
        	@Id
        	private String id;
        
        	//외래키 매핑 시 여러 컬럼을 매핑해야 함 -> joinColumns 어노테이션 사용
        	@ManyToOne
        	@JoinColumns({
        		@JoinColumn(name = "PARENT_ID1", referencedColumnName = "PARENT_ID1"),
        		@JoinColumn(name = "PARENT_ID2", referencedColumnName = "PARENT_ID2")
        	})
        	private Parent parent;
        ```
        
    - @EmbeddedId
        - 객체지향에 가까움
        
        ```java
        @Entity
        pubilc class Parent {
        	@EmbeddedId
        	private ParentId id;
        
        	private String name;
        }
        ```
        
        [식별자 클래스]
        
        ```java
        @Embeddable
        public class ParentId implements Serializable {
        
        	@Column(name = "PARENT_ID1")
        	private String id1;
        
        	@Column(name = "PARENT_ID2")
        	private String id2;
        	
        	//equals and hashCode 구현
        	...
        }
        ```
        
        [사용코드]
        
        ```java
        Parent parent = new Parent();
        ParentId parentId = new ParentId("myId1","myId2");
        parent.setId(parentId);
        parent.setName("parentName");
        em.persist(parent);
        ```
        
- equals()
    - 기본
        - 동일성 비교를 함

### JPA Auditing

- Spring Data JPA에서 시간에 대해 자동으로 값을 넣어주는 기능
- 자동으로 시간을 매핑해서 db 테이블 내에 넣어준다.