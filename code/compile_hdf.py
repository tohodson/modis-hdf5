from pyIST import *

##############
terra_dir = '/Users/tohodson/Desktop/modis_download/MOST/MOD29E1D.005/'
aqua_dir = '/Users/tohodson/Desktop/modis_download/MOSA/MYD29E1D.005/'
hdf_file = '/Users/tohodson/Desktop/AQ_IST.hdf5'
DATAFIELD_NAME='Ice_Surface_Temperature_SP'



aqua_count = count_files(aqua_dir,'*.hdf')
terra_count = count_files(terra_dir,'*.hdf')

print aqua_count
print terra_count
print terra_count - aqua_count
day_count = 90 * 15 # 15 years with at most 90 days per year

################################################################################
# main


f = h5py.File(hdf_file,'r+')  #turned off for saftey

terra_set = f['/daily/MOST'] # remove XXX
terra_set.attrs.create('dates',MODIS_dates(terra_dir),dtype='S10') #remove
'''
#load terra files
######################
terra_set = f.create_dataset("/daily/MOST", (terra_count,4501,4501), dtype=np.uint16, compression="lzf", shuffle=True)
terra_set = f['/daily/MOST']
terra_set.attrs.create('dates',MODIS_dates(terra_dir),dtype='S10')


counter = 0
for filename in find_files(terra_dir, '*.hdf'):

    hdf = SD(filename, SDC.READ)
    # Read dataset.
    data_raw = hdf.select(DATAFIELD_NAME)
    aqua_set[counter] = data_raw[:,:]
    counter = counter +1
    print 'terra ' + str(counter)


#load aqua files
##################
aqua_set = f.create_dataset("/daily/MOSA", (aqua_count,4501,4501), dtype=np.uint16, compression="lzf", shuffle=True)
aqua_set.attrs.create('dates',MODIS_dates(aqua_dir),dtype='S10')




counter = terra_count - aqua_count #align daily records with terra


for filename in find_files(aqua_dir, '*.hdf'):

    hdf = SD(filename, SDC.READ)
    # Read dataset.
    data_raw = hdf.select(DATAFIELD_NAME)
    aqua_set[counter] = data_raw[:,:]
    counter = counter +1
    print 'aqua ' + str(counter)



'''
f.close()

