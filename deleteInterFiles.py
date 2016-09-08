#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import hdfs
import os.path
def delete(webhdfsPath):
    hdfs.delete(webhdfsPath, recursive=True)
def loop(fileName, processId):
    
    while(not os.path.isfile(fileName)):
        time.sleep(1)
        print "waiting to find {0}".format(fileName)

    basePath = "http://{0}:50070".format(config.host['hdfshost'])
    fastq = "{0}/fastq_{1}".format(basePath, processId)
    align = "{0}/align_{1}".format(basePath, processId)
    snv = "{0}/snv_{1}".format(basePath, processId)
    qa = "{0}/qa_{1}".format(basePath, processId)
    delete(fastq)
    delete(align)
    delete(snv)
    delete(qa)
    return
def main():
    initId = 15

    for processId in range(11, 13):
        loop("/online/GCBI/result/{0}/result.zip".format(processId), processId)
    return

main()
