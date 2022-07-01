# vue-python-graphql
vue3, pinia, urql, windicss, daisyui, vite, python, fastapi, strawberry-graphql, sqlalchemy, poetry

## DB 정보 입력 (mysql, mariadb로 개발되어 있음)
backend폴더에 .config파일 수정  
[DATABASE]  
DB_USER_NAME =  
DB_USER_PASSWD =   
DB_HOST = 127.0.0.1  
DB_NAME =   


## DB 테스트 테이블 생성 (테스트를 위하여 대충 만든 것 임)
```
CREATE TABLE `tb_code_m` (  
	`C_ID` VARCHAR(10) NULL DEFAULT NULL COLLATE 'utf8mb3_general_ci',  
	`C_PARENT_ID` VARCHAR(10) NULL DEFAULT NULL COLLATE 'utf8mb3_general_ci',  
	`C_NAME` VARCHAR(100) NULL DEFAULT NULL COLLATE 'utf8mb3_general_ci',  
	`C_ENG_NAME` VARCHAR(100) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',  
	`C_DESCRIPTION` VARCHAR(1000) NULL DEFAULT NULL COLLATE 'utf8mb3_general_ci'  
)  
COLLATE='utf8mb3_general_ci'  
ENGINE=InnoDB  
;  
CREATE TABLE `tb_code_problem` (  
	`CP_SEQ` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,  
	`CP_CATEGORY_CD` VARCHAR(10) NULL DEFAULT NULL COLLATE 'utf8mb3_general_ci',  
	`CP_TITLE` VARCHAR(100) NULL DEFAULT NULL COLLATE 'utf8mb3_general_ci',  
	`CP_LEVEL_CD` VARCHAR(10) NULL DEFAULT NULL COLLATE 'utf8mb3_general_ci',  
	`CP_CONTENT` TEXT NULL DEFAULT NULL COLLATE 'utf8mb3_general_ci',  
	`CP_TAG` VARCHAR(100) NULL DEFAULT NULL COLLATE 'utf8mb3_general_ci',  
	`CP_LAPTIME` DATETIME NULL DEFAULT NULL,  
	PRIMARY KEY (`CP_SEQ`) USING BTREE  
)  
COLLATE='utf8mb3_general_ci'  
ENGINE=InnoDB  
AUTO_INCREMENT=9  
;  
CREATE TABLE `users` (  
	`id` VARCHAR(50) NOT NULL DEFAULT 'AUTO_INCREMENT' COLLATE 'utf8mb3_general_ci',  
	`name` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8mb3_general_ci',  
	`password` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8mb3_general_ci',  
	PRIMARY KEY (`id`) USING BTREE  
)  
COLLATE='utf8mb3_general_ci'  
ENGINE=InnoDB  
;  
```

## FRONTEND 패키지 설치
frontend 폴더에서 
```
npm install
```
실행 시킴

## BACKEND 패키지 설치
### poetry 처음 설치의 경우 (파이썬 Python 2.7 아니면 3.5이상, 필자는 3.10.X)
osx / linux / bashonwindows은 아래 curl url을 터미널에 입력해서 설치하면 된다
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```
### poetry가 설치되어 있는 경우
```
poetry install
```
install 후 .venv 가상환경이 생성되니 VSCODE로 작업 시 python: select interpretor를 .venv/Scrpits/python.exe를 설치하자 (안하는 경우 실행은 되겠지만 코드 warning을 마주하게 된다. app/root.py에서 vscode 디버깅하세요)

```
poetry run python main.py
```
로 실행한다.

## FRONTEND 실행
```
npm run dev
```
