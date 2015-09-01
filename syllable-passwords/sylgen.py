#!/usr/bin/env python

# koremutake syllables
SYLLABLES = ["ba", "be", "bi", "bo", "bu", "by", "da", "de", "di", "do", "du", "dy", "fe", "fi", "fo", "fu", "fy", "ga", "ge", "gi", "go", "gu", "gy", "ha", "he", "hi", "ho", "hu", "hy", "ja", "je", "ji", "jo", "ju", "jy", "ka", "ke", "ko", "ku", "ky", "la", "le", "li", "lo", "lu", "ly", "ma", "me", "mi", "mo", "mu", "my", "na", "ne", "ni", "no", "nu", "ny", "pa", "pe", "pi", "po", "pu", "py", "ra", "re", "ri", "ro", "ru", "ry", "sa", "se", "si", "so", "su", "sy", "ta", "te", "ti", "to", "tu", "ty", "va", "ve", "vi", "vo", "vu", "vy", "bra", "bre", "bri", "bro", "bru", "bry", "dra", "dre", "dri", "dro", "dru", "dry", "fra", "fre", "fri", "fro", "fru", "fry", "gra", "gre", "gri", "gro", "gru", "gry", "pra", "pre", "pri", "pro", "pru", "pry", "sta", "ste", "sti", "sto", "stu", "sty", "tra", "tre", "er", "ed", "in", "ex", "al", "en", "an", "ad", "or", "at", "ca", "ap", "el", "ci", "an", "et", "it", "ob", "of", "af", "au", "cy", "im", "op", "co", "up", "ing", "con", "ter", "com", "per", "ble", "der", "cal", "man", "est", "for", "mer", "col", "ful", "get", "low", "son", "tle", "day", "pen", "pre", "ten", "tor", "ver", "ber", "can", "ple", "fer", "gen", "den", "mag", "sub", "sur", "men", "min", "out", "tal", "but", "cit", "cle", "cov", "dif", "ern", "eve", "hap", "ket", "nal", "sup", "ted", "tem", "tin", "tro", "tro"]

from random import choice
import sys

def print_usage():
    print("usage: %s length" % sys.argv[0])
    sys.exit(1)

if len(sys.argv) == 2:
    try:
        length = int(sys.argv[1])
    except ValueError:
        print_usage()
else:
    print_usage()

result = ""

for i in range(length):
    result += choice(SYLLABLES)

print(result)
