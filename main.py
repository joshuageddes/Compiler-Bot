import subprocess
import sys


def runCode(filePath):

    file = open(filePath , 'r')



    #subprocess.run() runs external "program" in a seperate environment
    #sys.executable gives path to Python execute

    result = subprocess.run(
        [sys.executable, "-c", file.read()], capture_output=True, text=True, timeout=1
    )

    #Prints out successful shell output
    stdout = result.stdout

    #Prints out error messages
    stderr = result.stderr

    output = stdout + stderr

    print(output)

    file.close()

    return output

def testImport(num):
    print(num)