import sys
import os
import time
from itertools import cycle

# required project
from app import constant as c
from app import helper as h
from app import database as db
from app import helper
from app import config

## 
# Class responsable for read files, extract blocks by interval and insert in database
##
class IOStreams:

    def __init__( self ):
        self.database = db.Database()
    
    def getBlockIntervalPositions( self, fileName ):
        positions = list()
        fileName = c.PATH_INPUT+fileName
        STRING_BLOCK_SEPARATOR = config.STRING_BLOCK_SEPARATOR
        if config.STRING_BLOCK_SEPARATOR == None:
            h.logger(f"Unidentified environment variables")
        else:
            if os.path.isfile(fileName):
                with open(fileName) as f:
                    for num, line in enumerate(f, 1):
                        if STRING_BLOCK_SEPARATOR in line:
                            positions.append(str(num))
                    positions.append(str(num))
        return positions
    
    def createFile( self, content, rootPath=c.PATH_OUTPUT, ext=config.EXT_DEFAULT_OUTPUT ):    
        pathAndFileName= rootPath + h.generateIdentify() + ext
        with open(pathAndFileName, 'w+') as f:
            for item in content:
                f.write("%s\n" % item)
        f.close
        h.logger(f"Created file {pathAndFileName}")
    
    def register( self, content ):
        invoiceId = self.database.execute( h.queryInsertInvoiceTemplate(), (h.generateIdentify().upper(), "waiting"))
        for item in content:
            self.database.execute( h.queryInsertInvoiceItemTemplate(), (invoiceId, item.replace('\n','')))

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
    
    def getContentFileByInterval( self, fileName, positions, maxLine, batch=1 ):
        blocks = list()
        running = True
        listCycle = cycle(positions)
        nextItem = next(listCycle)
        fileName = c.PATH_INPUT+fileName
        for item in range(1, maxLine):
            while running:
                thisItem, nextItem = nextItem, next(listCycle)
                block = self.extractContentBlockFileByInterval( fileName, start=thisItem, end=nextItem )
                self.register( content=block )
                blocks.append( block )
                h.logger(f"Extracted the file detail #{str(item+1)}/{maxLine} of batch {batch}: StartLine: {str(thisItem)} - EndLine: {str(nextItem)}")
                break
        return blocks