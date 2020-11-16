***
# Default Jenkins Setting

## Dev
#### Flatform
AWS(ubuntu18.04)

#### VM
Docker


***
## Docker 설치 <sup id="a1">[1](#f1)</sup>
###### 1. 이번 버전의 도커 관련 패키지들을 삭제한다

```bash
sudo apt-get remove docker docker-engine docker.io containerd runc
```





###### 2. 도커 엔진 설치

최신 버전 설치
```bash
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

특정 버전 설치
```bash
apt-cache madison docker-ce

  docker-ce | 5:18.09.1~3-0~ubuntu-xenial | https://download.docker.com/linux/ubuntu  xenial/stable amd64 Packages
  docker-ce | 5:18.09.0~3-0~ubuntu-xenial | https://download.docker.com/linux/ubuntu  xenial/stable amd64 Packages
  docker-ce | 18.06.1~ce~3-0~ubuntu       | https://download.docker.com/linux/ubuntu  xenial/stable amd64 Packages
  docker-ce | 18.06.0~ce~3-0~ubuntu       | https://download.docker.com/linux/ubuntu  xenial/stable amd64 Packages
  ...
sudo apt-get install docker-ce=<VERSION_STRING> docker-ce-cli=<VERSION_STRING> containerd.io
```

><b id="f1"><sup>1</sup></b> 참고 : https://docs.docker.com/engine/install/ubuntu/ [↩](#a1)<br>


***
## Jenkins 설치
###### 1. Docker를 통한 Jenkins 이미지 받기

```bash
sudo docker pull jenkins/jenkins:lts
```



###### 2. Jenkins 이미지를 컨테이너로 실행



```bash
docker run -d -p 8181:8080 -v /jenkins:/var/jenkins_home --name jm_jenkins -u root jenkins/jenkins:lts
// 위 명령어 옵션설명 
-d	detached mode 흔히 말하는 백그라운드 모드
-p	호스트와 컨테이너의 포트를 연결 (포워딩)
-v	호스트와 컨테이너의 디렉토리를 연결 (마운트)
–name	컨테이너 이름 설정
-u 실행할 사용자 지정

맨 마지막 jenkins/jenkins:lts 는 실행할 이미지의 레포지토리 이름이며 만약 이미지가 없을 경우 이미지를 docker hub 에서 땡겨오므로 주의한다.
```







###### 3. k3a205.p.ssafy.io:8181로 접속해서 추가설치를 한다.

처음에 접속하면 Admin password를 요구한다. __/var/jenkins_home/secrets/initialAdminPassword__를 통해 확인한다.
혹은
```bash
sudo docker logs [컨테이너 이름]
```
을 통해서도 확인가능하다.

![image1](./image/jenkins_admin_password.JPG)

sudo docker logs의 내용


패스워드를 페이지에서 입력하면 플러그인 설치 창이 나온다.
![image2](./image/jenkins_plugin_install.JPG)

Install suggested plugins를 선택하면 기본적인 플러그인들을 설치한다.

플러그인 설치 후 초기 계정을 생성하고 접속한다.


###### 4. Jenkins에 접속하여 두 가지 플러그인(gitlab, publish over SSH)를 더 설치한다. 설치는 Jenkins 관리 - 플러그인 관리 에서 할 수 있다.
![image3](./image/jenkins_plugin_manage.JPG) <br>

![image4](./image/jenkins_plugin_manage_gitlab.JPG) <br>

![image5](./image/jenkins_plugin_manage_ssh.JPG) <br>

검색은 설치 가능 탭에서 검색하여 설치한다.




***
## gitlab - Jenkins 간 트리거 구축

###### 1. Jenkins 상에서 새로운 item - Freestyle project를 클릭하여 새 프로젝트를 생성한다.

###### 2. 프로젝트에 접속하고 구성 탭에 들어간 후 빌드 유발 탭에 들어가 고급 버튼을 클릭한다. 이 때 GitLab webhook URL을 기억한다..

![image6](./image/jenkins_setting_1.JPG) <br>

###### 3. Secret token을 generate하여 복사하고 기억한다.

![image7](./image/jenkins_setting_2.JPG) <br>

###### 4. GitLab의 연동하고자 하는 프로젝트에 들어가서 Settings - Integrations 항목에 들어간다. URL 란에 아까 기억했던 GitLab webhook URL을 입력하고 Secret Token 란에 아까 generate했던 값을 적어 넣는다. Push Events 란에 트리거가 유발되는 브랜치 이름을 적어 넣는다. 우리 프로젝트는 develop에서 활발히 이뤄지므로 develop으로 설정했다. 적어넣은 후 밑의 Add Webhook 버튼을 눌러 추가한다.


![image8](./image/jenkins_setting_3.JPG) <br>



###### 5. 푸쉬 이벤트를 테스트해보고 정상이면 계속 진행한다. 밑의 사진의 Push Events 로 테스트할 수 있다.

![image9](./image/jenkins_setting_4.JPG) <br>

성공하면 http 200 응답을 돌려받는다. 

![image10](./image/jenkins_setting_5.JPG) <br>



###### 6. 다시 Jenkins의 구성 탭에 들어가 소스 코드 관리로 들어간다. Git을 선택하고 Repository URL은 깃랩 프로젝트 URL, Branch Specifier은 빌드할 브랜치를 선택한다.(사진 상과 같이 입력한다.) 그리고 Credentials을 생성한다. 

![image11](./image/jenkins_setting_6.JPG) <br>


Credentials를 생성할 때 Kind는 Username with password를 선택하고 Scope는 Global을 선택한다. 나머지는 공백으로 놔둬도 되지만 ID는 GitLab ID, Password는 GitLab Password를 적어넣고 Add 버튼을 누른다.
누르고 빠져나온 뒤 Apply와 저장 버튼을 누른다.

![image12](./image/jenkins_setting_7.JPG) <br>