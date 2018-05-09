import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import json

# Computer vision frequency of attributes by type (bar)
def freq_analysis_bar():
	sns.set(style='white')

	x = ('0.00', '0.05', '0.10', '0.15', '0.20', '0.25')
	n = np.genfromtxt('../analysis/frequent.csv')

	d = {'minimum frequency':[], 'attributes':[], 'Type': []}
	for i in range(1, len(n)):
		d['minimum frequency'].append(x[i])
		d['minimum frequency'].append(x[i])
		d['minimum frequency'].append(x[i])

		d['attributes'].append(n[i][2]/n[0][2])
		d['attributes'].append(n[i][1]/n[0][1])
		d['attributes'].append(n[i][0]/n[0][0])

		d['Type'].append('Official Rescuers')
		d['Type'].append('Rescuees')
		d['Type'].append('Volunteer Rescuers')

	df = pd.DataFrame(data=d)
	# print(df)
	ax = sns.barplot(x='minimum frequency', y='attributes', hue='Type', data = df, palette='Blues')

	sns.despine(bottom=True, left=True)
	plt.xlabel('Minimum Frequency')
	plt.ylabel('Percentage of Total Attributes')
	plt.title('Computer Vision Attributes Frequency Analysis')
	plt.show()

# Computer vision frequency of attributes by type (violin)
def freq_analysis_violin():
	sns.set(style='white')

	with open('../output/vr.json') as f:
			vr = json.loads(f.read())

	with open('../output/r.json') as f:
			r = json.loads(f.read())

	with open('../output/or.json') as f:
			o = json.loads(f.read())

	allf = {}
	vf = {}
	for x in vr:
		for a in x['attributes']:
			if a not in allf:
				allf[a] = 0
			if a not in vf:
				vf[a] = 0
			allf[a] += 1
			vf[a] += 1

	rf = {}
	for x in r:
		for a in x['attributes']:
			if a not in allf:
				allf[a] = 0
			if a not in rf:
				rf[a] = 0
			allf[a] += 1
			rf[a] += 1

	of = {}
	for x in o:
		for a in x['attributes']:
			if a not in allf:
				allf[a] = 0
			if a not in of:
				of[a] = 0
			allf[a] += 1
			of[a] += 1

	for x in allf:
		allf[x] /= float(len(vr) + len(r) + len(o))

	for x in vf:
		vf[x] /= float(len(vr))

	for x in rf:
		rf[x] /= float(len(r))

	for x in of:
		of[x] /= float(len(o))


	d = {'Frequency':[], 'Type':[]}
	for x in vf:
		d['Frequency'].append(vf[x])
		d['Type'].append('Volunteer Rescuers')

	for x in rf:
		d['Frequency'].append(rf[x])
		d['Type'].append('Rescuees')

	for x in of:
		d['Frequency'].append(of[x])
		d['Type'].append('Official Rescuers')

	for x in allf:
		d['Frequency'].append(allf[x])
		d['Type'].append('Combined')

	df = pd.DataFrame(data=d)
	ax = sns.violinplot(x='Type', y='Frequency', data=df, palette='Blues')
	plt.title('Computer Vision Attributes Frequency Analysis')

	sns.despine(bottom=True, left=True)
	plt.show()

# Accuracy of signal vs noise stacking classifier (bar)
def signal_noise_bar():
	sns.set(style='white')

	# n = np.genfromtxt('../output/optimal.json')
	with open('../output/optimal.json') as f:
		n = json.loads(f.read())
	d = {'minimum frequency':[], 'accuracy':[]}
	for x in n:
		d['minimum frequency'].append(x[0])
		d['accuracy'].append(x[1])

	df = pd.DataFrame(data=d)
	# print(df)
	ax = sns.barplot(x='minimum frequency', y='accuracy', data = df, palette='Blues')

	sns.despine(bottom=True, left=True)
	plt.xlabel('Minimum Frequency')
	plt.ylabel('Accuracy')
	plt.title('Signal vs Noise')
	plt.xticks(rotation='vertical')
	axes = plt.gca()
	axes.set_ylim([.95, 1.])
	plt.show()

# Accuracy of respondent type stacking classifier (bar)
def resp_types_bar():
	sns.set(style='white')

	# n = np.genfromtxt('../output/optimal.json')
	with open('../output/optimal_resp.json') as f:
		n = json.loads(f.read())
	d = {'minimum frequency':[], 'accuracy':[]}
	for x in n:
		d['minimum frequency'].append(x[0])
		d['accuracy'].append(x[1])

	df = pd.DataFrame(data=d)
	# print(df)
	ax = sns.barplot(x='minimum frequency', y='accuracy', data = df, palette='Blues')

	sns.despine(bottom=True, left=True)
	plt.xlabel('Minimum Frequency')
	plt.ylabel('Accuracy')
	plt.title('Respondent Types Accuracy')
	plt.xticks(rotation='vertical')
	axes = plt.gca()
	axes.set_ylim([.65, .85])
	plt.show()

# Accuracy of signal vs noise stacking classifier with svm (bar)
def signal_noise_stacking_svm():
	sns.set(style='white')
	with open('../output/optimal_stack_large.json') as f:
		data = json.loads(f.read())
	d = {'minimum frequency':[], 'accuracy':[]}
	d['minimum frequency'] = [x[0] for x in data]
	d['accuracy'] = [x[1] for x in data]

	df = pd.DataFrame(data=d)
	ax = sns.barplot(x='minimum frequency', y='accuracy', data=df, palette='Blues')

	sns.despine(bottom=True, left=True)
	plt.xlabel('Minimum Frequency')
	plt.ylabel('Accuracy')
	plt.title('Signal vs Noise Accuracy (Stacking with SVM)')
	plt.xticks(rotation='vertical')
	axes = plt.gca()
	axes.set_ylim([.90, 1])
	plt.show()

# Accuracy of signal vs noise stacking classifier with mlp (bar)
def signal_noise_stacking_mlp():
	sns.set(style='white')
	with open('../output/optimal_stack_large_mlp.json') as f:
		data = json.loads(f.read())
	d = {'minimum frequency':[], 'accuracy':[]}
	d['minimum frequency'] = [x[0] for x in data]
	d['accuracy'] = [x[1] for x in data]

	df = pd.DataFrame(data=d)
	ax = sns.barplot(x='minimum frequency', y='accuracy', data=df, palette='Purples')

	sns.despine(bottom=True, left=True)
	plt.xlabel('Minimum Frequency')
	plt.ylabel('Accuracy')
	plt.title('Signal vs Noise Accuracy (Stacking with MLP)')
	plt.xticks(rotation='vertical')
	axes = plt.gca()
	axes.set_ylim([.90, 1])
	plt.show()

# Accuracy of respondent type classifier and base classifiers (line)
def resp_types_accuracies_line():
	sns.set(style='white')
	with open('../output/optimal_resp_svm_line.json') as f:
		data = json.loads(f.read())
	t = ['svm', 'gnb', 'mnb', 'bnb', 'knn', 'dt', 'sgd', 'mlp']
	d = {'minimum frequency':[], 'accuracy':[], 'type':[]}

	for x in data:
		d['minimum frequency'].append(x[0])
		d['accuracy'].append(x[1])
		d['type'].append('stacked')
		for i in range(len(x[2])):
			d['minimum frequency'].append(x[0])
			d['accuracy'].append(x[2][i])
			d['type'].append(t[i])

	df = pd.DataFrame(data=d)
	# ax = sns.tsplot(x='minimum frequency', y='accuracy', unit='type', data=df, palette='Blues')

	plt.plot([x[0] for x in data], [x[2][0] for x in data])
	plt.plot([x[0] for x in data], [x[2][1] for x in data])
	plt.plot([x[0] for x in data], [x[2][2] for x in data])
	plt.plot([x[0] for x in data], [x[2][3] for x in data])
	plt.plot([x[0] for x in data], [x[2][4] for x in data])
	plt.plot([x[0] for x in data], [x[2][5] for x in data])
	plt.plot([x[0] for x in data], [x[2][6] for x in data])
	plt.plot([x[0] for x in data], [x[2][7] for x in data])

	plt.plot([x[0] for x in data], [x[1] for x in data])
	plt.axis([0,.1,0,1])

	sns.despine(bottom=True, left=True)
	plt.xlabel('Minimum Frequency')
	plt.ylabel('Accuracy')
	plt.title('Respondent Type Classifier Accuracy (Stacking with SVM)')
	plt.xticks(rotation='vertical')
	plt.show()

# Accuracy of signal vs noise stacking classifier and base classifiers (line)
def signal_noise_accuracies_line():
	sns.set(style='white')
	with open('../output/optimal_noise_svm_line.json') as f:
		data = json.loads(f.read())
	t = ['svm', 'gnb', 'mnb', 'bnb', 'knn', 'dt', 'sgd', 'mlp']
	d = {'minimum frequency':[], 'accuracy':[], 'type':[]}

	for x in data:
		d['minimum frequency'].append(x[0])
		d['accuracy'].append(x[1])
		d['type'].append('stacked')
		for i in range(len(x[2])):
			d['minimum frequency'].append(x[0])
			d['accuracy'].append(x[2][i])
			d['type'].append(t[i])

	df = pd.DataFrame(data=d)
	# ax = sns.tsplot(x='minimum frequency', y='accuracy', unit='type', data=df, palette='Blues')

	plt.plot([x[0] for x in data], [x[2][0] for x in data])
	plt.plot([x[0] for x in data], [x[2][1] for x in data])
	plt.plot([x[0] for x in data], [x[2][2] for x in data])
	plt.plot([x[0] for x in data], [x[2][3] for x in data])
	plt.plot([x[0] for x in data], [x[2][4] for x in data])
	plt.plot([x[0] for x in data], [x[2][5] for x in data])
	plt.plot([x[0] for x in data], [x[2][6] for x in data])
	plt.plot([x[0] for x in data], [x[2][7] for x in data])

	plt.plot([x[0] for x in data], [x[1] for x in data])
	plt.axis([0,.1,0,1])

	sns.despine(bottom=True, left=True)
	plt.xlabel('Minimum Frequency')
	plt.ylabel('Accuracy')
	plt.title('Signal vs Noise Classifier Accuracy (Stacking with SVM)')
	plt.xticks(rotation='vertical')
	plt.show()

# resp_types_bar()
signal_noise_stacking_mlp()
# signal_noise_accuracies_line()