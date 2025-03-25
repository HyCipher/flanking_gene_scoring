def scoring(ref_ortho_id, sp_ortho_id):
    ref_ortho_id_no_nan = ref_ortho_id.dropna()
    sp_ortho_id_no_nan = sp_ortho_id.dropna()

    same_elements = ref_ortho_id_no_nan.isin(sp_ortho_id_no_nan)  # 找到相同的元素
    num_same_elements = same_elements.sum()  # 统计相同的数量

    return num_same_elements