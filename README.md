![로고](images/README/로고.png) <-만들면 업데이트

# 📕 Photory

AI 기반 동화책 자동생성 서비스

<br>

## 📆 프로젝트 개요

- **진행 기간**: 2020.10.12 ~ 
- **목표**
  - 사진의 업로드를 통해서 간단하게 이쁜 동화책을 생성하는 웹 서비스 개발
- **계획서**
  - <a href="documentation/계획서/(SSAFY)자율 프로젝트 계획서 양식_A205.pdf">계획서</a>

<br>

## 🐤 프로젝트 소개

 추후 정리

<br>

## 🔧 Tech Stack

<details>
    <summary>Front</summary>
    <ul>
        <li>Vue CLI</li>
        <li>Vuex</li>
        <li>Vuetify</li>
    </ul>
</details>

<details>
    <summary>Back</summary>
    <ul>
        <li>Django</li>
		<li>Flask</li>
        <li>Swagger</li>
        <li>EC2</li>
    </ul>
</details>

<br>

## 📝프로젝트 사용법

Photory 시작 방법입니다.

### Frontend

1. Install NPM packages

```bash
cd vue_client
npm i
```

2. Run server

```
npm run server
```

<br>

### Backend

1. 가상환경 실행 후 진행
2. Install packages

```bash
# 가상환경 먼저 실행 후 진행
cd django_server
pip install -r requirements.txt
```

3. Migration 진행

```
python manage.py makemigrations
python manage.py migrate
```

4. Run server

```
python manage.py runserver
```

<br>

### AI server

1. 가상환경 실행 후 진행
2. Install packages

```bash
# 가상환경 먼저 실행 후 진행
cd flask_server
pip install -r requirements.txt
```

3. Run server

```
python ai_server.py
```

<br>

## ERD

- [ERD 클라우드 주소](https://www.erdcloud.com/d/XM57mdPw6JPgRRYFn)

<br>

## ✨주요 기능

추후 정리

<br>

## 🕛Gantt

```mermaid
gantt
    dateFormat  YYYY-MM-DD
    title       Photory 일정

    section 기획
    기획            :done,    des1, 2020-10-12,3d
    기술 학습(AI)         :done,  des2, after des1, 6d
    목업         :done,  des2, after des1, 3d

    section 프론트엔드
    Vue 기본세팅 :  done, 2020-10-19,1d
    메인페이지   :  done, 2020-10-20, 3d
    로그인 구현  :  done, 2020-10-20, 4d
    Createstory        :active,2020-10-26, 6d
    Mystory          :active,2020-10-26, 6d
    Sharestory    :active,2020-10-26, 6d
    StoryEdit     :active,2020-10-26, 6d

    section 백엔드
    Django 기본세팅               :done, 2020-10-19, 1d
    Login API      :     done, 2020-10-24, 3d
    Story API      :     active, 2020-10-26, 6d
    Member API      :     active, 2020-10-26, 6d
    AI server API      :     active, 2020-11-02, 6d

    section AI서버
    Flask 기본세팅               :done, 2020-10-19, 1d
    AI기술 research      :     done, 2020-10-20, 3d
    AI 구현:      active, 2020-10-23, 10d
    
    section 기타
    통합 점검: active, 2020-11-02, 10d
    UCC제작 : active, 2020-11-09, 7d
    발표준비 :active, 2020-11-09, 7d
```



## 👨‍👩‍👦‍👦팀원

##### **이다현**

- 🐶Github: [@DahyeonL](https://github.com/DahyeonL)

##### **김선민**

- 🐱Github:[@tyhtm3](https://github.com/tyhtm3)

##### **최현우**  

- 🐭Github: [@pica-git](https://github.com/pica-git)

##### **황수현**

- 🐹Blog: [@황수현](https://황수현.site/)

##### **방소윤**

- 🐰Github: [@bbangso](https://github.com/bbangso)

<br>

## 🎞 최종산출물

추후 첨부