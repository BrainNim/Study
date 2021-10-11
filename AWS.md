# AWS EC2 인스턴스 생성시 초기설정
신규 EC2 인스턴스를 새로 생성할 일이 많지 않기 때문에  
기본적으로 설정해줘야 하는 것들을 매번 검색하고 있는 자신을 발견한다.
적어두면 상대적으로 덜 까먹고, 까먹더라도 한번에 관리하기 편할 것 같아 정리해둔다.

## git 설치
### 리눅스
#### 1) yum 업데이트
`sudo yum update -y`
#### 2) git 설치
`sudo yum install git -y`  
`git version  # 설치 확인`

### 우분투
#### 1) apt 업데이트
`sudo apt update`


#### 부가문서
- git private repo pull할 때 로그인 생략 [링크](https://github.com/BrainNim/Study/blob/main/Git.md)

#### 참고문서
- [git 설치](https://chucoding.tistory.com/23)


## pip 설치
### 리눅스
#### 1) pypa.io 설치
`curl -O https://bootstrap.pypa.io/get-pip.py`
#### 2) pip 설치
`python3 get-pip.py --user`
#### 참고문서
- [Linux에 Python, pip 및 EB CLI 설치](https://docs.aws.amazon.com/ko_kr/elasticbeanstalk/latest/dg/eb-cli3-install-linux.html)

### 우분투
#### 1) pip 설치
`sudo apt install python3-pip`
#### 2) PATH 설정
- 홈 디렉토리(~/)에서 vim으로 `.bashrc` 파일을 연다
- 맨 마지막 줄에 다음과 같이 입력하고 저장한다
```
export PATH="(사용할 경로):$PATH"
# export PATH="/home/ubuntu/.local:$PATH"
```

#### 참고문서
- [우분투 pip install path설정](https://www.tuwlab.com/ece/231)


## netstat 활용
#### 설치
`sudo apt install net-tools`
#### PID 확인
`netstat -lntp`
#### PID 강제종료
`sudo kill -9 {pid번호}`



# AWS Lambda layers 설정과 함수설정
특히 layers의 경우 초기에만 작업을 하다보니 세부적인걸 까먹고 오류가 발생해서
매번 어디서 실수했던건지 다시 검색하게 된다. 정리해두자.


## Library.zip 생성
#### Library.zip의 형태
```
Library.zip
   ㄴ Python
        ㄴ bs4
        ㄴ ...
```

#### 각 라이브러리의 설치, Library.zip 생성
1) 설치할 [Library]-[python] 폴더에서 cmd 열기
2) `pip install {라이브러리 이름} -t .`
3) [Library] 폴더 압축 

#### 주의
- pandas, numpy를 Lambda에서 사용할 경우, 일반적인 pip install pandas를 사용하면 안됨
- Amazon Linux와 호환되는 pandas, numpy를 다운받아야 하기 때문.
- numpy: *numpy-1.18.1-cp(버전)-cp(버전)m-manylinux1_x86_64.whl 를 [다운로드](https://pypi.org/project/numpy/#files)
- pandas: *manylinux_x86_64.whl 패키지 중 자신이 설정한 python 버전에 맞는 것을 [다운로드](https://pypi.org/project/pandas/#files)
- `unzip {.whl}`
