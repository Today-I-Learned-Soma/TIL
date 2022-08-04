# TIL

## Python Enum

이미지에서 인식된 객체 중 신호등의 색깔에 따라 초록불, 빨간불로 구분하고, 향후 더 다양한 종류의 신호등을 추가할 수 있도록 enumeration 객체를 사용했다.

```python
from enum import Enum

class TrafficLight(Enum):
	Red = 0
	Green = 1
```

그런데, Yolo에서 사용하는 클래스 이름을 `TrafficLight` enum으로 변환하는 로직은  `TrafficLight` 안에 있어야 할 것 같았다. 이를 위해, Yolo 이름과 enum 이름을 매핑해주는 딕셔너리를 static 변수로 가지고 있고 싶었다.

`Enum` 안에서 enumration에 포함되지 않는 static 변수를 선언하는 방법에 대해 찾아본 결과, 내 용도에 제일 가까운 것은 `_ignore_ = ["ignoreField"]` 와 같이 변수로 선언되지만 enum으로는 등록하지 않을 필드를 등록하는 것이었다. 그러나 이는 아래 예시처럼 enum case를 만들기 편하도록 중간 변수를 만드는 용도였고, 이를 `TestEnum.TestData`와 같이 접근하는 것은 불가능했다. (`TestEnum` 안의 함수에서도 불가능)

```python
# https://torbjorn.tistory.com/622

from dataclasses import dataclass
from enum import Enum

class TestEnum(Enum):
	_ignore_ = ["TestData"]
	  
	@dataclass
	class TestData:
		title: str
		exclude: str

		def dict(self):
			return {k: v for k, v in  self.__dict__.items() if k != "exclude"}

	A = TestData(title="hello", exclude="world")
	B = TestData(title="hello2", exclude="world2")

c = TestEnum.A.value
print(c.dict())
print(list(TestEnum))
```

이를 해결하기 위해, 처음에는 클래스 바깥에 전역 변수를 선언했다가, 나중에는 일단 `Enum`을 선언하고 이후에 멤버로 따로 등록해주는 방법을 택했다.

```python
from enum import Enum, auto

class TrafficLight(Enum):
  Red = 0
  Green = 1

  @staticmethod
  def fromYoloClassName(className: str):
    if className in TrafficLight.yoloClassNames:
      return TrafficLight[ TrafficLight.yoloClassNames[className] ]
    else:
      raise ValueError("invalid className for traffic light!")


TrafficLight.yoloClassNames = {
    "R_Signal": "Red", 
    "G_Signal": "Green"
}
```

만약, 위의 코드가 선언되지 않은 변수 `TrafficLight.yoloClassNames`를 미리 참조하고 있다는 점이 읽기 불편하고, 이 변수를 해당 `Enum` 안에서만 사용할 것이라면, 다음과 같이 함수의 파라미터로 전달할 수도 있다. 이는 함수의 default parameter는 함수가 정의될 때 미리 생성되어 반복 호출에 재사용된다는 점을 이용한 우회책이다. 그러나 이 경우 다른 코드에서 static variable로 불러와 사용할 수 없었고, 내 사용 용도에는 맞지 않았다.

```python
class TrafficLight(Enum):
  Red = 0
  Green = 1

  _ignore_ = ["yoloClassNames"]
  yoloClassNames = {
    "R_Signal": "Red", 
    "G_Signal": "Green"
  }

  @staticmethod
  def fromYoloClassName(className: str, yoloClassNames = yoloClassNames):
    if className in yoloClassNames:
      return TrafficLight[ yoloClassNames[className] ]
    else:
      raise ValueError("invalid className for traffic light!")
```


# References

[enum value로 @dataclass 사용하기](https://torbjorn.tistory.com/622)

[[StackOverflow] Declare a static variable in an enum class](https://stackoverflow.com/questions/36003273/declare-a-static-variable-in-an-enum-class)

