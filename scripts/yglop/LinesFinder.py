import os
import shutil


def path_writer(work_dir):
    files_path = []
    for root, dirs, files in os.walk(work_dir):
        for filename in files:
            files_path.append(os.path.join(root, filename))
    return files_path


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


# writes data to memory 
def data_logger(ru_files_old):
    data = {}
    for i in ru_files_old:
        with open(i) as f:
            parsed_data = parser(f)
            for k, v in parsed_data.items():
                data[k] = v
    return data


# writes data to files
def writer(data, k, file_path, file_name):  
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    with open(file_path + file_name, 'a') as f0:
        print(k, ' =', data[k], file=f0, end='', sep='')
    return


def create_ru_new(en_files_path, ru_files_path_old, ru_files_path_new):
    en_files = path_writer(en_files_path)

    ru_data_old = data_logger(path_writer(ru_files_path_old))
    
    for _file in en_files:
        with open(_file) as f:
            data = parser(f)

        addition = _file.split('en-US')[1]
        file_name = addition.split('/')[-1]
        work_dir = addition[:len(file_name) * -1]

        for k in data:
            if k not in ru_data_old:
                writer(data, k, ru_files_path_new + work_dir, file_name)
    return


def merge_ru(ru_files_path_old, ru_files_path_new):
    ru_files_new = path_writer(ru_files_path_new)

    for _file in ru_files_new:
        with open(_file) as f:
            data = parser(f)
        
        addition = _file.split('ru-RU/new')[1]
        file_name = addition.split('/')[-1]
        work_dir = addition[:len(file_name) * -1]

        for k in data:
            writer(data, k, ru_files_path_old + work_dir, file_name)
    
    shutil.rmtree(ru_files_path_new)
    return


def write_translated_to_new(ru_files_path_new, ru_files_path_translated):
    ru_files_new = path_writer(ru_files_path_new)

    ru_data_translated = data_logger(path_writer(ru_files_path_translated))

    for _file in ru_files_new:
        with open(_file) as f:
            data = parser(f)

        addition = _file.split('ru-RU/new')[1]
        file_name = addition.split('/')[-1]
        work_dir = addition[:len(file_name) * -1]

        f0 = open(_file, 'w')
        f0.close()

        for k in data:
            if k in ru_data_translated:
                data[k] = ru_data_translated[k]            
                
            writer(data, k, ru_files_path_new + work_dir, file_name)
        
    return


def main():
    ru_files_path_old = './Locale/ru-RU/old'
    ru_files_path_new = './Locale/ru-RU/new'
    ru_files_path_translated = './Locale/ru-RU-t'
    en_files_path = './Locale/en-US'

    print('что вы хотите сделать?')
    print('создать новую локализацию: n')
    print('залить новую локализацию в старую: y')
    print('залить существующий перевод в новую локализацию: a (убедитесь что папка с новым переводом названа "ru-RU-t")')

    selected_mode = str(input())

    if selected_mode == 'n':
        create_ru_new(en_files_path, ru_files_path_old, ru_files_path_new)
    elif selected_mode == 'y':
        merge_ru(ru_files_path_old, ru_files_path_new)
    elif selected_mode == 'a':
        write_translated_to_new(ru_files_path_new, ru_files_path_translated)
    else:
        print('емае')

    return


tmp = main()
