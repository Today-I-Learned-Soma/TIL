## 오늘 배운 것

---

## JPA Cascade Type

---

- ALL: 상위 엔티티에서 하위 엔티티로 모든 작업을 전파
- PERSIST: 하위 엔티티까지 영속성 전달
- MERGE: 하위 엔티티까지 병합 작업을 지속 → 두 엔티티를 조회한 후 업데이트
- REMOVE: 하위 엔티티까지 제거 작업을 지속 → 연결된 하위 엔티티까지 제거
- REFRESH: DB로부터 인스턴스 값을 다시 읽어오기 → 연결된 하위 엔티티까지 새로고침
- DETACH : 영속성 컨텍스트에서 엔티티 제거 → 연결된 하위 엔티티까지 영속성 제거

### 예제]

```java
<post.java>
public void addComment(Comment comment) {
	this.getcomments().add(comment);
	comment.setPost(this);
}
```

- 아무 cascade를 걸지 않았을 경우 → save시 Post만 저장이 된다.
- cascade.persist옵션 → comment도 같이 저장이 된다.

## CascadeType.REMOVE vs orphanRemoval = true

- CascadeType.REMOVE : 부모 엔티티 삭제 시 자식 엔티티도 삭제
    - 부모 엔티티가 자식 엔티티와의 관계를 제거해도 자식 엔티티는 삭제되지 않고 그대로 남아있다.
- orphanRemoval = true
    - 부모 엔티티가 자식 엔티티와의 관계 제거시 자식도 그대로 사라진다.
    

## Fetch Join vs Join

---

- 일반 Join
    - 조회의 주체가 되는 Entity만 SELECT해서 영속화
    - 오직 JPQL에서 조회하는 주체가 되는 엔티티만 조회해서 영속화
    - join 대상에 대한 영속성까지는 관여X → LazyInitializationException발생
- Fetch Join
    - 조회의 주체가 되는 Entity외에 Fetch Join이 걸린 연관 Entity도 함께 SELECT 해서 모두 영속화
    - 모두 영속화하기 때문에 FetchType이 Lazy인 엔티티를 참조하더라도 이미 영속성 컨텍스트에 들어있기 때문에 따로 쿼리가 실행되지 않은 채로 N+1문제가 해결됨

### 일반 Join을 사용하는 이유

- 필요한 Entity만 영속성 컨텍스트에 올려서 사용

## `@JsonIgnoreProperties({"hibernateLazyInitializer"})` 란?

- DB에서 데이터를 가져올 때 field위에 hibernateLazyInitializer이라는 필드가 추가적으로 존재함
    - 이것을 무시하지 않으면 그들은 JSON형식으로 직렬화될 것이다.
- 불필요한 직렬화를 피하기 위함
    - 직렬화된 JSON은 hibernateLazyInitializer 필드가 없으므로 만약에 발견시에 그들을 무시해라 라는 의미

## 에러 발생

---

```java
No serializer found for class 
org.hibernate.proxy.pojo.javassist.JavassistLazyInitializer and no 
properties discovered to create BeanSerializer (to avoid exception, disable 
SerializationFeature.FAIL_ON_EMPTY_BEANS) (through reference chain: 
org.bubu.booksroom.app.utility.response.ApiResponse["data"]
->org.bubu.booksroom.provider.entity.Book_$$jvst6d6_8["tags"]
->java.util.ArrayList[0]
->org.bubu.booksroom.provider.entity.Tag$$_jvst6d6_1["handler"])
```

- jpa에서 lazy로딩 시 사용되는 handler가 json변환시 오류를 발생

### Hibernate

- 자바 언어를 위한 ORM 프레임워크
- JPA의 구현체, JPA 인터페이스를 구현, 내부적으로 JDBC API를 사용

@SpringBootTest → 내부에 @Transactional 이 들어감 → rollback을 시켜버림

- 하나의 프로세스에서 관리를 할 수 있기 때문에 롤백이 가능하다.

OSIV 찾아보기

## 오늘 느낀 것

---

## 내일 할 일

---

- 레디스 구축하기
- AWS 파라미터 설정
- 패치조인