# Methodology 1
# Complexity of the Python Language

First, a brief history of Python. After all, evolution has to start somewhere.

Python was conceived in the late 1980's by Guido Van Rossum who at the time was working on the ABC (interpreted) language. 
Named after Monty Python, implementation was started in 1989 by and was being developed at the same time as many other 
languages such as Ruby and Perl. While the Benevolent Dictator for Life {BDFL} liked many of ABC's features, he had a number 
of gripes, especially when it came down to the limited extensibility of the language. Rossum wanted a better way to access 
conduct system administration tasks than the current way of writing C programs or shell scripts to access system kernels. All
of this combined with a lot of free time led to the birth of Python.

Python was first posted on USENET in February 1991 but the first major version (1.0) wasn't released until January 1994. 
Furthermore, the most remarkable advances in Python weren't released until 16 October 2000 as version 2.0. This release had 
major features such as garbage collection and support for unicode. Version 2.0 also included a shift to a transparent, 
community-backed development process. Currently, there are 73 versions available for download and, while commonly viewed as a
"scripting language," Python has now been realized as a general-purpose programming language.

Python's transparency means that its core really has two major components: 1) The ACUTAL core as officially developed by 
Rossum's team and his succesors, and 2) its packages developed by the community. These packages can be easily installed 
as-needed onto a machine via <i>Pip</i> or <i>easy install</i>, and imported into a project using keyword <i>import</i>.

If you're reading this README file, you know that this is Methodology 1, studying the evolution of Python's complexity. It is
split into two parts - Part A will investigate the officially developed source code, while Part B will investigate the 
community contributions, the Python packages.

In context of the <i>entire project</i>, this methodology took the most time to complete. However, M1 also yieled the most significant data asserting Python's overall evolution.

For more information about Python's history, check out the links below:

[Guido Van Rossum's Blog - "A brief timeline of Python"](http://python-history.blogspot.ca/2009/01/brief-timeline-of-python.html)

[Guido Van Rossum's Blog - "Introduction and Overview"](http://python-history.blogspot.ca/2009/01/introduction-and-overview.html)

[General Python FAQ](https://docs.python.org/2/faq/general.html#why-was-python-created-in-the-first-place)

[The Zen of Python](https://www.python.org/dev/peps/pep-0020/)

I'll leave it up to you to research - feel free to leave comments about Python's origins. The point of this project is to find some interesting information however, so let's get started.

----------------------

PART A - Steps for inspecting the Python Source code
----------------------

1.0 VISUALIZATION

1.1. View video visualization of all the commits/changes made to the Python source code structure over time
    
1.2. Infer some interesting information about the evolution of Python's structure such as the addition (or removal) of a 
significant modules, how constantly changes have been made, and trends such as number of developers, files added, etc., etc.

Metrics: Benchmark screenshots

2.0 STATISTICS

2.1. Visit Python downloads page (lists a link to every version)
    
2.2. <b>Create a script</b> to parse each version <i>name</i>, upload <i>date</i>, and <i>size</i> of downloadable file

2.3. Visualize the version <i>date</i> vs<i>size</i> in a line graph; infer useful information

2.4. Read Python documentation to determine key differences between versions - were new features added with each release?
  
Metrics: Version name, upload date, version size; Time, Number of uploads, Size of Download files
  
  

PART B - Method/Steps for inspecting the Python Package index
----------------------

1. Visit the Python Package Index; investigate the number of packages available

2. <b>Create a script</b> to parse each package <i>name</i>, upload <i>date(s)</i> download <i>size(s)</i>
  
3. Analyze and visualize data in graphs; infer useful results


Metrics: Time, date, size; Number of Packages, number of upload dates, number of uploads per date, sizes of package downloads


----------------------


Sources and generated Raw Files
----------------------

As a warning, this section is LARGE. Here I provide all source links (external and internal), and step-by-step instructions on how to execute the scripts to obtain useful output.

First, I review sources and run commands for Part A (source code analysis; <i>two versions</i>). Next, I cover the sources and run commands for Part B (package index analysis; two parts). 

---------

<b>Part A - Sources and Run instructions </b>

[Gource Video - Evolution of Python](https://www.youtube.com/watch?v=cNBtDstOTmA)

[Download Python](https://www.python.org/downloads/)

[Script 1 Source](./1_ActualSource/downloadSizeParser.py)

<b>Script 1 (Version 1) Run instructions</b>

1) Compile and execute via <i>python downloadSizeParser.py >> out.txt </i>

* 'out.txt' will contain the number of links at the top of the document, then list every version download URL on different lines

Brief explanation: Script 1's failure

This script was my first attempt at trying to get all Python download names,
URLs, and sizes from the official downloads page. This page listed every version name and download link in a table - the 
size and date of the upload was not included, meaning that each URL needed to be visited and crawled for information.

This script successfully parsed all version URLs but, before writing a script to visit each information page, I discovered
that each one was in a different format. Formats ranged from rich webpages with or without information tables, to simple 
text documents. Due to time limitations and the difficulty of working with Selenium, I wasn't make a script to handle 
collection of the remaining information (release date, name, and size). 

Instead, I switched to a web-based extraction tool, Import.io. This was the first time I've used the tool; instructions on how I created my script is included [here](./1_ActualSource/ImportIO_CreateInstructions.md).

<b>Script 1 (Version 2): Run instructions</b>

Import.io API's  are not availble to download as an executeable script. That is, you can only run them online from the owner
account to collect their most recent information via link. Click [here](https://api.import.io/store/data/af4727c3-172c-4724-8aae-2a08c027aa91/_query?input/webpage/url=https%3A%2F%2Fwww.python.org%2Fdownloads%2F&_user=74da2cd9-e085-4c6c-ae74-816f39e485f3&_apikey=379mdmuoSESoXQu8NdDdK8K3jMl0VNhE7iMaRKc63%2Ft%2FettzhfVRbChxR78S%2BbsyOCq%2FwM8zlqaml%2FDu%2FVk7JQ%3D%3D) 
for the raw data of my extractor. 

From the Import.io application, I was able to get the (above) raw data into an excel by clicking "GET API", "TSV", and 
finally, "download as CSV" (useful data: Number, version, release date) ([Click to view Screenshot](./1_ActualSource/Images/ImportIO/3_importIO.png)).

This API collects the first part of my data - the name, and URL. To gather the download size and date, I had two options: a) 
attempt to create several import.io scripts, each handling a different page format , or b) manually visit each page and 
collect data myself. Due to time constraints, I chose the latter. The run steps are listed below:

Manual parsing - remaining data

2) Visit each URL parsed from <i>script 1, verision 1</i>, and get the size of the <i>GZipped source tarball</i> download (Bytes). 

3) Add data to the excel file generated from <i>script 1, verision</i>

4) Highlight the "Release Date" and file size columns

5) Go to <i>File Menu > Insert > Chart > Line</i> to plot graph

----------------

<b>Part B - Sources and Run instructions </b>

[Python Package Index](https://pypi.python.org/pypi)

[Script 2: Scrapy web crawler](./2_PythonPackages/partB/partB/spiders/dmoz_spider.py)

[Script 3: JSON web data handler](./2_PythonPackages/Raw/jsonHandler.py)

<b>Script 2 Run instructions:</b>

1) Navigate to: <i>partB > partB > spiders </i>

2) Open command line and run <i>scrapy crawl PiPyIndex -o items.json</i> (NOTE: Must execute from root 'partB' folder where 'scrapy.cfg' is located)

3) Produces raw file: [items.json](./2_PythonPackages/Raw/items.json)

Script 2 uses <i>Scrapy</i> in order to crawl and parse the PyPi index. In total, the script iterates over the entire index table (approximately 60977 active package links), collecting every package name and URL. It then follows each link to the appropriate package information page to parse the upload date(s) and size(s) of the download.

<b> Script 3 Run instructions: </b>

1) Navigate to directory "Raw"; Open command window. Two output options:

2.1.1) <b>[Default output]</b> Execute <i>python jsonHandler.py >> out.txt</i>

2.1.2) 'out.txt' will have two columns of data: Date (yyyy-mm-dd) and file size (Bytes). [Sample output available here](./2_PythonPackages/Raw/printOut_datesSizes.txt).

2.2.1) <b>[Output number of uploads per day]</b> Open jsonHandler.py; Add a comment to line 129 (<i>print dateKey, sumSizeDateDict[dateKey]</i>) and remove comment from line 132 (<i> print_numUploads_dates(bigDateList)</i>). Save file.

2.2.2) Execute <i>python jsonHandler.py >> out.txt</i>

2.2.3) 'out.txt' will have two columns, Date (yyyy-mm-dd) and total number of Bytes uploaded that day ([Sample output available here](./2_PythonPackages/Raw/printOut_dateTimes.txt)).

3) Copy data into Excel and sort into columns (separation indicated by the space)

4) Highlight both columns and go to <i>File Menu > Insert > Chart > Line</i> to plot graph

jsonHandler.py uses the JSON package in order to parse the raw data into arrays I can use. It then manipulates, sorts the dates, and counts the relevant information for output.

Excel/Grap source files:

[Excel file 1: Tabularized data of download date and size of download](./2_PythonPackages/Raw_Processed/dates_downloadSizes.xlsx)

[Excel file 2: Tabularized data of TOTAL package upload sizes per unique date](./2_PythonPackages/Raw_Processed/dates_downloads.xlsx)

----------------------

Results
----------------------


<b>Part A - Source code results</b>

* 1.0 GOURCE VISUALIZATION

While watching the Gource video, I took a screenshot for every 5 years that passed. The first fifteen years (first 3 images) have an apparent constant increasing size rate - each structure is more detailed than the last, and have more developers. In the video, there are not sudden changes, except for one or two directories suddently appearing or disappearing.

![Screenshot 1](./1_ActualSource/Images/GOURCE_hq_python_0yrs.png)
Figure 1: Python file structure in 1991; year 0

![Screenshot 2](./1_ActualSource/Images/GOURCE_hq_python_5yrs.png)
Figure 2: Python file structure in 1996; year 5

![Screenshot 3](./1_ActualSource/Images/GOURCE_hq_python_10yrs.png)
Figure 3: Python file structure in 2001; year 10

Around year 10, we see a few major additions and deletions, but overall less growth : the structure seems to have plenty of changes but the structure remains somewhat constant.

![Screenshot 4](./1_ActualSource/Images/GOURCE_hq_python_15yrs.png)
Figure 4: Python file structure in 2006; year 15

![Screenshot 5](./1_ActualSource/Images/GOURCE_hq_python_20yrs.png)
Figure 5: Python file structure in 2011; year 20


* 2.0 WEB SCRAPERS: DOWNLOADS and DOCUMENTATION

This first trend graph is from scraper 1, where we parsed the every Python version's download page for their release date and download size, then plotten them against eachother.

![Graph 1](./1_ActualSource/Images/TrendGraph_PythonVersionSize.png)

Graph 1: Trend graph of Python core version download sizes


<b>NOTE:</b> An improvement on this graph could have been done by separating the minor and major releases into two graphs. While this trend graph is positive and succesfully shows the increasing size and complexity of the Python core, the high and low peaks indicate that some releases were likely just fixes for a number of bugs, and did not add any new features.


The Gource video and graph - separately and together - certainly confirm that Python has certainly increased in size. But has functionality also increased?

As a final result for Part A, the major changes between each (major) Python release has been tabularized [here](../M1_ComplexityLanguage/1_ActualSource/table_MajorChanges_perRelease) (12 tables total, versions 2.0 - 3.4).

As an overall result, while the number of new features is not always growing, the new features are always an improvement on the previous system, and thus adding new functionality.


<b>Part B - package index results</b>

First, some interesting numbers:

As of 08/02/2015: 

* 54,986 packages registered on the PyPi index available for download

* 1,965,678,267 downloads by users

To start, I reviewed the PyPi index saved some statistics about the file sizes and popularity (number of downloads) of certain packages. However, I quickly realized that this information would not show the evolution of Python. I have therefore not included it in my analysis but, if you're still interested in this information, I've included it 
[here](./2_PythonPackages/InterestingPopularityNumbers.md).

Graph 2 visualizes results of script 2, the number of packages uploaded on each unique upload date. It intends to determine the speed/how often new packages are added or updated, which could then prove the "constant change" evolution criteria of many software projects.

![Graph 2: Plotting the number of packages uploaded per date](./2_PythonPackages/Images/chart_upDatevsNumberOf.png)
Graph 2: Number of packages uploaded per date

<b>NOTE:</b> Unfortunately, this data/graph is not as accurate or useful as I had hoped. I was under the impression that the 
table included on each package's information page was the <i>history</i> of the package, listing every version, upload date, 
and size of the package over the years, similar to how the official Python download page is set up. The table actually only 
lists the most current versions available for download on each of the different systems (e.g., win32, win64, or amd64) and/or
the different compression types available for download (e.g., gz tarball, etc.). In summary, the PyPi website is largely 
disorganized for research/historical data (it's built for finding the package you need quickly) and did not have the 
information I needed.

Ultimately, this means that graph 2 represents the number active packages on each date, the ones evolving in time with the 
Python source code.

Finally, script 3 produced graph 3. It is similar to graph 2, except where that it plots the total number of Bytes of each day (size vs time) instead of each release. 

![Graph 3](./2_PythonPackages/Images/chart_uploadSizesVSDate.png)
Graph 3: Number of bytes uploaded per date

I generated this because I wanted to see if, as the Python source code grew in size (Graph 1), if the sizes of packages also grew. However, this graph's data had the same issue as graph 2, where the parsed information is exclusively the most recent information, indicating only the number of actively updated packages.


Discussion and Analysis
----------------------

To start, I'd like to review which software laws I believe each part proved.

Reference: [The Laws of Evolution: Page 11](http://flosshub.org/sites/flosshub.org/files/2013HerraizRRG_CSUR.pdf)

<b>Part A</b>

I believe the Gource visualization directly proved:

Law I: Continuous change <i>(adapt or else become unsatisfactory)</i>

Law II: Increasing complexity <i>(maintain or reduce)</i>

Law VI: Continuous growth <i>(functionality must be continual enhanced)</i>

Captured in the 5 screenshots, and certainly true if you watch the entire ~14 minute video, it is clear to see that there are constantly new additions (and removals) being made to the source structure - this is both law I and II, where the additions are progressive, and any readjustments are anti-regressive to ensure the files didn't get too complicated.

The graphs produced from the index scrapings also prove continuous change, and the table of changes (per release) assert Law 
VI, where it is clear to see that all changes are not exclusively maintenance - there are new features being consistently 
added.

<b>Part B</b>

As I mentioned in the results section, I had some issues with the data significance of part B (most recent information per package rather an entire history). It did however, give insight as to the number of packages being updated and re-released in time with the Python a version. The graphs show that packages also have to be updated and evolve, not just the source code.

In addition to the three laws proved in part A, I believe part B also proves Law V: Conservation of familiarity. If packages were to fall behind and not longer work with the most recent Python releases, users would not have the same features they're used to. They could either adapt and forfeit their previous knowledge, and learn workarounds for their tasks, or continue working in an old version, and miss out on increased functionality.

Tools
----------------------
  
* Gource/Youtube

* Import.io

* Scrapy
 
* Selenium

* Excel (tabularizing and graphing)
  

 
Obstacles
----------------------

<b>Part A</b>

Originally, I wanted to read all of the Python release notes for information such as "What's New" and number of fixes. 
Unfortunatley, not only does each document not contain the same information (some are short, some are long), the notes and 
matching download page were all formatted slightly different. In the limited time of this project, I was not able to make a 
script that could consistently find and parse the relevant information. As a result, I was only able to skim the surface of 
available information. 

A second automation issues was the fact that not every download page provided the same download file type. While some pages 
offered, for example, gzipped source tarballs, xz compressed tarballs, <i>and</i> executable installers, others included only
one type. Luckily, this one type was the standard type available across all downloads, but this limited my information 
source. Furthermore, if two pages offered the same multiple types, they were likely to have been ordered differently in the 
download table. This meant I couldn't just parse the first entry in every table - I had to perform some sort of search to 
find the right entry. While a trivial issue to fix, it would have required significantly more testing to confirm I had the 
right data.

A final issue with parsing Python source files was the fact that some pages (usually older) didn't include the download link 
directly there, and instead advised users to visit a different page. This page then included all relevant information. I 
could have created a more in-depth script to handle this situation but again, the time constraint of this project forced me 
to visit each page manually, find the correct information display, and run the script from there. 


<b>Part B</b>

The detailed information about each package was not in the format I expected. I thought the table on each page was a history 
of versions available for that package, similar to how the Python source download page was set up in Part A. My original 
intention was to map the changes in a few of the most popular packages to show how they have contributed more to Python over 
time, thus contributing to the overall evolution of the language, but had to readjust.

-------------------

Future work
-------------

In the future I could:

* Re-collect the relevant data, then separate the package size information for the major and minor releases. Obtain two separate trend graphs.

* Create a script for each Python package download page variation; automate the data collection process

*  Parse the Python release notes/documentation to automatically parse information such as: number of fixes, what's changed, etc.


---------------------

Other Sources / References / Readings
-------------------------------------

[Python FAQ](docs.python/org/2/faq/general.html#why-was-python-created-in-the-first-place)

