# Methodology 1
# Complexity of the Python Language

First, a brief history of Python. After all, evolution has to start somewhere.

Python was conceived of in the late 1980's. Named after Monty Python, implementation was started in in 1989 by Guido Van Rossum (Benevolent Dictator for Life {BDFL}). It was being developed at the same time as many other languages, such as Ruby and Perl, who were also gaining popularity. Rossum was implementing the ABC (interpreted) language, and while learning lots about language design, had a number of "Gripes" with ABC. He liked a few things about it, especially its extensibility, but he still wanted something else. Furthermore, he wanted a better way to access system Kernels and other system administration tasks then the current processes of writing C programs or shell scripts. With all of that, Python was born.

Python was first posted in USENET in February 2001 but, the first major version (1.0) in January 1994, but the most signifcant advances were released in version 2.0 on 16 October 2000, with major features such as garbage collection and support for unicode. This release also included a shift to a transparent, community-backed process. Currently, there are 73 versions available for download. While viewed as a "scripting language," Python has been realized as a general-purpose programming language.

Python's transparency means that its core code really has two major components: 1) The ACUTAL core as officially developed by Rossum's team and his succesors, and 2) its packages developed by the community. These packages can be easily installed as-needed onto a machine via <i>Pip</i> or <i>easy install</i>, and imported into a project using keyword <i>import</i>.

In terms of this project, this methodology took the most time to complete, but also yieled the most significant data showing Python's evolution. It's split into two parts: A - Python Core/Source code and B - Python Packages.

For more information about Python's hisotry, check out the links below:

[Guido Van Rossum's Blog - "A brief timeline of Python"](http://python-history.blogspot.ca/2009/01/brief-timeline-of-python.html)

[Guido Van Rossum's Blog - "Introduction and Overview"](http://python-history.blogspot.ca/2009/01/introduction-and-overview.html)

[General Python FAQ](https://docs.python.org/2/faq/general.html#why-was-python-created-in-the-first-place)

[The Zen of Python](https://www.python.org/dev/peps/pep-0020/)

The rest is up to you to find out. The point of this project is to find some interesting information, so let's get started.

----------------------

PART A - Method/Steps for inspecting the Python Source code
----------------------

1.0 VISUALIZATION

1.1. View Gource video visualizing the commits to the Python source code over time; save some benchmark screenshots
    
1.2. Infer some interesting information about the evolution of Python's structure such as the addition (or removal) of a significant modules, how constantly changes have been made, and trends such as number of developers, files added, etc., etc.

2.0 STATISTICS

2.1. Visit the Python's downloads page (lists a link to every version)
    
2.2. <b>Create a script</b> to parse each version name, upload date, and size of downloadable file

2.3. Visualize the version date vs size via graphs; infer useful information

2.4. Read some Python documentation to determine what were the key differences between versions - were new features added with each release?
  
Metrics: Time, Number of uploads, Size of Download files
  
  

PART B - Method/Steps for inspecting the Python Package index
----------------------

1. Visit the [Python Package Index](https://pypi.python.org/pypi); investigate the number of packages available

2. <b>Create a script</b> to parse each package name, upload date(s), download size(s)
  
3. Analyze and visualize data and infer useful results.  


Metrics: Number of Packages, number of upload dates, number of uploads per date, sizes of package downloads


----------------------


Sources and generated Raw Files
----------------------

As a warning, this section is LARGE. First, I go over the sources and run commands for Part A. I had to create two versions of a script since the first one didn't work.  Next, I go over sources and run commands for Part B which had two parts, the crawler and output data handler, of which you can do two different things with it.  

---------

<b>Part A - Sources and Run instructions </b>

[Gource Video - Evolution of Python](https://www.youtube.com/watch?v=cNBtDstOTmA)

<b>Script 1 Version 1 Run instructions</b>

[Script 1 Source](./1_ActualSource/downloadSizeParser.py)

1) Compile and Execute with: <i>python downloadSizeParser.py</i>

<b>NOTE:</b> This script was my first attempt at trying to get all Python download version names, URL, and download sizes. The version download size was not available from the original Python download page, meaning that each URL needed to be crawled. After parsing all URLs, I discovered that each page was in a different format, ranging from rich webpage to simple text. Due to time limitations and the difficulty of working with Selenium, I couldn't make a script to handle gathering the remaining information (release date, name, and size). Instead, I switched to Import.io to gather information for this part. 

This was the first time I've used the tool; instructions on how I created my script are included [here](GITLINK).

<b>Script 1 (Version 2): Run instructions</b>

Import.io API's themselves are not availble to download as a script. That is, you can only execute them to collect their most recent imformation via link. Click [here](https://api.import.io/store/data/af4727c3-172c-4724-8aae-2a08c027aa91/_query?input/webpage/url=https%3A%2F%2Fwww.python.org%2Fdownloads%2F&_user=74da2cd9-e085-4c6c-ae74-816f39e485f3&_apikey=379mdmuoSESoXQu8NdDdK8K3jMl0VNhE7iMaRKc63%2Ft%2FettzhfVRbChxR78S%2BbsyOCq%2FwM8zlqaml%2FDu%2FVk7JQ%3D%3D) for the raw data of my extractor.

From the Import.io application howver, I was able to get my data into an excel file, detailed below:

1) Clicked "GET API", "TSV", and finally, "download as CSV" (useful data: Number, version, release date).

At this point, most of my data had been collected - I had two options to collect the download size from each unique download page: 1) attempt to create several import.io scripts to handle every variation (same time-consuming problem as before), or 2) manually visit each page and collect the information. I chose the latter.

So, my steps to collect the URL download information and graph the information were run as follows:

1) Visit each URL parsed from <i>script 1, verision 1</i>, and get the size of the <i>GZipped source tarball</i> download (Bytes). 

2) Add to the excel file generationed from <i>script 1, verision 2 (Import.io API)</i>

3) Highlight the "Release Date" and file size columns

4) Go to <i>File Menu > Insert > Chart > Line</i>


----------------

<b>Part B - Sources and Run instructions </b>

[Script 2: Scrapy web crawler to get Python Package information](./2_PythonPackages/dmoz_spider.py)

[Script 2: Compiled python file](./2_PythonPackages/dmoz_spider.pyc)

[Scrapy-generated 'resources' file](./2_PythonPackages/Resources) (re: script 2)


*** CHANGED -- UPDATE LINK LOCATION Script 2 Run instructions:

1) Navigate to partB > partB > spiders

2) Open command line and run <i>scrapy crawl PiPyIndex -o items.json</i>

3) Produces raw file: [items.json](./2_PythonPackages/Raw/items.json)


[Script 3: JSON handler](./2_PythonPackages/jsonHandler.py) - process information from script 2 into text output useable in excel.



Script 3 Run instructions:

1) Navigate to directory "Raw"; Open command window. You have two output options below:

2.1.1) [Default output] Execute <i>python jsonHandler.py >> out.txt</i>

2.1.2) 'out.txt' will have two columns of data: Date (yyyy-mm-dd) and file size (Bytes). [Produced output available here](./2_PythonPackages/Raw/printOut_dateSizes.txt).

2.2.1) Open jsonHandler.py; Add a comment to line 129 (<i>print dateKey, sumSizeDateDict[dateKey]</i>) and remove comment from line 132 (<i> print_numUploads_dates(bigDateList)</i>)

2.2.2) Save and execute <i>python jsonHandler.py >> out.txt</i>; 'out.txt' will have two columns, Date (yyyy-mm-dd) and total number of Bytes uploaded that day. [Produced output available here](./2_PythonPackages/Raw/printOut_dateTimes.txt).

3) Copy data into excel and sort into columns (separation indicated by the space)

[Excel file 1: Tabularized data of download date and size of download](./2_PythonPackages/Raw_Processed/dates_downloadSizes.xlsx)

[Excel file 2: Tabularized data of TOTAL package upload sizes per unique date](./2_PythonPackages/Raw_Processed/dates_downloads.xlsx)

4) Graph data (included in the next section)

----------------------

Results
----------------------

Woo, finally! We reached the result files for the source code/package inspection. Here I've included all useful information and discuss what they mean.

----------------------

<b>Part A</b>

GROUP 1 - RESULTS OF GOURCE VISUALIZATION

Here i've include some benchmark screenshots (every 5 years) of the Gource video depicting the committed changes of Python. You can see how the number and locations of files, as well as the number of developers increase.

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

** DISCUSSION OF THE GOURCE SCREENSHOTS


GROUP 2 - RESULTS OF WEB SCRAPERS and DOCUMENTATION

This first trend graph is from scraper 1, where we parsed the Python download pages for the release date of each version, and that version's download size.

![Graph 1](./1_ActualSource/Images/TrendGraph_PythonVersionSize.png)

Graph 1: Trend graph of Python core source code download sizes

** DISCUSSION OF: 

Finally, click [here]() to see a LARGE table of the major changes in each feature.

Combining all three sources of information, it is clear that Python the python source code has been evolved with respect to complexity (source files; Law ??) and feature additions (Law ??).


<b>Part B</b>

TEXT: Number of uploads per unique date

![Graph 2](./2_PythonPackages/Images/chart_upDatevsNumberOf.png)
Graph 2: placeholder

TEXT: Sizes of total uploads per unique date

![Graph 3](./2_PythonPackages/Images/chart_uploadSizesVSDate.png)
Graph 3: placeholder


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
 
* Selenium

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
