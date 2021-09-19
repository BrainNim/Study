# BeautifulSoup
BeautifulSoup를 활용하는 건 정말 간단하고 쉽다.  
문제는 내가 자꾸 까먹는다는 점이다. 그동안 어딘가에 정리를 해두긴 했었는데 어느 폴더에, 어느 파일에 했는지조차 까먹을 때도 많다.  
그래서 정리해 두려고 한다.

### soup.select 활용방식
- 태그, 클래스, 아이디, 기타속성 구분  
`soup.select('태그명')`  
`soup.select('.클래스명')`  
`soup.select('#아이디명')`  
`soup.select('태그명[속성명1=값1]')`  

- 자식, 자손 탐색  
`soup.select('태그명 > 바로아래태그명 > 그바로아래태그명')`  # 태그 > 자식 > 자식  
`soup.select('태그명 > 바로아래태그명 멀리있는하위태그명')`  # 태그 > 자식 자손  

- 불필요한 하위 태그 제거
```python
sample = soup.select_one('태그명')
sample.불필요태그명.decompose()
print(sample)
```

이걸 기억 못해서 정리한다니...
