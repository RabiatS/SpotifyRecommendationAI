import csv
from ColumnEnum import ColumnEnum
import HDBSCAN

artistEnum = {}


def main():
    data = loadData()
    data = cleanData(data)
    #print(str(data))
    model = HDBSCAN.TrainModel(data)



# loads sample data from file
def loadData():
    data = []
    with open('Dataset/spotify.csv', newline='\r\n', encoding='utf8') as csvfile:
        reader = csv.reader(csvfile)
        skipFirst = True
        for row in reader:
            if skipFirst:
                skipFirst = False
                continue
            data.append(row)
    return data


# converts data to all numeric values for training and testing
# artist names will be added to a dictionary for consistency
# TODO: output this dictionary to a file
# TODO: load dictionary from file on startup
def cleanData(data):
    for row in data:
        # editing items in descending index order to avoid messing up indexing
        # avoiding converting date to numeric plus year covers information
        row.pop(ColumnEnum.release_date.value)
        # name has no relevance on song similarity (in my opinion)
        row.pop(ColumnEnum.name.value)
        # ID is not relevany
        row.pop(ColumnEnum.id.value)
        # convert artist to enumeration
        if row[ColumnEnum.artists.value] not in artistEnum:
            val = len(artistEnum)
            artistEnum[row[ColumnEnum.artists.value]] = val
            row[ColumnEnum.artists.value] = val
        else:
            val = artistEnum[row[ColumnEnum.artists.value]]
            row[ColumnEnum.artists.value] = val

        # cast all data in list to floats
        i = 0
        while i < len(row):
            row[i] = float(row[i])
            i = i + 1
    data = data[0:2000]
    return data


if __name__ == "__main__":
    main()