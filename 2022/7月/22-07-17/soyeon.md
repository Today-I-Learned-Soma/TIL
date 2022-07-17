## 참고 URL

---

[https://medium.com/29cm/선물하기-서비스-개발기-c5cdca816269]![1](https://user-images.githubusercontent.com/84591000/179418219-421caa0e-67f1-48ff-8abd-f37ee5bf40f3.png)

- SQS를 사용하는 이유
    - 취소 또는 주문의 배송 처리는 Commerce Service가 담당 → Gift Service에서 이를 먼저 알 수 없다.
    - `pub/sub구조` 적용
        - 주문과 선물하기 간의 `상태 동기화`를 위해 Commerce Service에서 메시지로 발급
        - Gift Service에서는 이를 수신하여 주문상태를 최신화
        

![2](https://user-images.githubusercontent.com/84591000/179418220-6c12e59e-98cb-437b-8407-4bccdeff89f6.png)

- commerce batch → 선물하기 주문 후 7일이 경과해도 수령자가 수락/거절 표현 안할 시 만료 처리

![3](https://user-images.githubusercontent.com/84591000/179418221-588b530c-05ee-4f39-a9c6-2e3fca044108.png)

- 다양한 상태 정의
    
![4](https://user-images.githubusercontent.com/84591000/179418225-e6d8f2bd-f78c-4fa5-87c8-f8bd449293de.png)
    

## 오늘 느낀 것

---

- 팀원한테 바라는 만큼 나도 잘하자
- 일정변경사항은 미리미리 말하기

## 내일 할 일

---

메시지 큐(카프카 공부)

API 설계
