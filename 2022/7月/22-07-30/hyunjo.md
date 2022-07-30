# React useState hook의 특징

> 비동기적으로 처리된다.

## 살펴보기

아래와 같이 짜면 count가 3이어도 실행될 수 있다.
왜냐면 state는 변경되지 않았는데 코드는 실행될 수 있기 때문이다.

```jsx
function App() {
  let [count, setCount] = useState(0);
  let [age, setAge] = useState(20);

  return (
    <div>
      <div>안녕하십니까 전 {age}</div>
      <button
        onClick={() => {
          setCount(count + 1);
          if (count < 3) {
            setAge(age + 1);
          }
        }}
      >
        누르면한살먹기
      </button>
    </div>
  );
}
```

## 해결하기

> useEffect: 특정 state가 변경될 때 useEffect를 실행할 수 있다

```jsx
function App() {
  let [count, setCount] = useState(0);
  let [age, setAge] = useState(20);

useEffect(()=>{
  if ( count != 0 && count < 3 ) {
    setAge(age+1)
  }
 }, [count])

  return (
    <div>
      <div>안녕하십니까 전 {age}</div>
      <button
        onClick={() => {
          setCount(count+1);
        }}
      >
        누르면한살먹기
      </button>
    </div>
  );

```
