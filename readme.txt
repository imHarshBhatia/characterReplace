This code basically removes the non-ascii characters from all the files in the input folder and saves all the files in the output folder.

Before following the steps to create an exe file, make sure you have Python installed on your system.

Steps to create an .exe file of the script.

To Create the exe file of the python script.
1. Install pyinstaller using pip
  Run the command pip install pyinstaller on the command prompt on windows as admin.
2. After installing pyinstaller, open command prompt as admin in the path where your script is placed.
3. Run the command pyinstaller --onefile <script_name>.py
4. The .exe file would be placed in the dist folder.
5. Copy the .exe file and place the file where the script is existing.
