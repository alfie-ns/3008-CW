### 1. THE "EUROVISION" STRATEGY (Neo4j Section)

**The Core Task:**
Even though the brief says "UK Charts," the lecturer explicitly stated:

> "The data you've got for your non relational database is based on Eurovision." 
> 
> 

**How this changes your approach:**

* **Nodes:** Instead of `(Song)` and `(Artist)`, you will likely be creating nodes like `(Country)`, `(Contestant)`, or `(Song)`.
* **The "Create" Pattern:** The lecturer demonstrated the exact syntax you need for **Exercise 1** (creating the database).

---

### 2. LECTURER’S "GOLDEN SYNTAX" FOR NEO4J

The lecturer gave a very specific, step-by-step walkthrough of how they want you to type commands. Follow this *exact* style to avoid the "port errors" and syntax issues they warned about.

#### A. The "Create" Command (Verbatim Protocol)

* **Syntax:** `CREATE (variable:Label)`
* 
**Lecturer's Rule:** "For create, we just use the rounded brackets. And nicely for the lazy individuals among us, it puts a second one in for you." 


* **Example (Lecturer's Demo):**
```cypher
CREATE (name:Lauren)

```


*(Note: You will adapt this to `CREATE (c:Country)` or similar for Eurovision).*

#### B. The "Variable Naming" Warning (Crucial)

* 
**The Trap:** "Try to avoid variable names, like `for`, in things that will also be variable names because it will highlight them as green and then it won't let you use them because it's protected." 


* **The Fix:** Use simple, non-command variables (e.g., use `p` for person, `c` for country). Do not use SQL words like `select`, `match`, or `where` as variable names.

#### C. Handling Errors

* **The "Incomplete" Error:** If you see `Expected (...)`, it usually means you missed a bracket. The lecturer noted: "It expected those rounded brackets." 


* 
**The "Memory" Trick:** "Flicking up and down with the arrow keys will do first and last commands."  Use this to fix typos without retyping the whole line.



---

### 3. THE "PORT ERROR" SURVIVAL GUIDE (High Priority)

The lecturer spent significant time on this. It is a known failure point for this assignment.

* 
**The Trigger:** "If you just exit Neo4j without saving or without stopping the database, it does cause errors with ports." 


* **The Consequence:** You cannot restart the database.
* 
**The Only Fix:** "Delete the database and the project and start all over again." 


* **The Prevention:** Always click **STOP** on the database (turn the blue bar to grey) before closing the application window.

---

### 4. SUBMISSION & FORMATTING (Adapted from Brief context)

Based on the brief's structure and the lecturer's comments, here is how you must format the Neo4j work:

1. 
**Text Output Only:** "If you want to look at it as a data... you can get it as a nice little text table... if you click text, you can just copy and paste this into your text file for your submission." 


2. **No Code in Report / Code in Exercises:**
* 
**Set Exercises (Neo4j):** "I will be running your code to make sure it runs."  -> **Submit exact Cypher code.**


* 
**Report:** "I do not want to see your code in the report."  -> **Submit interpretation only.**