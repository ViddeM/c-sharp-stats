import os
import datetime

def countLines():
    now = datetime.datetime.now()

    projectPath = "Some_Path"

    emptyLinesCount = 0
    commentLinesCount = 0
    XMLCommentLinesCount = 0
    codeLinesCount = 0

    text = ""
    for subdir, dirs, files in os.walk(projectPath):
        for file in files:
            if file.endswith(".cs"):
                filepath = os.path.join(subdir, file)
                fileText = open(filepath, 'r')
                text += fileText.read()

                with open(filepath) as f:
                    for line in f.readlines():
                        if not line.strip():
                            emptyLinesCount += 1

                        line = line.strip()
                        if (line.startswith('///')):
                            XMLCommentLinesCount += 1
                        elif (line.startswith('//')):
                            commentLinesCount += 1
                        else:
                            codeLinesCount += 1

                print('counted lines in: ' + filepath)

    filename = "codestats_"
    filename += str(now.year) + '_' + str(now.month) + '_' + str(now.day) + '_' + str(now.hour) + '_' + str(now.minute) + '_' + str(now.second)
    writepath = "D:/CodeStats/"
    filenamewithpath = (writepath + filename + ".txt")

    print('Number of empty lines = ' + str(emptyLinesCount) + "\nNumber of normal comment lines = " + str(commentLinesCount) + "\nNumber of xml comment lines = " + str(XMLCommentLinesCount) + "\nNumber of lines of c# code = " + str(codeLinesCount))
    print('Total number of lines = ' + str(emptyLinesCount + commentLinesCount + XMLCommentLinesCount + codeLinesCount))
    print('Writing stats to file ' + filenamewithpath)
    statsfile = open(filenamewithpath, "w+")
    statsfile.write('Number of empty lines = ' + str(emptyLinesCount) + "\nNumber of normal comment lines = " +
                    str(commentLinesCount) + "\nNumber of xml comment lines = " + str(XMLCommentLinesCount) +
                    "\nNumber of lines of c# code = " + str(codeLinesCount) +
                    '\nTotal number of lines = ' + str(emptyLinesCount + commentLinesCount + XMLCommentLinesCount +
                    codeLinesCount))



countLines()