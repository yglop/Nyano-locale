### how to use: ToDo

new_data_dir = './new_data/'
nyano_data_dir = './nyanotrasen/'

import os

# writes file dirs for new_data locale
new_data_files = []
for root, dirs, files in os.walk(new_data_dir):
    for filename in files:
        new_data_files.append(os.path.join(root, filename))

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


# writes data to memory from aromoon locale
translated = {}
for _ in new_data_files:
    with open(_) as f:
        parsed_data = parser(f)
        for k, v in parsed_data.items():
            translated[k] = v

# writes data to files
for _ in new_data_files:
    with open(_) as f:
        translated_file_data = parser(f)
        
        addition = _.split('new_data')[1]
        
        # setting up working dirs
        base_dir = nyano_data_dir        
        file_name = addition.split('/')[-1]
        work_dir = addition[:len(file_name) * -1]

        for k in translated_file_data:
            if  not os.path.exists(base_dir + work_dir):
                os.makedirs(base_dir + work_dir)
            with open(base_dir  + work_dir + file_name, 'a') as f0:
                print(k, ' =', translated_file_data[k], file=f0, end='', sep='')
                print(k)


