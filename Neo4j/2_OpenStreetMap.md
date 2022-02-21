# Open Street Map

### The model
#### DB 스키마 확인하기
```
CALL db.schema.visualization()
```
![image](https://user-images.githubusercontent.com/87905878/154916479-7055ad85-cbec-4a5d-b586-679cd9013377.png)  
  
단, 이번 튜토리얼에서는 아래의 노드, 관계 스키마만 사용하여 학습한다.
![image](https://user-images.githubusercontent.com/87905878/154916973-8e9de4a5-42d6-4875-9eba-3f331ed15aa7.png)
- OSMNode: 장소와 장소간의 접합 노드
- PointOfInterest:OSMNode: 장소와 장소 간의 접합 노드 + 주요지점(동상, 레스토랑, 테니스코트 등)
- ROUTE: 각 노드 간의 물리적 거리(미터)를 속성으로 가짐

### Introduction to Spatial
Cypher는 공간정보 데이터를 지원한다.  Cypher가 지원하는 공간정보 데이터 형식은 크게 두가지이다.  
그리고 두 형식에서 모두 두 지점 간의 distance() 계산을 지원한다.
#### Geographic coordinate reference systems
- 위도,경도(,+높이) WGS84(,WGS84-3D)
#### Cartesian coordinate reference systems
- 데카르트 좌표계(x,y, +z)


### Looking for a clock
#### 속성명으로 찾기 (type:'clock')
```
MATCH (p:PointOfInterest {type:'clock'})
RETURN p.name
```

#### 거리가 100M 이내인 Node 탐색
```
MATCH (p1:PointOfInterest {type:'clock'}), (p2:PointOfInterest)
WHERE p1<>p2 AND distance(p1.location,p2.location) < 100
RETURN p1,p2
```
주의: `WHERE p1<>p2`에서 쌍방향은 `<-->`가 아닌, `<>`


### Distances (직선거리 vs 경로상 거리)
#### 직선거리
```
Match (p1:PointOfInterest {type:'clock'}), (p2:PointOfInterest {name :'Zoo School'})
RETURN distance(p1.location,p2.location)
```

#### 경로상 거리
```
MATCH path=shortestpath((p1:PointOfInterest {type:'clock'})-[:ROUTE*]-(p2:PointOfInterest {name:'Zoo School'}))
WITH relationships(path) AS rels
UNWIND rels AS rel
RETURN sum(rel.distance)
```
