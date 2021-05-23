#!/usr/bin/python3
import os
from sys import stdout
import time

string = "ANTONIO"

if os.path.exists('files/'):
    """making a new directory to put all the tmp files"""
    os.mkdir('files')

"""Prints a string with a small amounnt of delay between each character"""
for let in string:
    """"""
    stdout.write(let)
    stdout.flush()
    time.sleep(0.01)
print()

"""CLEANING"""

if os.path.exists('files/'):
    os.rmdir('files')
