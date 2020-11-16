
import time
from progressbar import *

class Load:
    def __init__(init,count,sleep,callstart,callrun,callback,url,ssl):
        callstart()
        widgets=[
            RotatingMarker(),
            ' [', Timer(), '] ',
            Bar(),
            ' (', ETA(),')',
        ]
        bar = ProgressBar(max_value=count, widgets=widgets, redirect_stdout=True)
        for i in range(count+1) :
            time.sleep(sleep)
            callrun(i,bar,count,url,ssl)
        callback()