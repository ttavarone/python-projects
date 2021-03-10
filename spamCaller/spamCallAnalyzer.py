import csv

#global variables
phoneNum = "" #intended as a temp variable for use across functions
region = ""  #intended as a temp variable for use across functions
currentDate = ""

#csv input cleaners
def phoneNumCleaner(num):
    if isinstance(num, str):
        length = len(num)
        if "+" in num:
            countryCode = num[:3]
            if (countryCode == "+01") or ("+1" in num):
                while length > 10:
                    numStart = length - 10
                    num = num[numStart:length]
                return num
        elif length >= 10:
            while length > 10:
                numStart = length - 10
                num = num[numStart:length]
            return num
        else:
            if length >= 10:
                return num[:10]
            else:
                return "error: number length < standard 10"
            #get the country to cross reference or fill in the region
        #fills in the region
    elif not isinstance(num, str):
        return phoneNumCleaner(str(num))
    else:
        #eventually change this for proper error handling
        return "error: input not recognized"

def regionCleaner(input):
    pass

def dateCleaner(input):
    pass

def timeCleaner(input):
    pass

#country code parser, returns a region based off a search from countryCode.json
def countryCode():
    pass

#function takes csv and converts it to dict for easier manipulation
def csvToDict(file):
    #opens file from params and calls it csvfile
    with open(file, newline='') as csvfile:
        #reader is DictReader object that auto-maps values to keys specified
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['phoneNum'],row['region'],row['date'],row['time'],row['amtOfCalls'])

#def main():
    #csvToDict("")
print(phoneNumCleaner("3478219908"))
    
#if name == main etc..........