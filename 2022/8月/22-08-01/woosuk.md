# TIL

## Flask와 Ngrok 이용해 Google Colab에 ML 추론 서버 배포하기

오늘은 ML 서버를 간단하게 배포해 테스트할 일이 있어서, GPU를 활용할 수 있는 Colab 환경에 Flask로 배포하기로 했다.

Ngrok을 이용하면 기존 서버 코드를 거의 변경하지 않고 빠르게 서버를 퍼블릭 도메인에 배포할 수 있다.

### Dependency 세팅

내가 사용한 Colab 환경에는 기본적으로 Flask 패키지가 설치되어 있다. Ngrok 서비스를 사용하기 위해 필요한 추가 디펜던시를 설치한다.

[Ngrok 홈페이지](https://ngrok.com/)에서 계정을 생성한 후, [dashboard > Authtoken](https://dashboard.ngrok.com/get-started/your-authtoken)을 복사해 아래 `ngrok` 커맨드로 등록해야 정상적으로 Ngrok 호스팅을 사용할 수 있다.

```shell
!pip install flask-ngrok
!pip install pyngrok==4.1.1
!ngrok authtoken '<ngrok auth token>'
```

### Model 불러오기

학습이 완료된 [YOLOv5](https://github.com/ultralytics/yolov5) 모델을 불러와 추론에 활용하기 위해, 공식 레포지토리 코드를 불러온다.

```python
%cd /content
!git clone https://github.com/ultralytics/yolov5.git
%cd yolov5
!pip install -r requirements.txt

import sys
sys.path.append("/content/yolov5")
```

YOLOv5 모델 코어인 `DetectMultiBackend`를 `AutoShape` 클래스로 감싸면, 귀찮은 텐서 변환 없이 `PIL.Image` 객체를 input으로 바로 활용할 수 있다.

```python
import torch
from yolov5.models.common import DetectMultiBackend, AutoShape

def get_model(model_path="/content/train/exp13/weights/best.pt"):

	DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

	model = AutoShape(
		DetectMultiBackend(weights=MODEL_PATH,
						   device=torch.device(DEVICE))
	)

	return model
```

### Flask 추론 서버

본 서버는 HTTP multipart/form-data 콘텐츠 타입으로 이미지를 전송받고, YOLOv5 모델을 거쳐 bounding box 형태의 출력을 반환하는 간단한 추론 서버이다.

Flask request에서 Multipart 데이터를 뽑아내는 방법은 아래와 같다. (Method는 반드시 POST여야 함)

```python
from flask import request
  
app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def file_upload():
	im_file = request.files['img'] 	# request: multipart form data -> extract image data
	...
```

전송받은 jpg 포맷의 이미지를 `PIL.Image` 객체로 읽은 후, YOLOv5 모델에 입력해 결과를 얻는다.
```python
	im_bytes = im_file.read()
	im = Image.open(io.BytesIO(im_bytes))

	results = model(im, size=640)
```

전체 서버 코드는 아래와 같다.
```python
from flask import Flask, url_for, redirect, render_template, request
from flask_ngrok import run_with_ngrok
from werkzeug.utils import secure_filename
from PIL import Image
import os, io

model = get_model()

app = Flask(__name__)
run_with_ngrok(app) 	# starts ngrok when the app runs

@app.route('/upload', methods=['POST'])
def file_upload():

	print("request recieved")
	im_file = request.files['img'] 	# request: multipart form data -> extract image data

	im_bytes = im_file.read()
	im = Image.open(io.BytesIO(im_bytes))

	results = model(im, size=640)

	results.save(save_dir='/content/runs/detect')	 # save yolo result visualization

	return results.pandas().xyxy[0].to_json(orient="records")

if __name__ == '__main__':
	app.run()
```


# Reference

[[Velog] [Flask] 파일 업로드 (File Upload)하기](https://velog.io/@kho5420/Flask-%ED%8C%8C%EC%9D%BC-%EC%97%85%EB%A1%9C%EB%93%9C-File-Upload%ED%95%98%EA%B8%B0)

[[Velog] [오늘의 배움] 045 flask.request](https://velog.io/@sangmin7648/%EC%98%A4%EB%8A%98%EC%9D%98-%EB%B0%B0%EC%9B%80-045)

[YOLOv5 repository > models/common.py](https://github.com/ultralytics/yolov5/blob/master/models/common.py)