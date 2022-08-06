# GitHook

## 정의

Git은 중요한 작업이 발생할 때 사용자 지정 스크립트를 실행하는 방법

## 사용 방법

stage(git add로 커밋대상이 된 파일)가 된 파일에 우리가 설정해둔 명령어를 실행해주는 라이브러리를 활용하여 원하는 컨벤션 자동화를 할 수 있다.

```json
//package.json
"lint-staged": {
  "*.js": "eslint --cache --fix",
  "*.{js,css,md}": "prettier --write"
}
```

```shell
git add .
npx lint-staged
```

## 사용 이유

협업시 코딩 컨벤션을 지키는 것은 중요한데, 이를 놓치는 경우가 있을 수 있으므로 자동화해놓는 것이 좋다.
