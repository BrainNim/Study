# Surprise
몇년전 간단한 형태의 추천시스템을 만드는 것도 꽤 고생했던 것으로 기억하는데  
최근 솔루션화를 준비하다보니 더 쉽게 추천시스템을 만들 수 있도록 도와주는 라이브러리가 있다는 것을 알게 되었다.  
[Surprise소개페이지](http://surpriselib.com/)에 따르면 다음과 같은 것들을 할 수 있다고 한다.  
- baseline algorithms, neighborhood methods 그리고 SVD,PMF 등의 matrix factorization-based과 기타등등의 알고리즘
- 코사인, 피어슨, MSD 등의 유사도
- 알고리즘 성능평가  

왜 이제야 알게되었나 싶기도 하고 잘 활용해볼까 싶어서 정리해두려고 한다. ([Surprise공식문서](https://surprise.readthedocs.io/en/stable/))


## Reader Class
유저 ; 아이템 ; rating ; [타임스탬프] 의 형태로 이루어진 데이터를 읽어는 클래스  
`classsurprise.reader.Reader(name=None, line_format=u'user item rating', sep=None, rating_scale=(1, 5), skip_lines=0)`


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
