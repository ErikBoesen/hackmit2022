import pandas as pd
import numpy as np

class Classifier:
    def __init__(self, data_path: str):
        df = pd.read_csv(data_path)
        self.train_labels = df.iloc[:, 0]
        self.train_data = df.iloc[:, 1:len(df.columns)]
    
    def classify_row(self, row):
        return self.classify(row, self.train_data, self.train_labels, 5)

    def classify(self, test_row, train_data, train_labels, k):
        """Return the k most common classes among k nearest neigbors to test_row."""
        distances = self.fast_distances(test_row, train_data)
        data = {'Company': train_labels, 'Distance': distances}
        distance_data = pd.DataFrame(data)
        distance_data = distance_data.sort_values('Distance')
        result = distance_data.iloc[0:k]
        return result['Company']

    def fast_distances(self, test_row, train_data):
        """An array of the distances between test_row and each row in train_rows.

        Takes 2 arguments:
        test_row: A row of a table containing features of one
            test movie (e.g., test_20.iloc[0]).
        train_table: A table of features (for example, the whole
            table train_20)."""
        test_row = test_row.values.tolist()
        train_data = train_data.values.tolist()

        distances = []

        for train_row in train_data:
            n = len(train_row)
            sum = 0
            for i in range(n):
                sum += (train_row[i] - test_row[i])**2
            distances.append(sum**(1/2))

        return distances
