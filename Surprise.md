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


## Basic algorithms
타 알고리즘들에 대한 성능비교용 알고리즘  

### NormalPredictor
- 정규분포를 통해 rating을 랜덤으로 예측하는 모델

### BaselineOnly
- 단순한 형태의 회귀분석모델
- hat_r(u,i) = mu + b(u) + b(i)
- 오차함수: Sigma(r(u,i) - hat_r(u,i))^2
- 오차함수최적화: SGD(Stochastic Gradient Descent) / ALS(Alternating Least Squeares) => method 인수를 통해 선택가능


## KNN(K-Nearest Neighbors) algorithmms
KNN을 활용한 알고리즘

### (사전에 결정하고 갈 내용) 유사도 추정방식
Surprise에서는 4가지 방식의 유사도 추정방식을 지원함
- `cosine` : 코사인 유사도
- `msd` : Mean Squared Difference
- `pearson` : 피어슨 상관
- `pearson_baseline` : 피어슨 상관과 달리, 평균값이 아닌 베이스라인 모형에서 예측한 값을 활용해 계산한 상관
예시)
``` python
sim_options = {'name': 'pearson'}
algorithm = surprise.KNNBasic(sim_options=sim_options)
result = cross_validate(algorithm, data)
```
### KNNBasic
- 
### KNNWithMeans

### KNNBaseline


## 성능평가
### RMSE(Root Mean Squared Error)
### MAE(Mean Absolute Error)
### FCP(Fraction of Concordant Pairs)
예시)
``` python
# cross validation을 수행하는 경우
from surprise.model_selection import cross_validate
'(중략)'
results = cross_validate(algorithm, data, measures=['RMSE'], cv=3, verbose=False)


# accuracy를 평가하는 경우
from surprise import accuracy
'(중략)'
predictions = algorithm.fit(trainset).test(testset)
accuracy.rmse(predictions)
```


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


#### 참고문서
- [Surprise소개페이지](http://surpriselib.com/)
- [Surprise공식문서](https://surprise.readthedocs.io/en/stable/)
- [데이터사이언스스쿨](https://datascienceschool.net/03%20machine%20learning/07.01%20%EC%B6%94%EC%B2%9C%20%EC%8B%9C%EC%8A%A4%ED%85%9C.html)
