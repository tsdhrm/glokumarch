import os
import csv
import random

random.seed(4)

def export_to_csv(pff, nff, export_dst):
    export_path = export_dst+"/selected_dataset.csv"
    with open(export_path, "w", newline='', encoding="UTF8") as file:
        writer = csv.writer(file)
        concatenated_data = [*pff, *nff]
        writer.writerow(["ImagePath", "Labels"])
        for i in range(len(concatenated_data)):
            if i < len(concatenated_data)//2:
                row_data = [concatenated_data[i], 1] 
            else:
                row_data = [concatenated_data[i], 0]
            writer.writerow(row_data)

def balance_data(nfname, pnum):
    nfbalanced = random.sample(nfname, pnum)
    return nfbalanced

def get_fname_list(csvsrc):
    posfname = list()
    negfname = list()
    with open(csvsrc) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                posfname.append(row[1]) if row[4] == "1" else negfname.append(row[1])
            line_count+=1
    nfb = balance_data(negfname, len(posfname))
    return posfname, nfb

def select_data(pname, nname):
    pfullfname = list()
    nfullfname = list()
    for data in os.listdir(DATASET_SRC):
        for i in range(0, len(pname)):
            if data == pname[i]:
                pfullfname.append(os.path.join(DATASET_SRC, data))
            elif data == nname[i]:
                nfullfname.append(os.path.join(DATASET_SRC, data))
    return pfullfname, nfullfname

def main():
    global DATASET_SRC 
    global CSV_SRC

    DATASET_SRC = "/home/tsdhrm/Pictures/trials/KAGGLE_RETINA/ORIGA/Images_Cropped"
    CSV_SRC = "/home/tsdhrm/Pictures/trials/KAGGLE_RETINA/ORIGA/OrigaList.csv"
    CSV_DST = "/home/tsdhrm/Documents/dev/cobaRetina"

    p_fname, n_fname = get_fname_list(CSV_SRC)
    p_fullfname, n_fullfname = select_data(p_fname, n_fname)
    export_to_csv(p_fullfname, n_fullfname, CSV_DST)





if __name__ == "__main__":
    main()



