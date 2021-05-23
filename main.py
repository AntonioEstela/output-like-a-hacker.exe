#!/usr/bin/python3
import os
from shutil import rmtree
from sys import stdout
import time


def printWithDelay(string):
    """Prints a string with a small amounnt of delay between each character"""
    for let in string:
        """"""
        stdout.write(let)
        stdout.flush()
        time.sleep(0.001)
    print()

def openFile(path):
    """Function that opens a file and then pass the content to the printWithDelay function to print its content"""
    with open(path, 'r') as f:
        printWithDelay(f.read())

if __name__ == "__main__":

    command = 'wget -d -o files/{} -O files/{} {}'

    """Getting some data to print"""
    if not os.path.exists('files/'):
        """making a new directory to put all the tmp files"""
        os.mkdir('files')
        os.system(command.format('output', 'data1', 'https://raw.githubusercontent.com/AntonioEstela/output-like-a-hacker.exe/main/logs/log-example-1.log'))
        os.system(command.format('output_2','data2', 'https://raw.githubusercontent.com/AntonioEstela/monty/master/main.c'))    

    """Open the files and then print its content"""
    try:
        openFile('files/output')
        openFile('files/data1')
        openFile('files/output_2')
        openFile('files/data2')
    except FileNotFoundError:
        print("Wrong Path")

    """CLEANING"""

    if os.path.exists('files/'):
        rmtree('files')
