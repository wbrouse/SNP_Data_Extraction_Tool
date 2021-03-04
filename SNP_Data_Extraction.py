#SNP_Data_Extraction.py
"""
By Warren B. Rouse, Moss Lab, Iowa State University

Extract data from log.out ScanFold-Scan file
Extracted data will include average MFE, ED, and z-score as well as maximum and minimum ED 

To print results
Usage: python ScanFold.out TranscriptCoordofSNP 

To write to a file 
Usage: python ScanFold.out TranscriptCoordofSNP > outfilename.txt

"""
import sys
import os

bpi = []				#defining the column in the text file that will be turned into a list
bpj = []				#defining the column in the text file that will be turned into a list
dG = []					#defining the column in the text file that will be turned into a list		
zscore = []				#defining the column in the text file that will be turned into a list
ED = []					#defining the column in the text file that will be turned into a list

filename = sys.argv[1]					#Defining user input file needed for to run the program as filename
SNP_Location = int(sys.argv[2])				#Defining user input SNP location need to run the program as SNP_Location

with open(filename , 'r') as fp:			#Open input file in read mode and refer to it as short name
	lines = fp.readlines()[1:]			#Read all lines in the input file except the first header line
	for line in lines:				#For loop that will define define a name to the respective column
		data = line.split('\t')			#Split data into respective column at tabs
		first = (data[0].strip())		#Pull out first column (nt i) from text file and strip the next line symbol from output
		second = (data[1].strip())		#Pull out second column (nt j) from text file and strip the next line symbol from output 
		third = float(data[3].strip())		#Pull out fourth column (dG) from text file and strip the next line symbol from output		
		fourth = float(data[4].strip())		#Pull out fifth column (zscore) from text file and strip the next line symbol from output
		fifth = float(data[6].strip())		#Pull out sixth column (ED) from text file and strip the next line symbol from output
		bpi.append(first)			#Create list of first column data
		bpj.append(second)			#Create list of second column data
		dG.append(third)			#Create list of fourth column data
		zscore.append(fourth)			#Create list of fifth column data
		ED.append(fifth)			#Create list of sixth column data
	flanki = int(SNP_Location - 120)		#Defining flanki as number of data upstream of user input SNP Location
	flankj = int(SNP_Location + 120)		#Defining flankj as number of data downstream of user input SNP Location
	if flanki < 0:					#If statement to ensure that any SNP closer than 120nt from beginning of the transcript will start at nt 1 and not throw an error 
		flanki = 1
	average_dG = int(sum(dG[flanki:flankj]))/241				#Defining average_dG as the integer sum of flanki and flankj divided by total number of nt (241)
	print("Average dG: " + str(average_dG))					#Print out average_dG
	average_zscore = int(sum(zscore[flanki:flankj]))/241			#Defining average_zscore as the integer sum of flanki and flankj divided by total number of nt (241)
	print("Average Z-Scoe: " + str(average_zscore))				#Print out average_score
	average_ED = int(sum(ED[flanki:flankj]))/241				#Defining average_ED as the integer sum of flanki and flankj divided by total number of nt (241)
	print("Average ED: " + str(average_ED))					#Print out average_ED
	max_ED = int(max(ED[flanki:flankj]))					#Defining max_ED as the maximum value between flanki and flankj
	print("Max ED: " + str(max_ED))						#Print out max_ED
	min_ED = int(min(ED[flanki:flankj]))					#Defining min_ED as the minimum value between flanki and flankj
	print("Minimum ED: " + str(min_ED))					#Print out max_ED
