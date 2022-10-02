import pandas as pd
import numpy as np

class Classifier:
    def __init__(self, data_path: str):
        df = pd.read_csv(data_path)
        self.train_labels = df.iloc[:, 0]
        self.train_data = df.iloc[:, 2:len(df.columns)]

        print(self.train_data)
    
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
        counts_matrix = np.asmatrix(train_data.values)
        diff = np.tile(test_row.values, [counts_matrix.shape[0], 1]) - counts_matrix
        np.random.seed(0) # For tie breaking purposes
        distances = np.squeeze(np.asarray(np.sqrt(np.square(diff).sum(1))))
        eps = np.random.uniform(size=distances.shape)*1e-10 #Noise for tie break
        distances = distances + eps
        return distances
