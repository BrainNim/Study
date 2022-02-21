# crontab 활용

## ubuntu에서 crontab을 활용해 python파일 실행시키기

### 1. crontab 작성  
#### 1) 에디터로 들어가기
```
crontab -e
```  
#### 2) crontab 수정
```
python3 /home/ubuntu/test.py >> /home/ubuntu/test.log
```
해당 경로의 test.py를 실행, 그 print결과를 test.log 파일에 저장


### 2. crontab 상태확인
#### 1) 에디터 수정내용 확인
```
crontab -l
```

#### 2) crontab 재실행 후 상태 확인
```
service cron srestart
service cron status
```

#### 3. 결과 확인
```
cat test.log
```

#### 4. crontab 설정 삭제
```
crontab -r
```
단, 모든 설정이 모두 삭제되니 
