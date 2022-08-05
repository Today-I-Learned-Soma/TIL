# TIL

## 커밋메시지를 한 번에 수정하기: `git rebase` 의 `reword` 옵션

git 커밋메시지에 종류에 따라 태그를 달아 놓는데, 언제부터인가 헷갈려서 다른 것으로 달아놓은 커밋이 10개쯤 쌓여 있었다.

`git rebase -i` 인터렉티브 리베이스에서 바꾸고 싶은 커밋을 `edit`으로 `git commit --amend`를 통해 하나하나 수정할 수 있겠지만, 그러기에는 너무 귀찮고 한 번에 수정할 수 있는 방법이 있을 것 같았다.

아니나다를까, 리베이스 옵션을 `edit`이 아닌 `reword`로 하면, 해당 커밋들의 커밋 메세지 파일만 순회하면서 메세지를 변경할 수 있다. 

그런데 이것도 파일을 직접 순회하면서 고쳐주는 식이라, 몇십 개 이상의 커밋메시지를 전반적으로 바꾸려면 리베이스 옵션 중 `exec` 을 통해 한 번에 나열해주거나, 다른 툴을 이용해야 할 것 같다. 참고할 만한 스택오버플로우 소스들을 아래 달아 놓는다.

#### !!!중요!!! 

그냥 rebase를 사용하면, 수정된 커밋들의 author date는 그대로지만 commiter date가 수정되면서 GItHub에 올라가는 커밋 시각이 하나로 통일된다! 아래와 같이 옵션을 주면 커밋 시각 변경 없이 작동한다.

```shell
git rebase -i <commit hash> --committer-date-is-author-date 
```

참고로, `git log`에서 보여지는 커밋 시각은 author date이다. GitHub에서 사용하는 commiter date를 함께 확인하려면 아래와 같이 로그를 뽑으면 된다.

```shell
git log --pretty=fuller
```


# References

[Git Commit 기록 정리하기 (git rebase)](https://velog.io/@shin6949/Git-Commit-%EA%B8%B0%EB%A1%9D-%EC%A0%95%EB%A6%AC%ED%95%98%EA%B8%B0-git-rebase)

[이전 commit message 수정하기(reword)](https://sukvvon.tistory.com/68)


https://stackoverflow.com/questions/29198289/with-git-rebase-is-there-a-way-to-reword-commit-messages-in-the-git-rebase-todo


https://stackoverflow.com/questions/12394166/how-do-i-run-git-rebase-interactive-in-non-interactive-manner