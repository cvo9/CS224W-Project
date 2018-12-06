import csv
import numpy as np
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import snap
import sys

def plot_deg_distr():
	G = snap.LoadEdgeList(snap.PUNGraph, "disease-chemical.tsv", 0, 1)
	snap.PlotOutDegDistr(G, "deg_distr", "Out degree distribution for disease-drug network")

plot_deg_distr()