import re
import os

def replace_non_ascii(inputdir,outputdir):
    file_read = open(inputdir,"r",encoding="utf8")
    file_out = open(outputdir,"w+",encoding="utf8")
    file_read.seek(0)
    file_out.seek(0)
    log = file_read.read()
    file_out.write(re.sub(reg_ex,"",log))
    file_read.close()
    file_out.close()

def read_all_files(path,inputPath,outputPath):
    count = 0
    for file in os.listdir(path):
        inputfile = inputPath+file
        outputfile = outputPath+"a"+str(count)+".xml" if count > 0 else outputPath+"a.xml"
        replace_non_ascii(inputfile,outputfile)
        count += 1

reg_ex = re.compile('[^\x00-\x7F]')
path = os.getcwd() + "\Input"
inputPath,outputPath = "./Input/","./Output/"
read_all_files(path,inputPath,outputPath)
