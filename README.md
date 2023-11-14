
# DiffDock Protocol For Biochem course 

**[Original Paper](https://arxiv.org/abs/2210.01776)**\
**[DiffDock GitHub](https://github.com/gcorso/DiffDock)**

### Prerequisites

 - [ ] Obtain [LigPlot License](https://www.ebi.ac.uk/thornton-srv/software/LigPlus/applicence.html)
 - [ ] Install [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/) 
 - [ ] Open Conda Terminal 
 - [ ] Create folder C:\tmp (Windows) or /tmp (Mac/Linux)\
	Linux/Mac Users: Run <code>mkdir /tmp </code>\
	Windows Users: Run <code>mkdir C:\tmp </code>
 - [ ] Download [Chimera](https://www.cgl.ucsf.edu/chimerax/download.html)
 - [ ] Download [LigPlot](https://www.ebi.ac.uk/thornton-srv/software/LigPlus/download2.html)

 - [ ] Open LigPlot (ensure the tmp folder path is set correctly)
#### Troubleshooting:
Is LigPlot not opening?
 - [ ] You may need to install [Java](https://www.java.com/en/download/help/download_options.html)

## Obtaining Protein-Ligand Docked Poses Using DiffDock
1. Navigate to [DiffDock HuggingFace Space](https://huggingface.co/spaces/simonduerr/diffdock)
2. Upload the 2hyy_single.pdb and paste in the ligand SMILES sequence
3. Reduce number of samples to 10.
4. Download the result.
5. The results will be in zipped file. Extract them.


## Merging the Samples in Chimera(X)
In Chimera(X), open the 2hyy_single.pdb

Then open rank#.sdf

(Sidenote, you can see all the test ligand positions by opening rank#_reversediffusion)\
Take a moment to investigate the beauty that is biochemistry

Under File, Click save. Alternatively Ctrl(Windows/Linux)+S or Command(Mac)+S

![Picture of Save Screen](https://github.com/tkella47/BioChem_DiffDock/blob/main/Screenshot%202023-11-14%20145211.png?raw=true)

Make sure that both the sdf model and pdb model are selected.

Give your file a name and save it.

## Processing the PDB File

Next download [process_ligand_protein.py](https://github.com/tkella47/BioChem_DiffDock/blob/main/process_ligand_protein.py)

Navigate to the same directory as process_ligand_protein.py

Then run 
```
python process_ligand_protein PATH_TO_YOUR_SAVE_FILE.pdb
```
This will save a file <code>diffdocked.pdb</code> in the same place as the python file.

Additionally, if you wish to provide a different name or path for your file
simply run

```
python process_ligand_protein PATH_TO_YOUR_SAVE_FILE.pdb --output_path DESIRED_NAME_OR_PATH
```

## Viewing in LigPlot
Make sure LigPlot is open
Click File: Open : Browse
**Open the DiffDocked PDB file first**

#### Compare to Crystal Structure
Download [2HYY.pdb](https://files.rcsb.org/download/2HYY.pdb)
Click File: Open: Browse : 2hyy.pdb

In the bottom right hand corner, you can split the screen to see the difference between the structures



 

