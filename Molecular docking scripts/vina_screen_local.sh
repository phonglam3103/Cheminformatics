#! /bin/bash
mkdir out
for f in *.pdbqt; do
    b=`basename $f`
    echo Processing ligand $b
    vina2 --config conf.txt --ligand $f --out out/${b} 
done
