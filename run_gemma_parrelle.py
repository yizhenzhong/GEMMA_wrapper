import subprocess
import sys
import glob
import argparse


def ifier(commander):
        ify = subprocess.Popen(commander,shell=True)
        ify.wait()


def get_genes(bfile):
        gene_f = open(bfile+".gene_list")
        gene_list = []
        for line in gene_f:
                gene_list.append(line.split()[0])
        return gene_list


def main(args):
        bfile = args.bfile
        matrix = args.matrix
        out = args.out
        gemma = args.gemma
        cov = args.cov
        lmm = args.lmm
        index = int(args.index)
        gene_list = get_genes(bfile)
        files = sorted(glob.glob('./output/*.assoc.txt'), key=str.lower)
        files_exist = map(lambda x: x.split("/")[-1].split("_")[-1],files)
        for i in range(index*1000,(index+1)*1000):
                gene = gene_list[i]
                if gene+".assoc.txt" in files_exist:
                        script = "echo " + gene +";"+gemma+" -bfile "+bfile+" -snps snp_list/" + gene+"_snp_list.txt -k "+matrix+" -lmm "+lmm+" -o "+out+"_"+gene+" -n "+str(i+1)+" -c "+ cov
                        print script
                        #ifier(script)
                else:
                        print 'already run'
                        continue
      



if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument('--bfile',help='GEMMA bfile prefix')
        parser.add_argument('--index',help='Parallel batch')
        parser.add_argument('--matrix',help='Relatedness matrix')
        parser.add_argument('--out',help='Output prefix')
        parser.add_argument('--cov',help='Covariate file')
        parser.add_argument('--gemma',help='GEMMA executable')
        parser.add_argument('--lmm',help="LMM model")
        args = parser.parse_args()
        main(args)
