from app import io
from app import helper as h
import datetime as dt

def run( pathAndFileName ):
    startTime = dt.datetime.now().strftime("%Y/%m/%d at %H:%M:%S")
    h.logger(f"Initiating file data extraction process.")
    inputFileName = h.replaceFilename(pathAndFileName)
    
    ios = io.IOStreams()
    positions = ios.getBlockIntervalPositions( inputFileName )
    packages = h.splitList( positions, 2 )
    if len(packages) > 0:
      for num, package in enumerate(packages.items()):
        ios.getContentFileByInterval( inputFileName, positions=package[1], maxLine=len(package[1]), batch=num+1 )
    endTime = dt.datetime.now().strftime("%Y/%m/%d at %H:%M:%S")
    h.logger(f"Extraction process closed.")
    h.logger(f"Started at {startTime} and finished at {endTime}")

#run('.\\storage\\input\\text-small.txt') # call test