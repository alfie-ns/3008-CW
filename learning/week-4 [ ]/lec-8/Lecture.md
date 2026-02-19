
1. CRITICAL ASSESSMENT INTELLIGENCE [HIGHEST PRIORITY]
⭐⭐⭐ Direct Coursework Alignment: The 10-Mark Pre-processing Goldmine
The lecturer explicitly linked this session to your 3500-word Report, which requires you to analyse the UK Annual Population Survey.
 * The Verbatim Hint: "You know, 70 out of the 70 marks available for your report, I believe I've put 10 on how you deal with that missing data. So trying to emphasise this is an important area that you need to think about."
 * The Rubric Connection: This matches the "Pre-processing of the data (10 Marks)" criterion. Furthermore, the rubric requires the report to "explain how the data has been pre-processed and the effects of this".
 * The Required Justification: You cannot just remove or impute data silently. You must document why. Quote: "That's why there's a section in your report dedicated with marks to explaining how you're dealing with missing data and therefore what the problems could be when you make conclusions from it."
⭐⭐ The Golden Rule for First-Class Marks
 * Quote: "Always kind of think about what could this missingness imply? What does the imputation or how can the invitation [imputation] affect the different bits that I'm doing?"
 * Meaning: To achieve an Excellent (70-100%) grade, you must critically appraise the data. If you impute values using a mean or median, you must explicitly state the potential bias this introduces into your COVID-19 employment analysis.
2. The Complete ‘Alpha’ Brief: Comprehensive Directives
 * ⭐⭐⭐ WARNING - Bias Introduction: "We can impute different values or interpolate use means averages to put in that missing data that does come with a weather warning because it can bias your results."
 * ⭐⭐⭐ WARNING - Flawed Conclusions: "Keep in mind that anything you derive from data that data sets that have missed large amounts of missingness could be flawed. There could be edge cases which you can't pick up because that data is missing."
 * ⭐⭐ The "Small Amount" Rule: "If you have a small amount of missingness, fine, that's not going to make much of a difference." (She defines "small" as roughly 2% to 5%. If it's over 10-20%, do not just omit it without heavy justification).
 * ⭐⭐ The Lecturer's Preferred Coding Tool: She strictly uses R, specifically the tidyverse package. "You might notice that a lot of my R code begins with the tidyverse... I get a bit lazy and just load all them in at once."
3. Exhaustive Topic Breakdown with Complete Quotation
A. Missing Completely At Random (MCAR)
 * Definition: The missing information is independent of both observable variables and unobservable parameters.
 * Lecturer's Voice: "The best case scenario... It's not due to any of the variables that you're looking at... completely at random. Totally."
 * Pitfall: "However, this is a completely unrealistic assumption to make. It's a very strong assumption to make and it's one that we can't actually make that often in practice."
B. Missing At Random (MAR)
 * Definition: Missingness can be fully accounted for by variables where there is complete information.
 * Lecturer's Voice: "One however that we can... do tend to make is what's called missing at random... it is assumption that you can't actually statistically verify... we must rely on the reasonableness of the explanation."
 * Analogy: "You step on the scales but the battery's gone flat... That missing data tells me nothing. The battery went flat."
C. Missing Not At Random (MNAR)
 * Definition: Data that is neither MAR nor MCAR.
 * Lecturer's Voice: "It's a no response, but it tells us something, we do need to include it... Unfortunately I am too heavy for the scale... It's now telling me that, okay, you're too heavy... there is useful information hidden within that missingness."
D. Dealing with Missingness: Three Methods
There are three main methods for dealing with missing data: omission, imputation, and analysis.
 * Omission: "This is essentially, if it's missing, it's gone. I don't care, I'm going to reject it from my data set." Removing all cases containing missing data. Best for very large datasets with tiny missing percentages (e.g., her Poole Harbour dataset where 0.00111% was missing).
 * Imputation: "Essentially we guess... we're going to fill in the blanks... usually what we do is if they are numerical, we will have a look at the distribution of them and go, there's not many extreme values, so I'm going to take the mean." Using medians is preferred if extreme outliers exist.
 * Analysis (Generative/Discriminative): Allowing machine learning algorithms to handle it. "Pick a machine learning algorithm that will deal with missing data for you. Some such algorithms are called cart [Classification and Regression Trees]."
4. Complete Lecturer’s Lexicon: Terminology Database
 * Imputation / Matrix Completion: Filling in missing values. Used heavily in recommender systems via Principal Components.
 * Structured Missingness: "The values have an association with the question before it is explicit within that." Often caused by leading questions in surveys (e.g., "Do you smoke?" followed by "How many a day?").
 * Censored Values: "If you're doing studies where especially transplant studies tend to get these a lot where people can die, unfortunately they call sensors [censors].".
 * Planned Missingness: A deliberate study design strategy, used to reduce participant burden.
5. Coursework Success Blueprint (UK Annual Population Survey)
To get excellent marks on your report, apply the lecturer's logic directly to your UK Annual Population Survey dataset:
 * Initial Tabulation (Explore the Data):
   * Action: Load your data using tidyverse and tabulate the missingness.
   * Quote: "Make sure you tabulate the data, have a look at the missing values, look at the range of values that you can get that are actually present, and decide from there where you're going to go with that."
 * Declare Your Assumptions (The "Why"):
   * Action: When you find missing data in the COVID-19 dataset, write a paragraph explaining why you think it is missing (MAR vs MNAR).
   * Quote: "My assumption doesn't have to be your assumption... I am going to impute values NA with one. If anybody got an na, they're going to have a one... What I'm trying to emphasise is that there is no right way of dealing with the data. It's very much up to you, your interpretation of why it should be missing."
 * Implement and Document the Fix:
   * Action: If you use imputation, state whether you used mean, median, or a specific logical replacement, and note the potential bias. This explicitly hits the "Pre-processing of the data (10 Marks)" requirement.
6. Q&A and Hidden Curriculum Extraction
 * Live Coding Reality Check: During the lecture, Dr Ansell struggles slightly with the R gsub function vs mutate when replacing NAs ("This is the dangers of live coding, because you cannot remember off the top of your head.").
   * Strategic Insight: She values the logic of why you replace a value over perfect syntax memory. When writing your report's methodology, focus heavily on why you chose a specific pre-processing step, not just the code used to do it.
 * Data Visualisation: She highly recommends visualising missingness to gain marks: "Producing these tables, producing bar charts to show the level of missingness in the different columns is also a nice visual way of showing perhaps what was going on."
 * Plagiarism & AI Warning: Remember that for the report, Assisted AI use is permitted for idea generation and language refinement, but you must write your own code and perform your own analysis. You must also include the Generative AI Declaration.
Would you like me to help you draft the specific "Data Pre-processing and Missingness Assumptions" section of your report based on her exact expectations?
