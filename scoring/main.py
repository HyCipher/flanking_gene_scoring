import csv
import chunk_making as cm
import argparse
import output
import os


def launch(variable):
    orthogroup = f"/BiO/Live/rooter/Downloads/ortholog/protein_seq_dual/{variable}_Dmelref/OrthoFinder/Results_May20/Orthogroups/Orthogroups.tsv"
    synteny = f"/BiO/Live/rooter/Downloads/ortholog/alignment/updated_result/{variable}_synteny_result.tsv"
    # synteny = f'/BiO/Live/rooter/Downloads/supplement/scoring/hahaha.tsv'
    # output_path = f"/BiO/Live/rooter/Downloads/supplement/scoring/test_synteny_result.tsv"
    output_path = f"/BiO/Live/rooter/Downloads/supplement/scoring/test_11/{variable}_synteny_result.tsv"
    # output_path_o2a = f'/BiO/Live/rooter/Downloads/supplement/scoring/result_one2all/test_synteny_result.tsv'
    output_path_o2a = f"/BiO/Live/rooter/Downloads/supplement/scoring/test_12/"
    #------------
    orthogroup = f"/BiO/Live/rooter/Downloads/ortholog/protein_seq_dual/Dmir_Dmelref/OrthoFinder/Results_May20/Orthogroups/Orthogroups.tsv"
    synteny = f"/BiO/Live/rooter/Downloads/ortholog/alignment/Dmir_supplementary.csv"
    output_path = f"/BiO/Live/rooter/Downloads/supplement/scoring/supplementary/Dmir_synteny_result_supplementary"

    with open(synteny, "r") as synteny_file:
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
            output.o2o_output(ref_chunk, sp_chunk, output_path)
        
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
    # launch('Dgun')

 
if __name__ == '__main__':
    main()