from pyIST import *
import h5py
import numpy.ma as ma
import numpy as np
from datetime import datetime
from datetime import timedelta

date_format = '%Y.%m.%d'
hdf_file = '/Users/tohodson/Desktop/AQ_IST.hdf5'

f = h5py.File(hdf_file,'r+')  #turned off for saftey

terra_daily = f['/daily/MOST']
dates = terra_daily.attrs['dates']
start_date = datetime.strptime(dates[0],date_format)
end_date = datetime.strptime(dates[-1],date_format)

years = end_date.year - start_date.year #just prescibe as 15

dsize  = (years*3, 4501, 4501) # size of monthly datasets

## means = f.create_dataset('/monthly/mean/MOST', dsize,
##                          dtype=np.uint16,
##                          compression="lzf")

## pdd   = f.create_dataset('/monthly/pdd/MOST', dsize,
##                          dtype=np.uint16,
##                          compression="lzf")
means = f['/monthly/mean/MOST']
pdd = f['/monthly/pdd/MOST']

tFreezing = int(273.15*100)
count = 0

year = start_date.year

while year < end_date.year:
#for year in xrange(start_date.year, end_date.year):
    for month in [12,1,2]:
        if month ==1:
            year = year + 1
        start = datetime(year, month, 1)
        stop  = start + timedelta( days=31 ) #TODO fix

        # start = 
        # stop = datetime.strf ()month , year + 1

        window = date_clip(terra_daily, dates,
                           start.strftime(date_format),
                           stop.strftime(date_format) )
        print window.shape
        ma.masked_where(window<=5000, window, copy=False) #fill_value=0

        # calculate the monthly mean 
        #means[count] = np.asarray( masked.mean(axis=0)) 
        
        # count PDD's in each cell over the month
        pdd[count] = ( window > tFreezing ).sum( axis=0 )

        f.flush()
        print count
        del window
        
        count = count + 1
    
