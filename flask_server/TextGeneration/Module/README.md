## 실행법

### environment

```sh
python == 3.7.5
pip == 20.2.4
cuda == 10.1 update2
cudnn == 7.6.5 + 8.0.2  ## 우선 7.6.5버젼을 cuda 라이브러리에 넣은 후 8.0.2버젼을 다운받아서 cuda 라이브러리에 넣는다.
```

### INSTALL

```sh
!pip install -r requirements.txt
```

### 모델 다운로드

https://drive.google.com/drive/folders/1TiB6P_z1VQf0nvR4gZCD3GG-Bp20Fox-?usp=sharing <-- 학습한 모델

narrativeKoGPT2_checkpoint_tokenized_ver3_bat1_epoch300.tar 파일을 checkpoints 폴더에 넣는다.

#### 실행

Test.py 파일 참고
