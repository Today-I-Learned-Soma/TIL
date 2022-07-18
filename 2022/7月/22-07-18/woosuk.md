## TIL

### Swift에서 range include check 하기

1. `~=` operator
```swift
if 10...100 ~= 50 {
    print("Number is inside the range")
}
```

2. `contains()` method
```swift
if (10...100).contains(50) {
    print("Number is inside the range")
}
```

3. 활용: `comparator` 을 implement 하는 다양한 object에서 비교를 간단하게 (**`Date` 에서 특히 유용**)

```swift
let firstPerson = "Adelide"
let lastPerson = "Zach"
let peopleRange = firstPerson...lastPerson
if peopleRange ~= "woosuk" {
	print("woosuk is in the range!")
}
```

### Lazy Properties

-   무겁고 오래 걸리는 로직이라면, computed property 혹은 함수로 매번 실행하는 것이 아니라 `lazy var` 을 통해 실행 결과를 저장해놓는 것이 낫다
-   외부에서 변경(mutate) 불가능하도록 `private` 설정하면 신뢰성을 높일 수 있다.
    
```swift
struct Run {
	let startTime = Date()
	
    lazy private(set) var elapsedTime: TimeInterval = {
        sleep(2)    // do some heavy workloads
        
        return Date().timeIntervalSince(startTime)
    }()
}

var run = Run()
print(run.elapsedTime)	// 2.016505002975464
sleep(2)
print(run.elapsedTime)	// 2.016505002975464
```
    
-   lazy property가 변경 가능한(mutable) property에 의존하면, 복잡도 상승
    -   나중에 mutable property가 바뀌어도 lazy property는 바뀌지 않음 → 싱크가 안맞음
	➡️ lazy property가 의존하는 다른 property 또한 변경 불가능해야 함 (immutable → `let` 으로 할당)

> **질문. 무거운 연산으로 caching해 놓고는 싶은데, 가끔 한 번씩 재계산할 일이 있으면 어떻게 할까? 외부 컨텍스트에서 갖고 있거나, 캐시 프라퍼티를 따로 만들거나, 의존성 변수에 setter를 등록하는 방법이 있기는 할 텐데, 이만큼 succint한 방법은 없을지.**

### 클로저에서의 [weak self]
간단히 정리하면, **`self`를 사용하는 클로저를 만든 뒤 그것을 계속 가지고 있으면, 순환참조를 유발한다.**

`self`를 참조하는 클로저를 계속 가지고 있는 상황:
- (다른 객체에 래핑하거나 해서) `self`의 property에 저장
- `Timer` 등, 스스로 deallocate 하지 않는 객체에 콜백으로 제공

## Reference

[How to check whether a value is inside a range](https://www.hackingwithswift.com/articles/90/how-to-check-whether-a-value-is-inside-a-range)

[Using Lazy Initialization, how do we reset the var?](https://developer.apple.com/forums/thread/15735)

[You don’t (always) need [weak self]](https://velog.io/@haanwave/Article-You-dont-always-need-weak-self)