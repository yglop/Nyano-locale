### how to use: ToDo

old_nyanotrasen_dir = './ru-RU-old/'
new_nyanotrasen_dir = './ru-RU-new/'

import os

# writes file dirs for nyano locale
old_nyanotrasen_files = []
for root, dirs, files in os.walk(old_nyanotrasen_dir):
    for filename in files:
        old_nyanotrasen_files.append(os.path.join(root, filename))

# writes file dirs for nyano locale
new_nyanotrasen_files = []
for root, dirs, files in os.walk(new_nyanotrasen_dir):
    for filename in files:
        new_nyanotrasen_files.append(os.path.join(root, filename))

# parse fluent data into dict
def parser(f):
    data = {}
    txt = f.readlines()
    key = ''
    val = ''
    tmp_key = ''
    tmp_val = ''
    for line in txt:
        if ' =' in line and line[0] != ' ':
            if line.split('=')[1] == '':
                tmp_key = line.strip('=') 
                tmp_val = ''
                val = ''                     
            else:
                tmp = line.split('=', 1)
                tmp_key = tmp[0]
                tmp_val = tmp[1]
                val = ''
        else:
            tmp_val = line
        
        key = tmp_key.strip()
        val += tmp_val
        if len(key) > 0:
            data[key] = val
    return data

# writes data to memory from already translated nyano locale
data_old_nya = {}
for _ in old_nyanotrasen_files:
    with open(_) as f:
        parsed_data = parser(f)
        for k, v in parsed_data.items():
            data_old_nya[k] = v


# writes data to files
for _ in new_nyanotrasen_files:
    with open(_) as f:
        data_new_nya = parser(f)
        
        addition = _.split('ru-RU-new')[1]
        
        # setting up working dirs
        base_dir = './ru-RU-old/new_data/'        
        file_name = addition.split('/')[-1]
        work_dir = addition[:len(file_name) * -1]

        # writes folder & files in "./autotranslate/ru-RU/"
        for k in data_new_nya:
            if k not in data_old_nya:
                if not os.path.exists(base_dir + work_dir):
                    os.makedirs(base_dir+ work_dir)
                with open(base_dir + work_dir + file_name, 'a') as f0:
                    print(k, ' =', data_new_nya[k], file=f0, end='', sep='')     
