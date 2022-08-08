### 할일

---

스프링 시큐리티 블로그 총정리

s3 → sqs → lambda →ec2까지 → 테스트 완료

## 오늘 배운 것

---

## Spring  Bean이란

- Spring의 DI Container에 의해 관리되는 POJO(Plain Old Java Object)
- 스프링을 구성하는 핵심 요소
- 등록 방법
    - @Bean 이용
        - **`수동`**으로 스프링 컨테이너에 빈을 등록
            1. 개발자가 직접 제어가 불가능한 라이브러리를 활용할 때
            2. app의 전범위 적으로 사용되는 클래스를 사용할 때
            3. 다형성을 이용하여 여러 구현체들을 등록해줘야 할 때
        - 설정 클래스에는 @Configuration을 붙여주면 된다.
            - **반드시 @Configuration 안에서 @Bean을 사용해야만 싱글톤이 보장되므로 함께 사용해줘야 한다.**
        - **메소드 이름**으로 bean 이름이 결정된다.
        
        ```java
        @Configuration
        public class ResourceConfig {
        	@Bean
        	public Resource resource() {
        		return new Resoure();
        	}
        }
        ```
        
    - @Component 이용
        - 해당 어노테이션이 붙은 클래스들은 자동으로 빈 등록을 해준다.
        - @Controller, @Service, @Repository, @Configuration등이 해당된다.

## Security Filter

- 필터 체인
    - 스프링 시큐리티는 필터들을 체인처럼 엮어 놓아 해당 필터들을 거쳐야만 서블릿에 도달할 수 있게 된다.

- Security Config 설정

```java
@Configuration
@EnableWebSecurity //해당 애노테이션을 WebSecurityConfigurerAdapter을 상속하는 객체에 붙여주면 SpringSecurityFilterChain에 등록된다.
public class SecurityConfig extends WebSecurityConfigurerAdapter {

	@Override
	protected void configure(HttpSecurity http) throws Exception {
		http
				.authorizeRequests() // 요청에 의한 보안검사를 시작
				.anyRequest().authenticated() // 어떤 요청에도 보안검사를 한다.
		.and()
				.formLogin() // 보안 검증은 formLogin방식으로 하겠다.
				.loginPage("/login.html") // 사용자 정의 로그인 페이지
				.defaultSuccessUrl("/home") // 로그인 성공 후 이동 페이지
				.failureUrl("/login.html?error=true") // 로그인 실패 후 이동 페이지
				.usernameParameter("username") // 아이디 파라미터명 설정
				.passwordParameter("password") // 패스워드 파라미터명 설정
				.successHandler(loginSuccessHandler()) // 로그인 성공 후 핸들러
				.failureHandler(loginFailerHander()) // 로그인 실패 후 핸들러
				.permitAll() // 무조건 접근을 허용
```

## CSRF(Cross Site Request Forgery)

- 사용자가 의도치 않은 위조 요청을 보내는 것을 의미
- CSRF Token
    - 임의의 난수를 생성하고 세션에 저장
    - 백엔드는 요청을 받을 때마다 세션에 저장된 토큰과 전달받은 토큰의 값이 같은지 확인
- Spring Security는 default로 CSRF Protection을 적용하는 데, 상태를 변화시킬 수 있는 GET 요청을 제외한 POST, PUT, DELETE 요청에 대해 적용시킨다.
    - html에서 다음과 같은 csrf토큰이 포함되어야 위조 요청을 받아들여진다.
    
    ```java
    <input type="hidden" name="${_csrf.parameterName}" value="${_csrf.token}"/>
    ```
    
- disable해도 상관없는 이유
    - rest api는 stateless하기 때문에 `서버에 인증정보를 보관하지 않는다` → csrf토큰을 보낼 이유가 없다.

## Reference

---

[Spring Security]

[스프링 시큐리티 기본 API및 Filter 이해](https://catsbi.oopy.io/c0a4f395-24b2-44e5-8eeb-275d19e2a536)

[S3_EVENT][TO_SQS]

[https://www.youtube.com/watch?v=ZDHy3pwJnyo](https://www.youtube.com/watch?v=ZDHy3pwJnyo)

[SQS][LAMBDA] [https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/with-sqs.html](https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/with-sqs.html)

[https://github.com/widdix/sqs-lambda-example](https://github.com/widdix/sqs-lambda-example)

[BOTO3][SQS]

[https://aws.plainenglish.io/sqs-with-aws-sdk-for-python-boto3-on-ec2-85d343ba0a49](https://aws.plainenglish.io/sqs-with-aws-sdk-for-python-boto3-on-ec2-85d343ba0a49)