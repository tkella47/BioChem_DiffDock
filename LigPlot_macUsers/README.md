# Mac Users Help
1. Download [LigPlot+](https://www.ebi.ac.uk/thornton-srv/software/LigPlus/)  \
You will need an academic license to do so.
2. Download [Java](https://www.java.com/en/download/manual.jsp) \
	Warning: You need to determine if you have an M1/2 Chip (Download ARM Java) or a Intel Chip (then download x64)
3. After you finish download LigPlus, find the zip folder in finder.
![Picture of Save Screen](https://github.com/tkella47/BioChem_DiffDock/blob/main/LigPlot_macUsers/screenshot_1.png?raw=true)
4. Double click on the zip file, and move the resulting LigPlus folder into the Users folder:
![Picture of Save Screen](https://github.com/tkella47/BioChem_DiffDock/blob/main/LigPlot_macUsers/upscaled_screenshot_2.png?raw=true)
5. Once you know that LigPlus is in your Users folder, open up “Terminal” 
6. Copy and paste the following into terminal:
 ```
 java -cp /Users/ -jar /Users/LigPlus/LigPlus.jar
 ```
7.  When you first open LigPlus, you will be brought to a window titled “Paths and Directories” \
Here, ensure that in Temporary Directory, it says <code>/tmp</code> and NOT <code>C:\tmp</code>

8. After downloading the proper Miniconda installer from Github link, go to downloads folder and make a New Terminal at Folder: \
Run 
```
bash Miniconda3-latest-MacOSX-x86_64.sh
```
**Warning x86 indicates an Intel chip** \
Your Mac may have an M1 or M2 chip, which is a different kind of chip.\
Follow these instructions
```
mkdir -p ~/miniconda3
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```
