import os
from os import walk
import string

def Make_vpaths(sourcePath, outputFile):
    groupDict = {}
    
    groupTag = "//@group"
    noGroupTag = "NO_GROUP"

    for (dirPath, dirNames, fileNames) in walk(sourcePath):
        for file in fileNames:
            thisGroup = noGroupTag
            filePath = os.path.abspath(dirPath + "/" + file).replace("\\", "/")
            fs = open(filePath, "r")
            lines = fs.readlines()
        
            for line in lines:
                tokens = line.split()
                for ind in range(0, len(tokens)):
                    if tokens[ind] == groupTag:
                        if ind != len(tokens) - 1:
                            thisGroup = tokens[ind + 1]
                            break
                if thisGroup != noGroupTag:
                    break
            if not thisGroup in groupDict:
                groupDict[thisGroup] = []
            groupDict[thisGroup].append(filePath)

    fout = open(outputFile, "w")
    fout.write("vpaths\n{")

    nGroups = len(groupDict)
    currentGroup = 0

    for group in groupDict.keys():
        fout.write("\n  [\"")
        fout.write(group)
        fout.write("\"] =\n  {\n")

        currentFile = 0
        for file in groupDict[group]:
            fout.write("\"" + file + "\"")
            currentFile += 1
            if currentFile != len(groupDict[group]):
              fout.write(",")
            fout.write("\n")

        fout.write("  }")
        currentGroup += 1
        if currentGroup != len(groupDict):
          fout.write(",")
            

    fout.write("\n}")
    fout.close()

