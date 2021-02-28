#Nama          : Clarisa Natalia Edelin
#NIM           : 13519213
#TUCIL 2 STIMA : Topological Sort dengan metode Decrease and Conquer

def bacafiletxt():
    with open("toposort8.txt") as A: #mengubah nama file sesuai dengan nama file yang diinginkan disini
        lines = A.read().strip().split("\n")
    lis = {}
    for line in lines:
        b = line.replace(" ", "").split(",")
        lis[b[0]] = b[1:]

    return(lis)

def hapusmatkultertentudaridict(soals,matkulygmaudiapus,keys):
    for q in range(len(soals)):
        #print(q)
        if soals.get(keys[q]) != None:
            if(len(soals.get(keys[q])) > 0):
                for j in range(len(soals.get(keys[q]))):
                    #print(q,j)
                    if((soals.get(keys[q])[j]) == matkulygmaudiapus):
                        #print('yas')
                        soals.get(keys[q]).remove(matkulygmaudiapus)
                        break
        
    return soals

def hasiltoposort(soal,indeksss):
    key = list(soal.keys())
    hasilsort = {}
    arrayhasilpersemester = []

    for i in range(len(key)):
        if len(soal.get(key[i])) == 0:
            arrayhasilpersemester.append(i) 

    for aaa in range(len(arrayhasilpersemester)):
        hapusmatkultertentudaridict(soal,key[arrayhasilpersemester[aaa]],key)

    for aaa in range(len(arrayhasilpersemester)):
        del soal[key[arrayhasilpersemester[aaa]]]

    hasilsort = {indeksss:[]}
    for aaa in range(len(arrayhasilpersemester)):
        if(hasilsort.get(indeksss)) == []:
            hasilsort[indeksss] = [key[arrayhasilpersemester[aaa]]]
        else:
            hasilsort[indeksss].append(key[arrayhasilpersemester[aaa]])

    keyhasilsort = list(hasilsort.keys())
    print("semester", keyhasilsort[0], " :" , hasilsort.get(keyhasilsort[0]))


    keysekarang = list(soal.keys())

    if(len(keysekarang)) != 0:
        indeksss += 1
        hasiltoposort(soal,indeksss)


#program utama
soal = bacafiletxt()
indeksss = 1

hasiltoposort(soal,indeksss)

