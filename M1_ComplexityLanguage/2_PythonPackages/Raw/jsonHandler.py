import json
# import re
from collections import Counter
from collections import OrderedDict

# I could have improved parsing with regular expressions; SAVE FOR LATER ATTEMPTS
# check = re.compile("""{[\s\S]*\"type":\s*\[\"([\s\S]*)\",\s\"Source\"],\s*\"upload\":\s*\[\"([0-9\-]*)\",\s*\"([0-9\-])*\"\],\s*\"descr\":\s*\[\"([\S\s]*)\"\],\s*\"size":\s*\[\"([0-9A-Za-z]*)\",\s*\"([0-9A-Za-z]*)\"\]}""")

def print_numUploads_dates(bigDateList):

    # DEBUG/CONFIRMATION - all dates (unsorted) in list #
    #for item in bigDateList:
    #    year   = item[0:4]
    #    month  = item[5:7]
    #    day    = item[8:]
    #    print year, month, day
    ###
    
    # Create list of iteratble items
    dateCount = Counter(bigDateList)
    
    # Sort the collection
    for (key,value) in sorted(dateCount.items()):
        print key, value
    
    print "\nFinding most and least common values (listed by date)\n"
    
    # Find most common dates
    mostCommon = dateCount.most_common(10)
    mostCommon = sorted(mostCommon)
    for item in mostCommon:
        print item
    print ""
    
    # Find least common dates -- useful?
    # leastCommon = []
    # i = 1
    # for i in range (1,11):
    #    leastCommon.append(dateCount.most_common()[-i])
    # leastCommon = sorted(leastCommon)
    #for item in leastCommon:
    #    print item


def main():
    with open('items.json') as file:
        # Open crawler's JSON results
        data = json.load(file)
    
        bigDateList     = []
        sumSizeDateDict = {}
    
        # DATA PROCESSING; Get each object piece
        for d in data:
            # Get URL (One entry)
            url     = d.get('url')
            if isinstance(url, unicode):
                url = url.decode('utf-8')
            # Get DESCRIPTION (one entry)
            descr   = d.get('descr')
            if isinstance(descr, unicode):
                descr = descr.decode('utf-8')
            
            type    = d.get('type')     # I need to find 'SOURCE' (correct/full package download); index number will be used to find matching upload date and size
            upDate  = d.get('upload')
            bigDateList.append(upDate)
            
            size    = d.get('size')
        
            flag = 0 # If more than one type, this flag shows I need to use source index

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
            
            sourceIndex =  0     # Assumed position of "SOURCE" (if flag == 0)
            if flag == 1:
                if "Source" in otherType:
                    sourceIndex = otherType.index('Source')
                else:
                    sourceIndex = 0
            
            # Some size information was not included; Make sure there's a value
            if not size:
                    pass
            else:
                tsize = size[sourceIndex]
                
                # 'tsize' is the correct integer for this loop iteration's date;
                
                ### DEBUG STATEMENTS 
                # print "SIZE == " + size[sourceIndex]
                # print "DATE --> " + upDate[sourceIndex]
                # print "Original tsize --> " + tsize
                ###
                
                # All units in BYTES; Handle KILO units
                if 'K' in tsize:
                    tsize = int(tsize.strip('KB'))*1000
                # Handle MEGA units
                elif 'M' in tsize:
                    tsize = int(tsize.strip('MB'))*1000000
                # Handle standard units
                else:
                    tsize = int(tsize.strip('B'))
                
                # Determine popularity (number of versions uploaded) of each date
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

                #!!# OPTION ONE: Print each unique date
                print dateKey, sumSizeDateDict[dateKey]

        #!!# OPTION TWO : Print the number of uploads per date (DETERMINE POPULARITY)
        # print_numUploads_dates(bigDateList)
        
        file.close()  # Close crawler's JSON data file
        

    
if __name__ == "__main__":
    main()