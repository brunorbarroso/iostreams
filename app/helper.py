# helper.py

def EdpLogger( message, modo='info' ):
    print(f"Debug [{modo}]: {message}")

def QueryInsertInvoiceTemplate():
    return """ INSERT INTO `invoice` (`id`, `identify`, `status`) VALUES (null,%s, %s)"""