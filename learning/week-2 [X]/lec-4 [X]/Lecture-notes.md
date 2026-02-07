BRITISH AI Lecture Intelligence System (v3.0 - Maximum Extraction Protocol)
Core Philosophy: Total Strategic Capture with 80/20 Prioritisation
Target: Coursework Hint Session (Eurovision & "The Pattern")
1. CRITICAL ASSESSMENT INTELLIGENCE [HIGHEST PRIORITY]
Direct Coursework Alignment (Exercise 3 & 4 Focus):
 * The "Hidden" Logic (Exercise 3): The lecturer’s comments about "A year ago" and "The year before" are the strategic key to solving Exercise 3 ("Find host countries who won that same year").
   * The Insight: In Eurovision rules, the Host of Year X is the Winner of Year X-1.
   * The "Pattern": Therefore, finding a "Host who won" is mathematically identical to finding a Country that won two years in a row (Back-to-Back Winners).
   * Assessment implication: You can solve or validate Exercise 3 by looking for the pattern: Winner(Year) == Winner(Year-1).
Exam/Implementation Hint:
 * "Doable Now": The transcript confirms that once you understand this temporal link ("The year before"), the task transitions from confusing ("what are we supposed to do?") to straightforward ("doable").
 * Refinement: “Make your pony [query/point] better” implies that a sophisticated answer uses this logical derivation rather than just raw data matching.
2. The Complete ‘Alpha’ Brief: Comprehensive Directives
 * ⭐⭐⭐ The "Year Before" Rule: Use the previous year's winner to determine or verify the current year's host. This is the "Pattern" the lecturer was actively hinting at.
 * ⭐⭐ Transcription Warning ("Pony"): The phrase “Make your pony better” is a confirmed audio hallucination in the transcript.
   * Correction: Read this as "Make your QUERY better" or "Make your POINT better". Do not look for a literal pony variable.
 * ⭐ The "Ryan" Benchmark: A student (Ryan) struggled with this specific logic ("One") despite claiming knowledge. This suggests the "Back-to-Back" logic is a common stumbling block.
3. Exhaustive Topic Breakdown with Complete Quotation
Topic: The "Pattern" Hint (Eurovision Logic)
 * Lecturer’s Definition: The relationship between the current dataset and the historical dataset.
 * Verbatim Signal:
   * “A year ago. The year before.”
   * “You understand what I'm hinting at? So you understand the pattern I'm hinting.”
 * Context: The lecturer explicitly states she lacks domain knowledge ("I don't know anything about Eurovision"), proving that the solution is logical/structural, not trivia-based. You do not need external geographical knowledge; you need the graph structure of (Year)-[:PREVIOUS]->(Year).
4. Complete Lecturer’s Lexicon: Terminology Database
 * "The Pattern":
   * Definition: The recursive relationship where Host(Y) = Winner(Y-1).
   * Application: Used to solve queries regarding hosting duties without needing complex city-to-country data cleaning, or to identify consecutive victories.
 * "Make your [Pony/Query] Better":
   * Context: Feedback given to a student regarding their implementation.
   * Meaning: Optimise your Cypher query. Likely refers to writing elegant code that uses the graph connections (relationships between years) rather than brute-force filtering.
5. Coursework Success Blueprint [ESSENTIAL SECTION]
Task-by-Task Alignment:
 * Exercise 3 (Host & Winner):
   * Strategy: Map the query to look for the "Pattern."
   * Cypher Logic: Your query should ideally demonstrate the link: (Country)-[:WON]->(Year T) AND (Country)-[:WON]->(Year T-1).
   * Note: If you use the provided Location CSV, this logic serves as the perfect validation step (or "First Class" extension) to prove the data is correct.
First-Class Indicators:
 * Structural Awareness: The lecturer values seeing that you understand how the data connects over time ("The year before"), not just that you can load a CSV file. Demonstrating this temporal awareness in your logic or report is a key differentiator.
6. Complete Q&A and Interactive Moments
Interaction: The "Ah-Ha" Moment
 * Lecturer: “A year ago. The year before.”
 * Student: “Okay, that's doable now. I was like, what are we supposed to do?”
 * Analysis: The student was likely trying to match string names (City vs Country) and failing. The lecturer's hint unlocked the alternative path: using the graph's time dimension.
Interaction: The Recording
 * Student: “Laurie, please, can you briefly say again...”
 * Lecturer: “I'll record it.”
 * Action: Ensure you have checked the formal announcement/recording mentioned, as it likely formalises this "Year Before" hint into a direct instruction.
