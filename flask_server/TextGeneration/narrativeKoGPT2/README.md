# StoryGenerationKoGPT2

## 1. 소개

[SKT-AI의 KoGPT2](https://github.com/SKT-AI/KoGPT2)와 [NarrativeKoGPT2](https://github.com/shbictai/narrativeKoGPT2), 인공지능 오픈소스로는 pytorch를 이용해 텍스트를 학습하는 gpt-2 모델 기존 NarrativeKoGPT2의 대부분 이용하여 학습하였으며 데이터 전처리와 미세한 수정사항이 들어가있다. 데이터 전처리는 자기가 원하는 데이터를 전처리하되 batch 하나당 \<s> ~내용 \<s>의 1024byte 이하의 데이터를 넣어야한다. 후에 발전된 샘플링 방법이랑 코드 업데이트 예정

## 2. 학습 모델

https://drive.google.com/drive/folders/1TiB6P_z1VQf0nvR4gZCD3GG-Bp20Fox-?usp=sharing

narrativeKoGPT2_checkpoint_tokenized_ver3_bat1_epoch495.tar 모델이 가장 최신 버전입니다.
narrativeKoGPT2_checkpoint_tokenized_ver3_bat1_epochxxx.tar 버젼 모델이 정상 작동하며 epoch495버젼은 과적합된 버전으로서 300~400 사이의 모델을 사용하는 것이 좋습니다.

## 3. Install

##### Development setting

```sh
python == 3.7.5
pip == 20.2.4
cuda == 10.1 update2
cudnn == 7.6.5 + 8.0.2  ## 우선 7.6.5버젼을 cuda 라이브러리에 넣은 후 8.0.2버젼을 다운받아서 cuda 라이브러리에 넣는다.
```

```sh
pip install jupyterlab
pip install -r requirements.txt

```

**\*** 윈도우에서는 torch 1.4.0이 설치가 안 되는 오류가 있습니다. 가급적 colab에서 모델을 학습하고 소설 생성하는 모듈을 이용할 때에 torch 1.5.0을 다운받아서 사용 하는 것을 권합니다.

## 4. 모델 학습 사용법

cmd에서 jupyter-lab 명령어를 사용해서 jupyter lab에 접속해 NarrativeKoGPT2_photory.ipynb에 접속한다.
NarrativeKoGPT2_photory.ipynb에서 save_path를 원하는 폴더로 설정하고 data_file_path 변수에 정제한 텍스트 데이터 경로를 지정한 후 실행.

## 5. 소설 생성 사용법

cmd에서 jupyter-lab 명령어를 사용해서 jupyter lab에 접속해 NovelGenerator_photory.ipynb에 접속한다.
NovelGenerator_photory.ipynb의 load_path 변수에 "checkpoints/'사용하고자 하는 모델'"을 입력 후 실행.
다운받은 모델은 checkpoints 폴더에 넣는다.

## 6. 라이센스

modified MIT 라이센스

## 7. 참조

- [SKT-AI/KoGPT2](https://github.com/SKT-AI/KoGPT2)
- [NarrativeKoGPT2](https://github.com/shbictai/narrativeKoGPT2)
