import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

def AP(models):
    fig, ax = plt.subplots(figsize=(20,10))
    c = 0
    for m in models:
        for k,v in results.items():
            if m in k:
                y = v[0][1:]
                plt.plot(x,y,marker='o',color=colors[c])
        c += 1

    plt.title("Avarage Precision",weight="bold")
    plt.xlabel("recall")
    plt.ylabel("precision")
    plt.xlim([0,10])
    plt.ylim([0,100])
    plt.xticks(x)
    BMF25 = mpatches.Patch(color='green', label='BMF25')
    TD_IDF = mpatches.Patch(color='blue', label='TD_IDF')
    Frequency = mpatches.Patch(color='black', label='Frequency')
    plt.legend(handles=[BMF25, TD_IDF, Frequency])
    plt.savefig(root + r"\Avarage_Precision.png")

def bars(models, metric):
    labels = []
    y = []
    fig, ax = plt.subplots(figsize=(20,10))
    width = 0.50
    for m in models:
        for k,v in results.items():
            if m in k:
                y.append(v[metric])
                labels.append(k)

    if metric == 1:
        plt.title("MAP",weight="bold")
    else:
        plt.title("NDCG",weight="bold")

    plt.ylim([0,100])
    x = np.arange(len(labels))
    bar = []
    bar.append(ax.bar(x[0], y[0], width,color="green"))
    bar.append(ax.bar(x[1], y[1], width,color="blue"))
    bar.append(ax.bar(x[2], y[2], width,color="black"))
    ax.set_xticklabels([])
    for b in bar:
        for i in b:
            height = i.get_height()
            ax.annotate('{}'.format(height),xy=(i.get_x() + i.get_width() / 2, height),xytext=(0, 3),textcoords="offset points",ha='center', va='bottom')

    BMF25 = mpatches.Patch(color='green', label='BMF25')
    TD_IDF = mpatches.Patch(color='blue', label='TD_IDF')
    Frequency = mpatches.Patch(color='black', label='Frequency')
    plt.legend(handles=[BMF25, TD_IDF, Frequency])

    if metric == 1:
        plt.savefig(root + r"\MAP.png")
    else:
        plt.savefig(root + r"\NDCG.png")
    
if __name__ == "__main__":
    root = os.path.abspath(os.curdir)

    results = {
				"BM25F":
					[
						[0.0, 79.875, 64.625, 61.375, 54.375, 51.083333333333336, 45.708333333333336, 37.041666666666664, 32.791666666666664, 19.708333333333332, 9.625],
						45,
						44
					],
				"TF_IDF":
					[
						[0.0, 55, 54, 47, 43, 37, 34, 32, 24, 19, 9],
						35,
						33
					],
				"Frequency":
					[
						[0.0, 51, 50, 46, 38, 34, 33, 30, 23, 19, 8],
						33,
						29
					]
	 		}

    plt.rcParams.update({'font.size': 16})
    x = [i for i in range(1,11,1)]
    colors = ['green', 'blue', 'black']
    models = ["BM25F", "TF_IDF", "Frequency"]
    AP(models)
    bars(models,1)
    bars(models,2)

    plt.show()
