# TIL

## Git Submodule

Git의 서브모듈은 다른 레포지토리의 코드를 디펜던시로 사용하기 위해 해당 레포의 특정 커밋을 태그하여 사용할 수 있는 기능이다. `git submodule` 커맨드를 통해 관련 기능을 사용해 보자.

#### 서브모듈 추가

서브모듈로 추가하고 싶은 레포지토리의 git 주소를 아래와 같이 추가하면, 해당 레포지토리의 콘텐츠가 불러와진다. 이 때 `.gitmodules` 파일이 추가되는데, 이는 서브모듈 레포지토리들과 파일 디렉토리의 매핑 정보를 담고 있다.
```shell
git submodule add https://github.com/ultralytics/yolov5.git
```

하위 프로젝트를 추가한 커밋을 만들고 푸쉬한다.
```shell
git add -am "add yolov5 submodule"
git push origin main
```

#### 서브모듈이 포함된 레포지토리 불러오기

서브모듈을 포함하고 있는 레포지토리를 `git clone` 하면, 서브모듈은 디렉토리만 생성될 뿐 안의 콘텐츠는 불러와지지 않는다. 아래 두 서브모듈 커맨드까지 실행해야 clone이 완료된다.

```shell
git clone <main repo>
git submodule init
git submodule update
```

또는, clone 옵션으로 한 번에 서브모듈까지 클론을 끝낼 수도 있다.
```shell
git clone --recurse-submodules https://github.com/ultralytics/yolov5.git
```

# References

https://git-scm.com/book/ko/v2/Git-%EB%8F%84%EA%B5%AC-%EC%84%9C%EB%B8%8C%EB%AA%A8%EB%93%88