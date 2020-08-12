import sys
from pathlib import Path
import csv
import re


# Hello ! This is the DNA software made by Arsalan Ghassemi for the Problem Set 6 of CS50's Introduction to Computer Science course.

# The user should input the command python dna.py file.csv file.txt with the csv file as the database of people to look in and the txt file as the DNA sequence to analyze.

# The software then returns the owner of the DNA by checking the Short Tandem Repeats in the DNA sequence.

# Feel free to send any ameliorations suggestions at contact@arsadevs.com


strs = []
dna = []
people = []


def main():
    if len(sys.argv) != 3 or sys.argv[1].count(".csv") == 0 or sys.argv[2].count(".txt") == 0:
        exit("Usage : python dna.py file.csv file.txt")
    with open(sys.argv[1], "r") as inputcsv:
        csvfile = csv.reader(inputcsv)
        for rows in csvfile:
            people.append(rows)
        del people[0]
    with open(sys.argv[1], "r") as inputcsv:
        csvfile = csv.reader(inputcsv)
        strs = next(csvfile)
        del strs[0]
    sequence = Path(sys.argv[2]).read_text()
    for i in strs:
        try:
            dna.append(str((max([len(x) // (len(str(i))) for x in re.findall(r'((?:' + str(i) + ')+)', sequence)]))))
        except ValueError:
            break
    for k in range(len(people)):
        if dna == people[k][1:]:
            exit(f'{people[k][0]}')

    exit("No match")


main()