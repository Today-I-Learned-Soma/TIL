## Spring Security란?
---
- 애플리케이션의 보안을 Spring기반으로 담당하는 스프링 하위 프레임워크
- 필터 기반으로 동작
   - HttpRequest가 특정 Filter의 조건에 부합하면 동작
- 인증(Authentication)과 인가(Authorization)가 가장 핵심포인트
- 인증
   - 보호된 리소스에 대해 접근한 주체가 작업을 수행해도 되는 주체인지 확인
- 인가
   - 해당 리소스에 대해 접근 가능한 권한을 가진 주체인지 확인



## 인증관련 아키텍처
---
![](https://velog.velcdn.com/images/sophia5460/post/ae1ab90c-5641-46eb-b323-1fb11f7215ef/image.png)

### [설명]
1. 로그인 요청 발생
- form 로그인 기반으로 요청을 보냄

2. UserPasswordAuthenticationToken 발급
- 아이디와 비밀번호를 기반으로 토큰 발급
     - front에서도 check과정이 있지만 한번 더 체크 해주는 것이 좋다.
     - 아이디와 비밀번호 NULL 체크
- AuthenticationFilter로 요청이 오게 됨
- 현상태는 미검증 Authentication
    	
3. 해당 토큰을 AuthenticationManager에게 전달
- Authentication Manager
     - 실제 인증을 처리할 AuthenticationProvider을 여러 개 가짐

4. 해당 토큰을 Authentication Provider에게 전달
- Authentication Provider
     - 실제 인증의 과정을 수행
       - 인증에 관한 부분은 authenticate함수에 작성
     - username으로 조회 후 password 일치 여부를 검사하는 방식을 사용
     
5. UserDetailsService로 조회할 아이디를 전달
- UserDetailsService에서 아이디를 기반으로 데이터를 조회

6. 아이디를 기반으로 DB에서 데이터를 조회 -> 결과 반환
- 결과가 조회되지 않았을 경우를 대비해 Exception 클래스를 추가

7. 인증처리 후 인증된 토큰을 Authentication Manager에게 반환

8. 인증된 토큰을 Authentication Filter에게 전달

9. 인증된 토큰을 SecurityContextHolder에 저장


## OAuth 2.0
- 타사의 사이트에서 접근 권한을 얻고 해당 권한을 기반으로 개발할 수 있도록 도와주는 프레임워크
### 용어
- Access Token
  - 로그인을 하지 않고 인증을 할 수 있도록 도와주는 인증토큰
  
- Resource Owner
  - 개인정보의 소유자 -> 유저
  
- Resource Server
  - 개인정보를 저장하고 있는 서버 (구글, 카카오)
    - 이름, 메일 등 제공
    
- Authorization Server
  - Oauth를 통해 인증, 인가를 제공해주는 서버 -> 토큰을 발급해준다.
=> Authorization Server을 통해 발급받은 토큰을 이용하여 Resource Server로부터 자원을 제공받는다.

### 흐름
![](https://velog.velcdn.com/images/sophia5460/post/d0c4b0f4-2676-4de3-92c0-252857668003/image.png)
1. Front -> Authorization Server로 로그인 요청
2. Authorization Server -> Front로 Authorization code발급
3. Front -> Back으로 Authorization code 전달
4. Back에서 해당 code를 통해 Authorization Server로 토큰 요청
5. Authorization Server에서 Access Token 발급 후 전달
6. Back에서 해당 Token을 통해 Resource Server한테 자원 요청
7. Resource Server는 자원 응답
--- 
*OAuth를 사용하더라도 이후 인증방법은 별도로 필요*
8. 유저 정보에 따라 JWT 토큰 발급
9. Back에서 Front로 유저정보 & JWT 토큰 전달
  
### [Front 역할]
- Authorization code를 Back에게 전달
- Back에서 전달 받은 Access, Refresh 토큰 저장
- 권한이 필요한 요청마다 Authorization **헤더**에 Access Token 같이 보내주기
- Access Token 만료시 Refresh Token을 이용해 갱신 -> 백엔드에게 요청
- Refresh Token 재발급 요청

### [Backend 역할]
- Authorization code로 Authorization Server에게 토큰 요청
- Access Token으로 Resource Server에 이름, 이메일 정보 요청
- DB에 존재하지 않으면 새로 등로, 존재하면 정보 업데이트
- Primary Key값으로 JWT토큰 생성
    - Refresh Token은 DB나 Redis에 저장
- 유저정보, Access&Refresh Token을 프론트로 전달
- Access Token만료 시 Refresh Token 검증 후 재발급

## Token의 종류
### Access Token
- 사용자 정보에 직접 접근이 가능한 정보만을 소유
- 짧은 만료시간, 세션에 담아 관리

### Refresh Token
- 새로운 Access Token을 발급받기 위한 정보를 가짐
- 외부에 노출되지 않도록 DB에 저장
  
  
  
  
  
  
API호출할 때마다 Access Token이 유효한지 검증 절차가 필요