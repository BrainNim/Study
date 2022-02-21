# Movies Project Tutorial

### What is Cyper?
SQL이 SQL쿼리를 사용하듯, Neo4j는 Cypher쿼리를 사용한다.
```
Match (m:Movie) where m.released > 2000 RETURN m limit 5
Match (m:Movie) RETURN M
```
SQL이 Select를 사용하듯, Cypher는 Match를 사용한다.  
그러나 SQL이 Select만으로 결과를 나타내는 것과 달리, Cypher는 RETURN이 있어야만 결과를 볼 수 있다.
![image](https://user-images.githubusercontent.com/87905878/152720932-2bd12f06-f47d-4ac2-a4f4-389e94366300.png)

  
### Elements of Neo4j
Neo4j의 기본 4가지 구성요소를 먼저 살표보자.  

#### 노드(Nodes)
엔티티를 나타낸다. 그래프 상에서는 동그란 원으로 나타난다.  
Cypher쿼리로는 `(p:Person)`과 같이 표현한다.  

#### 관계(Relationships)
두 노드 간의 연결관계를 의미한다. 그래프 상에서는 선으로 나타내며, 연결에 대한 속성을 지칭할 수 있다.  
Cypher쿼리로는 `[w:WORKS_FOR]`과 같이 표현한다.
```
MATCH (p:Person)-[d:DIRECTED]-(m:Movie) where m.released > 2010 RETURN p,d,m
```
![image](https://user-images.githubusercontent.com/87905878/152897563-abd86154-0228-4d14-a218-49d34c7f6446.png)

#### 라벨(label)
각 노드나 관계에 대한 이름이나 식별명을 의미한다(Person, Movie, DIRECTED 등)  
Cypher쿼리로는 `:Person`과 같이 :을 사용하여 표현한다.  
해당 노드에 대한 일종의 필터역할을 수행하며, 지정하지 않을 경우 모든 노드를 출력한다.  
![image](https://user-images.githubusercontent.com/87905878/152898644-5e35a3b3-78ff-445b-aaa3-5ab4da7bb4c5.png)

#### 속성(Properties)
노드나 관계의 속성을 나타내는 name-value 쌍이다.  
Cypher쿼리로는 `{name: 'John Doe'}`와 같이 표현하여
```
MATCH (m:Movie) return m.title, m.released
```
![image](https://user-images.githubusercontent.com/87905878/152899057-51b35af5-62c9-45cd-a13c-227fdb873222.png)


### Create a Node
SQL에서는 테이블을 생성할 때 Create를 사용한다면  
Cyper에서는 노드를 생성할 때 Create를 사용한다.
```
Create (p:Person {name: 'John Doe'}) RETURN p
Create (p:Person {name: 'John Doe'})  // 결과를 보여주지 않음
```

### Finding Nodes
위에서 언급한 바와 같이, Match를 통해 노드 및 관계를 찾으며, 이때 속성을 이용하거나 where을 활용해 조건을 설정할 수 있다.
```
// 동일한 결과를 나타내는 두 쿼리
Match (p:Person {name: 'Tom Hanks'}) RETURN p
MATCH (p:Person) where p.name = "Tom Hanks" RETURN p
```

### Merge Clause
Merge 절은 다음의 두 경우에 주로 사용할 수 있다.
1. 이미 존재하는 노드를 match하여 그 결과와 bind할 때
2. 새로운 노드를 create하고 그 노드와 bind할 때

```
MERGE (m:movie {title: 'Greyhound'})                              //1 
ON MATCH SET m.lastUpdatedAt = timestamp()                        //2
ON CREATE SET m.released = "2020", m.lastUpdatedAt = timestamp()  //3
Return m                                                          //4
```
1) "Greyhound"라는 제목을 가진 영화노드
2) 그 노드를 match할 수 있다면 업데이트일자를 지금으로 수정
3) 노드가 없다면 새로 create하고 개봉연도를 2020년으로, 업데이트일자를 지금으로 수정


### Create a Relationship
SQL에서와 달리, Cypher에서는 Match절과 Create절을 연속적으로 사용할 수 있다.  
이 점을 이용해 원하는 노드에서만 관계를 쉽게 설정할 수 있다.
```
MATCH (p:Person), (m:Movie)
WHERE p.name = "Tom Hanks" and m.title = "Cloud Atlas"
CREATE (p)-[w:WATCHED]->(m)
RETURN type(w)
```
![image](https://user-images.githubusercontent.com/87905878/152903476-c1720d16-aa97-474e-b5f6-1108b967b084.png) 관계가 새로 생성됨


### Advanced Cypher queries

#### Finding all people who have co-acted with Tom Hanks in any movie
```MATCH (tom:Person {name: "Tom Hanks"})-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(p:Person) return p,m,tom```
![image](https://user-images.githubusercontent.com/87905878/152905516-0ee8b99e-da27-48a4-adb2-8e8545aeb23f.png)  

```MATCH (p:Person)-[relatedTo]-(m:Movie {title: "Cloud Atlas"}) return p.name, type(relatedTo) as relatedTo```
![image](https://user-images.githubusercontent.com/87905878/152905873-34441437-1df3-4af5-b4e6-e932f3bc7dc9.png)


```MATCH (p:Person {name: 'Kevin Bacon'})-[*1..3]-(hollywood) return DISTINCT p, hollywood```
![image](https://user-images.githubusercontent.com/87905878/152906902-370ca489-f67f-45d8-9b41-542b96285329.png)  
Distinct: Table 형식으로 볼 때 동일한 노드, 관계 등에 대한 중복출력 방지(그래프형식으로 볼 때는 똑같은 결과)
