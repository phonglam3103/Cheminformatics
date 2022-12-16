#! /usr/bin/env python

import sys
import glob

def doit(n):
    file_names = glob.glob('*.pdbqt')
    everything = []
    failures = []
    i = 0
    print ('Found', len(file_names), 'pdbqt files')
    for file_name in file_names:
        file = open(file_name)
        lines = file.readlines()
        file.close()
        i+=1
        try:
            line = lines[1]
            result = float(line.split(':')[1].split()[0])
            #print(result, file_name)
            everything.append((result, file_name))
            #print (everything[i])
        except:
            failures.append(file_name)
    #everything.sort(lambda x,y: cmp(x[0], y[0]))
    everything.sort()
    #part = everything[:n]
    
    #for p in part:
    #    print (p[1],)
    #print
    f = open("Vina_sort.txt", "w")
    i = 0
    temp = ""
    for i in range(len(everything)):
        temp = str(everything[i])
        f.write (temp)
        f.write ('\n')
    f = open("Vina_sort.txt", "r")
    print (f.read())
    if len(failures) > 0:
        print ('WARNING:', len(failures), 'pdbqt files could not be processed')

if __name__ == '__main__':
	doit(10)
    #doit(int(sys.argv[1]))