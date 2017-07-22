#!/usr/bin/env python
import os
import os.path

def dirStats(dir):
    fileStats = {}
    for root, dirs, files in os.walk(dir):
        for file in files:
            extension = file.split(".")[-1]
            if (extension == file):
                #there is no extension for file
                pass
            else:
                fullfile = os.path.join(root, file) 
                size = os.path.getsize(fullfile)
                nFiles = 1
                average = size
                minimum = size
                maximum = size
                if extension in fileStats:
                    nFiles = fileStats[extension]['filesNumber'] + 1
                    average = int(((nFiles-1)*fileStats[extension]['filesAvgSize'] + size)/nFiles)
                    if (size > fileStats[extension]['filesMaxSize']):
                        maximum = size
                    else:
                        maximum = fileStats[extension]['filesMaxSize']
                    if (size < fileStats[extension]['filesMinSize']):
                        minimum = size
                    else:
                        minimum = fileStats[extension]['filesMinSize']

                lFile = {'filesNumber':nFiles, 'filesAvgSize':average, 'filesMinSize':minimum, 'filesMaxSize':maximum}
                fileStats[extension] = lFile
    for key in fileStats.keys():
        print ('There are %d files with extension \"%s\" with minimum size %d bytes, maximum size %d bytes and average size %s bytes' % (fileStats[key]['filesNumber'], key, fileStats[key]['filesMinSize'], fileStats[key]['filesMaxSize'], fileStats[key]['filesAvgSize'] ))

dirStats('/Users/dg/python_course')
