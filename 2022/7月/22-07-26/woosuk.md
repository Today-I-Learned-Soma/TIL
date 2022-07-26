# TIL

## Git Tag & Release 사용 방법

### Git Tag vs Release

GitHub의 Releases에 들어가보면, `Releases`와 `Tags`를 통해 개발 기록의 마일스톤을 볼 수 있다. Git의 tag 기능을 이용해 태그를 붙이고, GitHub 사이트에서 추가 정보를 붙여 Release를 내는 것이다.

Git의 tag은 다음 두 가지로 구분된다.
- 일반 tag: 이름만 존재 (ex. v1.13.1)
- 주석 tag: 이름과 설명, 서명, 타임스탬프

### Git Tag 사용 방법

- 일반 tag
```shell
$ git tag <tagname>
```
아래와 같이 태그를 달 커밋을 명시할 수 있다.
```shell
$ git tag <tagname> <commit hash>
```

- 주석 tag
```shell
$ git tag -a <tagname> -m "tag description"
```
참고로 여기서 `-m` 옵션을 명시하지 않으면 vim 에디터로 설명을 작성할 수 있다. 그러나 GitHub 상에서는 마크다운 효과 없이 커밋 메시지처럼 표시되므로, Release가 아닌 Tag에서 한 줄 이상으로 길게 작성하지 않는 편이다.

- 태그 삭제
```shell
$ git tag -d <tagname>
```

- 태그를 원격 저장소에 푸시
```shell
$ git push origin main --tags
```

- 등록된 태그 확인
```shell
$ git tag
```
또한, 일반적인 깃 로그에서도 태그를 확인할 수 있다.

# References

[[김종권의 iOS 앱 개발 알아가기] [git] tag (Release) 사용 방법 (terminal, source tree, remote 3가지 방법)](https://ios-development.tistory.com/356)