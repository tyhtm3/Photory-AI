# StoryGenerationKoGPT2

## 1. 소개

[SKT-AI의 KoGPT2](https://github.com/SKT-AI/KoGPT2)와 [NarrativeKoGPT2](https://github.com/shbictai/narrativeKoGPT2), 인공지능 오픈소스로는 pytorch를 이용해 텍스트를 학습하는 gpt-2 모델 기존 NarrativeKoGPT2의 대부분 이용하여 학습하였으며 데이터 전처리와 미세한 수정사항이 들어가있다. 데이터 전처리는 자기가 원하는 데이터를 전처리하되 batch 하나당 <s> ~내용 <s>의 1024byte 이하의 데이터를 넣어야한다. 후에 발전된 샘플링 방법이랑 코드 업데이트 예정

## 2. 학습 모델

https://drive.google.com/drive/folders/1TiB6P_z1VQf0nvR4gZCD3GG-Bp20Fox-?usp=sharing

narrativeKoGPT2_checkpoint_tokenized_ver3_bat1_epoch495.tar 모델이 가장 최신으로 정상 작동하는 모델이다

## 3. Install

설치 업데이트 예정

## 4. 사용법

NovelGenerator_photory.ipynb의 load_path 변수에 "checkpoints/'사용하고자 하는 모델'"을 입력 후 실행.
모델은 checkpoints 폴더에 넣는다.

## 5. 라이센스

modified MIT 라이센스

## 5. 참조

- [SKT-AI/KoGPT2](https://github.com/SKT-AI/KoGPT2)
- [NarrativeKoGPT2](https://github.com/shbictai/narrativeKoGPT2)
- [likejazz/korean-sentence-splitter](https://github.com/likejazz/korean-sentence-splitter)
