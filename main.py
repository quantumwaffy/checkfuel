from parsexml import parsing5676 as ps
from scanfiles import scan as sc
from calc import calculation
from time import sleep

dlist = []
def startgetinf():
    scan = sc()
    for file in scan.checkfiles():
        if file in dlist:
            print("Files done")
            scan.removefiles(file)
        else:
            dlist.append(file)
            train = ps()
            train.parsingxml(file)
            print("Parsing")
            print(dlist)
            sleep(2)
            train.gotosql()
            scan.movefiles(file)
            scan.removefiles(file)
            del train
    del scan

def sql():
    num_train = input("Input train number: ")
    inf = calculation()
    inf.sqlbyreq(num_train)
    inf.seestation()

# def make():
#     tr = calculation()
#     tr.maketrainsql()
# make()

def main():
    startgetinf()
    sql()
main()

# active = True
# while active:
#     sleep(3)
#     main()


















