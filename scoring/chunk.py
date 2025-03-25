class Chunk:
    def __init__(self, gid, chromosome, block):
        self.gid = gid
        self.chromosome = chromosome
        self.block = block

    def chromo_filter(self):
        self.block = self.block[self.block.iloc[:, 0] == self.chromosome]
