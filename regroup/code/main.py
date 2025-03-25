import csv
from pathlib import Path
from objectory import Synteny
import pandas as pd
import os


def ref_file_list():
    ref_list = []
    input_file = "/BiO/Live/rooter/Downloads/supplement/regorup/code/output.csv"

    with open(input_file, 'r') as Dmel_list:  # 修正缩进
        reader = csv.reader(Dmel_list)
        for i in reader:
            ref_list.append(str(i).strip('[]\'>'))
    
    return ref_list


def file_traversal(dir):
    folder_path = Path(dir)
    for file_path in folder_path.rglob('*'):
        if file_path.is_file():
            yield file_path
    return
            

def read_chunks(reader, border):
    chunk = []
    for row in reader:
        if border in row[0] and chunk:
            yield chunk
            chunk = []
        chunk.append(row)
    if chunk:
        yield chunk
    return


def output_result(data_dict, index, output_path, title):
    for i in index:
        mark = int(i[2].replace("score = ", ""))
        if mark > 15:
            print(i)
            with open(output_path, 'a') as output:
                writer = csv.writer(output)
                output.write(title.replace("_synteny_result.tsv", "")+'\n')
                writer.writerow(i)
            data_dict[i].to_csv(output_path, index=False, mode = 'a')
        print("------"*20)
    

def retrieve(ref_list, data_dict, title):
    base_dir = "/BiO/Live/rooter/Downloads/supplement/regorup/output"
    count = 0
    for gene in ref_list:
        count = count + 1
        highest_score = float('-inf')
        for key in data_dict.keys():
            if gene in key:
                tmp_score = int(key[2].replace("score = ", ""))
                if tmp_score < highest_score:
                    continue
                elif tmp_score == highest_score:
                    highest_key.append(key)
                    # print(len(highest_key))
                else:
                    highest_score = tmp_score
                    highest_key = [key]
        output_file = os.path.join(base_dir, gene)
        output_result(data_dict, highest_key, output_file, title)
                


def main():
    ref_list = ref_file_list()
    border = '>'
    # dir = '/BiO/Live/rooter/Downloads/supplement/regorup/test_data'
    dir = '/BiO/Live/rooter/Downloads/supplement/regorup/result_one2one'
    for file in file_traversal(dir):
        title = os.path.basename(file)
        data_dict = {}
        with open(file, 'r') as syn_file:
            reader = csv.reader(syn_file, delimiter=',')
            for unit in read_chunks(reader, border):
                cleaned_idx = [item.lstrip('>') for item in unit[0]]
                index, block = cleaned_idx, unit[1:]
                df = pd.DataFrame(block[1:], columns=block[0])
                idx = tuple(index)
                if idx in data_dict:
                    data_dict[idx]._append(df)
                else:
                    data_dict[idx] = df
            retrieve(ref_list, data_dict, title)
        print("===="*20)


if __name__ == '__main__':
    main()
