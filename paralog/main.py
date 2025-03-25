import csv
import pandas as pd
import argparse


def ortho_id_mapping(g_list, ortho_path, var, output_path):
    csv_data = pd.read_csv(ortho_path, delimiter='\t')

    with open(g_list, 'r') as chemo_list, open(output_path, 'a') as output_file:
        reader1 = csv.reader(chemo_list, delimiter='\t')
        # for index, ele in enumerate(reader1):
        for ele in reader1:
            if 'NP' in ele[2]:
                column_name = 'Dmelref.longest_protein'
            elif 'XP' in ele[2]:
                column_name = f'{var}.longest_protein'
            else:
                continue  # Skip if neither 'NP' nor 'XP' is found
            
            print(type(ele[2]))
            matching_rows = csv_data[
                csv_data[column_name].apply(lambda x: isinstance(x, str) and ele[2] in x.split(', '))]
            print(matching_rows)
            
            unit = ele[2] + "\t" + str(matching_rows.loc[:, f"{var}.longest_protein"].values).strip('[\']')
            # print(unit)
            # output_file.write(str(unit) + "\n")


def launch(variable):
    # variable = 'Dmel'
    orthogroups = f'/BiO/Live/rooter/Downloads/ortholog/protein_seq_dual/Dalb_Dmelref/OrthoFinder/Results_May20/Orthogroups/Orthogroups.tsv'
    chemoreceptor_gene_list = f'/BiO/Live/rooter/Downloads/ortholog/only_longest_chemo/output/{variable}.csv'
    output_path = f'/BiO/Live/rooter/Downloads/supplement/paralog/paralog_result/{variable}_paralogs.tsv'

    ortho_id_mapping(chemoreceptor_gene_list, orthogroups, variable, output_path)


def main():
    # parser = argparse.ArgumentParser(description='paralog extraction.')

    # Add parameters
    # parser.add_argument('--var', metavar='variable', type=str, help='file name', required=True)

    # args = parser.parse_args()
    # launch(args.var)
    launch("Dmelref")


if __name__ == '__main__':
    main()
