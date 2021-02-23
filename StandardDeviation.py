class StandardDeviation:

    def mean(self, dataSet):
        return sum(dataSet) / len(dataSet)

    def median(self):
        pass

    def mode(self):
        pass


sd = StandardDeviation()

mean = sd.mean([20, 5, 8, 26])

print('Mean of [20, 5, 8, 26] is: ', mean)