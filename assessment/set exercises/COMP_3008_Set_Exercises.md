---
title: "COMP3008: Set Exercises"
header-includes:
  - \usepackage{graphicx}
  - \usepackage{caption}
  - \usepackage{tikz}
  - \usetikzlibrary{positioning, arrows.meta}
  - \usepackage{xcolor}
  - \usepackage{float}
  - \usepackage{array}
  - \usepackage{tabularx}
  - \usepackage{mdframed}
  - \usepackage{booktabs}
  - \usepackage{pgfplots}
  - \pgfplotsset{compat=1.18}
  - \usepackage{listings}
  - \usepackage{hyperref}
  - \usepackage{multirow}
  - |
      \lstdefinelanguage{Cypher}{
        keywords={MATCH, MERGE, CREATE, RETURN, WITH, WHERE, ORDER, BY, DESC, ASC, LOAD, CSV, HEADERS, FROM, AS, SET, CONSTRAINT, UNIQUE, IF, NOT, EXISTS, FOR, REQUIRE, IS, COUNT, LIMIT, AND, OR, IN, COLLECT, DELETE, DETACH, OPTIONAL, UNWIND, CASE, WHEN, THEN, ELSE, END},
        keywordstyle=\color{blue}\bfseries,
        ndkeywords={toInteger, toLower, trim, sum, avg, count, collect, size, length, type, id, labels, keys, properties},
        ndkeywordstyle=\color{teal}\bfseries,
        sensitive=false,
        comment=[l]{//},
        commentstyle=\color{gray}\itshape,
        stringstyle=\color{red},
        morestring=[b]',
        morestring=[b]"
      }
      \lstset{
        language=Cypher,
        numbers=left,
        breaklines=true,
        breakatwhitespace=true,
        postbreak=\mbox{\textcolor{gray}{$\hookrightarrow$}\space},
        basicstyle=\ttfamily\small,
        columns=flexible,
        escapeinside={(*@}{@*)},
        showstringspaces=false
      }
---
# TODO

- [ ] extract Lauren’s code and code alike but perhaps better

- [ ] relationship in caps

- [ ] complex one-shot queries {…}

 - [ ] LaTeX diagram that has fully context within cw  

- [ ] remember to utilise the `lecture-notes.md` from ALL the relevant lectures notes, dynamically whilst making the coursework
- [ ] Go as far as conceptually as possible, as far complex as the subject goes
- [ ] Make the code work ASAP and start talking about it using what's learnt in the module

## 1. Set-exercise 1

- [ ] image/diagram of data model from cw brief
- [ ] add in concise comments to the code somehow

\begin{mdframed}[leftline=true, rightline=false, topline=false, bottomline=false, linewidth=2pt, linecolor=gray]
\textit{- [X] Create a Neo4j database to store the data comprised in the CSV files. The database should respect the data model displayed in the example in the figure below, please note that the image below has had some nodes hidden for clarity. You have to provide all the commands needed to create the database and populate it with the data in the CSV files, and you must provide them in the exact order you propose to execute them. If you create indexes, you must also include the commands for index creation. Your database will be recreated, and the only way to do so is by following the commands that you will provide, in the order in which you provide them.}
\end{mdframed}

The database respects the specified data-model, with **no properties on relationships** as per Lauren's instructions. The intermediate nodes i.e. `Entry` and `Vote`, store the detailed attributes of which would otherwise be properties on relationships.

### 1.1 Data Model

\begin{figure}[H]
\centering
\begin{tikzpicture}[
    node distance=2.5cm,
    every node/.style={font=\small},
    entity/.style={circle, draw=blue!60, fill=blue!10, thick, minimum size=1.2cm},
    intermediate/.style={circle, draw=orange!60, fill=orange!10, thick, minimum size=1.2cm},
    rel/.style={-{Stealth[length=2mm]}, thick}
]
    % Nodes
    \node[entity] (year) {Year};
    \node[entity, right=3cm of year] (location) {Location};
    \node[entity, below=2cm of year] (country) {Country};
    \node[intermediate, right=3cm of country] (entry) {Entry};
    \node[intermediate, below=2cm of country] (vote) {Vote};

    % Relationships
    \draw[rel] (year) -- node[above] {\footnotesize HOSTED\_AT} (location);
    \draw[rel] (year) -- node[left] {\footnotesize Winning\_Entry} (entry);
    \draw[rel] (entry) -- node[above] {\footnotesize PERFORMED\_BY} (country);
    \draw[rel] (country) -- node[left] {\footnotesize GAVE} (vote);
    \draw[rel] (vote) to[bend left=30] node[right] {\footnotesize TO} (country);
    \draw[rel] (year) to[bend right=40] node[left] {\footnotesize HAD} (vote);
\end{tikzpicture}
\caption{Eurovision Database Data Model (no relationship properties)}
\end{figure}

**Nodes:**

\begin{tabular}{|l|l|}
\hline
\textbf{Node Label} & \textbf{Properties} \\
\hline
\texttt{Year} & \texttt{year} (integer) \\
\hline
\texttt{Country} & \texttt{name} (string, lowercase) \\
\hline
\texttt{Location} & \texttt{name} (string, lowercase) \\
\hline
\texttt{Entry} & \texttt{song}, \texttt{artist}, \texttt{running\_order}, \texttt{total\_points} \\
\hline
\texttt{Vote} & \texttt{points}, \texttt{points\_type} \\
\hline
\end{tabular}

**Relationships (no properties):**

\begin{tabular}{|l|l|}
\hline
\textbf{Relationship} & \textbf{Pattern} \\
\hline
\texttt{HOSTED\_AT} & (Year)-[:HOSTED\_AT]->(Location) \\
\hline
\texttt{Winning\_Entry} & (Year)-[:Winning\_Entry]->(Entry) \\
\hline
\texttt{PERFORMED\_BY} & (Entry)-[:PERFORMED\_BY]->(Country) \\
\hline
\texttt{GAVE} & (Country)-[:GAVE]->(Vote) \\
\hline
\texttt{TO} & (Vote)-[:TO]->(Country) \\
\hline
\texttt{HAD} & (Year)-[:HAD]->(Vote) \\
\hline
\end{tabular}

### 1.2 Database Creation Commands

Execute the commands that follow in the exact order shown to recreate the database.

**Step 0- Clear existing data (clean slate)**

\begin{lstlisting}
MATCH (n) DETACH DELETE n; // match to all nodes then detatch their relationships and delete their nodes
\end{lstlisting}

**Step 1- Create uniqueness constraints**

\begin{lstlisting}
CREATE CONSTRAINT year_unique IF NOT EXISTS // uniquely constrain year property on Year nodes if it doesn't already exist
FOR (y:Year) REQUIRE y.year IS UNIQUE; // require unique Year.year across all :Year nodes

CREATE CONSTRAINT country_unique IF NOT EXISTS
FOR (c:Country) REQUIRE c.name IS UNIQUE;

CREATE CONSTRAINT location_unique IF NOT EXISTS
FOR (l:Location) REQUIRE l.name IS UNIQUE;
\end{lstlisting}

**Step 2- Load Eurovision Winners data**

Creates `Year`, `Country`, `Location`, and `Entry` nodes. Establishes `HOSTED_AT`, `Winning_Entry`, and `PERFORMED_BY` relationships. Note \texttt{eurovision\_location.csv} is not loaded separately as it is a strict subset of this file (*1.3 Design Rationale*).

\begin{lstlisting}
LOAD CSV WITH HEADERS FROM 'file:///Eurovision_Winners.csv' AS row
MERGE (y:Year {year: toInteger(row.Year)})
MERGE (c:Country {name: toLower(trim(row.Country))})
MERGE (l:Location {name: toLower(trim(row.Location))})
CREATE (e:Entry {
    song: row.Song,
    artist: row.Artist,
    running_order: toInteger(row.Running_Order),
    total_points: toInteger(row.Total_Points)
})
MERGE (y)-[:HOSTED_AT]->(l)
CREATE (y)-[:Winning_Entry]->(e)
CREATE (e)-[:PERFORMED_BY]->(c);
\end{lstlisting}

**Step 3- Load Voting Results data**

Creates `Vote` nodes and `Country` nodes for all voting participants. Establishes GAVE, TO, and HAD relationships.

\begin{lstlisting}
LOAD CSV WITH HEADERS FROM 'file:///eurovision_results.csv' AS row
MERGE (from:Country {name: toLower(trim(row.From))})
MERGE (to:Country {name: toLower(trim(row.To))})
MERGE (y:Year {year: toInteger(row.Year)})
CREATE (v:Vote {
    points: toInteger(row.Points),
    points_type: row.Points_type
})
CREATE (from)-[:GAVE]->(v)
CREATE (v)-[:TO]->(to)
CREATE (y)-[:HAD]->(v);
\end{lstlisting}

### 1.3 Design Rationale

1. **No relationship properties**: Per Lauren's requirement, all detailed attributes are stored on intermediate nodes (`Entry` for winning song details, `Vote` for voting details) rather than on relationships.

2. **Case normalisation**: Country names are converted to lowercase using `toLower(trim(...))` to ensure consistency between the two CSV files (Winners uses Title Case, Results uses lowercase).

3. **Constraints first**: Uniqueness constraints are created before data loading to ensure data integrity and provide index support for MERGE operations.

4. **MERGE vs CREATE**: MERGE is used for entities that should be unique (Year, Country, Location), whilst CREATE is used for entities where duplicates are expected (Entry, Vote, and their relationships).

5. **eurovision\_location.csv not loaded**: This file contains only Year, Country, and Location columns---a strict subset of \texttt{Eurovision\_Winners.csv}. Both files identically skip 2020 (cancelled due to COVID-19), so no unique Year or Location data exists in the location file. Loading it would create redundant MERGE operations with no effect.

## 2. Set-exercise 2

## 3. Set-exercise 3

## 4. Set-exercise 4

# Appendices

## Appendix A: ...

## Appendix B: 5-Minute Video Demo

- YouTube link: [test](test)

## Appendix C: AI Declaration

\begin{figure}[H]
\centering
\includegraphics[width=0.55\textwidth]{image/ai-decl.png}
\caption{Student Declaration of AI Tool use in this Assessment Table}
\end{figure}

I declare that I've used the AI tools listed below whilst preparing this assessment. I've read and understood the University of Plymouth's policy on the use of AI tools in assessment and confirm that my use falls within the coursework's allowed categories, i.e. \textbf{A2 (Planning and Structuring Projects)} and \textbf{A4 (Research Assistance)}.

\renewcommand{\arraystretch}{1.1}
\setlength{\tabcolsep}{4pt}

\begin{tabular}{|>{\raggedright\arraybackslash}p{3.2cm}|
                >{\raggedright\arraybackslash}p{8cm}|
                >{\raggedright\arraybackslash}p{4cm}|}
\hline
\textbf{AI Tool Used} & \textbf{Purpose of Use} & \textbf{Extent of Use} \\
\hline
ChatGPT & Finding relevant pages to read in the paper \textbf{(A4)} & Few times if the paper is too long \\
\hline
ChatGPT & General conversations via web-search AI about prevalent papers to read about how the topics relates to others' studies \textbf{(A4)} & Few times at the end \\
\hline
\end{tabular}

- [X] I understand that the ownership and responsibility for the academic integrity of this submitted assessment falls with me, the student.
- [X] I confirm that all details provide above are an accurate description of how AI was used for this assessment.
