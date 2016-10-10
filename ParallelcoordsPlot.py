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
from matplotlib.ticker import *
import numpy as np

def MakeParallelcoordsPlot(InputFileName):
	
	#グラフ作成
	fig = pyplot.figure()
	ax = fig.add_subplot(1,1,1)
	
	#ファイル読み込み
	d = genfromtxt(InputFileName, delimiter="\t")
	
	# グラフ描画
	for (i, di) in enumerate(d):
		pyplot.plot(di, c="#ff0000")
	
	# 表示範囲の設定
	#ax.set_xlim((-0.03*len(d[0])), len(d[0])*0.7)
	ax.set_xticks(range(0,len(d[0])))
	ax.set_xticklabels(range(0,len(d[0])+1))
	
	dwidth = d.max() -d.min()
	ax.set_ylim(d.min()-0.08*dwidth, d.max()+0.3*dwidth)
	
	#x軸の値を整数値に
	pyplot.gca().xaxis.set_major_locator(MultipleLocator(1))
	
	
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
		
		sys.exit()
	
	InputFileName = argvs[1]
	ProblemName = ""
	
	MakeParallelcoordsPlot(InputFileName)
