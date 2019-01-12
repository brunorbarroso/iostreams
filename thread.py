import _thread
import time

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print(f"%s: %s" % ( threadName, time.ctime(time.time()) ))

# Create two threads as follows
try:
   _thread.start_new_thread( print_time, ("Thread-1", 2 ) )
   _thread.start_new_thread( print_time, ("Thread-2", 4 ) )
   con.connect( user='root', 
                password='',
                host='127.0.0.1',
                database='parse')
except:
   print("Error: unable to start thread")

while 1:
   pass