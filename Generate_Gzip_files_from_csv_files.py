import os       
import gzip
import shutil
extension = ".csv"
dir_name = r'E:\\<Path>\<source path where .csv files are present>'
dest_name= r'E:\\<path>\<target path where .gzip files needs to be generated>'
os.chdir(dir_name) # change directory from working dir to dir with files

for item in os.listdir(dir_name): # loop through items in dir
    if item.endswith(extension): # check for ".gz" extension
         file_name = os.path.abspath(item) # get full path of files
         with open(file_name, 'rb') as f_in:
                 with gzip.GzipFile(file_name+ '.gz',"wb") as f_out:
                     shutil.copyfileobj(f_in, f_out)