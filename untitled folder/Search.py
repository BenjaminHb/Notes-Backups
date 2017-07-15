#coding=utf-8

import csv

readerChEMBL = csv.DictReader(open('/Users/benjaminzhang/Downloads/main_ChEMBL_Test.csv', 'rb'))
resultChEMBL = {}
for item in readerChEMBL:
    resultChEMBL[item["MOLECULE_CHEMBL_ID"]] = item["TARGET_CHEMBL_ID"]
readerDrugBank = csv.DictReader(open('/Users/benjaminzhang/Downloads/main_DrugBank_Test.csv', 'rb'))
resultDrugBank = {}
for item in readerDrugBank:
    resultDrugBank[item["DrugBank_ID"]] = item["ChEMBL_ID"]

with open('/Users/benjaminzhang/Downloads/main_ChEMBL_Test.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)

print resultChEMBL
print resultDrugBank

csvFile = open("/Users/benjaminzhang/Downloads/Test.csv", "wb")
# 文件头以列表的形式传入函数，列表的每个元素表示每一列的标识
fileheader = ["MOLECULE_CHEMBL_ID", "DrugBank_ID_1", "TARGET_CHEMBL_ID", "DrugBank_ID_2"]

dict_writer = csv.writer(csvFile)
dict_writer.writerow(fileheader)


for i in resultChEMBL.items():
    MOLECULE_CHEMBL_ID = ""
    TARGET_CHEMBL_ID = ""
    DrugBank_ID_1 = ""
    DrugBank_ID_2 = ""
    for j in resultDrugBank.items():
        if i[0] == j[1]:
            DrugBank_ID_1 = j[0]
        else:
            DrugBank_ID_1 = ""
        MOLECULE_CHEMBL_ID = i[0]
        for w in resultDrugBank.items():
            if i[1] == w[1]:
                DrugBank_ID_2 = j[0]
            else:
                DrugBank_ID_2 = ""
            TARGET_CHEMBL_ID = i[1]
        if DrugBank_ID_1 <> "" or DrugBank_ID_2 <> "":
            print MOLECULE_CHEMBL_ID,",",DrugBank_ID_1,",",TARGET_CHEMBL_ID,",",DrugBank_ID_2
            dict_writer.writerow([MOLECULE_CHEMBL_ID,DrugBank_ID_1,TARGET_CHEMBL_ID,DrugBank_ID_2])

csvFile.close()



