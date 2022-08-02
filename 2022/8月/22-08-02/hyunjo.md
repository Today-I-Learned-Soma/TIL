# React 클래스 컴포넌트와 함수 컴포넌트 라이프사이클 비교

## componentDidMount

- componentDidMount 메소드는 컴포넌트를 처음 렌더링한 후에 실행되며 최초로 렌더링 되는 시점에만 단 한 번 실행된다.
- useEffect의 dependency list에 빈 배열을 전달하면 최초 렌더링 될 때 한 번만 실행된다.

## componentDidUpdate

- 라이프 사이클 이미지를 참고하면 다음과 같은 상황에서 update 가 발생한다.
  - props 가 바뀌는 시점
  - state 가 바뀌는 시점
  - 부모 컴포넌트가 re-render 되는 시점
  - forceUpdate 함수를 통해 강제로 렌더링되는 시점
- useEffect의 dependency list에 아무것도 전달하지 않으면 된다. dep List에 아무것도 전달하지 않으면 default 로 모든 state가 된다. 그러면 state 아무거나 바뀔 때마다 실행이 된다.
- 만약 특정 state가 바뀔 때마다 실행해주고 싶다면 dep list를 넣어준다. 특정 state가 바뀔때마다 useEffect의 콜백함수가 실행된다.

## componentWillUnmount

- 리액트 컴포넌트가 DOM에서 제거될 때 unmount를 한다.
- return function 이 componentWillUnmount 메소드 역할을 하게 된다. 이 반환 함수를 useEffect() 를 끝내며 실행하기에 clean-up 함수라고도 부른다.

```jsx
useEffect(() => {
  console.log("componentDidMount");
  return function componentWillUnmount() {
    console.log("componentWillUnmount");
  };
}, []);
```
