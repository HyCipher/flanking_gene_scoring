class Synteny:
    def __init__(self, index, block):
        self.index = index
        self.block = block


class Block:
    def __init__(self, ref_chr, ref_start, ref_end, ref_gid, ref_pid, ref_oid, sp_chr, sp_start, sp_end, sp_gid, sp_pid, sp_oid):
        self.ref_chr = ref_chr
        self.ref_start = ref_start
        self.ref_end = ref_end
        self.ref_gid = ref_gid
        self.ref_pid = ref_pid
        self.ref_oid = ref_oid
        self.sp_chr = sp_chr
        self.sp_start = sp_start
        self.sp_end = sp_end
        self.sp_gid = sp_gid
        self.sp_pid = sp_pid
        self.sp_oid = sp_oid