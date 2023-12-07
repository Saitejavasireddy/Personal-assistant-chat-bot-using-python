import subprocess
import wmi
import os
import sys
import webbrowser

if os.path.exists('Files and Document') == False:
    os.mkdir('Files and Document')
path = 'Files and Document/'


def isContain(text, list):
    for word in list:
        if word in text:
            return True
    return False


def createFile(text):
    # change the applocation as per your system path
    appLocation = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"

    if isContain(text, ["ppt", "power point", "powerpoint"]):
        file_name = "sample_file.ppt"
        appLocation = "C:\\Program Files (x86)\\Microsoft Office\\Office15\\POWERPNT.exe"

    elif isContain(text, ['excel', 'spreadsheet']):
        file_name = "sample_file.xsl"
        appLocation = "C:\\Program Files (x86)\\Microsoft Office\\Office15\\EXCEL.EXE"

    elif isContain(text, ['word', 'document']):
        file_name = "sample_file.docx"
        appLocation = "C:\\Program Files (x86)\\Microsoft Office\\Office15\\WINWORD.EXE"

    elif isContain(text, ["text", "simple", "normal"]):
        file_name = "sample_file.txt"
    elif "python" in text:
        file_name = "sample_file.py"
    elif "css" in text:
        file_name = "sample_file.css"
    elif "javascript" in text:
        file_name = "sample_file.js"
    elif "html" in text:
        file_name = "sample_file.html"
    elif "c plus plus" in text or "c + +" in text:
        file_name = "sample_file.cpp"
    elif "java" in text:
        file_name = "sample_file.java"
    elif "json" in text:
        file_name = "sample_file.json"
    else:
        return "Unable to create this type of file"

    file = open(path + file_name, 'w')
    file.close()
    subprocess.Popen([appLocation, path + file_name])
    return "File is created.\nNow you can edit this file"


