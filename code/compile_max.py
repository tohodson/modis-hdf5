# shebang line

import h5py
import numpy as np

filename = '/Users/tohodson/Desktop/AQ_IST.hdf5'
merge_path = '/daily/max'
aqua_path  = '/daily/MOSA'
terra_path = '/daily/MOST'

f = h5py.File(filename,'r+')

# merge arrays keeping only the highest value of the two inputs
def merge_warmest(data1, data2):
    return np.where( data1 > data2, data1, data2)

records, xdim, ydim = f[terra_path].shape

#f.create_dataset(merge_path, (records, xdim, ydim), dtype=np.uint16,  compression='lzf', shuffle=True)


for i in xrange(records):
    aqua = f[aqua_path][i][...]
    terra = f[terra_path][i][...]
    f[merge_path][i] = merge_warmest( aqua, terra )
    print 'merge ' + str(i)

f.close
