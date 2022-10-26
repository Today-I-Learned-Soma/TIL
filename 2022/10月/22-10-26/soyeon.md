# 테스트코드
## 어노테이션

- DataJpaTest
    - JPA 관련 테스트 설정만 로드한다.
        - JPA를 사용하여 데이터를 제대로 생성, 수정, 삭제하는지 테스트가 가능.
        - 내장형 DB로 테스트가 가능함
    - 기본적으로 @Transactional 어노테이션을 포함
        - 자동으로 롤백
    - 테스트용 TestEntityManager를 이용하면 persist, flush, find등 간단한 JPA 테스트가 가능
- AutoconfigureTestDatabase
    - 기본값 : Replace.Any : 내장된 임베디드 DB를 사용
    - NONE : ActiveProfiles에 설정한 프로파일 환경값에 따라 데이터 소스가 적용
- Extendwith
    - 확장기능 구현
    - 스프링의 경우 Extendwith(SpringExtension.class)와 같이 사용
- WebMvcTest
    - 단위테스트이다.
    - Spring MVC를 위한 테스트 ⇒  Controller가 예상대로 동작하는지 테스트 할 때 사용
        - 단일 컨트롤러를 대상으로 테스트가 가능
    - @Controller 사용가능
    - @Service, @Component, @Repository등은 사용 불가 → 해당 어노테이션이 붙은 Bean들은 ComponentScan 대상에서 제외된다 ⇒ 따라서 해당 Bean들은 Mocking해서 사용하는 것이 정석이다.
        - ex) @MockBean CompanyService companyService;
    - `SpringBootTest와 함께 사용 불가`
    - ex) WebMvcTest(000.class)
    - Mockmvc와 함께 사용
        - ex) mvc.perform(get(”/—-/—-”)
- private MockMvc mvc
    - 웹 API 테스트 할 때 사용
- AutoConfigureMockMvc
    - Springboot의 내장 서블릿 컨테이너 실행X, 모의적인 서블릿 환경 제공

## Mock vs Mockito vs Mockmvc

---

- Mock
    - 테스트를 위한 가짜 객체
    - 껍데기만 있는 객체
- MockBean
    - Bean의 껍데기만 가져오고 내부의 구현 부분은 모두 사용자에게 위임한 형태
- Mockito
    - Mock 객체를 간편하게 만들게 해주는 라이브러리
    - Mock 객체 직접 구현하지 않아도 되게끔 함
- MockMVC
    - Controller 테스트를 용이하게 해주는 라이브러리

## 정리

- 단위테스트
    - 컨트롤러 단
        - WebMvcTest + MockMvc사용
        - WebMvcTest로 컨트롤러 클래스 불러오고 @MockBean으로 서비스 레이어 가져옴, MockMvc를 통해 Rest API 테스트 진행