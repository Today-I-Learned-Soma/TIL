## 오늘 배운 것

---

- `Redis 서버`는 캐시와 세션데이터를 저장한다.
- 로그인이 필요한 서비스에 비로그인상태로 접근시 401(UNAUTHRIZED) 코드 반환
- 필수입력데이터에 NULL값을 입력시 400(BAD REQUEST) 반환
- 실패(아이디 중복) 상태값 : 409(CONFLICT)
    - 리소스의 충돌을 의미하는 상태코드
- 로그인이 되어있을 때만 조회가 가능 → 한번 더 비밀번호 체크해서 authorized확인하기

### DB 다수 조인 문제

- 다수의 테이블이 한번에 조인될 경우 데이터가 많을 때 성능저하 발생 가능 → 역정규화를 통해 조인 테이블을 줄이고자 함
- 정규화
    - 관계형 DB 설계에서 중복을 최소화하게 데이터를 구조화하는 프로세스
    - 일관성과 응집도를 높인다
    - 데이터의 Sync이슈를 최소화시키기 위해 필요
    - 필요한 데이터가 하나의 테이블에 있지 않는 경우가 많기 때문에 `다른 테이블과의 JOIN`을 통해 가져옴 → 데이터 조회의 비용을 증가
- 역정규화
    - 정규화된 DB에서 성능을 개선시키기 위해 사용되는 전략
    - DB의 비용을 최소화 하기 위해 중복을 허용 → 엔티티 통합 및 재조정

## In-memory

---

- 인-메모리 컴퓨팅
    - 운영을 위한 데이터를 HDD가 아닌 메인 메모리에서 수행하는 것
    - 과거보다 저장용량이 커졌기에 가능
- Cache
    - 데이터의 원본 or 원본 데이터를 통해 연산된 값을 `미리 저장`해두는 임시 저장소
    - 빠른 속도를 위해 사용 → 읽기 성능을 개선
        - 특히 동일한 요청에 대해 빠른 응답이 가능

## 주소 DB

---

- 주소 정보를 공공 데이터에서 가져오기
    1. 공공데이터포털에서 `건물정보 DB`를 제공
        1. 도로명주소, 지번주소, 좌표 등의 데이터 존재
    2. Cafe24 호스팅을 이용하여 MariaDB를 사용 → 관리툴로 PHPMyAdmin을 사용
    3. 파일이 너무 커서 DB에 한번에 넣을 수 없음
        1. 파일을 쪼개기 위해 Text File Cleaver을 사용

### 인덱스란?

---

- DB 테이블에 대한 검색 성능의 속도를 높여주는 자료구조
- `책에 있는 목차`라고 생각하면 편함
    - 원하는 카테고리를 목차에서 찾고 페이지 번호를 보고 찾아감
    - 인덱스에서 원하는 데이터를 찾고 저장된 물리적 주소로 찾아감
- 특정 컬럼에 인덱스를 생성하면 해당 컬럼의 데이터들을 정렬하여 `**별도의 메모리 공간**`에 물리적 주소와 함께 저장
    - 쿼리문의 where조건에 해당 인텍스 컬럼을 걸면 생성된 인덱스를 탈 수가 있다 → 검색 속도의 향상
- 사용 이유
    1. 조건 검색 Where 절의 효율성
        - 인덱스 테이블은 데이터들이 정렬되어 있기 때문에 데이터를 빠르게 찾을 수 있다.
    2. Order by 절의 효율성
        - Order by는 부하가 많이 걸리는 작업 → 해당 작업을 피할 수 있다.
    3. MIN, MAX의 효율적인 처리가 가능
        - MIN, MAX의 값을 레코드의 시작, 끝 값 한건씩만 가져오면 되기에 훨씬 효율적
- 단점
    - 정렬된 상태를 계속 유지시켜줘야 한다.
        - 레코드 내의 값의 변화 → 원본테이블, INDEX 테이블 둘 다 데이터 수정작업이 필요하다.
    - 검색시에도 인덱스가 무조건 좋지 만은 않다.
        - 10~15% 이하의 데이터를 처리하는 경우에만 효율적.
        - DB의 10%에 해당하는 저장공간이 추가로 필요
- 생성전략
    - 데이터의 분포도는 최대한, 조건절에 호출빈도가 높은 컬럼을 인덱스로 생성하는 것이 좋다.
    - 중복이 되지 않는 값으로 설정해야 한다. → 보통 PK로 인덱스를 건다.
    - 조건
        1. 조건절에 자주 등장하는 컬럼
        2. 항상 = 으로 비교되는 컬럼
        3. 중복되는 데이터가 최소한인 컬럼
        4. ORDER BY절에서 자주 사용되는 컬럼
        5. 조인 조건으로 자주 사용되는 컬럼
        6. 수정빈도가 낮은 컬럼
        7. Like와 함께 사용시 %가 뒤에 사용되도록 하기
- 예시
[테이블 생성]
    
    ```sql
    -- t_student 테이블 SCHEMA
    CREATE TABLE t_student (
      seq_no INTEGER PRIMARY KEY, -- sequence
      id CHAR(14) NOT NULL, -- 주민번호
      name VARCHAR(255) NOT NULL, -- 학생 이름
      age INTEGER NOT NULL, -- 나이
      grade INTEGER NOT NULL, -- 학년
      ins_timestamp     TIMESTAMP      NOT NULL -- 가입 일시
    )
    ```
    

[인덱스 추가]

```sql
-- single column index for id
CREATE INDEX si_id ON t_student (id);
-- single column index for name
CREATE INDEX si_name ON t_student (name);
-- multi column index for id, name
CREATE INDEX mi_id_name ON t_student (id, name);
-- multi column index for id, name, age
CREATE INDEX mi_id_name_age ON t_student (id, name, age);
...
```

***인덱스를 많이 설정한다고 해서 검색속도 향상XXX***

### 쿼리 튜닝과 DB 개선

---

- 데이터가 매우 많음 → 검색에만 10초가 걸림
    - 조회 성능을 높이기 위해서는 인덱스 처리가 필수이다.
- 개선사항
    1. 검색 조건을 정하기
        1. “읍면동리", “도로명", “건물명"으로 정한다
    2. 기존 테이블에서 “읍면동리" 부분을 group by 한다
    3. group by 한 결과를 [검색] 테이블에 넣는다.
        
        ```sql
        검색 테이블 생성 예시
        create table [검색]{
              "검색명" VARCHAR(255)
        }
        ```
        
    4. 도로명과 건물명도 동일한 방법으로 [검색] 테이블에 넣어주고 중복을 제거한다.
    5. [검색] 테이블에 “검색명"을 index로 걸어준다.
    6. 만들어준 [검색] 테이블에 like문을 걸면 실행속도가 엄청 빠르다
        
        ```sql
        select 검색명 from [검색] where 검색명 like '%대전%'
        ```
        

### 실행계획이란?

---

쿼리문 실행 시 DB 옵티마이저가 쿼리문을 실행하는 순서

- 예제
    
    ```sql
    -- SQL
    EXPLAIN
    SELECT *
    FROM board_data
        INNER JOIN users ON board_data.user_id = users.id
        INNER JOIN board ON board_data.board_id = board.id
    WHERE board_data.board_data_status = 'AVAILABLE'
    ORDER BY board_data.id DESC;
    ```
    
    - 실행계획
        
        ```sql
        -- 실행계획
        Sort  (cost=27.82..27.82 rows=1 width=4814) // 1)
          Sort Key: board_data.id DESC
          -> Nested Loop  (cost=0.28..27.81 rows=1 width=4814) // 2)
             -> Nested Loop  (cost=0.14..19.42 rows=1 width=3766) // 3)
                -> Seq Scan on board_data  (cost=0.00..10.75 rows=1 width=1145) // 4)
                     Filter: ((board_data_status)::text = 'AVAILABLE'::text)
                -> Index Scan using users_pkey on users  (cost=0.14..8.15 rows=1 width=2621) // 5)
                     Index Cond: (id = board_data.user_id)
             -> Index Scan using board_pkey on board  (cost=0.14..8.16 rows=1 width=1040) // 6)
                  Index Cond: (id = board_data.board_id
        ```
        

## 검색 팁

---

매물에 대한 기본정보는 네이버나 카카오 api를 통해 얻은 건물정보를 기반으로 저장 → 나머지 정보들만 세입자나 집주인이 입력하도록 함 → 그러면 검색할 때 기본정보를 기반으로 검색할 수 있게 된다.

## Spring boot

---

- @GeneratedValue
    - PK의 생성규칙을 나타냄
    - GenerationType.IDENTITY 옵션을 추가해야만 auto_increment가 된다.
- @NoArgsConstructor
    - 기본 생성자 자동 추가
- 실무에서는 Getter는 열어두고 Setter는 꼭 필요한 경우에만 사용
- @MappedSuperClass
    - JPA Entity클래스들이 해당 클래스를 상속할 경우 부모 클래스의 컬럼값들을 사용할 수 있도록 함
- @EntityListeners(AuditingEntityListener.class)
    - BaseTimeEntity클래스에 Auditing 기능을 포함
- @CreatedDate
    - Entity가 생성되어 저장될 때 시간이 자동 저장
- @LastModifiedDate
    - 조회한 Entity의 값을 변경할 때 시간이 자동 저장