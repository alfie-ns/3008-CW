COMP 3008 SET EXERCISES (Neo4j Queries)


Version: 2026.01.3 (VERIFY IS CORRECT VERSION)??

REMOVE BEFORE SUBMISSION:

- [ ] change this to .txt file

The "Year Before" Pattern: The central hint for the problem is to look at data from "A year ago" or "The year before." You must identify a specific pattern linked to this timeframe.
- No Domain Knowledge Required: You do not need to know anything about Eurovision to solve the problem (the lecturer explicitly states she doesn't either).
- The "Pony" Instruction: You are directed to "Make your pony better" (likely a transcription error for "Make your point better" or "Make your program better").
- Common Stumbling Block: This specific part of the coursework is a known difficulty; other students (specifically mentioned "Ryan") have had to ask about it despite claiming they understood it.
- Upcoming Resource: There will be a formal announcement and a recording released specifically clarifying this hint.

REMOVE REMOVE REMOVE BEFORE SUBMISSION

—---------------------------------------------------------------------------------------

Neo4j: a graph database management system that stores data as nodes (entities) and relationships (connections between entities), thereby enabling efficient traversal of highly connected datasets wherein traditional relational joins would instead be computationally expensive. Unlike tabular databases, Neo4j represents data as a property graph; nodes and relationships can hold key-value properties; queries are expressed in Cypher, a declarative pattern-matching language.

SET-EXERCISE 1.
Q: "Create a Neo4j database to store the data comprised in the CSV files. The database should respect the data model displayed in the example in the figure below, please note that the image below has had some nodes hidden for clarity. You have to provide all the commands needed to create the database and populate it with the data in the CSV files, and you must provide them in the exact order you propose to execute them. If you create indexes, you must also include the commands for index creation. Your database will be recreated, and the only way to do so is by following the commands that you will provide, in the order in which you provide them."

The database respects the specified data-model, with non-proporty releationships as abiding by Dr Ansell's instructions. The intermediate nodes i.e. `Entry` and `Vote`, store the detailed attributes of which would otherwise be properties on relationships.

1.1 Data Model

The data model centres on Year nodes representing each contest; it is connected to Location nodes via HOSTED_AT and to host Country nodes via HOSTED_BY. The winning entries are modelled as Entry nodes that store song, artist, running order and total points, linked from the year via Winning_Entry and to the performing country via PERFORMED_BY. The voting data uses Vote as an intermediate (in-between) node containing points and points' type, with Country nodes connected through GAVE and TO relationships, each vote linked to its year via Voting_Result. This intermediate node approach means you do not have to store properties on relationships to match Lauren's suggestion.

1.2 Database Creation commands

Execute the commands that follow in the exact order shown to recreate the database:

1.2.0- ## Clear existing data
    MATCH(n)DETACH DELETE n;

1.2.1- ## Create uniqueness constraints

    1.2.1a- ### Year Constraint
    ```
        CREATE CONSTRAINT year_unique IF NOT EXISTS
        FOR(y:Year)REQUIRE y.year IS UNIQUE;
    ```

    1.2.1b- ### Country Constraint
    ```
        CREATE CONSTRAINT country_unique IF NOT EXISTS
        FOR(c:Country)REQUIRE c.name IS UNIQUE;
    ```

    1.2.1c- ### Location Constraint
    ```
        CREATE CONSTRAINT location_unique IF NOT EXISTS
        FOR(l:Location)REQUIRE l.name IS UNIQUE;
    ```

1.2.2- ## Load Winners 
```
    LOAD CSV WITH HEADERS FROM 'file:///Eurovision_Winners.csv' AS row
    MERGE (y:Year {year: toInteger(row.Year)})
    MERGE (c:Country {name: toLower(trim(row.Country))})


- Intermediate entry node (Figure-1 Blue Node)
CREATE (e:Entry {
    song: row.Song,
    artist: row.Artist,
    running_order: toInteger(row.Running_Order),
    points: toInteger(row.Total_Points)
})

// Connect Year -> Entry -> Country
MERGE (y)-[:Winning_Entry]->(e)
MERGE (e)-[:PERFORMED_BY]->(c);
```

1.2.3- Load host countries (creates HOSTED_BY relationships)
```
    LOAD CSV WITH HEADERS FROM 'file:///eurovision_location.csv' AS row
    MATCH(y:Year {year: toInteger(row.Year)})
    MERGE(host:Country {name: toLower(trim(row.Country))})
    MERGE(y)-[:HOSTED_BY]->(host);
```

1.2.4- Load voting results
```
    LOAD CSV WITH HEADERS FROM 'file:///eurovision_results.csv' AS row
    MERGE(from:Country {name: toLower(trim(row.From))})
    MERGE(to:Country {name: toLower(trim(row.To))})
    MERGE(y:Year {year: toInteger(row.Year)})
    CREATE (v:Vote { // wher
        points: toInteger(row.Points),
        points_type: row.Points_type
    })
    CREATE(from)-[:GAVE]->(v)
    CREATE(v)-[:TO]->(to)
    CREATE(y)-[:Voting_Result]->(v);
```

An intermediate-node approach is the core design decision as Eurovision voting is a ternary relationship i.e. Country(A) gave X points \to Country B in Year Y. One cannot model this cleanly as a single edge because Cypher edges connect exactly two nodes; introducing a third dimension (the year) onto a relationship property would work syntactically but kills traversability. With Vote as an intermediate node, every dimension of the relationship is a first-class citizen you can MATCH on directly. Same logic applies to Entry — a song winning isn't a property of a country or a year, it's the intersection of both, so it earns its own node.
The MERGE/CREATE distinction matters: MERGE for Country, Year, and Location because duplicates are meaningful errors (would silently fracture the graph), CREATE for Vote and Entry because every row genuinely is a new instance — no two votes are "the same vote."

---

1.3 Design Rationale

Adherence to no properties on relationships contains intermediate nodes i.e. Entry and Votem instead of story propertiess such as...

1.3.1 NO RELATIONSHIP PROPERTIES:

SET-EXERCISE 2.
Q: "Produce a Neo4j query to list all the countries that have won the competition more than twice. The query should include the country and be listed in descending order, that is the country which has won the greatest number of times should be listed first, followed by the country which has the second greatest, and so on. Your answer must show the query followed by the result with the columns appropriately named."

The below takes the database and formats it in a way that can be interogated

    MATCH(y:Year)-[:Winning_Entry]->(e:Entry)-[:PERFORMED_BY]->(c:Country)
    WITH c.name AS Country, count(y) AS Wins
    WHERE Wins > 2
    RETURN Country, Wins
    ORDER BY Wins DESC

SET-EXERCISE 3.
Q: "Produce a Neo4j query to find all the host countries which then also went on to win the contest that year. The query should list the winning nations, the song they won with and the year in which they won returned in chronological order. You should submit the query and the result with the columns appropriately named."

    MATCH(y:Year)-[:HOSTED_BY]->(host:Country),
        (y)-[:Winning_Entry]->(e:Entry)-[:PERFORMED_BY]->(winner:Country)
    WHERE host = winner
    RETURN winner.name AS Winning_Nation, e.song AS Song, y.year AS Year
    ORDER BY Year ASC

SET-EXERCISE 4.
Q: "Produce a Neo4j query to identify all the persistent friendships between countries. The query should list both countries and the number of points given. The query result should be listed in phabetical order by the country giving the points. You should submit the query and the result with the columns appropriately named."

    MATCH (a:Country)-[:GAVE]->(v1:Vote)-[:TO]->(b:Country),
      (y1:Year)-[:Voting_Result]->(v1),
      (a)-[:GAVE]->(v2:Vote)-[:TO]->(b),
      (y2:Year)-[:Voting_Result]->(v2)
WHERE y2.year = y1.year - 1
WITH a, b, sum(v1.points) AS PointsGiven
RETURN a.name AS Country_Giving, b.name AS Country_Receiving, PointsGiven
ORDER BY Country_Giving ASC


The bidirectional matching ensures only mutual voting relationships are returned i.e. both countries have given points to the other, hence the *friendship*; the aggregated total then reflects the strength of that mutual relationship over the dataset’s timespan.

---

REFERENCES

- Neo4j (2025) Cypher Manual: Core concepts. Available at: https://neo4j.com/docs/cypher-manual/current/queries/concepts/ (Accessed: 7 February 2026).

APPENDIX

APPENDIX A: AI DECLERATION: (modified greatly reduced template included despite non-use)

I declare that I've used \textbf{no} AI tools listed below whilst preparing this assessment. I have read and understood the University of Plymouth's policy on the use of AI tools in assessment and confirm that my use falls within the coursework's allowed categories, i.e. 3008 set exercises's non-usage.

- [X] I understand that the ownership and responsibility for the academic integrity of this submitted assessment falls with me, the student.
- [X] I confirm that all details provide above are an accurate description of how AI was used for this assessment.
