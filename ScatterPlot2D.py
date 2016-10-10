#!/usr/bin/env python
# coding: UTF-8
import os
import sys
import shutil
import time
import glob
import zipfile
import gzip
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from scipy import genfromtxt

import numpy as np

Alpha_x = 1.0
Alpha_y = 1.0

ProblemSettings =	{	"DTLZ1":["Plane", 0.5, 0.5, 0.5],
						"DTLZ2":["Sphere", 1.0, 1.0, 1.0],
						"DTLZ3":["Sphere", 1.0, 1.0, 1.0],
						"DTLZ4":["Sphere", 1.0, 1.0, 1.0],
						"WFG4":["Sphere", 2.0, 4.0, 6.0]
					}

def MakeScatterPlot2d(InputFileName, ProblemName):
	#グラフ作成
	fig = pyplot.figure()
	ax = fig.add_subplot(1,1,1)
	
	#ファイル読み込み
	d = genfromtxt(InputFileName, delimiter="\t")
	
	# 軸ラベルの設定
	#ax.set_xlabel("f1")
	#ax.set_ylabel("f2")
	
	#ParetoFront描画
	FlagSphere = False
	FlagPlane = False
	
	if ProblemName == "":
		pass
	else:
		
		if "DTLZ" in ProblemName:
			pyplot.gca().set_aspect('equal', adjustable='box')
		
		if ProblemSettings[ProblemName][0] == "Sphere":
			FlagSphere = True
			
		if ProblemSettings[ProblemName][0] == "Plane":
			FlagPlane = True
			
		# PFのサイズ
		Alpha_x = ProblemSettings[ProblemName][1]
		Alpha_y = ProblemSettings[ProblemName][2]
		
		#draw sphere
		if FlagSphere:
			#u, v = np.mgrid[0:0.5*np.pi:20j, 0:0.5*np.pi:10j] #0以上1以下のみ
			u = np.mgrid[0:0.5*np.pi:20j]
			x = np.cos(u)
			y = np.sin(u)
			
			x *= Alpha_x
			y *= Alpha_y
			
			ax.plot(x, y, '--', color="#87CEEB")
		
		#draw hyperplane
		if FlagPlane:
			u = np.mgrid[0:1.01:0.1]
			x = u
			y = 1-u
			
			x *= Alpha_x
			y *= Alpha_y
			
			ax.plot(x, y, '--', color="#87CEEB")
			
	# 表示範囲の設定
	if FlagSphere==True or FlagPlane==True:
		ax.set_xlim((-0.1*Alpha_x), Alpha_x*1.25)
		ax.set_ylim((-0.1*Alpha_y), Alpha_y*1.25)
		
		
	# グラフ描画
	ax.scatter(d[:,0], d[:,1], c="#ff0000", s=35)
	
	pyplot.savefig(InputFileName.split(".")[0]+".eps", bbox_inches="tight", transparent=True)
	pyplot.savefig(InputFileName.split(".")[0]+".png", bbox_inches="tight", transparent=True)
	#pyplot.show()

if __name__ == "__main__":
	argvs = sys.argv
	argc = len(argvs)
	
	
	if argc<2 or "-h" in argvs or "-H" in argvs:
		print("Usage:")
		print(argvs[0]+" <InputFileName> [Options]")
		
		print("\n[Options]")
		print("-H (Help)\t: Usage of this script")
		print("-PF \t\t: Plot with Pareto Front (-PF <Problem>)")
		
		sys.exit()
	
	InputFileName = argvs[1]
	ProblemName = ""
	
	if "-PF" in argvs:
		ProblemName = argvs[argvs.index("-PF")+1]
	
	MakeScatterPlot3d(InputFileName, ProblemName)
	
	
