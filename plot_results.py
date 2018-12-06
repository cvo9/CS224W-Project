import matplotlib.pyplot as plt
import numpy as np 
def plot_results():
	N = 4
	lr_node2vec = [0.806, 0.8198, 0.7893, 0.817]
	lr_network = [0.8464, 0.8665, 0.8071, 0.8357]
	lr_finger = [0.8114, 0.8455, 0.7468, 0.7931]
	lr_all = [0.8464, 0.8665, 0.8071, 0.8357]

	rf_node2vec = [0.8333, 0.9013, 0.7485, 0.8178]
	rf_network = [0.84, 0.9025, 0.7507, 0.8196]
	rf_finger = [0.8411, 0.8991, 0.7567, 0.8218]
	rf_all = [0.8416, 0.9034, 0.7534, 0.8216]

	ind = np.arange(N)  # the x locations for the groups
	width = 0.2       # the width of the bars

	fig = plt.figure()
	ax = fig.add_subplot(111)
	rects1 = ax.bar(ind, lr_node2vec, width, color='royalblue')
	rects2 = ax.bar(ind+width, lr_network, width, color='seagreen')
	rects3 = ax.bar(ind+2*width, lr_finger, width, color='red')
	rects4 = ax.bar(ind+3*width, lr_all, width, color='purple')

	# add some
	ax.set_ylabel('Scores')
	ax.set_title('Logistic Regression scores by method and metric')
	ax.set_xticks(ind + width / 2)
	ax.set_xticklabels( ('Accuracy', 'Precision', 'Recall', 'F1 Score'))

	ax.legend( (rects1[0], rects2[0], rects3[0], rects4[0]), ('node2vec', 'node2vec+Network', 'node2vec+Fingerprints', 'node2vec+Network+Fingerprints') , loc = 'lower right')
	plt.savefig('lr_results')

	fig = plt.figure()
	ax = fig.add_subplot(111)
	rects1 = ax.bar(ind, rf_node2vec, width, color='royalblue')
	rects2 = ax.bar(ind+width, rf_network, width, color='seagreen')
	rects3 = ax.bar(ind+2*width, rf_finger, width, color='red')
	rects4 = ax.bar(ind+3*width, rf_all, width, color='purple')

	# add some
	ax.set_ylabel('Scores')
	ax.set_title('Random Forest scores by method and metric')
	ax.set_xticks(ind + width / 2)
	ax.set_xticklabels( ('Accuracy', 'Precision', 'Recall', 'F1 Score'))

	ax.legend( (rects1[0], rects2[0], rects3[0], rects4[0]), ('node2vec', 'node2vec+Network', 'node2vec+Fingerprints', 'node2vec+Network+Fingerprints') , loc = 'lower right')
	plt.savefig('rf_results')

plot_results()