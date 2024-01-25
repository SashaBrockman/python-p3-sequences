#!/usr/bin/env python3

def print_fibonacci(length):
    sequence = []
    for n in range(length) :
        if len(sequence) < 1 :
            sequence.append(0)
        elif len(sequence) < 2 :
            sequence.append(1)
        else :
            sequence.append(sequence[n-1] + sequence[n-2])
    print(sequence)