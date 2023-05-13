### how to use: ToDo

arumoon_dir = './ru-RU/'
old_arumoon_dir = '../../Resources/Locale/ru-RU/arumoon/'
old_nyanotrasen_dir = '../../Resources/Locale/ru-RU/nyanotrasen/'
new_nyanotrasen_dir = '../../Resources/Locale/en-US/'

import os

# writes file dirs for aromoon locale
arumoon_files = []
for root, dirs, files in os.walk(arumoon_dir):
    for filename in files:
        arumoon_files.append(os.path.join(root, filename))

# writes file dirs for aromoon locale
arumoon_files_old = []
for root, dirs, files in os.walk(old_arumoon_dir):
    for filename in files:
        arumoon_files_old.append(os.path.join(root, filename))

# writes file dirs for translated nyano locale
old_nyanotrasen_files = []
for root, dirs, files in os.walk(old_nyanotrasen_dir):
    for filename in files:
        old_nyanotrasen_files.append(os.path.join(root, filename))

# writes file dirs for not translated nyano locale
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


# writes data to memory from aromoon locale
data_arumoon = {}
for _ in arumoon_files:
    with open(_) as f:
        parsed_data = parser(f)
        for k, v in parsed_data.items():
            data_arumoon[k] = v

# writes data to memory from nyano-aromoon locale
data_arumoon_old = {}
for _ in arumoon_files_old:
    with open(_) as f:
        parsed_data = parser(f)
        for k, v in parsed_data.items():
            data_arumoon_old[k] = v

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

        addition = _.split('en-US')[1]

        # setting up working dirs
        base_dir = old_nyanotrasen_dir[:-12]
        file_name = addition.split('/')[-1]
        work_dir = addition[:len(file_name) * -1]
        aru = 'arumoon/'
        nya = 'nyanotrasen/'
        new_data = 'new_data/'

        # writes folder & files in "./autotranslate/ru-RU/"
        for k in data_new_nya:
            if k in data_arumoon and (k not in data_arumoon_old):
                data_new_nya[k] = data_arumoon[k]
                if  not os.path.exists(base_dir + aru + work_dir):
                    os.makedirs(base_dir + aru + work_dir)
                with open(base_dir + aru + work_dir + file_name, 'a') as f0:
                    print(k, ' =', data_new_nya[k], file=f0, end='', sep='')
            elif k in data_old_nya:
                pass
            else:
                if not os.path.exists(base_dir + new_data + work_dir):
                    os.makedirs(base_dir + new_data + work_dir)
                with open(base_dir + new_data + work_dir + file_name, 'a') as f0:
                    print(k, ' =', data_new_nya[k], file=f0, end='', sep='')
                with open(base_dir + 'not_translated_data', 'a') as f1:
                    print('KEY = ', k, 'FILE = ', base_dir + new_data + work_dir + file_name, file=f1, end='', sep='')
