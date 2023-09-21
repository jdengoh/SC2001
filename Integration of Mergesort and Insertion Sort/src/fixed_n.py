import csv
import random
from time import process_time
from randomGenerator import randgen
from sortingAlgo import InsertionSort
from sortingAlgo import MergeInsertSort
from sortingAlgo import MergeSort
from sortingAlgo import Merge

header = ["S", "Avg Key Comp", "Avg Processing Time"]

fixedN = 1000000

with open("Integration of Mergesort and Insertion Sort/csv_files/fixed_n_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)

    #for n in range(1000, 10000000, 499995):
    for S in range(1, 51, 1):
        print("next operation")
        keyComp = 0
        cpuTime = 0

        for i in range(5):

            numlist = []
            randgen(numlist, 10000000, fixedN)
            
            # start timer
            cpu_start = process_time()

            keyComp += MergeInsertSort(numlist, 0, fixedN-1, S)

            # end timer
            cpu_end = process_time()
            cpuTime += cpu_end-cpu_start
        
        avg_keyComp = keyComp/5
        avg_cpuTime = cpuTime/5

        writer.writerow([S, avg_keyComp, avg_cpuTime])
        print("Completed run for s = " + str(S))
