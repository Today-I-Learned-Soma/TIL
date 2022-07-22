# ECMAScript 2022

## Class Field

- 언어 자체에서 지원하는 private 접근 제어자 추가
- public 필드 및 정적 필드 선언 방식 개선
- 정적 초기화 블록 추가

```jsx
class B {
  #hidden = 0;
  m() {
    return this.#hidden;
  }
}
```

## Top level await

await을 쓰기위해서는 항상 async가 필요했는데 해당 조건이 사라짐

```jsx
import { process } from "./some-module.mjs";
const dynamic = import(computedModuleSpecifier);
const data = fetch(url);
export const output = process((await dynamic).default, await data);
```

## **Object.hasOwn()**

- 객체가 해당 property를 가지고 있는지 쉽게 판별할 수 있음

```jsx
if (Object.hasOwn(object, "foo")) {
  console.log("has property foo");
}
```

## Error cause

- 에러의 이유를 확인할 수 있음

```jsx
try {
  await doJob();
} catch (e) {
  console.log(e);
  console.log("Caused by", e.cause);
}
// Caused by TypeError: Failed to fetch
```

## 메서드 at()

- 한마디로 음수 인덱스 접근 가능해졌다는 뜻

```jsx
const arr = [0, 1, 2, 3, 4];
arr[-1]; // undefined
arr.at(-1); // 4
```
