import csv
import random
from time import process_time
from randomGenerator import randgen
from sortingAlgo import InsertionSort
from sortingAlgo import MergeInsertSort
from sortingAlgo import MergeSort
from sortingAlgo import Merge

header = ["n", "Avg Key Comp", "Avg Processing Time"]

fixedS = 50



with open("Integration of Mergesort and Insertion Sort/csv_files/fixed_S_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)

    #for n in range(1000, 10000000, 499995):
    for n in range(20, 50, 10):
        print("next operation")
        keyComp = 0
        cpuTime = 0

        for i in range(5):

            numlist = []
            randgen(numlist, 10000000, n)
            print(numlist)
            # start timer
            cpu_start = process_time()

            #keyComp += MergeInsertSort(numlist, 0, n-1, fixedS)
            keyComp += InsertionSort(numlist, 0, n-1)
            print(numlist)

            # end timer
            cpu_end = process_time()
            cpuTime += cpu_end-cpu_start
        
        avg_keyComp = keyComp/5
        avg_cpuTime = cpuTime/5

        writer.writerow([n, avg_keyComp, avg_cpuTime])
        print("Completed run for n = " + str(n))




