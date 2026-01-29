# COMP3008 - Workshop 3: Queries in Neo4j

## Data Setup (from Workshop 2)

### Load CSV Data

```cypher
-- Load Tweets
LOAD CSV WITH HEADERS FROM "file:///tweets.csv" AS csvLine
CREATE (:Tweet {tweetID: csvLine.tweetID, username: csvLine.username, text: csvLine.text, date: csvLine.date});

-- Load Users
LOAD CSV WITH HEADERS FROM "file:///users.csv" AS csvLine
CREATE (:User {username: csvLine.username, source: csvLine.source});

-- Load Hashtags
LOAD CSV WITH HEADERS FROM "file:///hashtags.csv" AS csvLine
CREATE (:Hashtag {tag: csvLine.hashtag});
```

### Create Indexes

```cypher
CREATE INDEX FOR (t:Tweet) ON (t.tweetID);
CREATE INDEX FOR (u:User) ON (u.username);
CREATE INDEX FOR (h:Hashtag) ON (h.tag);
```

### Create Relationships

```cypher
-- POSTS: links Users to Tweets they published
MATCH (t:Tweet), (u:User)
WHERE t.username = u.username
MERGE (u)-[:POSTS]->(t)
RETURN u, t;

-- TAGS: links Tweets to their Hashtags
LOAD CSV WITH HEADERS FROM "file:///tweets_and_hashtags.csv" AS csvLine
MATCH (t:Tweet {tweetID: csvLine.tweetID})
MATCH (h:Hashtag {tag: csvLine.hashtag})
MERGE (t)-[:TAGS]->(h);
```

---

## Exercise 1 - Query the dataset using `MATCH()`

### 1. Find the most *prolific* users (users that published the largest number of tweets)

```cypher
MATCH (u:User)-[:POSTS]->(t:Tweet)
RETURN u.username, COUNT(t) AS tweet_count
ORDER BY tweet_count DESC
```

### 2. List the five most prolific users

```cypher
MATCH (u:User)-[:POSTS]->(t:Tweet)
RETURN u.username, COUNT(t) AS tweet_count
ORDER BY tweet_count DESC
LIMIT 5
```

### 3. Find all tweets by @EHFoundation237 and their hashtags

```cypher
MATCH (u:User {username: '@EHFoundation237'})-[:POSTS]->(t:Tweet)-[:TAGS]->(h:Hashtag)
RETURN t.text, h.tag
```

---

## Exercise 2 - Social Graph

### Create the graph

```cypher
CREATE
(anders:Person {name: 'Anders'}),
(bossman:Person {name: 'Bossman'}),
(caesar:Person {name: 'Caesar'}),
(george:Person {name: 'George'}),
(david:Person {name: 'David'}),
(anders)-[:KNOWS]->(bossman),
(anders)-[:KNOWS]->(david),
(anders)-[:BLOCKS]->(caesar),
(bossman)-[:KNOWS]->(george),
(bossman)-[:KNOWS]->(david),
(caesar)-[:KNOWS]->(george),
(david)-[:BLOCKS]->(anders)
```

### 1. Find all people connected to Bossman

Uses undirected match (`-[r]-`) to find any relationship in either direction.

```cypher
MATCH (p:Person)-[r]-(bossman:Person {name: 'Bossman'})
RETURN p.name, type(r) AS relationship
```

### 2. Wildcard query; all names and relationships between all people

```cypher
MATCH (a:Person)-[r]->(b:Person)
RETURN a.name, type(r) AS relationship, b.name
```

---

## Exercise 3 - Pets Graph with `COLLECT`

### Create the graph

```cypher
CREATE
(andy:Swedish:Person {name: 'Andy', age: 36}),
(timothy:Person {name: 'Timothy', nickname: 'Tim', age: 25}),
(peter:Person {name: 'Peter', nickname: 'Pete', age: 35}),
(andy)-[:HAS_DOG {since: 2016}]->(:Dog {name:'Andy'}),
(timothy)-[:HAS_CAT {since: 2019}]->(:Cat {name:'Mittens'}),
(fido:Dog {name:'Fido'})<-[:HAS_DOG {since: 2010}]-(peter)-[:HAS_DOG {since: 2018}]->(:Dog {name:'Ozzy'}),
(fido)-[:HAS_TOY]->(:Toy {name:'Banana'})
```

### 1. Use `COLLECT` to find the owner of a cat called Mittens

```cypher
MATCH (p:Person)-[:HAS_CAT]->(c:Cat {name: 'Mittens'})
RETURN COLLECT(p.name) AS owner
```

### 2. Use `COLLECT` to find all pet names

```cypher
MATCH (p:Person)-[:HAS_DOG|HAS_CAT]->(pet)
RETURN COLLECT(pet.name) AS pet_names
```

---

## Exercise 4 - Twitter dataset with `WITH` and `COLLECT`

### 1. Find all users that have published more than 100 tweets

```cypher
MATCH (u:User)-[:POSTS]->(t:Tweet)
WITH u, COUNT(t) AS tweet_count
WHERE tweet_count > 100
RETURN u.username, tweet_count
ORDER BY tweet_count DESC
```

### 2. Find all users with more than 900 tweets and the tweets they published

```cypher
MATCH (u:User)-[:POSTS]->(t:Tweet)
WITH u, COLLECT(t.text) AS tweets, COUNT(t) AS tweet_count
WHERE tweet_count > 900
RETURN u.username, tweet_count, tweets
```

### 3. Find the most common hashtags

```cypher
MATCH (t:Tweet)-[:TAGS]->(h:Hashtag)
WITH h, COUNT(t) AS usage_count
RETURN h.tag, usage_count
ORDER BY usage_count DESC
```

### 4. Find the hashtags most used by @EHFoundation237

```cypher
MATCH (u:User {username: '@EHFoundation237'})-[:POSTS]->(t:Tweet)-[:TAGS]->(h:Hashtag)
WITH h, COUNT(t) AS usage_count
RETURN h.tag, usage_count
ORDER BY usage_count DESC
```

### 5. Find the top 20 most common hashtags and the tweets that contain them

```cypher
MATCH (t:Tweet)-[:TAGS]->(h:Hashtag)
WITH h, COLLECT(t.text) AS tweets, COUNT(t) AS usage_count
RETURN h.tag, usage_count, tweets
ORDER BY usage_count DESC
LIMIT 20
```
