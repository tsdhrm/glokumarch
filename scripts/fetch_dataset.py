import os
import csv
import random

random.seed(4)

def balance_data(nfname, pnum):
    nfbalanced = random.choices(nfname, k=pnum)
    return nfbalanced

def get_fname_list(csvsrc):
    posfname = list()
    negfname = list()
    with open(csvsrc) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                posfname.append(row[0]) if row[1] == "1" else negfname.append(row[0])
            line_count+=1
    return posfname, negfname

def select_data(pname, fname):
    print(DATASET_SRC)
    return "sweet"

def main():
    global DATASET_SRC 
    global POSITVE_DST 
    global NEGATIVE_DST
    global CSV_SRC

    DATASET_SRC = "/home/tsdhrm/Pictures/trials/KAGGLE_RETINA/G1020/NerveRemoved_Images"
    POSITVE_DST = "/dataset/positiveimgs/"
    NEGATIVE_DST = "/dataset/negativeimgs/"
    CSV_SRC = "/home/tsdhrm/Pictures/trials/KAGGLE_RETINA/G1020/G1020.csv"


    p_fname, n_fname = get_fname_list(CSV_SRC)
    nf_balanced = balance_data(n_fname, len(p_fname))
    dataset = select_data(p_fname, nf_balanced)





if __name__ == "__main__":
    main()



