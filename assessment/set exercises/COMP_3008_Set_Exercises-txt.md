COMP 3008 SET EXERCISES (Neo4j Queries)
Version: 5.24.0

- [ ] work out N in query 3 or 4
- [ ] allowed to check with google that the queries are correct 
- [ ] talk about results from Neo4j
- [ ] remove anywhere in the code where a space is not needed
- [ ] persistent friendship: continuous between two parties
- [ ] talk about and perhaps cite maths
- [ ] manually check the results are correct despite working
- [X] Write in LaTeX
- [ ] remember to utilise the `lecture-notes.md` from ALL the relevant lectures, dynamically whilst making the coursework
- [ ] Go as far as conceptually as possible, as far complex as the subject goes
- [ ] Make the code work ASAP and start talking about it using what's learnt in the module

- [ ] CHANGE TO .txt

The "Year Before" Pattern: The central hint for the problem is to look at data from "A year ago" or "The year before." You must identify a specific pattern linked to this timeframe.

- No Domain Knowledge Required: You do not need to know anything about Eurovision to solve the problem (the lecturer explicitly states she doesn't either).
- The "Pony" Instruction: You are directed to "Make your pony better" (likely a transcription error for "Make your point better" or "Make your program better").
- Common Stumbling Block: This specific part of the coursework is a known difficulty; other students (specifically mentioned "Ryan") have had to ask about it despite claiming they understood it.
- Upcoming Resource: There will be a formal announcement and a recording released specifically clarifying this hint.

REMOVE REMOVE REMOVE BEFORE SUBMISSION

---

Neo4j: a graph-database management system that stores data as nodes (entities) and relationships (connections between entities), thus enabling efficient traversal of highly connected datasets wherein traditional relational joins would be too computationally expensive. Unlike tabular databases, Neo4j represents data as a property graph; nodes and relationships can hold key-value properties; queries are expressed in Cypher, a declarative pattern-matching language.

SET-EXERCISE 1.
Q: "Create a Neo4j database to store the data comprised in the CSV files. The database should respect the data model displayed in the example in the figure below, please note that the image below has had some nodes hidden for clarity. You have to provide all the commands needed to create the database and populate it with the data in the CSV files, and you must provide them in the exact order you propose to execute them. If you create indexes, you must also include the commands for index creation. Your database will be recreated, and the only way to do so is by following the commands that you will provide, in the order in which you provide them."

1.1 Data Model
The database respects the brief-specified data model, using intermediate nodes (Entry and Vote) to store detailed attributes to adhere to "no properties on relationships."

The model centres on Year nodes representing each contest, connected to Location nodes via HOSTED_AT. The winning entries are modelled as Entry nodes (storing song, artist, running order and total points) linked from the year via Winning_Entry and to the performing country via PERFORMED_BY.

The voting data uses a Vote intermediate node containing the points and points_type. Country nodes connect to the Vote node via GAVE and TO relationships. Each Vote is linked to its Year via Voting_Result. This avoids placing properties on edges, ensuring the graph remains in a valid property graph schema without data loss.

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

1.2.3- Load Locations (fulfils brief requirement to process all CSVs)
    // The 'Country' column duplicates winner data wherein only Location is extracted.
    // MERGE safely deduplicates data already captured in 1.2.2.
    LOAD CSV WITH HEADERS FROM 'file:///eurovision_location.csv' AS row
    MATCH(y:Year {year: toInteger(row.Year)})
    MERGE(l:Location {name: toLower(trim(row.Location))})
    MERGE(y)-[:HOSTED_AT]->(l);

1.2.4- Load voting results (creates Vote intermediate nodes)
    // The Country column contains host city slugs e.g. basel and malmo i.e. not country names,
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

    // Eurovision's implicit hosting rule: the winner of Year N hosts Year N+1.
    // A "host winner" is therefore a country that won Year N (earning the hosting
    // right) and also won Year N+1 (the contest it hosted).
    //
    // Implementation: traverse two Winning_Entry chains anchored on the same
    // Country node (c). The WHERE clause enforces strict year adjacency (N+1),
    // which maps directly onto the hosting rule without needing a separate
    // HOSTED_AT traversal.
    MATCH (y1:Year)-[:Winning_Entry]->(:Entry)-[:PERFORMED_BY]->(c:Country),
          (y2:Year)-[:Winning_Entry]->(e:Entry)-[:PERFORMED_BY]->(c)
    WHERE y2.year = y1.year + 1    // y1 = Year N (the win that confers host status)
                                   // y2 = Year N+1 (the hosted contest)
    RETURN c.name  AS Winning_Nation,
           e.song  AS Song,
           y2.year AS Year
    ORDER BY Year ASC

3.1 Expected results (5 rows, verified against raw CSV data):

    | Winning_Nation | Song                   | Year |
    |----------------|------------------------|------|
    | spain          | "Vivo cantando"        | 1969 |
    | luxembourg     | "Tu te reconnaitras"   | 1973 |
    | israel         | "Hallelujah"           | 1979 |
    | ireland        | "In Your Eyes"         | 1993 |
    | ireland        | "Rock 'n' Roll Kids"   | 1994 |

    Note: Country names are stored lowercase via toLower(trim(...)) in 1.2.2.

3.2 Empirical cross-check (raw CSV evidence for each result):

    1969 Spain:     Won 1968 ("La, la, la", London) → hosted 1969 Madrid (Spain) → won 1969 ("Vivo cantando") ✓
                    Special case: 1969 was a 4-way tie (Spain/UK/Netherlands/France). Only Spain
                    won the previous year (1968), so only Spain satisfies the consecutive-win
                    condition. The query handles this correctly via Country node identity.

    1973 Luxembourg: Won 1972 ("Apres toi", Edinburgh) → hosted 1973 Luxembourg city → won 1973 ("Tu te reconnaitras") ✓

    1979 Israel:    Won 1978 ("A-Ba-Ni-Bi", Paris) → hosted 1979 Jerusalem (Israel) → won 1979 ("Hallelujah") ✓

    1993 Ireland:   Won 1992 ("Why Me?", Malmo) → hosted 1993 Millstreet (Ireland) → won 1993 ("In Your Eyes") ✓

    1994 Ireland:   Won 1993 ("In Your Eyes", Millstreet) → hosted 1994 Dublin (Ireland) → won 1994 ("Rock 'n' Roll Kids") ✓

3.3 Rule-break years (actual host ≠ previous year's winner):

    The hosting rule breaks when a winning country declines or is unable to host
    and another broadcaster steps in. Determined by mapping each host city to its
    country and comparing against the prior year's winner:

    | Year | Host city  | Actual host     | Expected host (prev winner) | Historical reason                          |
    |------|------------|-----------------|-----------------------------|--------------------------------------------|
    | 1957 | Frankfurt  | Germany         | Switzerland (1956)          | Switzerland declined; Germany deputised    |
    | 1960 | London     | United Kingdom  | Netherlands (1959)          | Netherlands passed hosting to UK           |
    | 1963 | London     | United Kingdom  | France (1962)               | France declined; UK hosted again           |
    | 1972 | Edinburgh  | United Kingdom  | Monaco (1971)               | Monaco lacked broadcasting infrastructure  |
    | 1974 | Brighton   | United Kingdom  | Luxembourg (1973)           | Luxembourg declined due to cost            |
    | 1980 | The Hague  | Netherlands     | Israel (1979)               | Israel declined (cost/conflict concerns)   |
    | 2023 | Liverpool  | United Kingdom  | Ukraine (2022)              | Ukraine at war; UK hosted on their behalf  |

3.4 Does the query silently fail for any rule-break year?

    No. For a silent failure to occur, the same country would need to have won
    in both Year N-1 and Year N in a rule-break year, which would cause the query
    to return a false positive (a "host winner" that did not actually host).
    Verified exhaustively against the CSV:

    | Rule-break year | Prev winner    | Actual year winner | Same country? | Silent failure? |
    |-----------------|----------------|--------------------|---------------|-----------------|
    | 1957            | Switzerland    | Netherlands        | No            | None            |
    | 1960            | Netherlands    | France             | No            | None            |
    | 1963            | France         | Denmark            | No            | None            |
    | 1972            | Monaco         | Luxembourg         | No            | None            |
    | 1974            | Luxembourg     | Sweden             | No            | None            |
    | 1980            | Israel         | Ireland            | No            | None            |
    | 2023            | Ukraine        | Sweden             | No            | None            |

    In every rule-break year the prior winner and the actual winner are different
    countries, so the y2.year = y1.year + 1 + same-Country constraint matches
    zero rows — which is empirically correct (no actual host winner existed).

    One structural limitation exists independent of rule-break years: the query
    uses y2.year = y1.year + 1, which cannot bridge the 2020 COVID cancellation
    gap (2019 → 2021). If the 2019 winner (Netherlands) had also won in 2021,
    the query would silently miss it because 2021 ≠ 2019 + 1. Since Italy won
    2021, this limitation has no impact on the actual results.

---

SET-EXERCISE 4.
Q: "Produce a Neo4j query to identify all the persistent friendships between countries. The query should list both countries and the number of points given. The query result should be listed in alphabetical order by the country giving the points. You should submit the query and the result with the columns appropriately named."

- [ ] work out optimal years threshold for "persistence" (15 as starting point; experiment with 10, 20, 25 etc.

    MATCH (source:Country)-[:GAVE]->(v:Vote)-[:TO]->(target:Country),
          (y:Year)-[:Voting_Result]->(v)
    WITH source, target, count(DISTINCT y) AS Years_Voted, sum(v.points) AS Total_Points
    WHERE Years_Voted >= 15
    RETURN source.name AS Country_Giving, target.name AS Country_Receiving, Total_Points
    ORDER BY Country_Giving ASC, Total_Points DESC; // second sort shows highest-value friendships first within each alphabetical group

To mathematically codify "persistence", this query traverses the temporal dimension to calculate the distinct number of years a voting interaction occurred (`count(DISTINCT y)`). As Charron (2013) details, persistent friendships are commonly identified by analysing pairwise voting to detect "systematic collusive voting patterns" (5.2. Friendship-networks). By enforcing a strict threshold of at least (N) distinct contest years, the query filters out sporadic high-point exchanges and recent split-voting noise, isolating only genuine, long-term voting alliances. The alphabetical primary ordering fulfils the brief's requirement, whilst the secondary descending sort mathematically spotlights the strongest weighted interaction within each donor's friendship cluster.

---

REFERENCES

- Charron, N. (2013). Impartiality, friendship-networks and voting behavior: Evidence from voting patterns in the Eurovision Song Contest. Social Networks, 35(3), 484-497. Available at: https://doi.org/10.1016/j.socnet.2013.05.005

APPENDIX

APPENDIX A: AI DECLARATION:

I declare that I've used the AI tools listed below whilst preparing this assessment. I've read and understood the University of Plymouth's policy on the use of AI tools in assessment and confirm that my use falls within the coursework's allowed categories, i.e. {NON-USE}

- [X] I understand that the ownership and responsibility for the academic integrity of this submitted assessment falls with me, the student.
- [X] I confirm that all details provided above are an accurate description of how AI was used for this assessment.
