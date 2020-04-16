##This script is a learning from https://codechalleng.es/bites/7/
##Thanks to my teacher Julian Sequeira :)

#Goal of the script
#You need to calculate the time between these two events. First extract the timestamps from the log entries and convert them to datetime objects. 
#Then use datetime.timedelta to calculate the time difference between them.

from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    mylist1 = line.split()
    datetime_str = mylist1[1]
    datetime_object = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S')
    return datetime_object
    #pass


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    shutdown_lst = []
    #take an empty list of store the instances of the shutdown
    for line in loglines: #loop through the shutdown in the file
        #print (line)
        if "Shutdown initiated" in line: #if string present, store to list with append
            shutdown_lst.append(line)
            new_lst = map(convert_to_datetime,shutdown_lst) #map the function convert_to_datetime to each list item
            new_lst_item = [i for i in new_lst] #Get the items of the mapped list
            #print (new_lst_item)
            #print (str(new_lst_item[-1]-new_lst_item[0]))
    return (new_lst_item[-1]-new_lst_item[0]) #return the diff of the last element and first element
    #pass
