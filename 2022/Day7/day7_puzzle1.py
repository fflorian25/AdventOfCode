import copy

class Folder():
       
    def __init__(self, parent, path):
        self.parent=parent
        self.path=path
        self.folderChildList=[]
        self.fileDict={}
    
    def addFolderChild(self, folderChild):
        self.folderChildList.append(folderChild)

    def addFile(self, fileName, fileSize):
        self.fileDict[fileName]=fileSize
        
    def sizeFiles(self):
        size = 0
        for file, siz in self.fileDict.items():
            size += siz     
        return size
    
    def recurseSize(self):
        totalSize = self.sizeFiles()
        for elmt in self.folderChildList:
            totalSize += elmt.recurseSize()
        return totalSize
        
def pwd(beforePath, cmd):
    beforePathCopy=copy.deepcopy(beforePath)
    if ( cmd == ".."):
        beforePathCopy.pop()
        return beforePathCopy     
    
    else :
        beforePathCopy.append(cmd)
        return beforePathCopy
    
def toString(pwd):
    strPwd = ""
    if len(pwd)==1:
        return "/"
    for i in range(1,len(pwd)):
            strPwd += "/" + pwd[i] 
    return strPwd


currentPath=[] 
strCurrentPath=""
allFolder={} 
#create the root dir
allFolder["/"] = Folder("root", "/")
# read inputs
with open('input_day7.txt', 'r') as reader:
    line = reader.readline()
    
    while line != '':                     
        linespt =  line.strip("\n").split()
        
        #creation of Path
        if (linespt[0] == "$"):
            if (linespt[1] == "cd"):
                currentPath = pwd(currentPath, linespt[2] )
                strCurrentPath = toString(currentPath)
                
        else:
            #creation of folder
            if (linespt[0] == "dir"):
                strNewFolderPath=toString(pwd(currentPath, linespt[1]))
                
                allFolder[strNewFolderPath]=Folder(allFolder[strCurrentPath], pwd(currentPath, linespt[1]))
                allFolder[strCurrentPath].addFolderChild(allFolder[strNewFolderPath])
                
            #else create file
            else:
                allFolder[strCurrentPath].addFile(linespt[1], int(linespt[0]))
        
        line = reader.readline()
       
SizeInf100000=0
for folder  in  allFolder:
    sizeFolder=allFolder[folder].recurseSize()
    if sizeFolder < 100000:
        SizeInf100000+=sizeFolder
print("the ultimate score is :")
print(SizeInf100000)

    
    
