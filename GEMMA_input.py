import sys
import pandas as pd
import argparse
import subprocess


def get_index(exp,tfam):
        tfam_ind = []
        tf = open(tfam)
        for line in tf:
                tfam_ind.append(line.split()[0])
        print "number of samples in fam file:",len(tfam_ind)
        exp_f = open(exp)
        for line in exp_f:
                exp_ind = line.split()
                break
        
       
        exp_index = [exp_ind.index(i) for i in tfam_ind]
        return exp_index

def write_fam(fam, exp,exp_index,out):
        file_exp = pd.read_table(exp,sep ="\t")
        df_2 = file_exp.iloc[:,exp_index]
        df_2 = df_2.transpose()
        file_fam = pd.read_table(fam,sep=" ",header=None)
        df_1 = file_fam.iloc[:,:file_fam.shape[1]-1] #remove the last phenotype column
        df_c = pd.concat([df_1.reset_index(drop=True), df_2.reset_index(drop=True)], axis=1)
        df_c.to_csv(out+".fam",sep = " ",index=False, header=False)
        file_exp[["gene_id"]].to_csv(out+".gene_list", index=False, header=False) #write gene list

def ifier(commander):
        ify = subprocess.Popen(commander,shell=True)
        ify.wait()


def main(args):
        bfile = args.bfile
        exp = args.exp
        out = args.out
        fam = bfile + ".fam"
        exp_index = get_index(exp,fam)
        write_fam(fam,exp,exp_index,out)
        ifier("cp " + bfile +".bed " + out + ".bed")
        ifier("cp " + bfile +".bim " + out + ".bim")

if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument('--bfile',help='plink bfile prefix')
        parser.add_argument('--exp', help='Matrix eQTL expression file, colnames are the sample ID, the colnames for genes is gene_id')
        parser.add_argument('--out',help="output prefix")
        args = parser.parse_args()
        main(args)

