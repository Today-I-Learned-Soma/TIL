## 오늘 할일

---

- [x]  서버 구성 완료
- [x]  api test 완료 → media 업로드까지
- [ ]  페이징 처리

## 오늘 배운 것

---

### CORS(Cross-Origin Resource Sharing Policy)

- SOP(Same Origin Policy)
    - 동일한 출처의 Origin 만 리소스를 공유할 수 있는 것
    - 이를 검증하는 것이 CORS이다.
- CORS 발생 이유
    - Preflight 요청에서 적절한 Access-Control을 찾지 못하면 발생
    - 해결방법
        - CorsFilter로 직접 response에 header를 넣어주기
        - Controller에 @CrossOrigin 어노테이션 추가
            - 컨트롤러에서 특정 메서드 or 컨트롤러 상단부에 @CrossOrigin만 추가하면 됨
            - 단점
                - 컨트롤러가 많을 수록 설정해야 하는 어노테이션이 많아진다.
        - WebMvcConfigurer를 이용해서 처리하기
            - main함수에서 Bean으로 Configurer를 추가해주면 된다.

## NAT Gateway

- Network Address Translation
- 등록되지 않은 IP주소를 사용하는 사설 IP 네트워크가 인터넷에 연결 가능
- 프라이빗 서브넷 인스턴스 / AWS 서비스 간의 단방향 연결에 사용가능
    - 외부 트래픽이 프라이빗 인스턴스와 연결하는 것을 방지
- 퍼블릭 서브넷용 RT는 모든 트래픽을 > igw로 보냄
- 프라이빗 서브넷용 RT는 모든 트래픽을 > NAT로 보냄