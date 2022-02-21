# Neo4j
그래프DB를 공부해야할 일과 흥미가 생겼다. 하지만 그래프DB는 한번도 공부해본적이 없으니 기본부터 정리해보고자 한다.  
그래프DB의 종류로는 가장 많은 사용량을 자랑하는 Neo4j를 선택했다.  
이곳([Neo4j.com/developer](https://neo4j.com/developer/))의 튜토리얼을 차근차근 따라가 볼 예정이다.

## Cypher 구문

| Clause         | Description                                           |
|----------------|-------------------------------------------------------|
| MATCH          | 일치하는 패턴 찾기                                      |
| OPTIONAL MATCH | 패턴이 일치 하지 않으면 NULL 값으로 대체 되어 나옴        |
| WHERE          | MATCH, OPTIONAL MATCH, WITH 절의 결과를 필터링          |
| RETURN         | 쿼리의 결과를 리턴 ( 일반적인 SQL에서 select에 해당 )     |
| ORDER BY       | RETURN, WITH 뒤에 위치하여 출력 결과를 정렬              |

| Clause  | Description                                        |                                                              |
|---------|----------------------------------------------------|--------------------------------------------------------------|
| WITH    | 쿼리 결과를 다음 쿼리로 전달 ( 결과 임시 저장 )       |                                                              |
| UNWIND  | List, Map과 같이 Collect 결과를 개별 행으로 변환     |                                                              |
| FOREACH | UNWIND와 비슷 ( 데이터를 업데이트 하기 위한 용도 )    |- 변수의 scope는 괄호 안에서만 유효 </br>- MATCH는 사용할 수 없음 |
| UNION   | 여러 쿼리 결과를 결합                                |                                                              |
| SKIP    | 출력행 건너뛰기                                     | ORDER BY 를 사용하지 않으면 순서 보장 안됨                      |
| LIMIT   |                                                    |                                                              |
| USE     | 사용하는 DB 선택                                    | 주로 Fabric DB에서 사용                                       |

[참고](https://wildwhale.github.io/neo4j,/cypher/neo4j-clause-post/)

## Movies Project Tutorial
미국영화 데이터를 활용해 Neo4j와 Cypher의 기본 배우기 ([링크](https://github.com/BrainNim/Study/blob/main/Neo4j/1_Movies_Project_tutorial.md))

## Open Street Map
센트럴파크 지도, 경로 데이터를 활용해 배우기([링크](https://github.com/BrainNim/Study/blob/main/Neo4j/2_OpenStreetMap.md))
