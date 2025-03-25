import scoring_func as sf
import pandas as pd


# 一对一比对结果输出
def o2o_output(ref_chunk, sp_chunk, output_path):
    score = sf.scoring(ref_chunk.block.ortho_id_ref, sp_chunk.block.ortho_id_sp)
    ref_chunk.block.reset_index(drop=True, inplace=True)
    sp_chunk.block.reset_index(drop=True, inplace=True)

    merge_df = pd.concat([ref_chunk.block, sp_chunk.block], axis=1)
    # print(merge_df.info())
    tag = ">" + str(ref_chunk.gid) + ',' + str(sp_chunk.gid) + ',' + "score = "+str(score)

    # print(type(tag))
    print(merge_df.to_string(index=False, line_width=1000))

    with open(output_path, "a") as output:
        output.write(tag + "\n")
    # write_header = not os.path.exists(output_path)
    merge_df.to_csv(output_path, index=False, mode='a', header=True)
    # print("=====" * 20)
    

# 一对多比对结果输出
def o2a_output(ref_chunk, sp_chunk_list, output_path):
    
        for sp_i in sp_chunk_list:
            score = sf.scoring(ref_chunk.block.ortho_id_ref, sp_i.block.ortho_id_sp)
            
            ref_chunk.block.reset_index(drop=True, inplace=True)
            sp_i.block.reset_index(drop=True, inplace=True)
            merge_df = pd.concat([ref_chunk.block, sp_i.block], axis=1)
            tag = ">" + str(ref_chunk.gid) + ',' + str(sp_i.gid) + ',' + "score = "+str(score)
            with open(output_path, "a") as output:
                output.write(tag + "\n")
            merge_df.to_csv(output_path, index=False, mode='a', header=True)
            