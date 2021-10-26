"""
Name: Michael Diorio
lab8.py
"""
from lab7.lab7 import encode, encode_better


def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w+")
    i = 1
    for line in infile:
        words = line.split()
        for word in words:
            outfile.write(str(i) + " " + word + "\n")
            i = i + 1


def hourly_wages(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w+")
    for line in infile:
        parts = line.split()
        wage = float(parts[2])
        wage = wage + 1.65
        wage = wage * int(parts[3])
        outfile.write(parts[0] + " " + parts[1] + " " + (str("${:.2f}".format(wage))))


def calc_check_sum(isbn):
    acc = 0
    for i in range(10):
        pos = 10 - i
        acc = acc + (pos * int(isbn[i]))
    return acc


def send_message(file, friend):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "w+")
    for line in infile:
        outfile.write(line)


def send_safe_message(file, friend, key):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "w+")
    for line in infile:
        outfile.write(encode(line, key))


def send_uncrackable_message(file, friend, pad):
    infile = open(file, "r")
    pad_file = open(pad, "r")
    outfile = open(friend + ".txt", "w+")
    key = pad_file.read()
    for line in infile:
        outfile.write(encode_better(line, key))


def main():
    number_words("Walrus.txt", "WalrusOutput.txt")
    hourly_wages("hourly_wages.txt", "NewWage.txt")
    calc_check_sum("0072946520")
    send_message("message.txt", "Bob")
    # send_safe_message("secret_message.txt", "bob", )
    # send_uncrackable_message("safest_message.txt", )

    pass


main()
