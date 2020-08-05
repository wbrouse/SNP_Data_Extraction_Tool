# SNP_Data_Extraction_Tool

This script will pull data from the ScanFold-Scan log.out file for all 241 windows that contain an SNP. 

This script requires three arguments to run. First call python, then call the script name, then call the ScanFold-Scan log.out file, then input the location of the SNP.

The output is a single text file containing a header with average z-score, average delta G, average ED, max ED, and min ED below the respective header.
