import json
import platform
import sys

json_file_name = "config.json"

def write_json(table_name, key, value, filename='config.json'):
    with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data[table_name][key] = value
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

list=[]
list.append("/test_Files_Backup/jewel")
list.append("/test_Files_Backup/jewel2")
list.append("/test_Files_Backup/jewel3")
#print(list)

table_name='jewel_sources' 
key="testCases"
data=list
write_json(table_name, key, data)

table_name='destination'
data2="test_Files_Backup/backup_Location"
write_json(table_name,key, data2)


table_name='restore_destination'
data3="test_Files_Backup/restore_Location"
write_json(table_name,key, data3)

print("done with test_backup_2_insert.py")