
## Git

### commit

- ```bash
  이슈번호/브랜치이름 : 내용 (형식자유)
  ```
  
- ```bash
  ex)
  S0234165-1/hotfix : Update README.md
  ```

<br>

### branch

​	 master

​			|

​	  develop

​			|

​	각각 기능단위

### merge 순서
```bash
$ git pull origin devleop # 리모트 저장소로부터 pull
$ git branch [브랜치이름] # 브랜치 생성
$ git checkout [브랜치이름] # 브랜치 이동
--> 코드 작성...
$ git add .
$ git commit -m "commit 메시지"
$ git push origin [브랜치이름] # 리모트 저장소에 새로운 브랜치로 push
--> gitlab 사이트접속후 merge request # merge request시 브랜치 삭제 버튼 반드시 누르기
$ git checkout develop
$ git branch -d [브랜치이름] # 로컬 저장소 브랜치 삭제
$ git pull origin develop # 다시 처음부터 반복
```

<br>
