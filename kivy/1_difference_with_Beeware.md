## **Python만으로 어플을 만들 수 있었어?**

저같은 초보 코더들은 이것저것 만들어보고싶은 것이 많습니다.

하지만 네이티브 앱을 만들기 위해서는 안드나 IOS 네이티브 앱 개발을 위한 언어를 새로 배워야하고

웹을 만든 뒤 앱으로 씌우려고 해도 html과 css를 배워야합니다.

물론 저처럼 python만 아는 사람들을 위해 Django가 기본적인 틀을 배포해주고 있기는 하지만 언젠가부터 Django를 활용해서 커스터마이징 하기에는 한계가 많다는 얘기를 더 자주 듣게되었습니다.

그러면 어처피 아직 아무것도 안배운거, **Django 말고 다른걸 배워보자!**

라는 생각을 하게 되었습니다.

그리고 검색해보니 생각보다 쉽게 또다른 어플리케이션 개발 도구를 발견할 수 있었습니다.

**바로 kivy와 Beeware입니다!**

## **kivy vs Beeware**

- [Kivy Vs BeeWare(YouTube)](https://youtu.be/rK5Sw2jk__w)  
- [Python for Mobile App Development in 2022 – Kivy Vs BeeWare](https://www.monterail.com/blog/python-for-mobile-app-development)
  
kivy와 Beeware의 각각의 개별적인 특징은 위의 영상과 링크에 보다 상세히 적혀있으니 참고해보시면 많은 도움을 받으실 수 있을거라고 생각합니다.

저는 제가 둘 중 어떤 것을 선택했는지, 왜 선택했는지만 간략히 정리해볼까 합니다.

결과론적으로, 저는 kivy를 선택했습니다.

위의 정보들에서 제가 주로 관심을 가진 정보는 다음과 같습니다.

|   | kivy | Beeware |
| --- | --- | --- |
| UI supports | custom UI | native UI |
| phase | more established | development phase |

### 1\. UI supports: custom UI vs native UI

두 방식모두 저마다의 장단점이 있습니다.

custom UI는 본인이 원하는 형식대로 디자인하고 개발하기에 보다 편리합니다.

native UI는 안드로이드와 ios 각각에 맞춰 코드가 조금씩 다를 수 있지만, 각 유저들의 성향과 환경에 보다 친화적으로 개발할 수 있습니다.

참고로 저는 예쁜 디자인을 적용한 어플리케이션을 만들고자 하는것도 아니고,

그저 파이썬만으로 정말 어플리케이션을 만드로 apk파일을 만들어서 제 폰에서 구동이 되는지 경험해보고싶은 것이기 때문에 막연히 custom이 더 편하지 않을까 했습니다.

### 2\. phase: more established vs development phase

제게는 이 부분이 가장 크리티컬 했습니다.

웹, 앱과 같은 event-driven 기반의 프로그래밍을 해본적이 없기 때문에 보다 안정적이고, 참고할만한 자료가 많은 것을 선택하고 싶었습니다.(그럴거라면 처음부터 html, css같은 웹개발 도구나 다른 프론트용 언어를 배우는게 나을 수도 있겠지만 거기까지는 조금... 아직은... 무리.....)

정교하게 비교해본것은 아니지만 공식문서도 그렇고 stackoverflow도 그렇고 kivy에 정보가 더 많다고 느꼈습니다.

그래서 저는 **kivy**를 사용해보기로 했습니다!

다음에는 kivy 설치부터 공식문서의 튜토리얼을 차근차근 따라하며 kivy에 익숙해지는 과정을 거쳐볼까 합니다.

감사합니다

https://brain-nim.tistory.com/2
