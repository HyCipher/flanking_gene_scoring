import df_lization
from chunk import Chunk


def process_chunk(chunk, variable, orthogroup):
    ref_df = df_lization.DataFrameProcessor()
    sp_df = df_lization.DataFrameProcessor()

    ref_target, sp_target = chunk[0][0].strip('>'), chunk[0][1]

    for line in chunk[1:]:
        ref_df.dataframe_transform(line[0])
        sp_df.dataframe_transform(line[1])

    ref_df.tag_rename('ref')
    sp_df.tag_rename('sp')

    ref_chromo = ref_df.target_locking(ref_target, 'ref')
    sp_chromo = sp_df.target_locking(sp_target, 'sp')

    ref_df.protein_id_mapping('/BiO/Live/rooter/Downloads/ortholog/longest_bank/longest/Dmelref.longest.txt', 'ref')
    sp_df.protein_id_mapping(f'/BiO/Live/rooter/Downloads/ortholog/longest_bank/longest/{variable}.longest.txt', 'sp')

    ref_df.ortho_id_mapping(orthogroup, 'ref', variable)
    sp_df.ortho_id_mapping(orthogroup, 'sp', variable)

    ref_chunk = Chunk(ref_target, ref_chromo, ref_df.get_dataframe())
    sp_chunk = Chunk(sp_target, sp_chromo, sp_df.get_dataframe())

    ref_chunk.chromo_filter()
    sp_chunk.chromo_filter()

    return ref_chunk, sp_chunk


# 逐行读取
def read_chunks(reader, border, chunk_size):
    chunk = []
    for row in reader:
        if border in row[0] and chunk:
            yield chunk
            chunk = []
        chunk.append(row)
        if len(chunk) > chunk_size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk
