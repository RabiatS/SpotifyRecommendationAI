import hdbscan
import matplotlib.pyplot as plt
import random

def TrainModel(data):
    model = hdbscan.HDBSCAN(min_cluster_size=20, min_samples=10)
    labels = model.fit_predict(data)
    print(str(sorted(labels)))
    colorList = ['red', 'blue', 'green', 'purple', 'pink']
    i = 0
    for label in labels:
        r = random.random() * 255
        g = random.random() * 255
        b = random.random() * 255
        filtered_list_x = [data[i][0] for i in range(len(data)) if labels[i] == label]
        filtered_list_y = [data[i][4] for i in range(len(data)) if labels[i] == label]
        plt.scatter(filtered_list_x, filtered_list_y, 4, c=colorList[i])
        i = i +1
        if (i == len(colorList)):
            i = 0
    plt.xlabel("acousticness")
    plt.ylabel("dacibility")
    plt.show()
    return model