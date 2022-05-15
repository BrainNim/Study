# crontab 활용

## ubuntu에서 crontab을 활용해 python파일 실행시키기

### 1. crontab 작성  
#### 1) 에디터로 들어가기
```
crontab -e
```  
#### 2) crontab 수정
```
*         *           *         *          *
분(0-59)  시간(0-23)  일(1-31)   월(1-12)   요일(0-7,일월~토일)
```

```
* * * * 1-5 python3 /home/ubuntu/test.py >> /home/ubuntu/test.log
```
평일에만 매분 해당 경로의 test.py를 실행, 그 print결과를 test.log 파일에 저장
  
  
##### 출력 리다이렉션(output redirection)
```
* * * * 1-5 python3 /home/ubuntu/test.py >> /home/ubuntu/test.log 2>&1
```
`0 = stdIn, 1 = stdout, 2 = stderr`  
`2>&1` : 표준에러(stderr)도 test.log에 


### 2. crontab 상태확인
#### 1) 에디터 수정내용 확인
```
crontab -l
```

#### 2) crontab 재실행 후 상태 확인
```
service cron restart
service cron status
```

#### 3) 결과 확인
```
cat test.log
```

#### 4) crontab 설정 삭제
```
crontab -r
```
단, 모든 설정이 모두 삭제되니 주의



### 3. trouble shooting
#### 1) Permission denied 권한 문제 : crontab -e
![image](https://user-images.githubusercontent.com/87905878/154897008-9dbad366-b497-4e9d-8faf-1b771c6627f5.png)  
- 위의 에러는 아래와 같이 /tmp 파일에 대한 권한이 잘못된 경우
```
$ ls -ld /tmp/
# dr-xr-xr-x 133 root root 20480 Feb 21 15:12 /tmp.
```
![image](https://user-images.githubusercontent.com/87905878/154903631-e1f68f26-4193-47be-a0fd-36045eba5ba1.png)
- 이 경우 아래와 같이 권한을 복원한다.
```
$ chmod 1777 /tmp
```
[참고자료](https://www.thegeekdiary.com/user-unable-to-edit-crontab-error-tmp-crontab-lm34gsjv-permission-denied/)
