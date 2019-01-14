import random
import time

from app import constant as c

def logger( message, modo='info' ):
    print(f"Debug [{modo}]: {message}")

def queryInsertInvoiceTemplate():
    return """ INSERT INTO `invoice` (`id`, `identify`, `status`) VALUES (null,%s, %s)"""

def queryInsertInvoiceItemTemplate():
    return """ INSERT INTO `invoice_items` (`id`, `invoice_id`, `content`) VALUES (null,%s, %s)"""

def generateIdentify():
    unique = str( random.choice(c.STRING_LETTERS) + random.choice(c.STRING_LETTERS) + str(time.time()).replace('.', '') ).upper()
    logger(f"Generate identify: {unique}") # logging activities
    return unique

def splitList( lists, qty ):
    groups = {}
    indexLists = 0
    qtyItemsByList = int(len(lists)/qty) # number of invoices per group
    for group in range(0, qty):
        items = list()
        for item in range(0, qtyItemsByList):
            if item == 0 and indexLists > 0: # adds the last position of the previous block
                items.append( lists[indexLists-1] )
            items.append( lists[indexLists] ) # adds the positions of the current block
            if item == (qtyItemsByList-1) and indexLists > 0 and group < (qty-1): # adds the first position of the next block
                items.append( lists[indexLists+1] )
            logger(f"Create batch of intervals {group+1}/{qty} - item {item+1}/{qtyItemsByList} - {lists[indexLists]} - {indexLists}") # logging activities
            indexLists += 1
        groups[group] = items
    return groups

def replaceFilename( filename ):
      array = filename.split( c.DELIMITER_PATH )
      return array[len(array)-1]