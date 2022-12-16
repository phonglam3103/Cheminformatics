# Welcome to Phong's place for visuallisation
I have always been intriguing by the beauty of visuallisation on the top-tier journals. Since the first time I acknowledged these figures were created by Python and R, I have always tried my best to reproduce these figures and built my own styles.
In this folder, you may find some:
1. Pymol scripts to customize the bond, the atom label and the representation of either the protein or the ligands.
2. Python notebooks to draw histograms of the distribution of the docking score using seaborns and matplotly
3. Python notebooks to draw ROC curve to evaluate the molecular docking models (Beside RMSD of the cocrystallized ligands)
4. In process...

## How to use?
1. RMSD files: In order to use the RMSD plots, you should have a look at the template csv file (with the data retrieved from the MDs) name *RMSD_p.csv* to know how to use it.

2. Histogram: this notebook was written to plot the distribution of the docking score of the screened compounds from molecular docking process. You can have a look at Histogram.csv file to know the format of the input. (You will need to sort the docking score in an ascending order)

3. ROC: this notebook was written to evaluate docking protocol/docking models. Generally, you will need to dock the known active compounds (actives) and inactive compounds (usually virtually generated decoys) and assess the Area under the curve (AUC) of the ROC curve. Generally, the higher the AUC-ROC value, the better the model. You can use the Vina_sort.csv file as a template, with the active compounds being value 1 in the third collumn and the values of the decoys are 0. You also need to sort the docking score in an ascending order.
