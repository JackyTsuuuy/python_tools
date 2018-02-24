import sys

#assign param1 to File who needs to load
#read file and save to list
#remove repeat elements in list
#save new list to new file
param1 = sys.argv[1]
orgFile = open(param1,'r')
newFileName = 'new_' + str(param1)
newFile = open(newFileName,'w')
orgList = []
newList = []
for each_line in orgFile.readlines():
    each = each_line.strip()
    orgList.append(each)

newList = set(orgList)
for each in newList:
    print('writing : ' ,each)
    newFile.writelines(each + '\n')

orgFile.close()
newFile.close()
print('DONE!')