BRITISH AI Lecture Intelligence System (v3.0 - Maximum Extraction Protocol)
Core Philosophy: Total Strategic Capture with 80/20 Prioritisation
Status: ACTIVE
Input Source: Conversational Transcript (Coursework Q&A / Workshop Logistics)
Objective: Extract coursework specifications, implicit marking criteria, and imitating the lecturer's coding logic.
1. CRITICAL ASSESSMENT INTELLIGENCE [HIGHEST PRIORITY]
Direct Coursework Alignment Section:
 * Defining Variables is Subjective but Requires Justification:
   The lecturer explicitly states that defining parameters (specifically a "loaded system" in this context) is open to interpretation. You do not need to find a 'hidden' correct answer; you need to construct a reasonable one.
   * Lecturer Quote: "It's up to you how you define a load system... So as long as it's clearly [defined]... just anything reasonable."
   * Action: In your R code/report, explicitly comment on why you chose your cut-off points. Do not simply state them.
 * Data Cleaning is Mandatory:
   The lecturer confirms the dataset is flawed. If you run the code without cleaning steps, you will likely lose marks or generate errors.
   * Lecturer Quote: "I'm assuming it was right to kind of clean the data. Because there. Are some issues with that that I found. There is."
   * Action: Include a distinct 'Data Cleaning' section in your R script. Document the specific "issues" (likely missing values or outliers) you address.
 * Word Count Tolerance:
   Strict confirmation of the boundaries for the written component.
   * Lecturer Quote: "Plus, minus 10[%]."
 * The 'Golden Source' for Code Imitation:
   The lecturer points to a specific resource as the template for the exercises/code style.
   * Lecturer Quote: "So it's workshop nine, date of innovation [likely 'Data Visualisation' or similar phonetically]. Part two, Workshop nine."
2. The Complete ‘Alpha’ Brief: Comprehensive Directives
⭐⭐⭐ HIGHEST PRIORITY (Must Implement)
 * Clean the Data: The lecturer has personally found "issues" in the dataset. Your code must demonstrate the detection and handling of these issues.
 * Reference Workshop 9: The logic you need to imitate is located in "Workshop Nine, Part Two." If you are struggling with the code structure, this is the master key.
 * Variable Definition Strategy: You are authorised to choose your own thresholds (e.g., "A third", "50%"). The exact number matters less than the definition being "reasonable" and consistent.
⭐⭐ HIGH PRIORITY (Marking Criteria)
 * Interpretation is Key: The lecturer accepts different definitions provided "the interpretation is... fine."
 * Use the +/- 10% Buffer: You have a 10% margin on the word count. Use this to explain your R code logic if necessary.
⭐ NOTABLE INTELLIGENCE
 * Peer Collaboration Hint: There is confusion regarding the workshop numbering ("There is no workshop nine"). The lecturer suggests confirming with peers: "Friend at a Discord call and go through."
3. Exhaustive Topic Breakdown with Complete Quotation
Topic: Defining "Loaded Systems" / Thresholds
 * Lecturer’s Stance: Flexible, provided logic is sound.
 * Verbatim Quote: "Isn't that a loaded question? It's up to you how you define a load system. I've got a kind of range in my head. So as long as it's clearly... just anything reasonable."
 * Specific Numeric Hints:
   * "Given another country point in at least... A third of those you might want to go stronger."
   * "50% sense all this much."
   * Analysis: The lecturer is suggesting looking at proportions (1/3rd or 50%) when setting your definitions in the code.
Topic: Data Quality & Cleaning
 * Lecturer’s Warning: The data is not clean.
 * Verbatim Quote: "I'm assuming it was right to kind of clean the data. Because there. Are some issues with that that I found. There is."
 * Implication for Code: Your R script must have a block dedicated to identifying these issues (likely N/A values or formatting errors) before running analysis.
Topic: Source Material Location
 * Confusion & Clarification:
   * Student: "So which set of exercises are we doing?"
   * Lecturer: "So it's workshop nine, date of innovation. Part two, Workshop nine."
   * Warning: Another student asks, "There is no workshop nine, is there not?" ensuring you verify the correct file release (likely recently uploaded or mislabelled).
4. Complete Lecturer’s Lexicon: Comprehensive Terminology Database
 * "Loaded System"
   * Context: A variable or state within the coursework data.
   * Definition: Subjective. "It's up to you... anything reasonable."
 * "Range in my head"
   * Context: The lecturer has an internal marking guide but is open to student interpretation if justified.
 * "Issues" (Data)
   * Context: Errors in the raw CSV/Excel file.
   * Definition: Anomalies that require "cleaning" before analysis.
5. Coursework Success Blueprint [ESSENTIAL SECTION]
To successfully imitate the lecturer's code based on this interaction:
 * Locate Workshop 9, Part 2: This is the Rosetta Stone. Even if the numbering is confusing on the portal, find the file associated with "Part 2" or "Data [Innovation/Visualisation]." Copy the structure of this script exactly.
 * Coding the 'Definition':
   * Do not hard-code a single value without comment.
   * Use a variable for your threshold (e.g., threshold <- 0.5 or threshold <- 0.33).
   * Comment in code: "Defining loaded system as > 33% based on reasonable distribution analysis."
 * The Cleaning Block:
   * Insert a specific code chunk early in the script: clean_data <- raw_data %>% ...
   * Address the "issues" she found (likely na.omit or filtering distinct errors).
 * Handling 'Long Overdue Seven':
   * The transcript contains the phrase "Of course they have a long overdue seven." This is likely a transcription error for a specific data category (e.g., "Level 7", "Year 7", or a specific variable). Action: Check your dataset for any variable involving the number 7 or a category that stands out, and treat it as a special case.
6. Hidden Curriculum Extraction
 * The "Reasonableness" Test: The lecturer values pragmatic, defensible logic over finding a "perfect" theoretical answer. She is pragmatic.
 * Acceptance of Data Realities: She expects you to find the errors in the data. If you ignore the data quality issues, you fail the "competence" check.
7. Complete Q&A and Interactive Moments
 * Student: "What for word count, do you give like 10%?"
   * Lecturer: "Yes. That's great. Yeah. Plus, minus 10."
   * Significance: You have safe buffers for the written report.
 * Student: "I'm assuming it was right to kind of clean the data."
   * Lecturer: "Because there. Are some issues with that that I found."
   * Significance: Validates the data cleaning approach as correct and necessary.