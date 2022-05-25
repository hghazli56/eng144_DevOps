import os
import math, datetime, sys

working_directory = os.getcwd()

def return_pid():
    print(os.getpid())


def os_info():
    print(os.cpu_count())

print(working_directory)

print(sys.path)