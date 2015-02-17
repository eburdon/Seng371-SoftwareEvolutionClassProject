import json
import re
from collections import Counter # Count number of same dates
from collections import OrderedDict


# DATA HANDLING FUNCTIONS

def print_dates_countSizes():
    print "MERP"

# Create collection from big date list; determine the number of instances of each date; what are the most common? least?
# python jsonHandler.py > xxx.txt
def print_numUploads_dates(bigDateList):
    # DEBUG/CONFIRMATION - all dates (unsorted) in list #
    # for item in bigDateList:
    #    year = item[0:4]
    #    month = item[5:7]
    #    day = item[8:]
    #    print year, month, day
    ###
    dateCount = Counter(bigDateList)
    print "\nFinding most and least common values (listed by date)\n"
    mostCommon = dateCount.most_common(10)
    mostCommon = sorted(mostCommon)
    for item in mostCommon:
        print item
    
    print ""
    
    leastCommon = []
    i = 1
    for i in range (1,11):
        leastCommon.append(dateCount.most_common()[-i])
    leastCommon = sorted(leastCommon)
    for item in leastCommon:
        print item
        
    # Sort the collection
    # for (key,value) in sorted(dateCount.items()):
    #    print key, value


# I could have improved parsing with this; oops
check = re.compile("""{[\s\S]*\"type":\s*\[\"([\s\S]*)\",\s\"Source\"],\s*\"upload\":\s*\[\"([0-9\-]*)\",\s*\"([0-9\-])*\"\],\s*\"descr\":\s*\[\"([\S\s]*)\"\],\s*\"size":\s*\[\"([0-9A-Za-z]*)\",\s*\"([0-9A-Za-z]*)\"\]}""")

def main():
    with open('items.json') as file:
        data = json.load(file)
    
        bigDateList = []
        sumSizeDateDict = {}
    
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
            if not size:
                pass
            else:
                # print "SIZE -- " + size[sourceIndex]
                pass
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
                # bigDateList.append(str(upDate[sourceIndex]))
                # print upDate[sourceIndex]
                pass
            
            # Make sure there's a value in size
            if not size:
                    pass
            else:
                tsize = size[sourceIndex]
                
                ### DEBUG STATEMENTS 
                # print "SIZE == " + size[sourceIndex]
                # print "DATE --> " + upDate[sourceIndex]
                # print "Original tsize --> " + tsize
                ###
                
                # All units in BYTES; Handle KILO units
                if 'K' in tsize:
                    tsize = int(tsize.strip('KB'))*1000
                    # print "Kilo size == ", tsize
                  
                # Handle MEGA units
                elif 'M' in tsize:
                    tsize = int(tsize.strip('MB'))*1000000
                    # print "Mega size == ", tsize
                   
                # Handle standard units
                else:
                    tsize = int(tsize.strip('B'))
                    # print "Byte size == ", tsize
                
                
                # 'tsize' is the correct integer for this loop iteration's date; I want to sum the total sizes for each date via dictionary structure
                # print "Current size (Bytes) = ", tsize
                
                dateKey = upDate[sourceIndex]
                
                if  dateKey in sumSizeDateDict:
                    # If date already exist in dictionary as key; Get current value of dictionary
                    temp = sumSizeDateDict.get(dateKey)
                    # Sum new size value
                    newSize = temp + tsize
                    # Insert
                    sumSizeDateDict[dateKey] = newSize
                    # print sumSizeDateDict[dateKey]
                else:
                    # Date does not exist in library; insert current date
                    sumSizeDateDict[dateKey] = tsize

                #### FORMAT ME: Output this to file; Copy to Excel
                print dateKey, sumSizeDateDict[dateKey]
        
        # FUNCTION : Print the number of uploads per date
        # (DETERMINE POPULARITY)
        # print_numUploads_dates(bigDateList)
        
        file.close()
        #####
        
        

    
if __name__ == "__main__":
    main()