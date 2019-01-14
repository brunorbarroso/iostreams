from app import io
from app import helper as h

def run( pathAndFileName ):
    h.logger(f"Initiating file data extraction process.")
    inputFileName = h.replaceFilename(pathAndFileName)
    ios = io.IOStreams()
    positions = ios.getBlockIntervalPositions( inputFileName )
    packages = h.splitList( positions, 450 )
    for package in packages.items():
      ios.getContentFileByInterval( inputFileName, package[1], len(package[1]) )
    h.logger(f"Extraction process closed.")