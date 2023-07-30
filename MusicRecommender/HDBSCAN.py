import hdbscan
import matplotlib.pyplot as plt
import random
from ColumnEnum import ColumnEnum

def TrainModel(data):
    model = hdbscan.HDBSCAN(min_cluster_size=20, min_samples=1, prediction_data=True)
    labels = model.fit_predict(data)
    print(str(labels))
    """
    colorList = ['red', 'blue', 'green', 'purple', 'pink']
    i = 0
    ax = plt.axes(projection='3d')
    for label in labels:
        r = random.random() * 255
        g = random.random() * 255
        b = random.random() * 255
        filtered_list_x = [data[i][ColumnEnum.instrumentalness.value - 1] for i in range(len(data)) if labels[i] == label]
        filtered_list_y = [data[i][ColumnEnum.tempo.value - 3] for i in range(len(data)) if labels[i] == label]
        filtered_list_z = [float(data[i][ColumnEnum.year.value - 3]) for i in range(len(data)) if labels[i] == label]
        ax.scatter(filtered_list_x, filtered_list_y, filtered_list_z, c=colorList[i])
        i = i +1
        if (i == len(colorList)):
            i = 0
    plt.xlabel("instrumentalness")
    plt.ylabel("tempo")

    plt.show()
    """
    return model, labels

def GetRecommendation(modelTuple, input, data):
    labels = modelTuple[1]
    newLabels = hdbscan.approximate_predict(modelTuple[0], [input])
    if labels[0] == -1:
        print("input is an outlier")
        return -1
    else:
        clusterItems = [data[i] for i in range(len(data)) if labels[i] == newLabels[0]]
        index = int(random.random() * len(clusterItems))
        return clusterItems[index]