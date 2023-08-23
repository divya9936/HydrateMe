import time #inbuilt module in Python
from plyer import notification 
while (True):
   notification.notify(
       title="Please Have Some Water Now!!",
       message="Stay hydrated, stay vibrant. Your body deserves the best.",
       timeout=10
   )
   time.sleep(60*60)