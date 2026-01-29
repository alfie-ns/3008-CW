# COMP3008: Big Data Analytics

- [ ] Write in LaTeX
- [ ] remember to utilise the `lecture-notes.md` from ALL the relevant lectures, dynamically whilst making the coursework
- [ ] Go as far as conceptually as possible, as far complex as the subject goes
- [ ] Make the code work ASAP and start talking about it using what's learnt in the module

**Strategic plan for first-class achievement (70%+)**

## Quick Overview

* **Assessment** : 30% Set Exercises (Neo4j) + 70% Report (Document Classification)
* **Set Exercises Due** : Monday 17th March 2025, 15:00
* **Report Due** : Friday 2nd May 2025, 15:00
* **Target** : First-class degree (70%+)
* **Key Focus** : Use EXACTLY what they're teaching us

## Assessment Breakdown & Strategy

### Part 1: Set Exercises (30%) - Neo4j Database

**Target: 85%+ (these are technical marks)**

**Exercise 1 (15 marks) - Database Creation**

- [ ] Create Neo4j database for UK chart data
- [ ] Must provide ALL commands in exact execution order
- [ ] Include index creation commands
- [ ] Data model: Artist -> Track -> Chart Position relationships

**Exercises 2-4 (5 marks each) - Cypher Queries [ ]**

* [ ] Exercise 2: Artists with 4+ weeks at #1 (descending order)
* [ ] Exercise 3: Ed Sheeran tracks average valence
* [ ] Exercise 4: Most common artist per year (chronological)

**Neo4j Strategy:**

```
1. [ ] Learn Cypher query language fundamentals
2. [ ] Practice LOAD CSV commands for data import
3. [ ] Master CREATE, MATCH, WHERE, ORDER BY, AGGREGATE functions
4. [ ] Test all queries before submission
5. [ ] Submit as plain text file (.txt) - CRITICAL!
```

### Part 2: Report (70%) - Document Classification

**Core Task** : Classify 8 text files (book chapters) into max 3 genres using big data techniques

**Report Structure (4500 words ±10%)**

#### 1. Introduction (500 words) - Set the Scene

* Brief overview of document classification in big data
* Explain the task: 8 books, 3 genres max
* Outline approach and methods to be used

#### 2. Overview of Classification Methods (1000 words) - Theory

**Must include AT LEAST 3 methods they're teaching:**

* **TF-IDF (Term Frequency-Inverse Document Frequency)**
* **K-Means Clustering**
* **Support Vector Machines (SVM)**
* **Naive Bayes Classification**
* **Hierarchical Clustering**
* **Latent Dirichlet Allocation (LDA) - Topic Modeling**

*Focus on what we learn in lectures, not random methods*

#### 3. Application of Methods (1500 words) - Implementation

**For each method:**

* Data preprocessing steps (tokenisation, stop words, etc.)
* Parameter selection and justification
* Implementation details (Python libraries used)
* Screenshots of code and outputs

#### 4. Results (1000 words) - Analysis

**Detailed analysis of each method:**

* Accuracy/performance metrics
* Visualisation of results (plots, confusion matrices)
* Comparison between methods
* Which books grouped together and why

#### 5. Conclusions (400 words) - Final Decision

* Final genre groupings with justification
* Best performing method and why
* Limitations and potential improvements

#### 6. Reference List (100 words) - Harvard Style

* Academic papers on document classification
* Books from reading list
* Reliable online sources

## Technologies & Tools to Master

### For Set Exercises:

* **Neo4j Desktop/Browser** : Graph database interface
* **Cypher Query Language** : Neo4j's query language
* **CSV Import** : LOAD CSV commands for data ingestion

### For Report:

* **Python** (they'll teach us this for big data):
  * pandas (data manipulation)
  * scikit-learn (machine learning algorithms)
  * nltk/spacy (natural language processing)
  * matplotlib/seaborn (visualisation)
* **Text preprocessing techniques**
* **Feature extraction methods**
* **Classification algorithms**

## Weekly Study Plan

### 1–3 Neo4j Foundations

- [ ] Install Neo4j Desktop (if not already done)
- [ ] Learn and document Cypher basics: CREATE; MATCH; WHERE
- [ ] Practice with small datasets to reinforce each clause
- [ ] Master LOAD CSV and aggregation functions (COUNT; SUM; AVG)

### 4–5 Advanced Ne[ ] o4j

* [ ] Write complex Cypher queries spanning multiple relationship hops
* [ ] Set up and test indexes for performance optimisation
* [ ] Complete at least three practice exercises of increasing complexity

### 6–7 Transition [ ] & Report Prep

* [ ] Begin reading on document-classification fundamentals
* [ ] Collect and organise academic references (aim for 8–10 solid papers)
* [ ] Sketch your report structure (Introduction; Methods; Results; Discussion)

### 8–9 Classificat[ ] ion Theory

* [ ] Learn TF-IDF and implement a toy example in Python
* [ ] Study clustering (K-Means; hierarchical) with sample data
* [ ] Review classification algorithms (SVM; Naive Bayes) and code small de[ ] mos

### 10 Preprocessing & First Met[ ] hod

* [ ] Preprocess your 8 book files (tokenise; clean; vectorise)
* [ ] Implement TF-IDF + one classifier (e.g. Naive Bayes); record baseline metrics

### 11 Additional Methods & Comparison

* [ ] Add at least two more classifiers (e.g. SVM; decision tree)
* [ ] Compare results: accuracy; precision; recall; F1
* [ ] Create visualisations (confusion matrices; bar charts of metrics)

### 12 Write & Finalise Report

* [ ] Draft full report using your structure; embed tables/figures
* [ ] Refine analysis and conclusions based on your comparisons
* [ ] Perfect referencing (Harvard style) and run spell-check
* [ ] Proofread, check word count and prepare for submission

---

### Set Exercises Success Factors:

* **Accuracy** : Commands must work exactly as provided
* **Completeness** : Include ALL necessary commands
* **Order** : Database creation must follow logical sequence
* **Results** : Queries must return correct, well-formatted answers

### Report Success Factors:

**Research Quality (10 marks):**

* Multiple academic sources (not just websites)
* Clear connection between sources and content
* Depth of understanding demonstrated

**Method Overview (10 marks):**

* At least 3 classification methods
* Evidence-based explanations
* Proper citations throughout

**Detailed Analysis (20 marks):**

* Thorough results description
* Appropriate evidence and examples
* Clear methodology explanation

**Sensible Grouping (20 marks):**

* Logical genre classifications
* Well-reasoned justifications
* Evidence-supported decisions

**Professional Presentation (10 marks):**

* Clear structure and writing
* Proper referencing (Harvard style)
* Word count compliance (+/- 10%)

## Key Success Strategies

### For Neo4j (30%):

1. **Practice Early** : Don't wait for lectures to end
2. **Test Everything** : Verify all commands work before submission
3. **Index Strategy** : Create logical indexes for performance
4. **Query Optimisation** : Use efficient Cypher patterns

### For Report (70%):

1. **Method Selection** : Use what we learn in lectures
2. **Academic Sources** : Prioritise peer-reviewed papers
3. **Evidence-Based** : Support every claim with data
4. **Clear Writing** : Concise, professional language
5. **Visual Impact** : Include charts, confusion matrices, clusters

## Common Pitfalls to Avoid

### Neo4j Mistakes:

* ❌ Forgetting to include index creation commands
* ❌ Wrong command order (database won't recreate)
* ❌ Submitting as PDF instead of .txt file
* ❌ Incomplete LOAD CSV commands

### Report Mistakes:

* ❌ Using methods not taught in the module
* ❌ Insufficient academic references
* ❌ Weak justification for final groupings
* ❌ Exceeding word count (automatic penalty)
* ❌ Missing word count statement (5 mark penalty)

## Resources & Tools

### Official COMP3008 Materials:

* Lecture slides and recordings
* Lab exercise examples
* Provided CSV files (UK charts data)
* Provided text files (8 books)

### Essential Software:

* **Neo4j Desktop** (free community edition)
* **Python** with Anaconda distribution
* **Jupyter Notebooks** for report analysis
* **Reference manager** (Zotero/Mendeley)

### Academic Databases:

* IEEE Xplore
* ACM Digital Library
* Google Scholar
* University library resources

## Success Formula

 **Neo4j (30%)** :

* Perfect technical execution = 25/30 marks
* Focus on accuracy over innovation

 **Report (70%)** :

* Strong academic research = 15/20 marks
* Thorough analysis = 35/40 marks
* Professional presentation = 10/10 marks

 **Total Target** : 75/100 = First-class degree! 🎯

---

## Final Tips

1. **Attend Every Lecture** : They'll give specific guidance on methods to use
2. **Use Office Hours** : Friday 10am-12pm for personalised help
3. **Follow Module Materials** : Don't overcomplicate with external methods
4. **Document Everything** : Keep detailed notes of your process
5. **Start Early** : Both assessments require significant time investment

 **Remember** : This is about demonstrating mastery of what they teach, not showing off external knowledge!
