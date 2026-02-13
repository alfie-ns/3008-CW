COMP 3008: Analytics and Information Visualisation

1. CRITICAL ASSESSMENT INTELLIGENCE [HIGHEST PRIORITY]
⭐ THE "LINE GRAPH" GOLDEN RULE (Coursework Critical)
You explicitly noted the lecturer prefers a Line Graph. The transcript provides the specific context on how to do this successfully to get the marks.
 * The Trap: Do not just plot everything on one messy pane. The lecturer showed a "horrible" line plot of ferry data where everything was overlapping.
 * The First-Class Fix: The lecturer explicitly praised "altering the code slightly so that rather than showing them all on one pane, you actually spit it out".
 * The Strategy: When you generate your Line Graph for the coursework, use Small Multiples (faceting) rather than one cluttered chart. This demonstrates you understand the "Ferry Example" logic.
⭐⭐ Coursework: The "Three Types" Requirement
 * Explicit Instruction: "Bear in mind this for your report because you are probably going to need all four of them. Definitely three of them.".
 * Action: Your report must explicitly label and demonstrate at least three of the analytics types: Descriptive, Diagnostic, Predictive, or Prescriptive.
⭐⭐ The "Pie Chart" Instant Fail
 * Warning: "Pie charts are the work of the devil. They are misleading... If you really want to annoy me, give me a pie chart.".
 * Action: NEVER submit a pie chart. If you are tempted, use a Bar Chart instead.
⭐ Data Handling Hints
 * The Dataset: The lecturer mentions the coursework data has "over 300,000 rows per data set, over 400 variable.".
 * The Tool: "The coding is completely open." You do not have to use R, though the lecturer uses it for the demos.
2. The Complete ‘Alpha’ Brief: Comprehensive Directives
Top Tier Intelligence (⭐⭐⭐)
 * "Cater for every idiot": The lecturer’s favourite saying. If the graph isn't instantly understandable by an idiot (the lecturer self-identifies as one), it is a failure.
 * The 3D Ban: "The eye hates 3D. Your eyes are stupid... If possible, avoid 3D as much as you possibly can.".
 * Visualisation Goal: "Cluster but don't clutter.".
High Importance Warnings (⭐⭐)
 * Radar Charts: "I am not a fan of radar charts... very similar to pie charts." Avoid them because the eye cannot distinguish the small angles.
 * Context is King: Do not "shoehorn your data" into a pretty plot you found on Google. If the data type doesn't fit, don't force it.
 * Missing Data: "Missing data can be an issue and we need to decide carefully how we deal with it.".
3. Exhaustive Topic Breakdown with Complete Quotation
A. Analytics Definitions & Types
 * Lecturer Definition: "Analytics is the systematic computational analysis of data or statistics.".
 * Analytics vs Analysis:
   * Analysis is a subset: "focuses on the process of examining past data.".
   * Analytics is the whole pipeline: "storing, gathering, modeling... to gain knowledge.".
 * The Four Types (Memorise This List):
   * Descriptive: "What's happened? Tell people what's happened.".
   * Diagnostic: "Can we attribute a cause to whatever that event was?".
   * Predictive: "Look to the future and we try and guess as to what's going to happen... maybe black magic.".
   * Prescriptive: "Analytics driven by AI... help to make decisions and determine what do next.".
B. Data Visualisation Principles
 * Definition: "Translating information into a visual context to make data easier for the human brain to understand.".
 * The "Why": "Data has value... but it is only as valuable as the insights that can be gained from it.".
 * Characteristics of Good Visualisation:
   * Accuracy: Represents the trend truthfully.
   * Clear: Easy to understand immediately.
   * Empowering: The viewer knows what action to take next.
   * Succinct: Message received quickly without staring for 15 minutes.
C. Chart Types: The "Good vs Bad" Roster
 * Bar Charts: The safe bet. "When in doubt, use a bar chart.".
 * Histograms: Good for distribution. Warning: Do not use 3D histograms as they obscure the bell curve.
 * Scatter Plots: Essential for correlation. Warning: Do not force a trend line (like the COVID/Doctor pay example) where the R^2 is low.
 * Heat Maps: Excellent for showing density, but useless if all data concentrates in one spot.
 * Box Plots: Good for statistical summary, but can hide the shape of data (e.g., the "Dinosaurus" dataset looks identical to a normal distribution in a box plot).
 * Word Clouds: "Everyone loves a good word cloud," but often a bar chart is better for Likert scale (agree/disagree) data.
 * Network Plots: Appearance matters more than topology.
 * Maps: Critical Warning: Always account for population density. Maps that just colour huge states (like the Trump election map) are misleading.
 * Tree Maps: Use gradient colour scales to show relationships (Yellow to Red), rather than random colours.
 * Tables: Valid visualisation. "Don't always need a plot. Tables work just as well" for showing mean/standard deviation.
4. Requested Lists (From Lecture Slides)
Per your request, here are the specific lists demonstrated in the slides:
List 1: The Four Types of Analytics
 * Descriptive
 * Diagnostic
 * Predictive
 * Prescriptive
List 2: Why Analytics Are Important
 * Adopt informed and improved decision-making.
 * Enable more effective marketing.
 * Create a better and personalized customer experience.
 * Streamline operations.
 * Mitigate fraud.
List 3: Four Characteristics of Good Visualisations
 * Accuracy
 * Clear
 * Empowering
 * Succinct
List 4: Criteria for Selecting a Visualisation
 * Purpose
 * Type of Data
 * Context
List 5: Components of Successful Visualisation (The Venn Diagram)
 * Information (Data) + Story (Concept) = Interestingness
 * Story (Concept) + Goal (Function) = Usefulness
 * Goal (Function) + Visual Form (Metaphor) = Beauty
 * Visual Form (Metaphor) + Information (Data) = Integrity
5. Coursework Success Blueprint
The "Line Graph" Execution Strategy:
 * Select Time-Series Data: Ensure the data you pick is suitable for a line graph (e.g., trends over time).
 * Avoid the "Spaghetti" Plot: Do not put 20 lines on one axis.
 * Apply the "Ferry" Fix: Use Faceting (splitting the graph into multiple smaller panels) to show clarity. This directly addresses the lecturer's specific example of "good vs bad" layout.
The Methodology Checklist:
 * Step 1: Define the Purpose (Why am I showing this?).
 * Step 2: Select the Type (likely Bar or Line, never Pie).
 * Step 3: Ensure Context (Does the scale make sense? Are axes labelled?).
 * Step 4: Check Simplicity (Can an "idiot" understand it in 5 seconds?).
First-Class Indicators:
 * Handling Unbalanced Data: If your coursework data is unbalanced (like the insider threat example), mention how statistical models might pick up relationships better than ML models.
 * Acknowledging Limitations: Explicitly state if missing data was an issue and how you dealt with it.
6. Hidden Curriculum & Meta-Learning
 * Lecturer's "Pet" Book: "Information is Beautiful." Referencing this style or book in your report will likely be well-received.
 * Preferred Tools: The lecturer uses R and ggplot2 (BBC uses this too). While coding is open, using ggplot2 aligns with the lecturer's own workflow.
 * Humour & Tone: The lecturer appreciates pointing out "bad" visualisations (e.g., The BBC/Sky Sports bar chart disaster). Acknowledging why a visualisation might be bad in your critical analysis shows high-level understanding.
 * Real World Context: The lecturer loves examples like the "Tor Point Ferry" or "Babcock ships." Relate your data to real-world impact where possible.
7. Lecturer’s Lexicon
 * Analytics: "Systematic computational analysis.".
 * Analysis: "Examining past data.".
 * Data Visualisation: "Translating information into a visual context.".
 * Descriptive: "What has happened?".
 * Diagnostic: "Why did it happen?".
 * Predictive: "What will happen?".
 * Prescriptive: "How can we make it happen?".
 * Likert Data: Questionnaire data (Agree/Disagree) - best shown in Bar Charts, not Word Clouds.
Next Step for User
Would you like me to draft a Python (matplotlib/seaborn) or R (ggplot2) code snippet that specifically demonstrates the "Ferry" line graph layout (faceting) to ensure you hit that lecturer preference perfectly?
