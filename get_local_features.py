import csv
import numpy as np
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import snap
import sys

def readEmbeddingFile():
    # Read node embeddings file
    node_embeddings = {} # dict from node ID to embedding
    embeddingFile = "train_edges.emb"
    
    index = 0
    with open(embeddingFile) as new:
        for line in csv.reader(new, delimiter=" "):
            # Ignore header
            if index == 0:
                index += 1
                continue
            
            nodeID = int(line[0])
            embeddings = np.array([float(val) for val in line[1:]])
            
            node_embeddings[nodeID] = embeddings
            
            index += 1
    return node_embeddings


def getNeighbors(G):
    neighbor_ids = {}
    for node in G.Nodes():
        nid = node.GetId()
        deg = node.GetDeg()
        for j in range(deg):
            neighborId = node.GetNbrNId(j)
            if nid not in neighbor_ids:
                neighbor_ids[nid] = []
            neighbor_ids[nid].append(neighborId)
    return neighbor_ids

def addLocalFeatures(node_embeddings, G):
    neighbor_ids = getNeighbors(G)
    n = G.GetNodes()
    num_features = 2
    features = {}
    for i, node in enumerate(G.Nodes()):
        if i%100 == 0: print(i)
        # if i >10: break
        nid = node.GetId()
        deg = node.GetDeg()
        edgesOut = 0
        for neighbor in neighbor_ids[nid]:
            neighborI = G.GetNI(neighbor)
            for ID in neighborI.GetOutEdges():
                if ID not in neighbor_ids[nid]:
                    edgesOut += 1
        features[nid] = [deg, edgesOut]
    V_old = features
    for k in range(3):
        print(k)
        V_new = {}
        for i, node in enumerate(G.Nodes()):
            # if i > 10: break
            nid = node.GetId()
            feat_sum = np.zeros(len(V_old[nid]))
            if len(neighbor_ids[nid]) != 0:
                for neighbor in neighbor_ids[nid]:
                    feat_sum += V_old[neighbor]
                mean = [x / len(neighbor_ids[nid]) for x in feat_sum]
            else:
                mean = feat_sum
            V_new[nid] = np.append(V_old[nid], [mean, feat_sum])

        V_old = V_new.copy()
    return V_new

def writeEmbeddings():
    G = snap.LoadEdgeList(snap.PUNGraph, "disease-chemical.tsv", 0, 1)
    node_embeddings=readEmbeddingFile()
    V_new = addLocalFeatures(node_embeddings,G)
    # print (V_new)
    # print (node_embeddings)
    with open('local_features_embeddings.txt', 'w') as f:
        f.write("%d %d\n" % (G.GetNodes(), 54+128))
        for nid in node_embeddings:
            # print(node_embeddings[nid])
            # print(V_new[nid])
            embedding = np.append(node_embeddings[nid], V_new[nid])
            f.write("{}\t".format(nid))
            for item in embedding:
                f.write("%f " % item)
            f.write("\n")

writeEmbeddings()


# Read train/test sets and node embeddings files
def readFiles():
    
    # Read train/test sets
    train_nodes = []
    train_y = []
    
    test_nodes = []
    test_y = []
    
    trainFile = "train.tsv"
    testFile = "test.tsv"
    
    with open(trainFile) as new:
        for line in csv.reader(new, delimiter="\t"):
            train_nodes.append((int(line[0]), int(line[1])))
            train_y.append(int(line[2]))
    
    with open(testFile) as new:
        for line in csv.reader(new, delimiter="\t"):
            test_nodes.append((int(line[0]), int(line[1])))
            test_y.append(int(line[2]))
    
    # Read node embeddings file
    node_embeddings = {} # dict from node ID to embedding
    embeddingFile = "train_edges.emb"
    
    index = 0
    with open(embeddingFile) as new:
        for line in csv.reader(new, delimiter=" "):
            # Ignore header
            if index == 0:
                index += 1
                continue
            
            nodeID = int(line[0])
            embeddings = np.array([float(val) for val in line[1:]])
            
            node_embeddings[nodeID] = embeddings
            
            index += 1
    
    return train_nodes, train_y, test_nodes, test_y, node_embeddings




