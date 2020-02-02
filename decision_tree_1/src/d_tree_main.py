import os, sys
import tkinter as tk
from tkinter import filedialog
import numpy as np
import csv
from dTreeClass import dTree as dt

################################################
# @param [in]:  None
# @param [out]: File path to the input file
################################################
def getInFile():
  file_path = ""
  err = 0
  
  print("Please enter your input file.")
  file_path = filedialog.askopenfilename()
  if not file_path:
    err = 1
  else:
    print("You have selected: ", file_path)
  
  return err, file_path

################################################
# @param [in]:  Path to the input data file
# @param [out]: Input file data as an n * m matrix
################################################
def getInFileData(file_path):
  file_data = list()
  err = 0
  
  try:
    f = open(file_path)
    csv_reader = csv.reader(f)
    for row in csv_reader:
      file_data.append(row)
    if not file_data:
      err = 1
  except:
    err = 1
    file_data = list()
  
  return err, file_data

################################################
# @param [in]:  None
# @param [out]: None
################################################
def main():
  root = tk.Tk()
  root.withdraw()

  # Prompt user for input data file
  err, file_path = getInFile()
  if err:
    print("Please re-run and provide a file path.")
    sys.exit(1)
  # Get data from data file into list
  err, fileData = getInFileData(file_path)
  if err:
    print("Please re-run and provide a valid file path.")
    sys.exit(2)
  # Do stuff with the file data
  decTree = dt(fileData)
  err, root = decTree.runID3()
  if err:
    print("Error. An unexpected exception occurred.")
    sys.exit(3)
  print(root)
if __name__ == "__main__":
  main()
