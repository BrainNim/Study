# Git - AWS EC2
EC2 내부에서 git pull을 하려고 했더니 21년 8월 13일부터는 비밀번호가 아니라 git token을 활용해야한다고 한다.
관련 내용을 따라하기 매우 쉽게 블로그를 작성해주신 분들의 도움을 받았고, 나중에 내가 까먹을까봐 정리해둔다.

## git private repo pull할 때 로그인 생략
토큰을 발급받은 뒤, 토큰을 어딘가에 저장해두지 않으면 더이상 토큰을 확인할 수 있는 방법이 없기 때문에
어딘가에 자격증명을 저장해 두어야 한다.

Windows 자격증명을 설정하는 방법도 있지만, 나는 주로 AWS EC2에 직접 들어가서 pull 명령을 치기 때문에,
로그인 생략을 설정했다. 물론 보안상 문제가 있을 수야 있겠지만 그렇게 문제가 발생할만한 repository는 아니기 때문에...

#### 1) GitHub에서 Generate new token
`[Settings]-[Developer Settings]-[Personal access tokens]`
#### 2) EC2접속 후 git remote 설정
`git remote set-url origin https://<토큰>@github.com/<유저이름>/<repository이름>`  
`예) git remote set-url origin https://tokennumberblablabla@github.com/hhhsss0815/Study`


#### 참고블로그
- [git 토큰 생성](https://firstquarter.tistory.com/entry/Git-%ED%86%A0%ED%81%B0-%EC%9D%B8%EC%A6%9D-%EB%A1%9C%EA%B7%B8%EC%9D%B8-remote-Support-for-password-authentication-was-removed-on-August-13-2021-Please-use-a-personal-access-token-instead)
- [git private repo pull할 때 로그인 생략](https://yangeok.github.io/devops/2019/10/30/git-without-login.html)


## git default branch 이름 수정
```bash
git branch -m master main
git fetch origin
```

## github push 관련 오류
#### 1) [rejected] master -> master (fetch first) 에러
- 기존 local repository를 제거하고 새로 git init을 실행하여 푸쉬하는 등, 기존데이터가 손실될 우려로 푸쉬를 막은 경우에 발생
- +를 붙여서 강제로 푸쉬시키면 해결
```bash
git push origin +master
```
