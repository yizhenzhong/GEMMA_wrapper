import glob
import argparse


def parse(log):
        estimates =[ log.split("_")[-1].split(".")[0]]
        f = open(log)
        for line in f:
                if "pve estimate in the null model" in line:
                        items = line.split()
                        i = items.index("=")
                        estimates.append(items[i+1])
                if "se(pve) in the null model" in line:
                        items = line.split()
                        i = items.index("=")
                        estimates.append(items[i+1])
                else:
                        continue
                return estimates


def main(args):
        out = args.out
        files = sorted(glob.glob('./output/output*.log.txt'), key=str.lower)
        out_f = open(out+"_PVE.txt","w")
        out_f.write("\t".join(["gene","pve","se(pve)"])+"\n")
        for i in files:
                out_f.write("\t".join(parse(i))+"\n")
        out_f.close()



if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument('--out',help='Output prefix')
        args = parser.parse_args()
        main(args)

