#!/usr/bin/env python
#coding:UTF-8

import sys
from ScatterPlot3D import*
from ScatterPlot2D import*
from ParallelcoordsPlot import*

def MakePlotFig(InputFileName, ProblemName):
	nObj = 0
	with open(InputFileName) as InputFile:
		Line = InputFile.readline()
		nObj = len(Line.split("\t"))
		
	if nObj == 2:
		MakeScatterPlot2d(InputFileName, ProblemName)
		
	elif nObj == 3:
		MakeScatterPlot3d(InputFileName, ProblemName)
		
	elif nObj > 3:
		MakeParallelcoordsPlot(InputFileName)

if __name__ == "__main__":
	argvs = sys.argv
	argc = len(argvs)
	
	if argc<2 or "-h" in argvs or "-H" in argvs:
		print("Usage:")
		print(argvs[0]+" <InputFileName> [Options]")
		
		print("\n[Options]")
		print("-H (Help)\t: Usage of this script")
		print("-PF \t\t: Plotting Pareto Front (-PF <Problem>)")
		print("-F (File)\t: Plotting data from 1 file(-F <InputFileName>)")
		print("-S (Seq.)\t: Plotting data from [*.dat] files(-S <DirectorylyName>)")
		
		sys.exit()
	
	if "-PF" in argvs:
		ProblemName = argvs[argvs.index("-PF")+1]
	else:
		ProblemName = ""
	
	if "-F" in argvs:
		InputFileName = argvs[argvs.index("-F")+1]
		MakePlotFig(InputFileName, ProblemName)

	if "-S" in argvs:
		InputDirName = argvs[argvs.index("-S")+1]
		
		if InputDirName.endswith('/'):
			InputDirName.rstrip('/')
		
		DatFileNameList = glob.glob(InputDirName+"/*.dat")
		for DatFileName in DatFileNameList:
			MakePlotFig(DatFileName, ProblemName)
		



