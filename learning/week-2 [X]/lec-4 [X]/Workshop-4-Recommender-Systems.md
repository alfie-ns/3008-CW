# COMP3008 - Workshop 4: Recommender Systems

## Exercise 1 - Movie Database

### Setup: Load the movie dataset

Copy the entire contents of `movie_dataset_script.txt` and paste into Neo4j Browser, then run it.
This creates 133 actors, 38 movies and 253 relationships.

### Verify the dataset

**Count Actor nodes (should be 133):**
```cypher
MATCH (a:Actor)
RETURN COUNT(a) AS ACTORS
```

**Count Movie nodes (should be 38):**
```cypher
MATCH (m:Movie)
RETURN COUNT(m) AS MOVIES
```

**Count DIRECTED relationships (should be 44):**
```cypher
MATCH ()-[r:DIRECTED]->()
RETURN COUNT(r) AS DIRECTED_MOVIES
```

**Count ACTED_IN relationships (should be 172):**
```cypher
MATCH ()-[r:ACTED_IN]->()
RETURN COUNT(r) AS ACTED_IN
```

**Count PRODUCED relationships (should be 15):**
```cypher
MATCH ()-[r:PRODUCED]->()
RETURN COUNT(r) AS PRODUCED
```

**Count FOLLOWS relationships (should be 3):**
```cypher
MATCH ()-[r:FOLLOWS]->()
RETURN COUNT(r) AS FOLLOWS
```

**Count REVIEWED relationships (should be 9):**
```cypher
MATCH ()-[r:REVIEWED]->()
RETURN COUNT(r) AS REVIEWED
```

**Count WROTE relationships (should be 10):**
```cypher
MATCH ()-[r:WROTE]->()
RETURN COUNT(r) AS WROTE
```

### Find all movies Helen Hunt acted in (graph view)

```cypher
MATCH (helen:Actor {name: 'Helen Hunt'})-[:ACTED_IN]->(m:Movie)
RETURN helen, m
```

### Find all co-actors of Helen Hunt (7 actors)

```cypher
MATCH (helen:Actor {name: 'Helen Hunt'})-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(coActor:Actor)
RETURN DISTINCT coActor.name
```

### Display Helen Hunt's co-actors and shared movies as a graph

```cypher
MATCH (helen:Actor {name: 'Helen Hunt'})-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(coActor:Actor)
RETURN helen, m, coActor
```

### Find Helen Hunt's co-co-actors (61 records)

These are actors who acted with a co-actor of Helen Hunt but have NOT acted with Helen Hunt directly.

```cypher
MATCH (helen:Actor {name: 'Helen Hunt'})-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(coActor:Actor),
      (coActor)-[:ACTED_IN]->(m2:Movie)<-[:ACTED_IN]-(coCoActor:Actor)
WHERE NOT (helen)-[:ACTED_IN]->()<-[:ACTED_IN]-(coCoActor)
AND helen <> coCoActor
RETURN DISTINCT coCoActor.name
```

### Co-co-actors ranked by frequency

```cypher
MATCH (helen:Actor {name: 'Helen Hunt'})-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(coActor:Actor),
      (coActor)-[:ACTED_IN]->(m2:Movie)<-[:ACTED_IN]-(coCoActor:Actor)
WHERE NOT (helen)-[:ACTED_IN]->()<-[:ACTED_IN]-(coCoActor)
AND helen <> coCoActor
RETURN coCoActor.name, COUNT(*) AS FREQUENCY
ORDER BY FREQUENCY DESC
```

### All movies and actors between Helen Hunt and Kevin Bacon (graph)

```cypher
MATCH p = shortestPath((helen:Actor {name: 'Helen Hunt'})-[:ACTED_IN*]-(kevin:Actor {name: 'Kevin Bacon'}))
RETURN p
```

Or to see all paths:

```cypher
MATCH p = (helen:Actor {name: 'Helen Hunt'})-[:ACTED_IN*..6]-(kevin:Actor {name: 'Kevin Bacon'})
RETURN p
```

### All movies and actors between Tom Hanks and Tom Cruise

```cypher
MATCH p = shortestPath((tom:Actor {name: 'Tom Hanks'})-[:ACTED_IN*]-(cruise:Actor {name: 'Tom Cruise'}))
RETURN p
```

---

## Exercise 2 - Romeo and Juliet

### Setup: Load the Romeo and Juliet graph

Copy the entire contents of `romeo_and_juliet_graph.txt` and paste into Neo4j Browser, then run it.
This creates 11 characters and 32 FRIENDS_WITH relationships.

### Verify the dataset

**Count Franciscan characters (should be 1):**
```cypher
MATCH (n:Character:Franciscans)
RETURN COUNT(n) AS TOTAL_NUMBER_OF_FRANCISCANS
```

This also works (because only Franciscan nodes have the `Franciscans` label — both queries match the same nodes):
```cypher
MATCH (n:Franciscans)
RETURN COUNT(n) AS TOTAL_NUMBER_OF_FRANCISCANS
```

### Display Franciscan characters and their relationships (graph)

```cypher
MATCH (n:Franciscans)-[r]-(other)
RETURN n, r, other
```

### Display House of Verona characters and their relationships (graph)

```cypher
MATCH (n:House_of_Verona)-[r]-(other)
RETURN n, r, other
```

### Count mutual friends between Mercutio and Benvolio (should be 1)

```cypher
MATCH (mercutio:Character {name: 'Mercutio'})-[:FRIENDS_WITH]-(mutual)-[:FRIENDS_WITH]-(benvolio:Character {name: 'Benvolio'})
RETURN 'Mercutio and Benvolio' AS pair, COUNT(DISTINCT mutual) AS mutual_friends
```

### Count mutual friends between Mercutio and Capulet (should be 2)

```cypher
MATCH (mercutio:Character {name: 'Mercutio'})-[:FRIENDS_WITH]-(mutual)-[:FRIENDS_WITH]-(capulet:Character {name: 'Capulet'})
RETURN 'Mercutio and Capulet' AS pair, COUNT(DISTINCT mutual) AS mutual_friends
```

### Mutual friends between Mercutio and all non-friends (with count)

```cypher
MATCH (mercutio:Character {name: 'Mercutio'})-[:FRIENDS_WITH]-(mutual)-[:FRIENDS_WITH]-(c2:Character)
WHERE NOT (mercutio)-[:FRIENDS_WITH]-(c2)
AND mercutio <> c2
RETURN 'Mercutio and ' + c2.name AS pair, COUNT(DISTINCT mutual) AS mutual_friends
ORDER BY mutual_friends DESC
```

### Mutual friends between Mercutio and all non-friends (with names of mutual friends)

```cypher
MATCH (mercutio:Character {name: 'Mercutio'})-[:FRIENDS_WITH]-(mutual)-[:FRIENDS_WITH]-(c2:Character)
WHERE NOT (mercutio)-[:FRIENDS_WITH]-(c2)
AND mercutio <> c2
WITH c2, COLLECT(DISTINCT mutual.name) AS mutual_friend_names, COUNT(DISTINCT mutual) AS mutual_friends
RETURN 'Mercutio and ' + c2.name AS pair, mutual_friend_names, mutual_friends
ORDER BY mutual_friends DESC
```

### Mutual friends between Montague and all non-friends

```cypher
MATCH (montague:Character {name: 'Montague'})-[:FRIENDS_WITH]-(mutual)-[:FRIENDS_WITH]-(c2:Character)
WHERE NOT (montague)-[:FRIENDS_WITH]-(c2)
AND montague <> c2
RETURN 'Montague and ' + c2.name AS pair, COUNT(DISTINCT mutual) AS mutual_friends
ORDER BY mutual_friends DESC
```

### Generic query: Best friend recommendation for any character

Replace `'CHARACTER_NAME'` with the desired character name:

```cypher
MATCH (c1:Character {name: 'CHARACTER_NAME'})-[:FRIENDS_WITH]-(mutual)-[:FRIENDS_WITH]-(c2:Character)
WHERE NOT (c1)-[:FRIENDS_WITH]-(c2)
AND c1 <> c2
RETURN 'CHARACTER_NAME and ' + c2.name AS pair, COUNT(DISTINCT mutual) AS mutual_friends
ORDER BY mutual_friends DESC
```

Characters to check: Romeo, Benvolio, Prince Escalus, Paris, Juliet, Capulet, Friar Lawrence, The Nurse, Tybalt.