"""Enrollment analysis:  Summary report of majors enrolled in a class.
CS 210 project, Fall 2022.
Author:  Arya Krishnagiri
Credits: Brian Gilmore
"""
import doctest
import csv


def read_csv_column(path: str, field: str) -> list[str]:
    """
    >>> read_csv_column("roster_selected.csv", "Major")
    ['DSCI', 'CIS', 'BADM', 'BIC', 'CIS', 'GSS']
    """
    with open(path, newline = "") as csvfile:
        reader = csv.DictReader(csvfile)
        empty = []
        for elem in reader:
            empty.append(elem[field])
    return empty
        

def counts(column: list[str]) -> dict[str, int]:
    """Returns a dict with counts of elements in column.

    >>> counts(["dog", "cat", "cat", "rabbit", "dog"])
    {'dog': 2, 'cat': 2, 'rabbit': 1}
    """
    counts = {}
    for f in column:
        if f in counts:
            counts[f] += 1
        else:
            counts[f] = 1
    return counts

def read_csv_dict(path: str, key_field: str, value_field: str) -> dict[str, dict]:
    """Read a CSV with column headers into a dict with selected
    key and value fields.

    >>> read_csv_dict("data/test_programs.csv", key_field="Code", value_field="Program Name")
    {'ABAO': 'Applied Behavior Analysis', 'ACTG': 'Accounting', 'ADBR': 'Advertising and Brand Responsibility'}
    """
    rcdict= {}
    with open(path, newline="") as savedict:
        reader_2 = csv.DictReader(savedict)
        for row in reader_2:
            rcdict[row[key_field]] = row[value_field]
        return rcdict

def items_v_k(words:dict) -> [int,str]:
    newcount = []
    for key, value in words.items():
        swap = (value,key)
        newcount.append(swap)
    return newcount


def main():
    doctest.testmod()
    majors = read_csv_column("roster_selected.csv", "Major")
    counts_by_major = counts(majors)
    program_names = read_csv_dict("programs.csv", "Code", "Program Name")
    by_count = items_v_k(counts_by_major)
    by_count.sort(reverse = True) #From largest to smallest
    for count, code in by_count:
        program = program_names[code]
        print(count, program)

if __name__ == "__main__":
    main()
