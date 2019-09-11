#take en entrée les fichiers inputs
import coding
import glob

import unittest
import builtins
import sys
import debug

filtre = ""
name_input = "input"
name_output = "output"


folder_path_input = "filescoding/" +name_input
folder_path_output= "filescoding/" +name_output

output = []
verif = []
resume = []


def fake_input():
    return input_file.readline()


def fake_print(value):
    output.append(str(value))


def read_output():
    for lines in outputFile.readlines():
        verif.append(lines)


builtins.input = fake_input
builtins.print = fake_print

if __name__ == '__main__':
    resume.append("######################################################\n")
    resume.append("######################################################\n")
    resume.append("\t\t\t\t\tRESULTAT\n")
    resume.append("######################################################\n")
    resume.append("######################################################\n")

    for files in glob.glob(folder_path_input + "*"):
        if filtre!="" and files.find(filtre)<0 : continue
        input_file = open(files)
        outputFile = open(files.replace(name_input, name_output))
        read_output()
        coding.main()

        resume.append("Result file : " + input_file.name + "\t\t")
        resume.append("votre sortie : " + str(output) +" ")
        resume.append("vs attendu " +str(verif))
        resume.append(" \t ===========> " + str(output == verif))
        if(output!=verif):
            resume.append(" \t ===========>  même joueur joue encore...")
        resume.append("\n")
        output.clear()
        verif.clear()
    debug.show(''.join(resume))
