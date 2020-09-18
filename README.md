# readmExample

> 리드미 양식입니다. 꼭 따라야 할 필요는 없지만 뭘 넣을 지 고민된다면 참고해주세요

## 목차
- [개요](#개요)
- [기능](#기능)
- [유사 서비스](#유사-서비스) 
- [향후 전망](#향후-전망)
- [기술 스택](#기술-스택)
- [기술 설명](#기술-설명)
	- [ERD](#erd)
	- [디렉토리 구조도](#디렉토리-구조도)
	- [기타](#기타)
- [테스트 방법](#테스트-방법)

## 개요
> 프로젝트를 간략하게 설명해주세요  
> 프로젝트를 개발하게 된 동기도 들어가 있으면 좋습니다.

개요: 아이의 속마음을 들어보는 서비스 



## 기능
> 프로젝트의 기능들을 설명해주세요  
> 스크린샷이나 gif등으로 한눈에 볼 수 있게 하면 더 좋습니다

## 유사 서비스
> 프로젝트와 유사한 서비스들이 있다면 소개해 주고 여러분의 프로젝트 만의 차이점을 기술해주세요

## 향후 전망
> 부득이한 사정으로 프로젝트에 구현하지는 못했지만 보완할 점이나 추가할 점이 있다면 적어주세요

## 기술 스택
> 프로젝트를 구현 할 때 사용한 기술들을 적어주세요

![KakaoTalk_20200917_160232066](README.assets/KakaoTalk_20200917_160232066.png)

## 기술 설명

### ERD
> DB 및 백엔드를 구현할 때 ERD를 그려보고 리드미에 남겨주세요

![인사이드키즈 (4)](README.assets/인사이드키즈 (4).png)

### 디렉토리 구조도
> 폴더 구조가 어떻게 되는지 폴더, 파일별 역할들을 간략하게 적어주세요  
> 너무 자세히 적을 필요는 없습니다

AI/ : AI 테스트

backend/ : django설정

accounts/, contents/ : django app

frontend/ : vue.js 프로젝트

deployments: 배포 설정 파일



### 기타
> 이외에도 프로젝트를 이해하기 위해 필요한 것들을 적어주세요 (팀별 개발표준, API Documentation 등등...)

##### 개발 환경

- OS : ubuntu 18.04

- Python : 3.7.x

  - 패키지 관리자 : PIP

- node JS :  12.x

  - 패키지 관리자 : npm

- IDE : vs code

- Lint

  vs code의 세이브 시 자동 정렬 기능을 활성화하여 코드의 통일성이 유지

  JS : ES Lint (vs code extention)

  Python : pep8
  
  


##### Git commit 정책 (Angular Git Commit Coventions 참조)

- Jira Key는 1 commit 당 1 key 원칙 (단, sub Task의 경우 복수 키 허용)
  
- Commit 형식

  `git commit -m '[<Tag>] <Message>, <Option> <Jira Key>'`

  ex) 

  `git commit -m '[Feat] signup with email instead of username, resolves S03P22B106-76`
  
- Tag

  - Feat(feature)
    새로운 내용 추가 즉, Jira Issue Task 수행과 직결되는 내용의 추가 시

  - Fix(bug fix)
    버그 수정

  - Docs(documentation)
    문서 추가, 문서 수정

  - Style(frommatiing, missing semi colons, ...)
    코드 포맷팅 등 코드 자체의 변경 없이 Style 변경만 있는 경우

  - Refactor(Refactor)
    코드 리펙토링, 기능은 변하지 않았지만 구조가 변한 경우

  - Test(when adding missing tests)
    테스트 내용 추가

  - Chore(maintain)
    코드 관리, 구조 변경 등의 이슈 발생 시

  - [임시]Study

    Ai 및 프로젝트에 필요한 신규 기술을 학습한 내용을 커밋할 시

- Message

  Message는 작업 내용을 요약하며 50자 이내로 간결하게 작성

- Option

  `resolves` 등 jira의 smart commit 기능을 사용할시

- Jira Key

  jira에 커밋 내용에 해당하는 이슈 키

##### API Documentation




## 테스트 방법
> 프로젝트를 배포한 url과 테스트하기 위한 계정 ID/PW를 적어주세요

url : http://j3b106.p.ssafy.io/   ~~http://inside-kids.cf~~ (준비중)

TEST 계정

​	(준비중)

