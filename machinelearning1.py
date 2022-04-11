redcolor=0
red=0
orangecolor=1
orange=1
smooth=0
rough=1
apple=0
orange=1

#Put all data points in an array - features and labels in seperate arrays
features=[[redcolor,smooth],[orangecolor,rough],[redcolor,smooth],
          [redcolor,smooth],[orangecolor,rough],[orangecolor,rough],[redcolor,smooth]]
labels=[apple,orange,apple,apple,orange,orange,apple]

#import decision tree function from sklearn package and train it on your data
from sklearn import tree
classifier=tree.DecisionTreeClassifier()
classifier.fit(features,labels)

#take fresh input from user
inputcolor=input('Enter the color of the fruit: ')
if (inputcolor=='red' or inputcolor=='redcolor'):
    inputcolornew=0
else:
    inputcolornew=1
inputtexture=input('Enter the texture of the fruit: ')
if (inputtexture=='smooth'):
    inputtexturenew=0
else:
    inputtexturenew=1

#predict output for user's input and print output
if(classifier.predict([[inputcolornew,inputtexturenew]])==0):
    print('Fruit is an Apple')
else:
    print('Fruit is an Orange')