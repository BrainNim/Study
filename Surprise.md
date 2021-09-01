# Surprise
몇년전 간단한 형태의 추천시스템을 만드는 것도 꽤 고생했던 것으로 기억하는데  
최근 솔루션화를 준비하다보니 더 쉽게 추천시스템을 만들 수 있도록 도와주는 라이브러리가 있다는 것을 알게 되었다.  
[Surprise소개페이지](http://surpriselib.com/)에 따르면 다음과 같은 것들을 할 수 있다고 한다.  
- baseline algorithms, neighborhood methods 그리고 SVD,PMF 등의 matrix factorization-based과 기타등등의 알고리즘
- 코사인, 피어슨, MSD 등의 유사도
- 알고리즘 성능평가  

왜 이제야 알게되었나 싶기도 하고 잘 활용해볼까 싶어서 정리해두려고 한다. ([Surprise공식문서](https://surprise.readthedocs.io/en/stable/))


## Reader Class, Dataset Class
``` python
reader = Reader()  # Reader(name=None, line_format=u'user item rating', sep=None, rating_scale=(1, 5), skip_lines=0)
data = Dataset.load_from_df(df,reader)
```
- 이때 데이터의 형식 및 칼럼 순서는 아래와 같이 user;item;rating;(timestamp)로 이루어져야 함 (timestamp는 생략 가능)

| user | item | rating | (timestamp) |
|------|------|--------|-------------|
|  1   | 2162 | 3.5    | 15621862186 |
|  1   | 7325 | 4.5    | 15621892318 |
|  2   | 2162 | 1.0    | 15621921682 |




## GridSearchCV
surprise도 GridSearchCV를 지원한다. ([참고](https://surprise.readthedocs.io/en/stable/getting_started.html#load-from-df-example))
```python
from surprise import SVD
from surprise import Dataset
from surprise.model_selection import GridSearchCV

# Use movielens-100K
data = Dataset.load_builtin('ml-100k')

param_grid = {'n_epochs': [5, 10], 'lr_all': [0.002, 0.005],
              'reg_all': [0.4, 0.6]}
gs = GridSearchCV(SVD, param_grid, measures=['rmse', 'mae'], cv=3)

gs.fit(data)

# best RMSE score
print(gs.best_score['rmse'])

# combination of parameters that gave the best RMSE score
print(gs.best_params['rmse'])
```
