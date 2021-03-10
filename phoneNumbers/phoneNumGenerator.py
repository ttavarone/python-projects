import re
import random
import csv

areaCodes = []

def loadAreaCodes():
    codes = open("area-codes.csv")
    reader = csv.reader(codes)
    data = list(reader)
    codes.close()
    #print(data)
    return data
    #codeData = data

#assigns the region name to the input area code
def assignRegion(num, data):
	codes = loadAreaCodes()
	for obj in data:
		codeInDict = obj["code"]
		for code in codes:
			code = str(code)
			areaCode = code[2:5]
			#print(areaCode)
			if codeInDict == areaCode:
				length = len(code)
				region = ""
				if length <= 13:
					region = code[9:11]
				elif length > 13:
					length = length-2
					region = code[9:length]
				obj["region"] = region
	areaCodes = dictCleaner(data)

# def dictCleaner(data):
# 	for row in data:
# 		if row["region"] == 'Null':
# 			data.pop(str('Null'))
# 	return data

#creates a list of randomly generated phone numbers, h argument is a flag for
#   adding hyphens; if  h == false no hyphens, if h == true add hyphens
def numberGenerator(amount, h):
    phoneNumbers = []
    hNum = 10
    if h:
        hNum = 12
    for i in range(amount):
        num = ""
        for pos in range(hNum):
            if (pos == 3 or pos == 7) and h:
                num += "-"
            else:
                num += str(random.randint(0,9))
        phoneNumbers.append(num)
    return phoneNumbers

#must input as strings due to hyphens
def isPhoneNum(num):
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    phoneNumRegexOther = re.compile(r'\d{3}-\d{3}-\d{4}')
    mo = phoneNumRegex.search(num)
    try:
        mo = mo.group()
    except AttributeError:
        mo = "None"
    print(mo)

#adds area code to the dict of area codes and adds a region and count
def addAreaCode(num, region):
    if len(num) >= 3:
        num = num[:3]
    else:
        print("Error")
    exists = False
    for values in areaCodes:
        if num in values["code"]:
            count = values["count"]
            count += 1
            values["count"] = count
    if not exists:
        values = {
            "code":num,
            "count":1,
            "region":region
        }
        areaCodes.append(values)

numbers = numberGenerator(100, False)

for num in numbers:
    addAreaCode(num, "Null")
assignRegion(607, areaCodes)
# for entry in areaCodes:
#     print(entry)
#loadAreaCodes()
#isPhoneNum("347-821-7402")