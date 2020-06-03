#!/usr/bin/env/python


# Perform the Havel-Hakimi algorithm on a given sequence of answers.
# return true if the answers are consistent (i.e. it's possible that everyone is telling the truth)
# return false if the answers are inconsistent (i.e. someone must be lying)
#     Remove all 0's from the sequence (i.e. warmup1).
#     If the sequence is now empty (no elements left), stop and return true.
#     Sort the sequence in descending order (i.e. warmup2).
#     Remove the first answer (which is also the largest answer, or tied for the largest) from the sequence and call it N.
#     The sequence is now 1 shorter than it was after the previous step.
#     If N is greater than the length of this new sequence (i.e. warmup3), stop and return false.
#     Subtract 1 from each of the first N elements of the new sequence (i.e. warmup4).
#     Continue from step 1 using the sequence from the previous step.

# Eventually you'll either return true in step 2, or false in step 5.



import sys

# GLOBALS

N = None

def warmup1(arr):
    return [num for num in arr if num != 0]

def warmup2(arr): 
    return sorted(arr, reverse=True)

def warmup3(n, arr):
    return n > len(arr)

def warmup4(n, arr):
    arr = warmup2(arr)
    return [num-1 for num in arr[:n]] + arr[n:]

def hh(arr):
    arr = warmup1(arr) # Remove all zeroes
    if len(arr) == 0:
        print("Sequence is empty.")
        return True
    
    #Sort the sequence
    arr = warmup2(arr)

    N = arr.pop(0)

    if N > len(arr):
        print("False")
        return False
    
    arr = warmup4(N,arr)

    print("Recursion")
    hh(arr)




def main():
    print(hh([16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16]))

if __name__ == "__main__":
    main()