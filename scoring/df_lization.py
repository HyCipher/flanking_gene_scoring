import pandas as pd


class DataFrameProcessor:
    def __init__(self):
        self.df = pd.DataFrame(columns=['Chromosome', 'Start', 'End', 'gid'])

    def dataframe_transform(self, content):
        if isinstance(content, str):
            elem = content.strip('\t').split('\t')
            if len(elem) == 4:
                elem_df = pd.DataFrame([elem], columns=['Chromosome', 'Start', 'End', 'gid'])
                self.df = pd.concat([self.df, elem_df], ignore_index=True)
            else:
                print(f"Skipping line: {elem}. Expected 4 columns, got {len(elem)} columns.")
        elif isinstance(content, list):
            for line in content:
                self.dataframe_transform(line)
        else:
            raise TypeError("Expected a string or list.")

    def get_dataframe(self):
        return self.df

    def target_locking(self, target, condition):
        target_chromosome = self.df.query(f'gid_{condition} == "{target}"').loc[:, f'Chromosome_{condition}']
        stdout = target_chromosome.values[0]
        return stdout

    def tag_rename(self, condition):
        self.df = self.df.rename(columns=lambda x: x + '_' + condition)

    def protein_id_mapping(self, file_path, condition):
        csv_data = pd.read_csv(file_path, delimiter='\t', header=None)
        # self.df[f'pid_{condition}'] = None

        for index, ele in enumerate(self.df.iloc[:, -1]):
            # 查找匹配的行
            matching_rows = csv_data[csv_data[0] == ele]
            # 将匹配结果转换为字符串并存储在新列中
            if not matching_rows.empty:
                # 假设我们需要第二列的值
                self.df.at[index, f'pid_{condition}'] = matching_rows[1].values

    def ortho_id_mapping(self, file_path, condition, variable):
        csv_data = pd.read_csv(file_path, delimiter='\t')
        # self.df[f'ortho_id_{condition}'] = None
        
        for index, ele in enumerate(self.df.iloc[:, -1]):
            if 'NP' in str(ele):
                column_name = 'Dmelref.longest_protein'
            elif 'XP' in str(ele):
                column_name = f'{variable}.longest_protein'
            else:
                continue  # Skip if neither 'NP' nor 'XP' is found

            matching_rows = csv_data[csv_data[column_name].apply(lambda x: isinstance(x, str) and ele in x.split(', '))]

            if not matching_rows.empty:
                # Assuming we need the first value of the 'Orthogroup' column
                self.df.at[index, f'ortho_id_{condition}'] = matching_rows['Orthogroup'].values