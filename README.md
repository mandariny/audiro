# Audi:ro (웹 IoT 음악 공유 플랫폼)

## 0. 프로젝트 개요

- 음악을 통해 나와 음악취향이 비슷한 다른 사람을 연결해주는 공간 플랫폼

- 저희 어디로 팀은 유튜브에서 '어떤 노래 듣고 계세요?'와 같은 컨텐츠가 유행하는 것에서 착안해 특정 공간에서 가장 많이 듣는 노래, 다른 사람이 추천한 노래, 자신이 듣고 있는 추천하고 싶은 노래를 공유하는 서비스를 개발했습니다. 

- 웹 IoT 서비스로 기기를 이용해 노래와 함께 자신의 감상을 그림 엽서로 남길 수 있습니다. 또한 자신과 음악 취향이 맞는 사람에게 답장을 남기고 메신저로 연락하며 새로운 커넥션을 만들어갈 수 있습니다.

## 1. 팀원 및 역할
- 이가옥 - 팀장, 웹 백엔드, 웹 프론트엔드, 배포 
- 김성환 - 웹 백엔드
- 김호성 - 웹 프론트엔드
- 신승호 - 임베디드 IoT 기기 개발
- 윤소희 - 웹 백엔드, 웹 프론트엔드, DB 구성
- 조현영 - 임베디드 IoT 기기 개발

## 2. 프로젝트 진행 기간
- 2023.01.09 ~ 2023.02.17
- 리팩토링 진행중

## 3. 주요 기능 소개
### 키오스크-웹 연동

<img src="https://github.com/mandariny/audiro/blob/master/docs/service_gif/%ED%82%A4%EC%98%A4%EC%8A%A4%ED%81%AC-%EB%A1%9C%EA%B7%B8%EC%9D%B8.gif?raw=true" width=400>

### 엽서 작성 및 노래 추천

<img src="https://github.com/mandariny/audiro/blob/master/docs/service_gif/%ED%82%A4%EC%98%A4%EC%8A%A4%ED%81%AC-%EC%97%BD%EC%84%9C%EC%9E%91%EC%84%B1.gif?raw=true" width=400>

### 엽서 답장 및 메신저

### 특정인에게 그림 엽서 남기기

### 엽서 조회

## 4. 기술 스택
### BE
- Spring Boot
- Spring Data JPA
- Spring Security, JWT
- WebSocket, STOMP
- Swagger

### FE
- React.js
- Figma
- Styled Components

### Embedded
- Raspberry PI
- Python
- PyQT

### Database
- MySQL
- Redis

### ETC
- AWS EC2
- Nginx

### 협엽
- GitLab
- Jira

## 5. 프로젝트 설계
### 시스템 아키텍처

<img src="https://github.com/mandariny/audiro/blob/master/docs/Audiro-System%20Architecture.jpg?raw=true" width=500>

### [기능 명세서](https://www.notion.so/6725051b35fe4d6f90004f69f2aaf762?pvs=4)

<img src="https://github.com/mandariny/audiro/blob/master/docs/%EA%B8%B0%EB%8A%A5%EB%AA%85%EC%84%B8%EC%84%9C.jpg?raw=true" width=500>

### 와이어프레임

<img src="https://github.com/mandariny/audiro/blob/master/docs/%EC%99%80%EC%9D%B4%EC%96%B4%ED%94%84%EB%A0%88%EC%9E%84-%ED%82%A4%EC%98%A4%EC%8A%A4%ED%81%AC.jpg?raw=true" width=500>

> 키오스크

<img src="https://github.com/mandariny/audiro/blob/master/docs/%EC%99%80%EC%9D%B4%EC%96%B4%ED%94%84%EB%A0%88%EC%9E%84-%EC%9B%B9.jpg?raw=true" width=500>

> 웹

### [ERD](https://www.erdcloud.com/d/CoFy4Csr4yipdPoPE)

<img src="https://github.com/mandariny/audiro/blob/master/docs/ERD.jpg?raw=true" width=500>

### [API 명세서](https://www.notion.so/API-8dfd2fb3b01e45ef9d695bc092919932?pvs=4)

<img src="https://github.com/mandariny/audiro/blob/master/docs/%EB%AA%85%EC%84%B8%EC%84%9C1.jpg?raw=true" width=200>

> 분류

<img src="https://github.com/mandariny/audiro/blob/master/docs/%EB%AA%85%EC%84%B8%EC%84%9C2.jpg?raw=true" width=500>

> 세부 항목 예시

<img src="https://github.com/mandariny/audiro/blob/master/docs/%EB%AA%85%EC%84%B8%EC%84%9C3.jpg?raw=true" width=500>

> 세부 내용 예시

## 개발 과정
[노션에서 확인하기](https://www.notion.so/A402-2d611e98012743b9ada73afc8e9f9e79?pvs=4)
