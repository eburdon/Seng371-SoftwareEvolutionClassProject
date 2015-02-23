# Methodology 1
# Complexity of the Python Language

First, a brief history of Python. After all, evolution has to start somewhere.

Python was conceived of in the late 1980's. Named after Monty Python, implementation was started in 1989 by Guido Van Rossum (Benevolent Dictator for Life {BDFL}). Python was being developed at the same time as many other languages such as Ruby and Perl, who were gaining popularity. For work, Rossum was implementing the ABC (interpreted) language, and while he was learning plenty effective things about language design, Rossum a number of gripes with ABC. He liked a few things about it - especially its extensibility - but still felt severely limited. Rossum wanted a better way to access system Kernels and conduct system administration tasks than the current proces of writing C programs or shell scripts. With all of that, Python was born.

Python was first posted in USENET in February 1991 but, the first major version (1.0) wasn't released until January 1994. The most signifcant advances in the language however were released in version 2.0 on 16 October 2000, with major features such as garbage collection and support for unicode. This release also included a shift to a transparent, community-backed development process. Currently, there are 73 versions available for download. Finally, while commonly viewed as a "scripting language," Python has been realized as a general-purpose programming language.

Python's transparency means that its core code really has two major components: 1) The ACUTAL core as officially developed by Rossum's team and his succesors, and 2) its packages developed by the community. These packages can be easily installed as-needed onto a machine via <i>Pip</i> or <i>easy install</i>, and imported into a project using keyword <i>import</i>.

This methodology (in context of the project) will look at each of these parts separately in parts A and B. Looking back at the project, these two sub-methodologies took the most time to complete but also yielded the most significant data asserting Python's evolution.

For more information about Python's history, check out the links below:

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

As a warning, this section is LARGE. First, I'll go over the sources and run commands for Part A (source code analysis). In this part, I had to create two versions of the same script since the first one didn't correctly extract the information I needed. Next, I'll cover the sources and run commands for Part B (package index analysis) which in turn had two further parts, the crawler and output data handler.  

---------

<b>Part A - Sources and Run instructions </b>

[Gource Video - Evolution of Python](https://www.youtube.com/watch?v=cNBtDstOTmA)

[Script 1 Source](./1_ActualSource/downloadSizeParser.py)

<b>Script 1 Version 1 Run instructions</b>

1) Compile and Execute with: <i>python downloadSizeParser.py</i>

<b>Brief explanation: Script 1's failure</b> This script was my 
first attempt at trying to get all Python download version names, 
URL, and download sizes from the official downloads page. This 
page listed every version name and download link in a table - the 
size and date of the upload was not included, meaning that each 
URL needed to be crawled for information.

This script successfully parsed all URLs but, before writing a 
script to visit and parse each page, I discovered that each page 
was actually in a different format. They ranged from rich webpages 
to simple texts. Due to time limitations and the difficulty of 
working with Selenium, I couldn't make a script to handle
gathering requirments for the remaining information 
(release date, name, and size). Instead, I 
switched to Import.io service. This was the first time I've used the tool; instructions on how I created my script is included [here](./1_ActualSource/ImportIO_CreateInstructions.md).

<b>Script 1 (Version 2): Run instructions</b>

Import.io API's themselves are not availble to download as a script. That is, you can only execute them to collect their most recent imformation via link. Click [here](https://api.import.io/store/data/af4727c3-172c-4724-8aae-2a08c027aa91/_query?input/webpage/url=https%3A%2F%2Fwww.python.org%2Fdownloads%2F&_user=74da2cd9-e085-4c6c-ae74-816f39e485f3&_apikey=379mdmuoSESoXQu8NdDdK8K3jMl0VNhE7iMaRKc63%2Ft%2FettzhfVRbChxR78S%2BbsyOCq%2FwM8zlqaml%2FDu%2FVk7JQ%3D%3D) for the raw data of my extractor. From the Import.io application, I was able to get my data into an excel file whose steps are detailed below:

1) Clicked "GET API", "TSV", and finally, "download as CSV" (useful data: Number, version, release date) ([Screenshot](./1_ActualSource/Images/ImportIO/3_importIO.png)).

At this point, most of my data had been collected. I had two 
options for collecting the download SIZE, and DATE from each unique 
page: a) attempt to create several import.io scripts to handle 
every page variation, or b) manually visit each page and collect 

<b>Manual parsing - remaining data</b>

1) Visit each URL parsed from <i>script 1, verision 1</i>, and get the size of the <i>GZipped source tarball</i> download (Bytes). 

2) Add ata to the excel file generated from <i>script 1, verision</i>

3) Highlight the "Release Date" and file size columns

4) Go to <i>File Menu > Insert > Chart > Line</i> to plot graph indicating total number of upload bytes per day!

----------------

<b>Part B - Sources and Run instructions </b>

[Script 2: Scrapy web crawler to get Python Package information](./2_PythonPackages/partB/partB/spiders/dmoz_spider.py)

[Script 3: JSON handler](./2_PythonPackages/Raw/jsonHandler.py) - process information from script 2 into text output useable in excel.

<b>Script 2 Run instructions:</b>

1) Navigate to: <i>partB > partB > spiders </i>

2) Open command line and run <i>scrapy crawl PiPyIndex -o items.json</i> (NOTE: Must execute from root 'partB' folder where 'scrapy.cfg' is located)

3) Produces raw file: [items.json](./2_PythonPackages/Raw/items.json)


<b> Script 3 Run instructions: </b>

1) Navigate to directory "Raw"; Open command window. You have two output options below:

2.1.1) [Default output] Execute <i>python jsonHandler.py >> out.txt</i>

2.1.2) 'out.txt' will have two columns of data: Date (yyyy-mm-dd) and file size (Bytes). [Sample output available here](./2_PythonPackages/Raw/printOut_datesSizes.txt).

2.2.1) Open jsonHandler.py; Add a comment to line 129 (<i>print dateKey, sumSizeDateDict[dateKey]</i>) and remove comment from line 132 (<i> print_numUploads_dates(bigDateList)</i>)

2.2.2) Save and execute <i>python jsonHandler.py >> out.txt</i>; 'out.txt' will have two columns, Date (yyyy-mm-dd) and total number of Bytes uploaded that day. [Sample output available here](./2_PythonPackages/Raw/printOut_dateTimes.txt).

3) Copy data into excel and sort into columns (separation indicated by the space)

[Excel file 1: Tabularized data of download date and size of download](./2_PythonPackages/Raw_Processed/dates_downloadSizes.xlsx)

[Excel file 2: Tabularized data of TOTAL package upload sizes per unique date](./2_PythonPackages/Raw_Processed/dates_downloads.xlsx)

* All Graph data will be included and discussed in the next
section.

----------------------

Results
----------------------

Woo, finally - We reached the result files and explanations for the source code/package inspection. This section includes all useful information returned and discuss what they mean.

----------------------

<b>Part A - Source code results</b>

GROUP 1 - RESULTS OF GOURCE VISUALIZATION

Here i've include some benchmark screenshots (every 5 years) of the Gource video depicting the committed changes of Python. You can see how the number and locations of files, as well as the number of developers increase.

![Screenshot 1](./1_ActualSource/Images/GOURCE_hq_python_0yrs.png)
Figure 1: Python file structure in 1991; year 0

![Screenshot 2](./1_ActualSource/Images/GOURCE_hq_python_5yrs.png)
Figure 2: Python file structure in 1996; year 5

![Screenshot 3](./1_ActualSource/Images/GOURCE_hq_python_10yrs.png)
Figure 3: Python file structure in 2001; year 10

![Screenshot 4](./1_ActualSource/Images/GOURCE_hq_python_15yrs.png)
Figure 4: Python file structure in 2006; year 15

![Screenshot 5](./1_ActualSource/Images/GOURCE_hq_python_20yrs.png)
Figure 5: Python file structure in 2011; year 20

** DISCUSSION OF THE GOURCE SCREENSHOTS; Texty text text text.


GROUP 2 - RESULTS OF WEB SCRAPERS and DOCUMENTATION

This first trend graph is from scraper 1, where we parsed the Python download pages for the release date of each version, and that version's download size.

![Graph 1](./1_ActualSource/Images/TrendGraph_PythonVersionSize.png)

Graph 1: Trend graph of Python core source code download sizes


An improvement on this graph could have been done by separating the minor and major releases; this trend graph includes sizes for every release, including even the smallest minor updates. As such, this graph has a lot of "up and down." 


The Gource video and graph together tell us information about how 
Python has certainly increased in size - I think it's safe to 
assume that has increased in complexity (Law NUMBER). But what 
about functionality? Is the software also obeying Law NUMBER, the 
addition of new features lest the software become unsatisfactory 
and obsolete? 


I've tabularized (per released version) the major changes between 
Python releases. Click [here](../M1_ComplexityLanguage/1_ActualSource/table_MajorChanges_perRelease) and notice how the concepts are 
getting bigger and bigger, and features near-constantly being 
added in each new iteration. I believe this is an assertion of Law 
NUMBER.


<b>Part B - package index results</b>

Part B used Python package <i>Scrapy</i> (meta-project!) in order to create a web scraper, and required data handling code

This second trend graph attempts to visualize the number of packages upload on each unique upload date. This contributes to my attempt to determine the speed and evaluate the "constant change" criteria of many software projects.

![Graph 2: Plotting the total SIZE of each upload against the verion's upload DATE](./2_PythonPackages/Images/chart_upDatevsNumberOf.png)
Graph 2: placeholder

The third graph is similar to graph 2, except where it attempts to plot the total number of Bytes of each day (size vs time) instead of each release. I hoped this graph would contribute to trying to figure out when Python pacakges were added/released - is there more activity now than there was before?

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
