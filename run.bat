:: Prints a custom name in the title bar of the console window.
@TITLE WordCount

:: Shows the message on a clean line disabling the display prompt. Usually, this line goes at the beginning of the file.
@ECHO OFF

:: Creates variables
@set path=testFolder
@set ext=.txt

:: Prints the text after the space on the screen.
@ECHO ===================================
@ECHO Running: main.py %path% %ext%
@ECHO ===================================

:: Runs the program with arguments 'path' and 'ext'
"%~dp0main.py" path ext

@ECHO ===================================
@ECHO Printing results: testFolder.txt
@ECHO ===================================

::Prints results to console
@type "%~dp0outputs\testFolder.txt"

:: Prints Newline
@ECHO.
:: Tells the console window to stay open after running the command. If you do not use this option, the window will close automatically as soon as the script finishes executing.
@PAUSE