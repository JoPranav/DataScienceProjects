## importing scikit-learn (sklearn) for a simple decision tree  
from sklearn import tree

# Training Data [height,weight,shoe-size]
X = [[181,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],[175,64,39],[177,70,40],[159,55,37],[171,75,42],[181,85,43]]
# label data 
Y = ['male','female','female','female','male','male','male','female','male','female','male']

## train decision tree

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

## predict gender using decision tree
prediction = clf.predict([[190,70,43]])
print (prediction)