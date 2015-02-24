# University of Victoria
# Seng371 - Software Evolution 
# Project 1

By:     Erika Burdon

GitHub email: eburdonGIT@gmail.com

------------------------------------------
![You're a parser tongue, Harry!](https://i.imgur.com/LdJ7pZo.jpg)
------------------------------------------

This is my project repository deliverable for Project 1 as assigned in Seng 371 - Software Evolution at the University of Victoria, taught by Yvonne Coady.

COPYRIGHT:  http://creativecommons.org/licenses/by-nc-nd/4.0/
  > You can copy and redistribute this project & report in any medium or format.
  
  > You may NOT modify (remix or transform) the material and distribute it or use the material for commercial purposes.
  
  > You must give appropriate credit.
  
------------------------------------------

This Repo Contains:
-------------------
* My Evolutionary question
* Description of my methodologies using to answer my question (overview and specific)
* Results of my research (per method)
* Discussion and analysis (answer & future work; per method)
* Project management details

------------------------------------------


The Evolution of a Language
------------------------------------------

In this class so far, we have been discussing the evolution of ultra-large scale (ULS) projects and how they have evolved. We've looked at some different code bases, have read a few essays by Fred Brooks in his book "Mythical Man Month", and have learnt about the 8 laws of evolution. For project 1, each student has been asked to build some sort of "tool" and study a code base in order to answer questions about Software Evolution.

Instead of looking at a code base, I wanted to attempt to study the evolution of a programming language. This will be an in-depth, specific tool with 3 well defined methodologies as opposed to a general tool that I can apply to 3 different code bases/languages.

My question: <b>"How has Python become more powerful over time?"</b>

I have split my question into three ideas, each of which I believe contributes to the strength of a language.

1. Source Code (core; complexity of the language)

2. Supported Projects

3. Community (sociotechnical environment)

They each define some smaller questions their results hope to answer. 

This README file only contains a brief overview of each methodology. This entire project is intended to be reviewed in a report-syle format. Please visit folders M1\_ComplexityLanguage, M2\_SupportedProjects, and M3\_Community <i>in order</i> and read their README's (links provided in the next section). 

Each README includes explanations of the exact steps I took in each stage, as well as source files, compile/run instructions,
a list of links to each tool I used, a list of metrics, and a list of sources. They also include "Results" and "Discussion" 
sections reviewing the signifance of discovered data.

Overview of Methodologies
------------------------------------------

This section gives a brief overview of each methodology. Detailed steps, results (such as RAW files and some visualizations),
analysis and discussion, as well as future work are discussed only in the appropriate readme file.

<b>Complexity of the Language - <i>Source code</i></b> 

>How has Python grown? Can we determine if it has evolved into a more complex core?

[Methodology 1 README](./M1_ComplexityLanguage/M1_README.md)

Methodology 1 is split into two parts to match the Python construct - Part A examines the offical source code via 
visualization and version statistics, while Part B examines open-source contributions from the community in the Python 
Packages. Each part required at least one script to automate data collection. The results of each part, and of the entire 
methodology successfully asserted a number of software evolution laws.

------------------------------------------

<b>Supported Projects</b>

>How have the <i>kinds</i> of projects Python can support, evolved? Are users able to accomplish more with Python now than 
before?

[Methodology 2 README](./M2_SupportedProjects/M2_README.md)

Methodology 2 investigates how Python has been used. It looks into why Python may have been chosen over other dynamic or 
scripted languages and finds a number of examples showing the range of projects Python is currently able to support. While 
not returning as many numerical results as methodology 1, the results conclude the truth of a few software evolution laws. 

------------------------------------------

<b>Use of the Language - <i>Community</i></b> 

>How has the Python community grown? Why has this happened?

[Methodology 3 README](./M3_Community/M3_README.md)

The final methodology pursues the ways in which Python's socio-technical environment - the community formed by its developers
and users - are evolving. It relies on a number of anecdotal evidence which may be due to the fact that all changes to the 
community are relatively recent, and its effects have not yet been noticed.

------------------------------------------


Results
------------------------------------------

This project successfully asserted a number of Software Engineering laws by examining each part that form a language - its 
source code (internal and open source), supported platforms, and community. The three parts together have raised Python to a 
higher state and therefore demonstrate the evolution of the Python programming language.

Future Work
------------

More automation could be done during data collection. Read the "Future Work" section in each README file for more information 
related to that task.


Project Management
------------------------------------------

This was a self-directed project. I planned and met all milestones on my own. Helpful comments and tool suggestions were received from the SEng 371 class during labs during the course of the project.

----------------

Tools used:

* [Trello](https://trello.com/): Project planning tool that organizes tasks into cards on a board.

* Microsoft Effice - Excel

* [Import.io](https://import.io/)

* Gource

And others... all tools listed in the relevant README file.

------------------------------------------

Milestones:

January 30 - Finalize questions, methodologies, and tools - make sure they're reasonable!

Week of: Februrary 1 (First Sunday) - Begin & complete "Complexity of the Language - Source code"

Week of: February 8  - Begin & Complete "Complexity of the Language - Projects"

Week of: February 15 - Begin & complete "Use of the Language - Community"

February 22 - Ensure all data is compiled into repository. Prepare repo for submission

<b>February 23</b> - <b>Project Due Date!</b> Hand in results

------------------------------------------

Some obstacles:

Each README section includes an "Obstacles" section at the end listing the biggest problem faced while working on that task. 
In hindsight however, the biggest problem I faced was consistently the fact that the data I wanted to collect was either not 
available or not in the format I wanted. Collecting it would have either taken more time than I could dedicate to this 
project or simply not possible.

Furthermore, while I started this project off strong and effectively stayed with the timeline, other class assignments, lab 
work, midterms, and [BattleSnakes](https://github.com/sendwithus/battlesnake) took priority over research.

References
------------------------------------------

[SEng 371 Course GitHub Repository](https://github.com/ycoady/UVic-Software-Evolution)
