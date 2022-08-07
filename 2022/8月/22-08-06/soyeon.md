## 오늘 할일

---

- Enum 인자로 받아오기
- List 인자로 받아오기
- S3 업로드 구현
- 젠킨스와 nginx 연동
- [https://medium.com/sjk5766/nginx-reverse-proxy-사용하기-e11e18fcf843](https://medium.com/sjk5766/nginx-reverse-proxy-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-e11e18fcf843)
- [https://dbjh.tistory.com/75](https://dbjh.tistory.com/75)

[중간 발표 이경용](https://www.notion.so/3c0600cb31e54b9db2dbaee141b126e6)

## Enum 인자로 받아오기

---

1. 문자열로 받아서 Enum으로 변환하기

```java
public enum BankCode {
	KB("004", "국민은행"),
	NH("011", "농협은행");

	private final String code;
	private final String bankName;

	public static BankCode of(String codeStr) {
		if (code == null) {
			throw new IllegalArgumentException();
		}
	
		for (BankCode bc : BankCode.values()) {
			if(bc.code.equals(codeStr) {
				return vc;
			}
		}
		
		throw new IllegalArgumentException("일치하는 은행코드가 없습니다.");
	}
}

public Result getList(@RequestParam String bankCodeStr) {
	BankCode bankCode = BankCode.of(bankCodeStr);
}
```

1. Converter 생성하기
    1. Converter 클래스를 생성
    
    ```java
    public class BankCodeRequestConverter implements Converter<String, BankCode> {
    	@Override
    	public BankCode convert(String bankCode) {
    		return BankCode.ofCode(bankCode);
    	}
    }
    ```
    
    b. 해당 컨버터를 추가함
    
    ```java
    @Configuration
    public class WebConfig implements WebMvcConfigurer {
    	@Override
    	public void addFormatters(FormatterRegistry registry) {
    		registry.addConverter(new BankCodeRequestConverter());
    	}
    }
    ```
    
     ⇒ 알아서 Enum값으로 들어온 param을 String으로 변환시켜 넣어줌
    

1. Enum 클래스에 @JsonCreator어노테이션을 사용해서 Enum을 변환해주는 메소드를 생성
    
    ```java
    public enum EventType {
    	
    	@JsonCreator
    	public static EventType from(String s) {
    		return EventType.valueOf(s.toUpperCase());
    	}
    
    }
    ```
    

## AWS의 파라미터 스토어

---

### 파라미터 규칙

<aside>
💡 {prefix}/{name}{profile-separator}{profile}/key

</aside>

- prefix
    - 파라미터의 접두사 지정 가능
    - 해당 값은 /로 시작해야 함
- name
    - 식별자 애플리케이션 이름
    - 없을 시 spring.application.name의 값을 참조
        - 이마저도 없을 시 ‘application’ 이름 부여
- profile-separator
    - 하나의 app을 여러 환경에 배포할 수 있게끔 구분자를 지정 → name과 함께 쓰임
        - ex) idiot_local, idiot_production
- profile
    - spring.config.active.on-profile에 지정된 값
- enabled
    - AwsParamStoreBootstrapConfiguration을 활성화함
    - default : true