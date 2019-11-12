from sklearn import datasets, tree, metrics
from sklearn.tree import export_graphviz
import pydotplus
import collections
import graphviz
import os
#os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/python/Lib/site-packages/graphviz'
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/python/Lib/site-packages/graphviz/'

if __name__ == "__main__":
    # Defining how much to train and test
    training_percentage = 0.7

    # Loading data and targets
    digits = datasets.load_digits()
    data = digits.data
    target = digits.target

    # Collecting input data
    nbr_tot_samples = data.shape[0]
    nbr_train_samples = int(nbr_tot_samples*training_percentage)
    nbr_test_samples = nbr_tot_samples-nbr_train_samples
    training_samples = data[0:nbr_train_samples]
    test_samples = data[nbr_train_samples:]

    # Collecting target data
    training_targets = target[0:nbr_train_samples]
    test_targets = target[nbr_train_samples:]

    # Creating classifier and training
    classifier = tree.DecisionTreeClassifier()
    classifier.fit(training_samples,training_targets)

    # Predicting
    predicted = classifier.predict(test_samples)
    print(predicted)

    print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(test_targets, predicted)))
    print("Confusion matrix:\n%s" % metrics.confusion_matrix(test_targets, predicted))
    
    # Visualize data
    dot_data = tree.export_graphviz(classifier, out_file=None) 
    graph = graphviz.Source(dot_data) 
    graph.render("iris", view=True) 