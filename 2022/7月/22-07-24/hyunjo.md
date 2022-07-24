# React Testing Library

## 정의

DOM Testing Library 기반으로 개발된 리액트 컴포넌트 테스트 라이브러리

## 설치 방법

```
npm install --save-dev @testing-library/react
```

## 사용 이유

- 유지보수 가능한 리액트 컴포넌트를 작성하고자 할 때
- 실제 사용자 경험과 유사한 방식의 테스트를 작성하고자 할 때 (구현 < 기능)

## Jest와의 비교

- Jest: 자체적인 test runner + test util 제공
- RTL: Jest 포함 React 컴포넌트 test util 제공

## 사용 방법

1. 컴포넌트 렌더링하기
   > src/App.test.js

```jsx
import React from "react";
import { render, screen } from "@testing-library/react";

import App from "./App";

describe("App", () => {
  test("renders App component", () => {
    render(<App />);
  });
  screen.debug();
});
```

2. 특정 엘리먼트 선택하기

```jsx
import React from "react";
import { render, screen } from "@testing-library/react";

import App from "./App";

describe("App", () => {
  test("renders App component", () => {
    render(<App />);

    screen.getByText("Search:");
    expect(screen.getByText(/Search/)).toBeInTheDocument();
  });
});
```

3. Type(Role)로 검색하기

```jsx
import React from "react";
import { render, screen } from "@testing-library/react";

import App from "./App";

describe("App", () => {
  test("renders App component", () => {
    render(<App />);

    expect(screen.getByRole("textbox")).toBeInTheDocument();
  });
});
```

## 비고

### getBy vs queryBy vs findBy

- getBy: default
- queryBy: 해당 엘리먼트가 없을거라고 가정할 때
- findBy: 해당 엘리먼트가 "결국에" 있을거라고 가정할 때 (비동기적인 경우)

4. 이벤트 발생시키기

```jsx
describe("App", () => {
  test("renders App component", async () => {
    render(<App />);

    // wait for the user to resolve
    // needs only be used in our special case
    await screen.findByText(/Signed in as/);

    expect(screen.queryByText(/Searches for JavaScript/)).toBeNull();

    fireEvent.change(screen.getByRole("textbox"), {
      target: { value: "JavaScript" },
    });

    expect(screen.getByText(/Searches for JavaScript/)).toBeInTheDocument();
  });
});
```

5. Callback Handler 사용하기
   > 독립적인 컴포넌트 단위테스트 할 때 (RTL이 권장하는 방식 X)

```jsx
describe("Search", () => {
  test("calls the onChange callback handler", async () => {
    const onChange = jest.fn();

    render(
      <Search value="" onChange={onChange}>
        Search:
      </Search>
    );

    await userEvent.type(screen.getByRole("textbox"), "JavaScript");

    expect(onChange).toHaveBeenCalledTimes(10);
  });
});
```

6. 비동기 테스트

```jsx
import React from 'react';
import axios from 'axios';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

import App from './App';

jest.mock('axios');

describe('App', () => {
  test('fetches stories from an API and displays them', async () => {
    ...
  });

  test('fetches stories from an API and fails', async () => {
    axios.get.mockImplementationOnce(() =>
      Promise.reject(new Error())
    );

    render(<App />);

    await userEvent.click(screen.getByRole('button'));

    const message = await screen.findByText(/Something went wrong/);

    expect(message).toBeInTheDocument();
  });
});
```
