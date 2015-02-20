# University of Victoria
# Seng371 - Software Evolution 
# Project 1

By:     Erika Burdon

------------------------------------------
![You're a parser tongue, Harry!](https://i.imgur.com/LdJ7pZo.jpg)
------------------------------------------

This is my project repository deliverable for Project 1 as assigned in Seng 371 - Software Evolution at the University of Victoria, taugh by Yvonne Coady.

COPYRIGHT:  http://creativecommons.org/licenses/by-nc-nd/4.0/
  > You can copy and redistribute this project & report in any medium or format.
  
  > You may NOT modify (remix or transform) the material and distribute it or use the material for commercial purposes.
  
  > You must give appropriate credit.
  
------------------------------------------

This Repo contains:
-------------------
* My Evolutionary question
* Description of my methodologies using to answer my question
* Results of my research
* Discussion and analysis (answer & future work)
* Project management details

------------------------------------------

Evolution of a Programming Language: PYTHON
------------------------------------------
My intention with this project is to attempt to map the evolution of Python. This will be an in-depth project of one codebase, of which I will define 3 methodologies and metrics.

Big question: How has Python become more powerful?

Judging the power of a language is a tough thing to do, so I'm going to attempt to answer it by looking at 3 key pieces of a language: its source code, the program built using the language, and its surrounding community (sociotechnical environment).

Overarching tools I'll be using:

Trello (project management)

==============================================================

1. <b>Complexity of the Language - <i>Source code</i></b> 
>Have the number of bugs [fixes required] increased over time? Is this because the source is becoming more complex? Has the language become more powerful over time?

  METHODOLOGY:
  
  A.1) Download the first and latest releases of Python (Python 2.0.1 and Python 2.7.9) {Download other releases later if more information is needed}.
  
  A.2) Look at the release notes for all releases and parse "What's New" and "What's Fixed", along with their dates.
  
  A.3) Analyze data and tabularize: LOC, Release dates, Number of items fixed, number of items added.

  B.1) Look at PyPi (https://pypi.python.org/pypi), the Python Package Index; find out when/how often new packages were added, including what kind of functionality they added. If stats/file sizes are included in their official listing, I can find out if these numbers are increasing over time.
  
  B.2) Analyze data. First determine, for each Month/Year, the number of packages available. I should be able to graph these results. Second, tabularize: Day/Month/Year, Package Name, Package size, LOC, Functionality. 
  
  From both sets of information, I should be able to infer whether or not the language has grown more powerful with the addition of more features by meeting needs of users, or if everything is simply a result of fixing bugs, and Python is in fact just as useful/useless as it was when it was first released.

  TOOLS: (More to come)
  
  Parsers - source code & web scraper


==============================================================

2. <b>Complexity of the Language - <i>Code bases (supported Projects)</i></b> 

>How have the <i>kinds</i> of projects Python can support, evolved? Have they gone from simple to more complex? Are programs with fewer LOC simpler (when written in Python)? Are users able to accomplish more with Python now than before?

  METHODOLOGY:
  
  a.1) I need to find two medium-sized programs on GitHub written in two different languages (e.g., Python and C) that achieve the same result (e.g., "Hello, World!")
  
  a.2) Compare their LOC - is Python generally simpler in size and verbosity?
  
  a.3) I can use GOURCE to compare the structure of the projects to find out: 1. how long it took to build, 2. compare complexity of the structure, and 3. average number of contributing developers. I can then tabularize this data and attempt to find a useful result.

  ** I just discovered that Reddit came online in 2008, and is majority based (~ 57%) in Python. As such, I want to quickly try to chart the number of code bases or significant sized projects (i.e., no small automation scripts) vs time, to see if they have increased
  
  b.1) Attempt to search GitHub for number of projects of a certain size written in python (open source); As time goes on, does this number increase? Are the average size of the projects also increasing?
  
  b.2) Attempt a google search to find other large projects written in Python.
  
  b.3) What types of tools are these? Large scripts, or functional programs?
  
  b.3) Are the majority of Python projects open source or private?

  TOOLS: (More to come)
  
  Source code parser
  
  Gource

==============================================================

3. <b>Use of the Language - <i>Community</i></b> 
>How has the Python community grown? How has the user base evolved from exclusively scripters/advanced developers to young kids?

   METHODOLOGY:
   
   A) Explore the python community at: https://www.python.org/community/ and find out what's going on publicly. Are most of the members purely acaemics or industry workers? How have the demographics (age, locations, purpose) changed over time?
   
   B) Explore GitHub by running a search - How many Python projects are there? Has this increased over time?
   
   C) Investigate teaching tools and programs (e.g., Hour of Code) - When did they include Python?
   
   D) Collect information on UVic teaching programs - When was Python introduced into the cirriculum? Why?
   
   
   TOOLS:  (To be determined - mostly manpower at this point)


Project Milestones (2015)
------------------------------------------
January 30 - Finalize questions, methodologies, and tools - make sure they're reasonable!

Week of: Februrary 1 (First Sunday) - Begin & complete "Complexity of the Language - Source code"

Week of: February 8  - Begin & Complete "Complexity of the Language - Projects"

Week of: February 15 - Begin & complete "Use of the Language - Community"

<b>February 19 - MIDTERM ONE</b>

February 21/22 - Ensure all data is tabularized; If a report is required, construct and edit report.

<b>February 23</b> (Final Monday of the Month) - <b>Project Due Date!</b> Hand in results

------------------------------------------
Thanks for Reading! Contact me anytime at eburdonGIT@gmail.com

===========================================

# Lab #4 - Data Collection and Experimentation
https://github.com/ycoady/UVic-Software-Evolution/issues/10

1. Assertion: Sizes of source code/files (release) increase over time
2. Data collection: Parse the python documentation for release names, dates, and Gzipped tarball downloads
3. See [graphed data here (Visualized with Excel)](M1A/Images/TrendGraph_PythonVersionSize.png)




===========================================
# Project repo should have the following components by END OF DAY, FEB 23
TODO: Reformat this ReadMe file to direct reader to each part

1. Question about software evolution you are setting out to answer (Why important)
2. The Methodolgy using to answer (explanation) (+ link to tools, copy of source code(s), instructions on how to run, link/list of data sources, list of metrics used and how they contribute to the answer)
3. Results (must be reproducable!; include RAW results, aggregates visualizations...)
4. Analysis (answer to question based on RESULTS; + Threats to validity and future work)
5. Project mangament documentation - Milestones and timelines (how met/work log; roles)
