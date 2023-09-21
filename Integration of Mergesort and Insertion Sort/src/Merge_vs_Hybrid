import csv
import random
from time import process_time
from randomGenerator import randgen
from sortingAlgo import InsertionSort
from sortingAlgo import MergeInsertSort
from sortingAlgo import MergeSort
from sortingAlgo import Merge

header = ["n", "Avg Key Comp", "Avg Processing Time"]

fixedN = 10000000

# Merge Sort
with open("Integration of Mergesort and Insertion Sort/csv_files/Merge_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)

    keyComp_Merge = 0
    cpuTime_Merge = 0
    
    for i in range(3):
        print("Running Merge Sort", i+1)
        numlist = []
        randgen(numlist, 10000000, fixedN)
        
        # Start timer
        cpu_start_Merge = process_time()
        keyComp_Merge += MergeSort(numlist, 0, fixedN-1)
        
        # End timer
        cpu_end_Merge = process_time()
        cpuTime_Merge += cpu_end_Merge-cpu_start_Merge
        
    # Find the average key comparisons and CPU time
    avg_keyComp_Merge = keyComp_Merge/3
    avg_cpuTime_Merge = cpuTime_Merge/3
    
    # Write to the csv file
    writer.writerow([fixedN, avg_keyComp_Merge, avg_cpuTime_Merge])
    print("Completed running Merge Sort",)

# Merge Insert Sort
with open("Integration of Mergesort and Insertion Sort/csv_files/MergeInsert_results.csv", "w", newline="") as f:  
    write = csv.writer(f)
    write.writerow(header)
    
    keyComp_Hybrid = 0
    cpuTime_Hybrid = 0
    
    for i in range (3):
        print("Running Merge Insert Sort", i+1)
        numlist = []
        randgen(numlist, 10000000, fixedN)
        
        # Start timer
        cpu_start_Hybrid = process_time()
        keyComp_Hybrid += MergeInsertSort(numlist, 0, fixedN-1, 2)
        
        # End timer
        cpu_end_Hybrid = process_time()
        cpuTime_Hybrid += cpu_end_Hybrid-cpu_start_Hybrid
        
    # Find the average key comparisons and CPU time
    avg_keyComp_Hybrid = keyComp_Hybrid/3
    avg_cpuTime_Hybrid = cpuTime_Hybrid/3
    
    # Write to csv file
    write.writerow([fixedN, avg_keyComp_Hybrid, avg_cpuTime_Hybrid])
    print("Completed running Merge Insert Sort")