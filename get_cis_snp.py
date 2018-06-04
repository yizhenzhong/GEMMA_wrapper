import glob
import argparse
import subprocess



def get_eqtls(out):
        f = open(out)
        next(f)
        eqtl = {}
        for line in f:
                items = line.split()
                gene = items[1]
                snp = items[0]
                if gene in eqtl:
                        eqtl[gene].append(snp)
                else:
                        eqtl[gene] = [snp]
        return eqtl


def write_snp_list(eqtls):
        for i in eqtls.keys():
                f_out = open("./test/"+i+"_snp_list.txt","w")
                f_out.write("\n".join(eqtls[i]))
                f_out.close()


def main(args):
        out = args.out
        eqtls = get_eqtls(out)
        subprocess.Popen("mkdir test",shell=True)
        write_snp_list(eqtls)

if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument('--out',help='Matrix eQTL cis-eQTL mapping results')
        args = parser.parse_args()
        main(args)
