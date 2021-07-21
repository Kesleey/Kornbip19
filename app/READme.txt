Hello!
1.  To run the program, have FLASK package installed in your python environment. (pip install flask)
2.  Run app.py and please check if you have the right file paths.
3.  Based on my research, it is impossible to upload a 'Folder/Directory' unless it is zipped.
    This is because the file selection windows is controlled by the operating system.
    The "Register a Student" button basically asks the user to upload a zip file.
    The program would then automatically, extract all the files contained in the zip file.
    All uploaded files will be contained in the "Uploads" folder inside the "static" folder.
    (It is then expected that the user should first put all the folder of each student in one zip file.)
4.  I was trying to upload multiple zip files, and extract them all at once but I don't know why it is not working.
    I have read somewhere that it is, again, because the file selection windows is controlled by the operating system.
    gods at stackoverflow suggests that a solution for this is to have a multiple upload fields... we don't want that.
    I would still try to work on this matter.
5.  Error handling and validation will be the UI team's next task for this week.
6.  While the UI team is improving, polishing, and developing the app, the others could start integrating the model into the app.
Thank you!

