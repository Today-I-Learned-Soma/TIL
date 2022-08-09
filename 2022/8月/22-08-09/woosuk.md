# TIL

## Anaconda 가상환경 Export & Import

Anaconda environment를 통해 간신히 맞춘 파이썬 패키지 디펜던시들을 yaml 파일로 저장해 놓으면, 다른 환경으로 옮기거나 배포를 할 때 큰 노가다(?)를 절약할 수 있다.

```shell
conda activate <conda env>
conda env export > conda_environment.yaml
```

Export한 yaml 파일을 통해 env를 생성하는 방법은 다음과 같다.

```shell
conda env create -f conda_environment.yaml
```


다만, 이렇게 export 할 경우 해당 env에 있는 디펜던시를 모두 기록하기 때문에, OS-specific 한 패키지도 포함될 가능성이 있다. 가능하면 배포 타겟이 될 OS와 진작에 같은 환경에서 작업하는 게 좋겠다.