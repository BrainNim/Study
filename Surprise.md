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
KNN을 기반으로 가중평균을 구해 가중치를 예측하는 알고리즘

### (사전에 결정하고 갈 내용) 유사도 추정방식
Surprise에서는 4가지 방식의 유사도 추정방식을 지원함
- `cosine` : 코사인 유사도
- `msd` : Mean Squared Difference
- `pearson` : 피어슨 상관
- `pearson_baseline` : 피어슨 상관과 달리, 평균값이 아닌 베이스라인 모형에서 예측한 값을 활용해 계산한 상관
<details>
<summary>참고. sim_options default 값 (접기/펼치기)</summary>
<div markdown="1">

|             |                                                                                            |
|-------------|--------------------------------------------------------------------------------------------|
| name        | 'MSD'                                                                                      |
| user_based  | True                                                                                       |
| min_support | (user_based=True) : common items의 최소 숫자 <br> (user_based=False) : common users의 최소 숫자 |
| shrinkage   | 100 (pearson_baseline에서만 사용)                                                          |
</div>
</details>


### KNNBasic

### KNNWithMeans
### KNNBaseline

예시)
``` python
sim_options = {'name': 'pearson'}
algorithm = surprise.KNNBasic(sim_options=sim_options)
result = cross_validate(algorithm, data)
```
<details>
<summary>참고. 파라미터 default 값 (접기/펼치기)</summary>
<div markdown="1">

|             | KNNBasic | KNNWithMeans | KNNWithZScore |
|-------------|----------|--------------|---------------|
| k           | 40       | 40           | 40            |
| min_k       | 1        | 1            | 1             |
| sim_options | (dict)   | (dict)       | (dict)        |
| bsl_options | (dict)   | (dict)       | (dict)        |
| verbose     | True     | True         | True          |
</div>
</details>

## Matrix Factorization-based algorithms
- `SVD`
- `SVDpp`
- `NMF`: Non-negative Matrix Factorization(음수 미포함 행렬 분해) 기반
- `SlopeOne`:[참고문헌](https://arxiv.org/abs/cs/0702144)
- `Co-clustering`:[참고문헌](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.113.6458&rep=rep1&type=pdf)

예시)
``` python
algorithm = surprise.SVD(n_factors=15)
result = cross_validate(algorithm, data)
```
<details>
<summary>참고. 파라미터 default 값 (접기/펼치기)</summary>
<div markdown="1">
  
|              | SVD   | SVDpp | NMF   |
|--------------|-------|-------|-------|
| n_factors    | 100   | 20    | 15    |
| n_epochs     | 20    | 20    | 50    |
| biased       | True  |       | False |
| init_mean    | 0     | 0     |       |
| init_std_dev | 0.1   | 0.1   |       |
| lr_all       | 0.005 | 0.007 |       |
| reg_all      | 0.02  | 0.02  |       |
| lr_bu        | None  | None  | 0.005 |
| lr_bi        | None  | None  | 0.005 |
| lr_pu        | None  | None  |       |
| lr_qi        | None  | None  |       |
| reg_bu       | None  | None  | 0.02  |
| reg_bi       | None  | None  | 0.02  |
| reg_pu       | None  | None  | 0.06  |
| reg_qi       | None  | None  | 0.06  |
| random_state | None  | None  | None  |
| verbose      | False | False | False |
| init_low     |       |       | 0     |
| init_high    |       |       | 1     |
</div>
</details>

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

## 결과예측
### predict 메소드
알고리즘의 `predict`메소드를 활용하여 유저가 해당 아이템에 몇점을 부여할지 예측하는 방식
```python
algorithm.predict(uid, iid, r_ui=None, clip=True, verbose=False)

# Prediction(uid='57', iid='194', r_ui=None, est=4.347066481355011, details={'was_impossible': False})
```
#### 파라미터 & 결과값
##### 파라미터
- uid: 유저id(raw)
- iid: 아이템id(raw)
- r_ui: 실제 유저가 해당 아이템에 몇점을 부여했는가(default: None)
- clip: 예상치가 rating scale을 벗어날 경우, 해당 rating scale 최대/최솟값으로 변환할 것인가 (default: True)
예) rating scale은 1~5인데 예상치가 5.5인 경우, 5로 변환함  
- verbose: verbose(default: False)
##### 결과값
- est: 예상 rating

### get_neighbors 메소드
알고리즘의 `get_neighbors`메소드를 이용하여 (특정 유저와 가까운 유저), (특정 아이템과 가까운 아이템) K개를 찾음
```python
algorithm.get_neighbors(iid, k)
```
- [x] 주의: KNN관련 알고리즘만 사용가능함
##### 파라미터
- iid: inner id(int) => trainset 생성시, 내부 코드가 돌아가기 위해 생성되는 내부용 유저id or 아이템id 
- [x] 주의: iid 파라미터는 'raw'가 아닌, 'int'임
- raw id와 inner id간의 변환은 `trainset`의 `to_inner_uid()`, `to_inner_iid()`, `to_raw_uid()`, `to_raw_iid()`메소드를 통해 가능함

### get_top_n 함수 생성
Surprise 내에 get_top_n 함수는 존재하지 않지만, [공식문서](https://surprise.readthedocs.io/en/stable/FAQ.html#how-to-get-the-top-n-recommendations-for-each-user)에서는 각 유저별로 top_n 아이템을 추천할 수 있는 함수를 만드는 방법을 공개하고 있으며,  
그 활용방법 역시 매우 간단하다.
```python
top_n = get_top_n(predictions, n=10)
```
그 함수 내용 및 활용방식 전반은 다음과 같다.
```python
from collections import defaultdict

from surprise import SVD
from surprise import Dataset


def get_top_n(predictions, n=10):
    """Return the top-N recommendation for each user from a set of predictions.

    Args:
        predictions(list of Prediction objects): The list of predictions, as
            returned by the test method of an algorithm.
        n(int): The number of recommendation to output for each user. Default
            is 10.

    Returns:
    A dict where keys are user (raw) ids and values are lists of tuples:
        [(raw item id, rating estimation), ...] of size n.
    """

    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n


# First train an SVD algorithm on the movielens dataset.
data = Dataset.load_builtin('ml-100k')
trainset = data.build_full_trainset()
algo = SVD()
algo.fit(trainset)

# Than predict ratings for all pairs (u, i) that are NOT in the training set.
testset = trainset.build_anti_testset()
predictions = algo.test(testset)

top_n = get_top_n(predictions, n=10)

# Print the recommended items for each user
for uid, user_ratings in top_n.items():
    print(uid, [iid for (iid, _) in user_ratings])
```




#### 참고문서
- [Surprise소개페이지](http://surpriselib.com/)
- [Surprise공식문서](https://surprise.readthedocs.io/en/stable/)
- [데이터사이언스스쿨](https://datascienceschool.net/03%20machine%20learning/07.01%20%EC%B6%94%EC%B2%9C%20%EC%8B%9C%EC%8A%A4%ED%85%9C.html)
