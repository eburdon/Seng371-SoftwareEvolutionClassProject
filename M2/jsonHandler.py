import json
import re
from collections import Counter # Count number of same dates
from collections import OrderedDict

## Functions to output the data I need
## I need information to plot graphs
    
    

# PRINT: number of uploads (y axis) vs upload date
def print_numUploads_dates(upDATE):
    print "TEST"


# {[\s\S]*\"type":\s*\[\"([\s\S]*)\",\s\"Source\"],\s*\"upload\":\s*\[\"([0-9\-]*)\",\s*\"([0-9\-])*\"\],\s*\"descr\":\s*\[\"([\S\s]*)\"\],\s*\"size":\s*\[\"([0-9A-Za-z]*)\",\s*\"([0-9A-Za-z]*)\"\]}

check = re.compile("""{[\s\S]*\"type":\s*\[\"([\s\S]*)\",\s\"Source\"],\s*\"upload\":\s*\[\"([0-9\-]*)\",\s*\"([0-9\-])*\"\],\s*\"descr\":\s*\[\"([\S\s]*)\"\],\s*\"size":\s*\[\"([0-9A-Za-z]*)\",\s*\"([0-9A-Za-z]*)\"\]}""")

def main():
    with open('items.json') as file:
        data = json.load(file)
    
        bigDateList = []
    
        for d in data:

            # The URL and DESCR come from the initial loading page
            # There will always only ever be ONE entry
            url     = d.get('url')
            if isinstance(url, unicode):
                url = url.decode('utf-8')
            
            descr   = d.get('descr')
            if isinstance(descr, unicode):
                descr = descr.decode('utf-8')
            
            type    = d.get('type')     # I need to find 'SOURCE'
            
            upDate  = d.get('upload')   # I need to get UPLOAD DATE; add every date to a list
            
            size    = d.get('size')     # I need to get SIZES
        
        
            flag = 0 # This flag will indicate if I need to find the corresponding source index

            if isinstance(type, list):
                otherType = []
                flag = 1
                for item in type:
                    otherType.append(item)
                    
            # THIS IS TO FIND THE INDEX OF 'Source'
            # Suppose I have three objects. They each have five
            # downloads associated with them, in different orders.
            # In every object, there is always at least once SOURCE.
            # I need to find where in the list (which row) the
            # source is in, and parse the correct size and upload
            # date with it.
            # if flag == 0:
            
            
            sourceIndex =  0     # Assumed position of "SOURCE"
            if flag == 1:
                if "Source" in otherType:
                    sourceIndex = otherType.index('Source')
                else:
                    sourceIndex = 0

            
            # Debugging: ensuring I can get each element to print the way I want
            # Confirm type = source
           ##  if not type:
           ##     print "Null type",
           ## else:
           ##     print type[sourceIndex],
           ## # Eventually get name from URL
           ## print url
           ## # Get size
           ## if not size:
           ##     print "Null size",
           ## else:
           ##     print size[sourceIndex],
           ## # Get upload date
           ## if not upDate:
           ##     print "Null upDate",
           ## else:
           ##     print upDate[sourceIndex],
           ## # Get package description
           ## try:
           ##     print descr[0]
           ## except:
           ##     print "NO DESCR"
            
           ## print ""
    
            # I now know where SOURCE is in every list; I want to add the correponding date to a big list to iterate through
            # bigDateList = []
            if not upDate:
                pass
            else:
                bigDateList.append(str(upDate[sourceIndex]))
        
        # I have a big list of every date parsed; I need to count which ones are the same
        # for item in bigDateList:
        #    print item
       
        
        yearList = []
        monthList = []
        dateList = []
        yearDict = {}
        i = 0;
        for item in bigDateList:
            monthDayDict = {}  ###
            year = item[0:4]
            month = item[5:7]
            day = item[8:]
            # yearList.append(item[0:4])
            # print "MONTH = " + 
            # print "DATE = " + 
            # print ""
        
        
        file.close()
        dateCount = Counter(bigDateList)
        print "\nFinding most and least common values\n"
        # ALL DATES (unsorted)
        # for key, value in dateCount.iteritems():
        #    print key +" -- ", value
        mostCommon = dateCount.most_common(3)
        print mostCommon
        leastCommon = []
        leastCommon.append(dateCount.most_common()[-1])
        leastCommon.append(dateCount.most_common()[-2])
        leastCommon.append(dateCount.most_common()[-3])
        print leastCommon , "\n"
        
        # Sort the collection
        for (key,value) in sorted(dateCount.items()):
            print key, value

    
if __name__ == "__main__":
    main()