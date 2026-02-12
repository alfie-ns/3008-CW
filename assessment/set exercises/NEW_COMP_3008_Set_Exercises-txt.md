COMP 3008 SET EXERCISES (Neo4j Queries)
Version: 5.24.0

- [ ] talk about results from Neo4j
- [ ] change to .txt file
- [ ] manually check the results are correct despite working

The "Year Before" Pattern: The central hint for the problem is to look at data from "A year ago" or "The year before." You must identify a specific pattern linked to this timeframe.

- No Domain Knowledge Required: You do not need to know anything about Eurovision to solve the problem (the lecturer explicitly states she doesn't either).
- The "Pony" Instruction: You are directed to "Make your pony better" (likely a transcription error for "Make your point better" or "Make your program better").
- Common Stumbling Block: This specific part of the coursework is a known difficulty; other students (specifically mentioned "Ryan") have had to ask about it despite claiming they understood it.
- Upcoming Resource: There will be a formal announcement and a recording released specifically clarifying this hint.

REMOVE REMOVE REMOVE BEFORE SUBMISSION

---

Neo4j: a graph database management system that stores data as nodes (entities) and relationships (connections between entities), thereby enabling efficient traversal of highly connected datasets wherein traditional relational joins would instead be computationally expensive. Unlike tabular databases, Neo4j represents data as a property graph; nodes and relationships can hold key-value properties; queries are expressed in Cypher, a declarative pattern-matching language.

SET-EXERCISE 1.
Q: "Create a Neo4j database to store the data comprised in the CSV files. The database should respect the data model displayed in the example in the figure below, please note that the image below has had some nodes hidden for clarity. You have to provide all the commands needed to create the database and populate it with the data in the CSV files, and you must provide them in the exact order you propose to execute them. If you create indexes, you must also include the commands for index creation. Your database will be recreated, and the only way to do so is by following the commands that you will provide, in the order in which you provide them."

1.1 Data Model
The database respects the specified data model, using intermediate nodes (Entry and Vote) to store detailed attributes to adhere to the principle of "no properties on relationships."

The model centres on Year nodes representing each contest, connected to Location nodes via HOSTED_AT and to host Country nodes via HOSTED_BY. The winning entries are modelled as Entry nodes (storing song, artist, running order and total points) linked from the year via Winning_Entry and to the performing country via PERFORMED_BY.

The voting data uses a Vote intermediate node containing the `points` and `points_type`. Country nodes connect to the Vote node via GAVE and TO relationships. Each Vote is linked to its Year via Voting_Result. This avoids placing properties on edges, ensuring the graph remains in a valid property graph schema without data loss.

1.2. Database Creation commands

Ensure commands that follow are executed in the exact order shown to recreate the database:

1.2.0- Clear existing data
    MATCH (n) DETACH DELETE n;

1.2.1- Create uniqueness constraints for Year, Country, and Location nodes if they do not already exist
    // Constraints to ensure data integrity and improve query performance
    CREATE CONSTRAINT year_unique IF NOT EXISTS FOR (y:Year) REQUIRE y.year IS UNIQUE;
    CREATE CONSTRAINT country_unique IF NOT EXISTS FOR (c:Country) REQUIRE c.name IS UNIQUE;
    CREATE CONSTRAINT location_unique IF NOT EXISTS FOR (l:Location) REQUIRE l.name IS UNIQUE;

1.2.2- Load Winners (creates/initialises Year, Country, Location, Entry nodes with their respective properties)
    LOAD CSV WITH HEADERS FROM 'file:///Eurovision_Winners.csv' AS row
    MERGE(y:Year {year: toInteger(row.Year)})
    MERGE(c:Country {name: toLower(trim(row.Country))})
    MERGE(l:Location {name: toLower(trim(row.Location))})
    CREATE(e:Entry {
        song: row.Song,
        artist: row.Artist,
        running_order: toInteger(row.Running_Order),
        total_points: toInteger(row.Total_Points)
    })
    MERGE(y)-[:HOSTED_AT]->(l)
    CREATE(y)-[:Winning_Entry]->(e)
    CREATE(e)-[:PERFORMED_BY]->(c);

1.2.3- Load host countries (creates HOSTED_BY relationships)
    LOAD CSV WITH HEADERS FROM 'file:///eurovision_location.csv' AS row
    MATCH(y:Year {year: toInteger(row.Year)})
    MERGE(host:Country {name: toLower(trim(row.Country))})
    MERGE(y)-[:HOSTED_BY]->(host);

1.2.4- Load voting results (creates Vote intermediate nodes)
    LOAD CSV WITH HEADERS FROM 'file:///eurovision_results.csv' AS row
    MERGE(from:Country {name: toLower(trim(row.From))})
    MERGE(to:Country {name: toLower(trim(row.To))})
    WITH row, from, to
    MATCH(y:Year {year: toInteger(row.Year)})
    CREATE(v:Vote {
        points: toInteger(row.Points),
        points_type: row.Points_type
    })
    CREATE(from)-[:GAVE]->(v)
    CREATE(v)-[:TO]->(to)
    CREATE(y)-[:Voting_Result]->(v);

    An intermediate-node approach is the core design decision as Eurovision voting is a ternary relationship i.e. Country(A) gave X points to Country B in Year Y. One cannot model this cleanly as a single edge because Cypher edges connect exactly two nodes; introducing a third dimension (the year) onto a relationship property would work syntactically but limits traversability, i.e., it minimises one's ability to pattern-match on the temporal dimension as you cannot write`MATCH (y:Year)-[:Voting_Result]->(v)` if the year is buried inside an edge property instead of being a node in its own right. With Vote as an intermediate node, every dimension of the relationship is a first-class citizen you can `MATCH` on directly. Same logic applies to Entry, a song winning is not a property of a country or a year,  it's the intersection of both, so it earns its own node.

    The MERGE/CREATE distinction matters: MERGE for Country, Year, and Location because duplicates are meaningful errors (would silently fracture the graph), CREATE for Vote and Entry because every row is a new instance and thus two votes are "the same vote." because each .csv row represents a unique-distinct voting event; MERGE would wrongly collapse rows sharing identical point values into a data-losing single node

1.3. Design Rationale

1.3.1 Handling Relationship Properties (Graph Reification)

Adherence to the no-properties-on-relationships constraint necessitates use of intermediate nodes. In a standard property graph, voting would typically be modelled as an edge `(Country)-[:VOTED_FOR {points: 12}]->(Country)`. However, compliance with this constraint means the relationship must be reified (the edge gets promoted to a first-class node capable of holding properties).

---

The pattern (`(Country)-[:GAVE]->(Vote)-[:TO]->(Country)`) creates a star schema around the interaction. This allows the `Vote` node to hold properties (points, type) and connects it to the `Year` context. This approach, known as reification, not only solves the constraint issue but also improves database extensibility; future attributes (jury details) can be added to the Vote node without refactoring the graph schema.

SET-EXERCISE 2.
Q: "Produce a Neo4j query to list all the countries that have won the competition more than twice. The query should include the country and be listed in descending order, that is the country which has won the greatest number of times should be listed first, followed by the country which has the second greatest, and so on. Your answer must show the query followed by the result with the columns appropriately named."

    MATCH(y:Year)-[:Winning_Entry]->(e:Entry)-[:PERFORMED_BY]->(c:Country)
    WITH c.name AS Country, count(y) AS Wins
    WHERE Wins > 2
    RETURN Country, Wins
    ORDER BY Wins DESC

---

SET-EXERCISE 3.
Q: "Produce a Neo4j query to find all the host countries which then also went on to win the contest that year. The query should list the winning nations, the song they won with and the year in which hey won returned in chronological order. You should submit the query and the result with the columns appropriately named."

    MATCH (y1:Year)-[:Winning_Entry]->(:Entry)-[:PERFORMED_BY]->(c:Country),
      (y2:Year)-[:Winning_Entry]->(e:Entry)-[:PERFORMED_BY]->(c)
    WHERE y2.year = y1.year + 1
    RETURN c.name AS Winning_Nation, e.song AS Song, y2.year AS Year
    ORDER BY Year ASC



This query works on Eurovision's hosting rule: the winner of Year N hosts Year N+1. By matching countries that won in consecutive years (y1 and y1+1), you can identify cases where a country won whilst hosting, since their y1 victory made them the y2 host the next time round.

---

SET-EXERCISE 4.
Q: "Produce a Neo4j query to identify all the persistent friendships between countries. The query should list both countries and the number of points given. The query result should be listed in alphabetical order by the country giving the points. You should submit the query and the result with the columns appropriately named."

    MATCH (source:Country)-[:GAVE]->(v:Vote)-[:TO]->(target:Country)
    WITH source, target, sum(v.points) AS Total_Points
    RETURN source.name AS Country_Giving, target.name AS Country_Receiving, Total_Points
    ORDER BY Country_Giving ASC, Total_Points DESC; // second sort shows highest-value friendships first within each alphabetical group

In network analysis a "persistent friendship" is quantified by the cumulative weight of interactions over time. As Charron (2013) details, this is commonly identified by analysing pairwise voting to detect "systematic collusive voting patterns" (5.2. Friendship-networks). By summing points across all years for each country pair, this query identifies enduring alliances, revealing which countries consistently support each other in the contest. The alphabetical ordering by the giving country allows easy reference, whilst the secondary ordering by total points highlights the strength of the friendships within each group.

---

REFERENCES

- Charron, N. (2013). Impartiality, friendship-networks and voting behavior: Evidence from voting patterns in the Eurovision Song Contest. Social Networks, 35(3), 484-497. Available at: https://doi.org/10.1016/j.socnet.2013.05.005

APPENDIX

APPENDIX A: AI DECLARATION:

I declare that I've used the AI tools listed below whilst preparing this assessment. I've read and understood the University of Plymouth's policy on the use of AI tools in assessment and confirm that my use falls within the coursework's allowed categories, i.e. {NON-USE}

- [X] I understand that the ownership and responsibility for the academic integrity of this submitted assessment falls with me, the student.
- [X] I confirm that all details provided above are an accurate description of how AI was used for this assessment.
