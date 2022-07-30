## Intro

> **원티드X프리온보딩 랩큐 팀 프로젝트를 학습 목적으로 처음부터 다시 구현한 레포지토리입니다.**

- 본 프로젝트에서 요구하는 서비스는 공공 데이터를 전달하는 REST API입니다.
- 본 서비스는 Open API 방식의 공공데이터를 수집 및 가공하여 클라이언트에게 새로운 데이터를 전달합니다.

<br>

> **Index**
- [Team Project](#team-project)
- [Environments](#environments)
- [Personal Project](#personal-project)
- [Etc](#etc)

<br>
<hr>

## Team Project

> **팀 프로젝트 소개**
- #### 👉 [팀 프로젝트 레포지토리 주소](https://github.com/F5-Refresh/labq)
  ```
   > 과제 제출기업: 랩큐(labq)
   > 팀명: F5-Refresh
   > 팀원: 5명
   > 프로젝트 기간: 22.06.29 ~ 22.07.01
  ```
<br>
<hr>

## Environments

<br>
<div align="center">
<img src="https://img.shields.io/badge/Python-blue?style=plastic&logo=Python&logoColor=white"/>
<img src="https://img.shields.io/badge/Django-092E20?style=plastic&logo=Django&logoColor=white"/>
<img src="https://img.shields.io/badge/Django Rest Framework-EE350F?style=plastic&logo=Django&logoColor=white"/>
</div>

<br>
<div align="center">
<img src="https://img.shields.io/badge/AWS EC2-FF9900?style=plastic&logo=Amazon AWS&logoColor=white"/>
<img src="https://img.shields.io/badge/Docker-%230db7ed.svg?style=plastic&logo=Docker&logoColor=white"/>
<img src="https://img.shields.io/badge/nginx-%23009639.svg?style=plastic&logo=NGINX&logoColor=white"/>
<img src="https://img.shields.io/badge/gunicorn-EF2D5E?style=plastic&logo=Gunicorn&logoColor=white"/>
<img src="https://img.shields.io/badge/Swagger-%23Clojure?style=plastic&logo=swagger&logoColor=white"/>
</div>

<br>
<hr>


## Personal Project

> **Period**
- #### ⚡️ 22.07.06 ~ 22.07.16

<br>

> **Analysis**
- #### 📌 필수 구현사항
  - REST API 기능
    ```
    * 서울시 하수관로 수위 현황과 강우량 정보를 수집합니다.(데이터 수집)
    * 공공데이터의 출력 값 중 GUBN_NAM과 GU_NAME을 기준으로 정보를 결합합니다.(데이터 결합)
    * 새롭게 가공한 데이터를 클라이언트에게 JSON 형태로 전달합니다.
    ```
  - 클라이언트 기능
    ```
    * GUBN(구분코드)를 명시해서 REST API를 호출할 수 있습니다.
    * 서버에서 전송받은 결과를 출력합니다.
    ```
  - 공공 데이터 수집 및 가공
    - 👉 [서울시 하수관로 수위 공공데이터](https://data.seoul.go.kr/dataList/OA-2527/S/1/datasetView.do) 
      ```
      > 데이터 출력형태
      
      [
          {
              "IDN": "01-0004",
              "GUBN": "01",
              "GUBN_NAM": "종로",
              "MEA_YMD": "2022-06-29 01:00:00.0",
              "MEA_WAL": 0.12,
              "SIG_STA": "통신양호"
          },
          {
              "IDN": "01-0003",
              "GUBN": "01",
              "GUBN_NAM": "종로",
              "MEA_YMD": "2022-06-29 01:00:00.0",
              "MEA_WAL": 0.12,
              "SIG_STA": "통신양호"
          },
        
          ... (중략)
        
          {
              "IDN": "01-0002",
              "GUBN": "01",
              "GUBN_NAM": "종로",
              "MEA_YMD": "2022-06-29 01:59:00.0",
              "MEA_WAL": 0.0,
              "SIG_STA": "통신양호"
          },
          {
              "IDN": "01-0001",
              "GUBN": "01",
              "GUBN_NAM": "종로",
              "MEA_YMD": "2022-06-29 01:59:00.0",
              "MEA_WAL": 0.56,
              "SIG_STA": "통신양호"
          }
      ]
      ```
    - 👉 [서울시 강우량 공공데이터](https://data.seoul.go.kr/dataList/OA-1168/S/1/datasetView.do)
      ```
      > 공공데이터 출력형태
      
      [
          {
              "RAINGAUGE_CODE": 1002.0,
              "RAINGAUGE_NAME": "부암동",
              "GU_CODE": 110.0,
              "GU_NAME": "종로구",
              "RAINFALL10": "2.5",
              "RECEIVE_TIME": "2022-06-29 20:19"
          },
          {
              "RAINGAUGE_CODE": 1001.0,
              "RAINGAUGE_NAME": "종로구청",
              "GU_CODE": 110.0,
              "GU_NAME": "종로구",
              "RAINFALL10": "0.5",
              "RECEIVE_TIME": "2022-06-29 20:19"
          },
          
          ... (중략)
          
          {
              "RAINGAUGE_CODE": 1104.0,
              "RAINGAUGE_NAME": "서소문",
              "GU_CODE": 111.0,
              "GU_NAME": "중구",
              "RAINFALL10": "0",
              "RECEIVE_TIME": "2022-06-29 19:29"
          },
          {
              "RAINGAUGE_CODE": 1101.0,
              "RAINGAUGE_NAME": "중구청",
              "GU_CODE": 111.0,
              "GU_NAME": "중구",
              "RAINFALL10": "0",
              "RECEIVE_TIME": "2022-06-29 19:29"
          }
      ]
      ```
 
- #### 📌 참고사항
  - 개발 언어는 Python으로 제한합니다.
  - 결과는 JSON 형식이어야 합니다.
  - 필요한 경우 요구사항을 추가로 정의해서 개발해주세요.
  - 객체지향 방식으로 개발하면 가산점이 있습니다.
  - 소스에 docstring을 넣어주세요.
 
<br>

> **Development**
- #### 🔥 프로젝트 구현기능
  - REST API 기능
    ```
    > Open API 방식의 공공데이터를 수집/가공하여 클라이언트에게 새로운 데이터를 전달하는 기능입니다.

    - 데이터 수집
      * 서울시 구(지역) 이름은 필수 값입니다.(query string)
      * 서울시의 구(지역 )이름을 받으면 구분코드로 변경하여 하수관로 수위 공공데이터를 요청합니다.
      * 하수관로 수위 공공데이터에서 구(지역) 이름을 추출하여 해당 지역의 강우량 공공데이터를 요청합니다.
    
    - 데이터 가공
      * 클라이언트 요청 시점을 기준으로 최근 1시간의 해당 지역 하수관로 수위 평균값을 산출합니다.
      * 클라이언트 요청 시점을 기준으로 최근 1시간의 해당 지역 강우량 총 합게를 산출합니다.
      * 단, 강우량 데이터는 해당 지역의 RAINGAUGE_NAME(강우량 계량기)별로 총 합계를 산출합니다.
      * 새롭게 산출된 데이터를 종합하여 클라이언트에게 JSON 형식으로 제공합니다.
      
    - 데이터 반환형태
      (종로구 예시)
      
      {
          "gu_name": "종로",
          "avg_water_level": 0.07,
          "raingauge_info" : [
              {
                  "raingauge_name": "종로구청",
                  "sum_rain_fall": 0
              },
              {
                  "raingauge_name": "부암동",
                  "sum_rain_fall": 0
              }
          ]
      }
    ```
  - 클라이언트 기능
    ```
    > 서울시의 구(지역) 이름을 선택하여 공공데이터를 호출할 수 있습니다.
    
    * Swagger UI를 클라이언트 기능으로 활용했습니다.
    * 서울시의 구(지역) 이름은 필수로 입력해야 하며, 구분코드가 아닌 지역명을 입력합니다.
    * 해당 API를 호출하기 위한 사용자 인증/인가 절차는 없습니다.
    ```
     
<br> 

> **API Docs**
- #### 🌈 API 명세서
  |ID|Feature|Method|URL|
  |---|----------|----|----|
  |1|Open API 형식의 서울시 공공데이터 반환|GET|api/seoul/sewerlevel-rainfall|
  
  
- #### ✨ Swagger UI
  #### ```✔️ Open API 형식의 서울시 공공데이터 반환``` 
  <img width="1000px" alt="스크린샷 2022-07-30 13 47 10" src="https://user-images.githubusercontent.com/89829943/181872841-4f75d0ce-a512-43c3-b91b-92f4e0d55106.png">
  <img width="1000px" alt="스크린샷 2022-07-30 13 47 33" src="https://user-images.githubusercontent.com/89829943/181872846-db40426c-7b95-4793-b406-c335c37b20bf.png">


<br> 

> **Deploy**
- #### 🏖 프로젝트 배포
  #### Docker, Nginx, Gunicorn을 사용하여 AWS EC2 서버에 배포했으며, 비용 등의 이유로 현재는 배포를 중단했습니다.
  <img width="1000px" alt="스크린샷 2022-07-30 13 51 54" src="https://user-images.githubusercontent.com/89829943/181874772-9fe95718-089f-4dc9-9e46-f58acac32d98.png">



<br> 

> **Test**
- #### 🚦 테스트코드 작성
  #### 전체 테스트코드: 29 cases
  
  |ID|Feature|Method|Success cases|Fail cases|
  |---|----|----|----|----|
  |1|Open API 형식의 서울시 공공데이터 반환|GET|25 case|4 cases|
  <img width="1000px" alt="스크린샷 2022-07-30 12 21 29" src="https://user-images.githubusercontent.com/89829943/181872390-d955cbd0-a607-4595-9cd2-942da5bfe264.png">

  #### 테스트 커버리지: 98%
  <img width="1000px" alt="스크린샷 2022-07-30 12 22 53" src="https://user-images.githubusercontent.com/89829943/181872405-67f19b93-68d7-4f3f-a43e-91b5cc14e799.png">

- #### ⛱ 테스트 모킹(mocking)
  #### patch 데코레이터를 사용하여 외부서비스(Open API)에 의존하지 않고 독립적으로 실행 가능한 테스트코드를 작성했습니다.
    ```
    > ex1) 서울시 하수관로 수위 Open API 반환 데이터 mocking
    
    @patch('core.utils.sewer_pipe.requests')
      def test_fail_seoul_data_due_to_sewer_pipe_open_api_error(self, mocked_requests):

          class MockedResponse:
              data = {
                  'DrainpipeMonitoringInfo':
                      {'RESULT': 
                          {'CODE': 'ERROR-500',\
                              'MESSAGE': '서버 오류입니다. 지속적으로 발생시 열린 데이터 광장으로 문의(Q&A) 바랍니다.'
                      }
                  }
              }
              content = json.dumps(data)

          mocked_requests.get = mock.MagicMock(return_value = MockedResponse())
    ```
    ```
    > ex2) 서울시 강우량 Open API 반환 데이터 mocking
    
    @patch('core.utils.rainfall.requests')
      def test_fail_seoul_data_due_to_rainfall_open_api_error(self, mocked_requests):

          class MockedResponse:
              data = {
                  'ListRainfallService':
                      {'RESULT': 
                          {'CODE': 'ERROR-500',\
                              'MESSAGE': '서버 오류입니다. 지속적으로 발생시 열린 데이터 광장으로 문의(Q&A) 바랍니다.'
                      }
                  }
              }
              content = json.dumps(data)

          mocked_requests.get = mock.MagicMock(return_value = MockedResponse())
    ```

<br> 

> **Issue**
- #### ⏰ 프로젝트 일정관리
  #### 프로젝트 진행사항을 칸반보드와 이슈티켓으로 관리했습니다.
  <img width="1000px" alt="스크린샷 2022-07-30 13 31 55" src="https://user-images.githubusercontent.com/89829943/181872461-df73165b-f9f7-451a-99e3-bafcb4378393.png">


<br>
<hr>

## Etc

> **Guides**
- #### ⚙️ 프로젝트 설치방법
  #### ```✔️ 로컬 개발 및 테스트용```
  
  1. 해당 프로젝트를 clone하고, 프로젝트 폴더로 이동합니다.
  <br>
  
   ```
   git clone https://github.com/pasitoapasito/wantedP.O-labq.git
   cd project directory
   ```
  
  2. 가상환경을 만들고, 프로젝트에 필요한 python package를 다운받습니다.
  <br>
  
  ```
  conda create --name project-name python=3.9
  conda activate project-name
  pip install -r requirements.txt
  ```
  
  3. manage.py 파일과 동일한 위치에서 환경설정 파일을 만듭니다.
  <br>
  
  ```
  ex) .env file 
  
  ## general ##
  DEBUG         = True
  ALLOWED_HOSTS = ALLOWED_HOSTS
  SECRET_KEY    = SECRET_KEY
  OPEN_API_KEY  = OPEN_API_KEY
  ```
  
  4. 개발용 서버를 실행합니다.
  <br>
  
  ```
  python manage.py runserver 0:8000
  ```

  #### ```✔️ 배포용```
  1. 배포용 서버에서 해당 프로젝트를 clone하고, 프로젝트 폴더로 이동합니다.
  <br>
  
  ```
  git clone https://github.com/pasitoapasito/wantedP.O-labq.git
  cd project directory
  ```
  
  2. manage.py 파일과 동일한 위치에서 도커 환경설정 파일을 만듭니다.
  <br>
  
  ```
  ex) .env file 
  
  ## general ##
  DEBUG         = True
  ALLOWED_HOSTS = ALLOWED_HOSTS
  SECRET_KEY    = SECRET_KEY
  OPEN_API_KEY  = OPEN_API_KEY
  ```
  
  3. docker-compose 명령을 사용하여 Nginx와 Django 서버 컨테이너를 실행시킵니다.
  <br>
  
  ```
  docker-compose -f ./docker-compose.yml up (-d)
  ```

<br>

> **Structure**
- #### 🛠 프로젝트 폴더구조

  ```
  📦api
   ┣ 📂migrations
   ┃ ┗ 📜__init__.py
   ┣ 📜__init__.py
   ┣ 📜admin.py
   ┣ 📜apps.py
   ┣ 📜models.py
   ┣ 📜serializers.py
   ┣ 📜tests.py
   ┣ 📜urls.py
   ┗ 📜views.py
   📦config
   ┗ 📂nginx
   ┃ ┗ 📜nginx.conf
   📦core
   ┣ 📂migrations
   ┃ ┗ 📜__init__.py
   ┣ 📂utils
   ┃ ┣ 📜api_settings.py
   ┃ ┣ 📜rainfall.py
   ┃ ┗ 📜sewer_pipe.py
   ┣ 📜__init__.py
   ┣ 📜admin.py
   ┣ 📜apps.py
   ┣ 📜models.py
   ┣ 📜tests.py
   ┗ 📜views.py
   📦labq
   ┣ 📜__init__.py
   ┣ 📜asgi.py
   ┣ 📜settings.py
   ┣ 📜urls.py
   ┗ 📜wsgi.py
   ┣ 📜.env
   ┣ 📜.gitignore
   ┣ 📜db.sqlite3
   ┣ 📜docker-compose.yml
   ┣ 📜Dockerfile
   ┣ 📜manage.py
   ┣ 📜README.md
   ┗ 📜requirements.txt
  ```
