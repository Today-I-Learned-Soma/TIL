# TIL

## Linux `nohup`을 통한 쉘 백그라운드 실행

### `nohup` 이란?

Linux에서 쉘 커맨드를 실행하면, 현재 세션(SSH 세션 등)과 연결을 끊었을 때 내가 실행한 프로세스가 모두 종료된다. `nohup`은 이러한 프로세스의 종료를 막는 기능으로, HUP(hangup) 신호를 무시하라는 의미이다 (no hangup).

```shell
$ nohup shell_script.sh
```

위와 같이 프로세스를 실행하면, 프로세스에서 출력한 아웃풋들은 `nohup.out`이라는 파일로 출력된다.

### `&` 을 이용한 백그라운드 실행 & 종료

쉘 커맨드 뒤에 `&`을 붙이면, 백그라운드 실행이 되어 곧바로 다른 커맨드를 이어 실행할 수 있다. 보통 딥러닝 모델 학습과 같이 오랫동안 실행시킬 작업을 할 때, 학습 서버에 SSH로 접속해서 `nohup`과 `&`를 세트로 쓰는 경우가 많다. 

```shell
$ nohup train.py --train-path=./data/train &
```

백그라운드 실행 중인 프로세스를 종료하려면, `ps` 커맨드를 통해 해당 프로세스의 코드를 찾아 `kill` 한다.

```shell
$ ps -ef | grep train.py
$ kill -9 <ps-code>
```

### `nohup`의 입출력 지정하기

`nohup`으로 실행한 프로세스의 출력은 기본적으로 `nohup.out`에 저장된다. 입출력 파일을 다른 곳에 저장하기 위해서는, 다음과 같이 리다이렉션을 할 수 있다. `&1`은 정상 출력을, `&2`는 에러 출력을 지정한다.

```shell
$ nohup shell_script.sh 1 > out.log 2 > err.log &
```

또는, 아래와 같이 에러도 같은 곳으로 출력할 수 있다.

```shell
$ nohup shell_script.sh > out.log 2 > &1 &
```

이외에도 `nohup` 입출력 리다이렉션이 필요한 상황이 발생할 수 있다. 바로 remote SSH 세션에서 프로세스를 실행하고 로그오프 할 때이다. `nohup`으로 실행하면 로그오프 시 HUP 신호가 가는 것을 막을 수 있지만, 오히려 세션이 백그라운드 데이터를 잃는 것을 막고자 로그오프가 되지 않는 (hang) 상황이 발생하는 것이다. 이 때 해결법은, 프로세스의 입출력을 모두 리다이렉션하는 것이다.

```shell
$ nohup ./myprogram > foo.out 2 > foo.err < /dev/null &
```


# References

https://joonyon.tistory.com/entry/%EC%89%BD%EA%B2%8C-%EC%84%A4%EB%AA%85%ED%95%9C-nohup-%EA%B3%BC-%EB%B0%B1%EA%B7%B8%EB%9D%BC%EC%9A%B4%EB%93%9C-%EB%AA%85%EB%A0%B9%EC%96%B4-%EC%82%AC%EC%9A%A9%EB%B2%95

https://ko.wikipedia.org/wiki/Nohup