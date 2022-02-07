# Neo4j
그래프DB를 공부해야할 일과 흥미가 생겼다. 하지만 그래프DB는 한번도 공부해본적이 없으니 기본부터 정리해보고자 한다.  
그래프DB의 종류로는 가장 많은 사용량을 자랑하는 Neo4j를 선택했다.  
이곳([Neo4j.com/developer](https://neo4j.com/developer/))의 튜토리얼을 차근차근 따라가 볼 예정이다.


## Movies Project Tutorial

### What is Cyper?
SQL이 SQL쿼리를 사용하듯, Neo4j는 Cypher쿼리를 사용한다.
```
Match (m:Movie) where m.released > 2000 RETURN m limit 5
Match (m:Movie) RETURN M
```
SQL이 Select를 사용하듯, Cypher는 Match를 사용한다.  
그러나 SQL이 Select만으로 결과를 나타내는 것과 달리, Cypher는 RETURN이 있어야만 결과를 볼 수 있다.
![image](https://user-images.githubusercontent.com/87905878/152720932-2bd12f06-f47d-4ac2-a4f4-389e94366300.png)

### Nodes and Relationships
Neo4j의 기본 4가지 구성요소 중 2가지를 먼저 살표보자.  
#### 노드(Nodes)
엔티티를 나타낸다. 그래프 상에서는 동그란 원으로 나타난다.  
Cypher쿼리로는 `(p:Person)`과 같이 표현된다.
#### 관계(Relationships)
두 노드 간의 연결관계를 의미한다. 그래프 상에서는 선으로 나타내며, 연결에 대한 속성을 지칭할 수 있다.  
Cyphe쿼리로는 `[w:WORKS_FOR]`과 같이 표현된다.


#### 라벨(label)
#### 속성(Properties)
