# Netlify 배포 자동화 (feat. Github Action)

## YAML (.yml)

- YAML Ain't Markup Language이라는 재귀적 이름으로 유명
- 원래는 Yet Another Markup Language 이었는데 마크업보다는 데이터에 중점을 두었음을 나타내기 위해 바꿈
- 최근에는 JSON, XML 등이 데이터 직렬화에 주로 사용되는 경향이 있어 YAML은 가벼운 마크업으로 사용되는 경우가 많음
- 들여쓰기로 구조체 구분, 하이픈(-)으로 리스트, 콜론(:)으로 키-값 나타냄
- Github Action에서는 workflow를 정의하기 위해 yaml을 사용함

## Github action

- .github/workflows에 workflow 정의하여 사용
- 커밋 push, PR생성, issue 생성 등의 event가 발생하면 특정 action을 취하도록 함
- Jobs에 step별로 해야할 action을 정의함
- action은 직접 정의하거나 미리 정의된 것을 사용할 수 있음
- 어떤 VM에서 돌아가게 할지 꼭 정의해야함
- 사용 예시
  ```yaml
  name: learn-github-actions //이름 지어줄 수 있음(optional)
  on: [push] // 어떤 이벤트에 대해 action 할지 (necessary)
  jobs:
    check-bats-version:
      runs-on: ubuntu-latest // 어떤 vm에서 돌아갈지 (necessary)
      steps:
        - uses: actions/checkout@v3 // 레포지토리로 체크아웃(necessary)
        - uses: actions/setup-node@v3 // 실행 환경 정의
          with:
            node-version: '14'
        - run: npm install -g bats // 해당 명령 실행함
        - run: bats -v
  ```

## 실제 스크립트

```yaml
name: "test-dev"

on:
  push:
    branches:
      - dev

jobs:
  test:
    name: build dev
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Use Node.js
        uses: actions/setup-node@v3
        with:
          node-version: 16

      - name: Cache node modules
        uses: actions/cache@v3
        id: Cache
        with:
          path: node_modules
          key: npm_packages-${{hashFiles('**/package-lock.json')}}

      - name: Install Dependencies
        if: steps.cache.outputs.cache-hit != 'true'
        run: npm install

      - name: Run build
        if: ${{always()}}
        run: npm run build

      - name: Deploy to Netlify
        uses: nwtgck/actions-netlify@v1.2
        with:
          publish-dir: "./dist"
          production-branch: dev
          github-token: ${{ github.token }}
          deploy-message: "Deploy from GitHub Actions"
          enable-pull-request-comment: false
          enable-commit-comment: true
          overwrites-pull-request-comment: true
        env:
          NETLIFY_AUTH_TOKEN: ${{ secrets.NETLIFY_AUTH_TOKEN }}
          NETLIFY_SITE_ID: ${{ secrets.NETLIFY_SITE_ID }}
        timeout-minutes: 1
```

## 참고자료

- [https://github.com/actions/checkout](https://github.com/actions/checkout)

- [https://velog.io/@godud2604/netlify-GitHub-Actions-사용하기-CICD](https://velog.io/@godud2604/netlify-GitHub-Actions-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-CICD)
- [https://dev.to/dancurtis/ci-cd-pipeline-with-netlify-and-github-actions-bcm](https://dev.to/dancurtis/ci-cd-pipeline-with-netlify-and-github-actions-bcm)
