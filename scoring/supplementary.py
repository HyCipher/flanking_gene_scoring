import csv
import chunk_making as cm
import argparse
import output
import os
from pathlib import Path

def list_all_files(directory):
    return [str(path) for path in Path(directory).rglob('*') if path.is_file()]

def launch(variable):
    orthogroup = f"/BiO/Live/rooter/Downloads/ortholog/protein_seq_dual/{variable}_Dmelref/OrthoFinder/Results_May20/Orthogroups/Orthogroups.tsv"
    synteny_dir = f"/BiO/Live/rooter/Downloads/ortholog/alignment/supplementary_result/Ir_unanalyzed/{variable}/"
    # synteny = f'/BiO/Live/rooter/Downloads/supplement/scoring/hahaha.tsv'
    # output_path = f"/BiO/Live/rooter/Downloads/supplement/scoring/test_synteny_result.tsv"
    output_path_dir = f"/BiO/Live/rooter/Downloads/supplement/scoring/Ir_unanalyzed/{variable}/"
    # output_path_o2a = f'/BiO/Live/rooter/Downloads/supplement/scoring/result_one2all/test_synteny_result.tsv'
    output_path_o2a = f"/BiO/Live/rooter/Downloads/supplement/scoring/supplementary/"
    
    if not os.path.exists(output_path_dir):
        os.makedirs(output_path_dir, exist_ok=True)
    
    files = list_all_files(synteny_dir)
    for file in files:
        # print(file)
        relative_path = os.path.relpath(file, synteny_dir)
        output_file_path = os.path.join(output_path_dir, relative_path)
        # print(output_file_path)
    
    
        with open(file, "r") as synteny_file:
            reader1 = csv.reader(synteny_file, delimiter=",")
            Starting = ">"
            chunk_size = 21
            ref_chunk_list = []
            sp_chunk_list = []
            
            for chunk in cm.read_chunks(reader1, Starting, chunk_size):
                if 'missing' in chunk[0]:
                    continue
                ref_chunk, sp_chunk = cm.process_chunk(chunk, variable, orthogroup)
                
                ref_chunk_list.append(ref_chunk)
                sp_chunk_list.append(sp_chunk)
                
                # # 输出一对一比对结果
                output.o2o_output(ref_chunk, sp_chunk, output_file_path)
        
        # 输出一对多比对结果
        # for ref_i in ref_chunk_list:
        #     try:
        #         directory_name = variable + '_Dmelref'
        #         full_path = os.path.join(output_path_o2a, directory_name)
        #         os.makedirs(full_path, exist_ok=True)
        #         filename = ref_i.gid + ".tsv"
        #         file_path = os.path.join(full_path, filename)
        #         # print(file_path)
        #         output.o2a_output(ref_i, sp_chunk_list, file_path)
        #     except Exception as e:
        #         print(f"创建目录时发生错误: {e}")


# 外部访问，参数输入
def main():
    parser = argparse.ArgumentParser(description='Flanking gene extraction.')

    # Add parameters
    parser.add_argument('-var', metavar='variable', type=str, help='file name', required=False)
    args = parser.parse_args()
    launch(args.var)
    print(f"{args.var} is done!")
    
    # launch("Dsubp")
    
    # list_file = '/BiO/Live/rooter/Downloads/zzzz.csv'
    # with open(list_file, mode='r', newline='', encoding='utf-8-sig') as file:
    #     reader = csv.reader(file)
        
    #     for row in reader:
    #         for variable in row:
    #             print(variable)
    #             launch(variable)

 
if __name__ == '__main__':
    main()