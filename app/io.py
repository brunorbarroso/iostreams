# app.py

import sys
import datetime as dt
from itertools import cycle

# required project
from app import constant as c
from app import helper as h
from app import db
from app import helper

## 
# Class responsable for read files, extract blocks by interval and insert in database
##
class IOStreams:

    def __init__( self ):
        self.database = db.Database( databaseUser="root", 
                            databasePassword="", 
                            databaseHost="127.0.0.1", 
                            databaseName="parse")
        self.database.connector()
        self.database.execute( helper.QueryInsertInvoiceTemplate(), ("UHAHUHUA1", "waiting"))
    
    def getBlockIntervalPositions( self, fileName ):
        positions = list()
        fileName = c.PATH_INPUT+fileName
        with open(fileName) as f:
            for num, line in enumerate(f, 1):
                if c.STRING_BLOCK_SEPARATOR in line:
                    num = str(num)
                    positions.append(num)
        return positions
    
    def createFile( self, content, rootPath=c.PATH_OUTPUT, ext=c.EXT_DEFAULT_OUTPUT ):    
        pathAndFileName=rootPath+dt.datetime.now().strftime("%Y%m%d%H%M%S")+ext
        with open(pathAndFileName, 'w+') as f:
            for item in content:
                f.write("%s\n" % item)
        f.close
    
    def register( self, content, rootPath=c.PATH_OUTPUT, ext=c.EXT_DEFAULT_OUTPUT ):    
        invoiceIdentify=rootPath+dt.datetime.now().strftime("%Y%m%d%H%M%S")
        for item in content:
            item

    def extractContentBlockFileByInterval( self, fileName, start, end ):
        contentBlock=list()
        with open(fileName) as infile:
            copy = False
            for num, line in enumerate(infile, 1):
                if num == int(start):
                    copy = True
                elif num == int(end):
                    copy = False
                elif copy:
                    contentBlock.append(line)
        return contentBlock
    
    def getContentFileByInterval( self, fileName, positions, maxLine ):
        blocks = list()
        running = True
        listCycle = cycle(positions)
        nextItem = next(listCycle)
        fileName = c.PATH_INPUT+fileName
        for item in range(1, maxLine):
            while running:
                thisItem, nextItem = nextItem, next(listCycle)
                block = self.extractContentBlockFileByInterval( fileName, start=thisItem, end=nextItem )
                self.createFile( content=block )
                blocks.append( block )
                h.EdpLogger(f"Capture Invoice Block #{str(item)}/{maxLine}: StartLine: {str(thisItem)} - EndLine: {str(nextItem)}")
                break
        return blocks