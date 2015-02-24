# Methodology 2
# Evolution of projects supported by Python

This is Methodolgy 2, the study of the evolution of projects supported by Python. Don't worry - this process is much smaller than methodology 1. It's a single focus that tries to look at reasons and trends behind using Python in projects.

The original intention with this methodology was to search GitHub and SourceForge for two medium-sized programs that 
accomplished the same task. I planned to parse some information such as lines of code (LOC), use Gource to inspect the 
changes in structures of the projects, then gather other source-file metrics. I later realized however, that this process 
would have just compared the two software programs and languages, not offering any insight into the evolution of Python.

As a result, I shifted my search into trying to find out why Python is chosen as a development language, then try to to graph
the number of and demand for Python projects over time, as well as the types/functionality of python projects developed over 
time. 

It's important to state that this section is lacking in hard numbers. It is much more research based, and I was not able to 
find resources to parse any significant numbers from. I researched blog posts and looked for trend graphs about the use of 
Python. 

----------

Steps
-----

1) Collect data on why Python may be chosen over another language (compare two programs {C and Python}; compare language development time)

2) Read some Python success stories and other Python documentation to determine what kind of projects have been supported using Python

3) Read blog posts and collect graphs to prove increased use of Python over time


----------

Sources
-------

[1] [Python success stories](https://www.python.org/about/success/)

[2] [Hello World - Python source file](./Source/Hello_World.py)

[3] [Hello World - C source file](./Source/HelloWorld.c)

[4] [Hello World - C object file](./Source/HelloWorld.o)

[5] [Hello World - C executable file](./Source/HelloWorld.exe)

[6] [Timing script](./Source/time_HelloWord.bat)

* See final section, "Other Sources / References / Readings" for links to text sources such as blog posts.

----------

Results
----------

To start, tried to determine the movtivation for using Python over another project language.

* Comparing source codes

As a basic example, lets look at the differences between the classic "Hello World" program in C and Python, source files 2 & 3 listed above..

MINIMAL SOURCE CODE STATS: 

<b>C</b>

LOC..........................5

Num non-alpha characters... 16

Num keywords................ 9

<b>Python</b>

LOC..........................1

Num non-alpha characters... 2

Num keywords............... 1

EXECUTION STATS:

<b>C</b>
Commands to go from raw source file to executable? .... 1 - 3
Required Files......................................... 2 - source, object, .exe
Run time............................................... 0.05s

<b>Python</b>
Commands to go from raw source file to executable? .... 1
Required Files......................................... 1 - source
Run time............................................... 0.22s

These results show that Python is simpler than the well known and powerful C language. It's less verbose, needs fewer 
keywords, and fewer lines. This is a valid reason why Python may be chosen over another static language, despite the execution time being nearly four times as long!

* Comparing development time

Graph 1 compares the development time of several languages. Its clear to see that Python is 5-10x faster to develop in than
the slowest language (Java). That is, you can have one developer build a feature in Python in 1 day vs over 5 days. From a business and project management perspective, this is a strong reason to choose Python over another language.

![Graph 1](./Images/productivity.png)

Graph 1: Model of project development time per language

Next I investigated the types of project developed over time by reading the Python documentation, as well as reading up on some Python success stores. From these posts, I have determined that Python can currently support:

    * web applications
    * Gui development
    * scientfic and Numeric processing
    * system adminstration
    * Games
    * Software development / management
    * Object databases
    * Network Programming

Continuing to read success stories and posting on web forums such as [Stack Overflow](https://stackoverflow.com/), these 
results show that the types of projects support by Python have so much evolved as they have simply used all features of 
Python as they were added. That is, Python code bases have simply realized the full power of Python.

Example 1: Social media - <b>Reddit</b>

Reddit was originally written in LISP. It was switched to Python after the lack of libraries.

Example 2: Data Analysis

David Smith wrote post on revolutionanalytics.com and included a graph charting the number of questions about Python and R 
on stack overflow as a marker for how active the language is. I've included it here below:

![Graph 2](./Images/graph_pythonVSractivity.png)

Graph 2: Increased activity of Python in Data Analysis environments

Given that R has been the 'de facto' standard for Data analysis, the fact that Python has had near-exponential growth in 
activity (number of questions), leads to the result that Python is being realized and accepted as a suitable language for 
projects other than pure scripting. Graph 2 is evidence of Python's general-purpose power over Domain-specific R.

Example 3: Web development

Another metric we can use to gauge the acceptance of Python over time is to examine employer demand for Python in domain-specific projects. It is safe to assume that, as Python evolved (increased functionality) and its potential realized, more employers would want to shift to the language, and therefore hire more people with expertise in the language. Graph 3
is a trend graph generated on [indeed.com](www.indeed.com), plotting the demand for various popular web technologies. Python again has clearly grown up to a competitive advantage over other languages.

![Graph3](./Images/jobgraph_python_weblanguages.png)

Graph 3: Trend graph depicting employer demand of web languages


----------


Discussion and Analysis
-----------------------

How do the results of methodology 2 contribute to the evolution of Python?

In brief, the results of this methodology has not provided any evidence that Python has changed. It has only shown that 
demand for Python skills is increasing. This data however, may indirectly prove Law I (continuing change), Law IV (continuing
growth), and Law VIII (Feedback system).

Recall Graph 1 from M1, the plot of download size vs release date. If we correlate increased download size with increased 
functionality, it makes sense that in the time frame (2008-2009) where more (minor) changes were being made to the Python 
source code, employer demand spiked in 2009 due to increased functionality of the language. If we assume that Python 
developers were receving feedback from the user community after the release of these changes, we can state that Law I and IV 
are true based on Law VIII.

----------


Tools
-------

None

----------


Obstacles
----------

Due to the lack of hard numbers and information, I had to change my question several times in order to try and get useful 
information about how the types of projects Python can support has evoloved, and how this ties into the overall evolution of 
the language. The greatest challenge I had in this part was constantly refining my question, direction, and scope in order to
ensure my results were actually useful.

----------


Future Work
----------

 * Try to create a script to automatically collect this information (get most recent information as-needed instead of relying on job posts)


Other Sources / References / Readings
-------------------------------------

[Reddit Blog - 'On lisp'](redditblog.com/2005/12/on-lisp.html)

[On the growth of ... Python](http://blog.revolutionanalytics.com/2013/12/r-and-python.html)

[Is Python becoming the king of the data science forest?](http://www.experfy.com/blog/python-data-science/)

[Popularity vs Productivity vs Performance](http://datavirtualizer.com/popularity-vs-productivity-vs-performance/)


