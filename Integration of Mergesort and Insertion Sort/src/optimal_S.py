import csv
import random
from time import process_time
from randomGenerator import randgen
from sortingAlgo import InsertionSort
from sortingAlgo import MergeInsertSort
from sortingAlgo import MergeSort
from sortingAlgo import Merge

header = ["n","S", "Avg Key Comp", "Avg Processing Time"]

for n in [1000, 10000, 100000, 1000000, 10000000]:
    with open("Integration of Mergesort and Insertion Sort/csv_files/optimalS_"+str(n)+"_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)

        for S in range(5, 20, 1):
            print("next operation")
            keyComp = 0
            cpuTime = 0

            for i in range(3):

                numlist = []
                randgen(numlist, 10000000, n)
                
                # start timer
                cpu_start = process_time()

                keyComp += MergeInsertSort(numlist, 0, n-1, S)

                # end timer
                cpu_end = process_time()
                cpuTime += cpu_end-cpu_start
            
            avg_keyComp = keyComp/3
            avg_cpuTime = cpuTime/3

            writer.writerow([n, S, avg_keyComp, avg_cpuTime])
            print("Completed run for s = " + str(S))

