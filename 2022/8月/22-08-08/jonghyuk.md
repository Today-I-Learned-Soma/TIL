# 오늘 배운점

---

## OAuth + JWT

- OAuth2.0 프로토콜은 CSRF 공격을 방지하기 위해 STATE 매개변수를 사용하는 것을 권장한다.
- 인증 중에 애플리케이션은 인증 요청(Authorization Request)에 이 매개변수를 전송하고, OAuth 공급자는 OAuth 콜백에서 변경되지 않은 매개변수를 반환한다. 애플리케이션은 OAuth 공급자로부터 반환된 상태 매개변수 값을 초기에 보낸 값과 비교하여 일치하지 않을 경우 인증 요청을 거부한다.
- 앞서 설명한 비교를 위해 쿠키를 활용하여 redirect_uri를 저장하도록 설계해야한다.

# 오늘 느낀점

---

- 막상 본격적으로 개발 들어가니까 기록하면서 학습하기가 되게 어려운 것 같다. 나름 꾸준히 써왔다고 생각했는데, 좀 더 익숙해질 필요가 있을 것 같다!

# 내일 목표

---

- 스프링 스터디