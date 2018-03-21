import networkx as nx
import random as r
import math as m
from scipy.stats import powerlaw as pw
import matplotlib.pyplot as plt
from collections import Counter

def Generation(nb_graph):
	N=[] #liste graphes
	fitC=[]
	fitD=[]
	diam=[]

	for i in range(nb_graph):
		n=r.randint(80,120)
		p=r.random()
		N.append(nx.fast_gnp_random_graph(n, p))
		
		diam.append(nx.diameter(N[i]))
		C=nx.clustering(N[i])
		D=nx.degree(N[i])		
		fitC.append(pw.fit(list(C.values()),discrete=True)[0])
		fitD.append(pw.fit(list(dict(D).values()),discrete=True)[0])
	F=fitness(fitC,fitD,diam)
	print(F)
	a=[]
	for j in range(nb_graph):
		a.append((N[j], F[j]))
	return a


def fitness(C,D,diam):
	minC, maxC, attC = min(C), max(C), (1-min(C))/(max(C)-min(C))
	minD, maxD,attD = min(D), max(D), (2.5-min(D))/(max(D)-min(D))
	minDiam, maxDiam = min(diam), max(diam)
	F=[]
	for i in range(len(C)):
		Ci = (C[i]-minC)/(maxC-minC)
		Di = (D[i]-minD)/(maxD-minD)
		diami = (diam[i]-minDiam)/(maxDiam-minDiam)
		F.append(((Ci-attC)**2/attC + (Di-attD)**2/attD + diami**2)/3)
	return F
	
def selection(population, nb_keep):
	newN=[]
	sort = sorted(population, key=lambda tup: tup[1])
	for i in range(nb_keep):
		newN.append(sort[i][1]) #changer le 1 par un 0 pour avoir les graphes
	return newN
	



Graphs = Generation(10)
N=selection(Graphs,5)
print(N)
#print(Graphs[0])


