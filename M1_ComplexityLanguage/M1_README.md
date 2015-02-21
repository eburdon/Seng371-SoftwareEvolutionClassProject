# Methodology 1
# Complexity of the Python Language

First, a brief history of Python. (There are currently 73 versions); TEXT TEXT TEXT TEXT TEXT

* It can be argued that Python's core code is made of two parts - the ACUTAL core as officially developed by Python, and its packages which can be easily installed onto a machine with <i>Pip</i> or <i>easy install</i>, and imported into a project using keyword <i>import</i>.

* This methodology took this most amount of time, and yieled the most significant data for this project.

* Broken into two parts. Why? -- REASON

----------------------

PART A - Steps for inspecting the Python Source code
----------------------

1.1. View Gource video visualizing the commits to the Python source code over time; save some benchmark screenshots
    
1.2. From the data, infer some intersting points such as the addition of a significant module, extensive refactoring, and trends such as number of developers, files added, etc., etc.
  


2.1. Visit the Python's downloads page (lists a link to every version)
    
2.2. <b>Create a script</b> to parse each version name, upload date, and size of downloadable file

2.3. Visualize the version date vs size; infer useful information
  
Metrics: M1, M2...
  

PART B - Steps for inspecting the Python Package index
----------------------

1. Visit the [Python Package Index](https://pypi.python.org/pypi); investigate the number of packages available

2. <b>Create a script</b> to parse each package name, upload date(s), download size(s)
  
3. Analyze and visualize data and infer useful results.  


Metrics: M1, M2...

----------------------

Sources and generated Raw Files
----------------------

<b>Part A</b>

[Gource Video - Evolution of Python](https://www.youtube.com/watch?v=cNBtDstOTmA)

[Script 1: Source Download Date_Size parser](./1_ActualSource/downloadSizeParser.py)

* Script 1 Run instructions: getting Python release information

1) Merp merp merp.

2) Herp herpa derp



<b>Part B</b>

[Script 2: Scrapy web crawler to get Python Package information](./2_PythonPackages/dmoz_spider.py)

[Script 2: Compiled python file](./2_PythonPackages/dmoz_spider.pyc)

[Scrapy-generated 'resources' file](./2_PythonPackages/Resources)

* Script 2 Run instructions: getting Python packages information

1) Merp merp merp.

2) Herp herpa derp

3) Run command BLAH produces raw file: [items.json](./2_PythonPackages/Raw/items.json)

[Script 3: JSON handler - process information from script 2 into text output useable in excel](./2_PythonPackages/jsonHandler.py)

* Script 3 Run instructions:

1) Merp merp merp.

2) Herp herpa derp

3) THIS produces raw text output of dates and sizes: 
[Package_dateVSsize](./2_PythonPackages/Raw/printOut_dateSizes.txt)

4) THIS produces raw text output of number of uploads on each unique dates: 
[Package_dateVSnumTimes](./2_PythonPackages/Raw/printOut_dateTimes.txt)

5) THIS produces text output of most and least common upload dates: 
[Package_dateVSsize](./2_PythonPackages/Raw/printOut_leastMostCommon.txt)

[Excel file 1: Tabularized data of download date and size of download](./2_PythonPackages/Raw_Processed/dates_downloadSizes.xlsx)

[Excel file 2: Tabularized data of TOTAL package upload sizes per unique date](./2_PythonPackages/Raw_Processed/dates_downloads.xlsx)


----------------------

Results
----------------------

Texty text text

<b>Part A</b>

TEXT: Gource visualization TEXT

![Screenshot 1](./1_ActualSource/Images/GOURCE_hq_python_0yrs.png)
Figure 1: Python file structure in 1991; year 0

![Screenshot 2](./1_ActualSource/Images/GOURCE_hq_python_5yrs.png)
Figure 1: Python file structure in 1996; year 5

![Screenshot 3](./1_ActualSource/Images/GOURCE_hq_python_10yrs.png)
Figure 1: Python file structure in 2001; year 10

![Screenshot 4](./1_ActualSource/Images/GOURCE_hq_python_15yrs.png)
Figure 1: Python file structure in 2006; year 15

![Screenshot 5](./1_ActualSource/Images/GOURCE_hq_python_20yrs.png)
Figure 1: Python file structure in 2011; year 20

TEXT TEXT: Trend graph: Python releases (dates) vs size of download - inreasing complexity?

![Graph 1](./1_ActualSource/Images/TrendGraph_PythonVersionSize.png)

Graph 1: Trend graph of Python core source code download sizes

<b>Part B</b>

TEXT: Number of uploads per unique date

![Graph 2](./2_PythonPackages/Images/chart_upDatsvsNumberOf.png)
Graph 2:

TEXT: Sizes of total uploads per unique date

![Graph 3](./2_PythonPackages/Images/chart_uploadSizesVSDate.png)
Graph 3:


Discussion and Analysis
----------------------

<b>Part A</b>

Texty text text

<b>Part B</b>

The PyPi website was not build for data analysis and is largely disorganized for efficient research - it is build for finding the package you need (based on name) as quickly as possible.


Tools
----------------------
  
* Gource/Youtube

* Import.io

* Scrapy

* Excel (tabularizing and graphing)
  

 
Obstacles
----------------------

<b>Part A</b>

If I had more time, I could have attempted to make a scraper to get details about each new version/major release from Python's documentation pages (such as number of fixes, what's changed...). 

Unfortunatley, not only does each release document not contain the same information (number of fixes), every download page and subsquent documentation was formatted slightly differently than the other. I wasn't able to make a script to consistently handle the information on each unique page within the time frame of this project. As such, I only skimmed the surface of the available information.

Another issue was that not every download page provided the same download file type. While some pages offered gzipped source tarballs, xz compressed tarballs, and executable installers, others included <i>only</i> the gzipped source tarball. This limited my information source to one file size only. Furthermore, if two pages offered the same types and number of downloads, they may have been ordered differently in the same table, meaning I couldn't just parse the first entry in every table. While this was a trivial issue to fix, it did require more testing to confirm I had the right data.

A final issue with parsing Python source files was the fact that some pages (usually older) didn't include the download link directly there, and instead advised users to visit a different page, which then included all relevant information. I could have created a more in-depth script to handle this situation but again, the time constraint of this project forced me to visit each page manually, find the correct information display, and run the script from there. 

For future work, I could try to sort the information based on release type, major N.X or minor N.N.X. This would have sorted my data points a little better, and may be the reason why my trend graph is so spiky - minor releases tend to be smaller in size, while major releases include several new developments and restructures.


<b>Part B</b>

The detailed information about each package was not in the format I expected. I thought the table on each page was a history of versions available for that package, similar to how the Python source download page was set up in Part A. My original intention was to map the changes in a few of the most popular packages to show how they have contributed more to Python over time, thus contributing to the overall evolution of the lanugage.


-------------------

Future work
-------------

Texty text text
