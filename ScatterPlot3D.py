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
Alpha_z = 1.0

ProblemSettings =	{	"DTLZ1":["Plane", 0.5, 0.5, 0.5],
						"DTLZ2":["Sphere", 1.0, 1.0, 1.0],
						"DTLZ3":["Sphere", 1.0, 1.0, 1.0],
						"DTLZ4":["Sphere", 1.0, 1.0, 1.0],
						"WFG4":["Sphere", 2.0, 4.0, 6.0]
					}

def MakeScatterPlot3d(InputFileName, ProblemName):
	# グラフ作成
	fig = pyplot.figure()
	ax = Axes3D(fig)
	
	# 軸ラベルの設定
	ax.set_xlabel("f1")
	ax.set_ylabel("f2")
	ax.set_zlabel("f3")
	
	# 向きの設定
	ax.view_init(50, 30)
	
	# ファイル読み込み
	d = genfromtxt(InputFileName, delimiter="\t")
	
	#ParetoFront描画
	FlagSphere = False
	FlagPlane = False
	
	if ProblemName == "":
		pass
	else:
		if ProblemSettings[ProblemName][0] == "Sphere":
			FlagSphere = True
			
		if ProblemSettings[ProblemName][0] == "Plane":
			FlagPlane = True
		
		# PFのサイズ
		Alpha_x = ProblemSettings[ProblemName][1]
		Alpha_y = ProblemSettings[ProblemName][2]
		Alpha_z = ProblemSettings[ProblemName][3]
		
		#draw sphere
		if FlagSphere:
			#u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j] #球
			u, v = np.mgrid[0:0.5*np.pi:20j, 0:0.5*np.pi:10j] #0以上1以下のみ
			x=np.cos(u)*np.sin(v)
			y=np.sin(u)*np.sin(v)
			z=np.cos(v)
			
			x *= Alpha_x
			y *= Alpha_y
			z *= Alpha_z
			
			ax.plot_wireframe(x, y, z, color="#87CEEB")
		
		#draw hyperplane
		if FlagPlane:
			u, v = np.mgrid[0:1.01:0.1, 0:1.01:0.1]
			x = u[u[:,0] >= 0]
			y = v
			z = 1-(u+v)
			for (i,zi) in enumerate(z):
				for (j,zij) in enumerate(zi):
					if zij < 0:
						z[i][j] = 0
						x[i][j] = 0.1 * i
						y[i][j] = 1-0.1 * i
			
			x *= Alpha_x
			y *= Alpha_y
			z *= Alpha_z
		
			ax.plot_wireframe(x, y, z, color="#87CEEB")
	# 表示範囲の設定
	if FlagSphere==True or FlagPlane==True:
		ax.set_xlim(0, Alpha_x*1.2)
		ax.set_ylim(0, Alpha_y*1.2)
		ax.set_zlim(0, Alpha_z*1.2)
		#ax.dist = 15
		
		rows_x, cols_x = np.where(d>Alpha_x*1.2)
		d=np.delete(d, rows_x[np.where(cols_x==0)],0)
		
		rows_y, cols_y = np.where(d>Alpha_y*1.2)
		d=np.delete(d, rows_y[np.where(cols_y==1)],0)
		
		rows_z, cols_z = np.where(d>Alpha_z*1.2)
		d=np.delete(d, rows_z[np.where(cols_z==2)],0)
	
	# グラフ描画
	ax.plot(d[:,0], d[:,1], d[:,2], "o", color="#ff0000", ms=6, mew=0.5)
	
	pyplot.savefig(InputFileName.split(".")[0]+".png", bbox_inches="tight", transparent=True)
	pyplot.savefig(InputFileName.split(".")[0]+".eps", bbox_inches="tight", transparent=True)
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
	
	
