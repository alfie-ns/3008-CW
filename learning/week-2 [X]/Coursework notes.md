This is a critical lecture as it bridges theory directly into the practical coursework mechanics.
Here is your intelligence dossier.

1. CRITICAL ASSESSMENT INTELLIGENCE [HIGHEST PRIORITY]
This section dictates exactly how you secure marks and avoid throwing them away.
Direct Coursework Alignment
 * The "One-Shot" Rule (CRITICAL): You must perform complex queries in a single execution.
   > "I am looking for complex queries done in one go. If you do split it out and do it into two or three, you will be penalised... You should be able to do the queries that I'm asking you to do in one line of code."
   > 
 * Relationship Properties Constraint:
   > "For your coursework, I don't want you to put any properties on the relationships. You can do this if you want to experiment outside, but you don't need to for the coursework."
   > 
 * Defining Relationships:
   > "For your coursework, please follow the ones [relationship definitions] I have given you." (Do not invent your own relationship types for the assignment; use the lecturer's schema).
   > 
 * Data Sets Mentioned:
   * Eurovision (Urban Sun): Nodes have properties (when, who won, where held).
   * Voting Data: Country info, who voted, points given.
Exam & Marking Pattern Recognition
 * The "Maths Marking" Style: The lecturer adopts a mathematical marking approach regarding data loading errors.
   > "If there is an issue with you loading in the data... I docked the marks in the first one, but none in the subsequent ones because it's an error that's been carried forward."
   > 
 * Data Integrity Warning:
   > "Think about the data. I do throw little curveballs like that." (Reference to students incorrectly removing duplicates in a previous year's music chart coursework).
   > 
2. The Complete ‘Alpha’ Brief: Comprehensive Directives
⭐⭐⭐ Critical Intelligence (Immediate Action Required)
 * Query Performance: The more complex the data, the slower relational databases become (order of \log_2). Graph databases (Neo4j) run in constant time once the starting index is found. This is why "one-shot" queries are mandatory.
 * The Collect Pitfall:
   * collect() [with brackets]: Removes null values.
   * collect [no brackets]: Keeps null values.
   * Context: Sometimes nulls are data (e.g., hidden crime locations). "Sometimes we want to remove null values, sometimes we don't."
 * Merge Function: Used for both querying (Match) and creating relationships. If the pattern exists, it does nothing; if not, it creates it.
⭐⭐ High Priority Concepts
 * Data Model Hierarchy:
   * Conceptual: Big picture, top-down, no tech details.
   * Logical: Adds detail, structure, and flow but generic (no specific hardware).
   * Physical: Specific hardware/software implementation.
 * Graph Terminology:
   * Nodes: Equivalent to records/rows.
   * Edges: Relationships/Links (Must have a type, must have a direction, must have a start and end node).
   * Properties: Key-value pairs stored on nodes (and optionally relationships, but not for this coursework).
⭐ Notable Warnings
 * "Intuitive" is a Trap: "Try to avoid intuitive tags because what makes sense to you won't make sense to somebody else."
 * Relationship Direction: There is no standardisation. Does a Tweet link to a Hashtag, or a Hashtag to a Tweet? It is up to the designer (you/the lecturer).
 * Dangling Arrows: "We can't have an end that goes nowhere... If you don't have an end node, Neo4j will throw up a nice error for you."
3. Exhaustive Topic Breakdown with Complete Quotation
Topic: The Purpose of Data Modelling
 * Definition: "Managing access and limiting access to the people who need it for their job is all part of the data model."
 * Why bother?: eliminating redundancies, GDPR compliance, creating a "single source of truth".
 * Lecturer’s Warning: "I won't be holding the university up as a pinnacle example... The ease at which you can get information is probably not as best it could be."
Topic: Types of Data Models
 * Relational: "Traditional tables of columns and rows... comforting... 70s everybody loves it."
 * Dimensional: "Less rigid... they love them in business... very, very closely knitted to that business need."
 * Entity Relationship (Network/Graph): "Structures is the graphical form. We use the shapes, boxes, nodes to represent data and then we have lines, arrows representing the relationships."
 * Object Orientated: Uses inheritance. "Cheap to run because all the functions and attributes can just be reused." Note: Lecturer finds it odd this isn't more popular given OO programming's dominance.
Topic: Graph Databases (Neo4j focus)
 * Structure: "No more rows, no more columns... A series of clusters collection nodes and edges."
 * Performance: "As soon as it finds the right index off, it squiggles in its path. So it runs in constant time."
 * Key Concept - Nodes: "Equivalent to that record or row in a database. Except this time not all our nodes may contain all the same information."
 * Key Concept - Relationships (Edges):
   > "Always must have a type... They must have a direction... There should always be a start and an end node."
   > 
Topic: Key Neo4j Functions
 * MERGE: "Fantastic kind of general purpose, does a lot of different things, be careful what it does." It ensures a pattern exists.
 * WITH: "We can manipulate any output before it gets passed into subsequent queries." Used to limit entries or create new variables to push down the pipeline.
 * COLLECT: "If we want to create everything into a single aggregated list."
4. Complete Lecturer’s Lexicon: Comprehensive Terminology Database
 * Single Source of Truth: A state where data is consistent across an organisation. Lecturer skepticism: "I want a second source of truth because I didn't trust the single source of truth."
 * Nodes (aka Vertices): The entities in the graph. "I am going to call them nodes. Be aware if you are reading around in the literature they may call them vertices."
 * Edges (aka Links/Relationships): The connections. "I'm going to call them edges... but they could also be called links."
 * Intuitive: A problematic term. "What's intuitive to me could be complete gobbledygook to somebody else."
 * Constant Time: The performance characteristic of a graph database query after the index is found.
 * Wildcard (*): "Keep throwing them forward, keep shoving them down through the pipeline." Used in WITH * to pass all variables.
5. Coursework Success Blueprint [ESSENTIAL SECTION]
Task-by-Task Alignment
 * Designing the Schema:
   * Do: Use the specific relationship types provided in the brief.
   * Do Not: Add properties to relationships (e.g., date of voting) for this specific assignment.
 * Writing Queries:
   * Requirement: Chain your queries. Use the WITH function to pass variables from one stage to the next.
   * Pattern: MATCH -> WITH (filter/transform) -> MATCH -> RETURN.
   * Avoid: Running a query, getting a result, copying that result, and writing a second query. This will lose marks.
Methodology Preferences
 * Step-by-Step Construction: "By all means, do them separately to begin with and you see what you should be getting, but they should be done as one."
 * Data Cleaning: Be extremely careful about removing duplicates.
   > "Can a song go back to being number one? Yes." (If you remove duplicates based on song title, you lose the re-entry data).
   > 
6. Hidden Curriculum Extraction
 * Lecturer's Interests:
   * Scooby Doo: Uses the "Gang" to explain relationships (Timmy is a dog, Shaggy is owner, etc.).
   * Crime Data: Has a morbid fascination ("If you want to seriously rethink your life choices, crime data is always a good one").
   * Ethics/Netflix: Interested in how complex data (profiles, watch lists) is structured.
 * Pet Peeves:
   * University IT systems ("I am definitely will not be holding the university up as a pinnacle example").
   * The word "Intuitive".
 * Philosophical Position: "Don't go down the rabbit hole straight away." She values the Conceptual Model (drawing it out) before touching code.
7. Complete Q&A and Interactive Moments
 * Scenario: Lecturer shows a graph of Scooby Doo characters.
   * Lecturer: "Do you recognise these characters?"
   * Student Response: (Positive identification).
   * Lecturer Note: "The first time I did this I used the famous five. There was a bit of confusion."
 * Scenario: Discussing relationship types.
   * Lecturer: "We could have Scrappy on there... Is it cousin?"
   * Student: "Yeah... They are colleagues as well."
   * Insight: Shows that multiple relationships can exist between two nodes (Cousin AND Colleague).
8. Computational Thinking Patterns
 * The "Pipeline" Mental Model: The lecturer views Neo4j queries as a flow of data. You grab data (MATCH), you manipulate/filter it (WITH), and you shove it to the next stage.
 * Debugging Philosophy:
   > "If they go wrong and you put it in your set exercises, I'm going to have to debug for you, so please don't."
   > 
   * Implication: Test your chained queries rigorously.
 * Data Reality vs. Data Model:
   * Real-world data is messy (e.g., crime locations being null for privacy).
   * The model must account for this (e.g., using collect without brackets to keep the nulls to show volume of crime even if location is unknown).
9. Meta-Learning Intelligence
 * Study Strategy:
   * Draw it first: "No words, picture to describe the structure... If somebody wanted to tell me how to set up a relational database, they're going to draw me a box."
   * Resources: Use the "Code along example" provided on the DLE (Digital Learning Environment) with the IMDb data. This is your training ground for MERGE, WITH, and COLLECT.