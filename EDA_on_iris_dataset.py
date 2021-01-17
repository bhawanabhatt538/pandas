import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Load Iris.csv into a pandas dataFrame.
iris=pd.read_csv("../datafile/IRIS.csv")
print(iris)

print('\n')

#Q=how many features and data points in the dataset
print(iris.shape)
#there are 150 rows and 5 columns

#(Q) What are the column names in our dataset?
print(iris.columns)

#(Q) How many data points for each class are present?
#(or) How many flowers for each species are present?
print('flowers for each species=','\n',iris.species.value_counts())

#Iris is a balanced dataset as the number of data points for every class is 50.

#2-D Scatter Plot:
iris.plot(kind='scatter',x='sepal_length',y='sepal_width')
plt.show()
#cannot make much sense out it.
#What if we color the points by thier class-label/flower-type.
sns.set_style('whitegrid');
sns.FacetGrid(iris,hue='species',height=5)\
.map(plt.scatter,'sepal_length','sepal_width')\
.add_legend()
plt.show()

# # Notice that the blue points can be easily seperated
# # from red and green by drawing a line.
# # But red and green data points cannot be easily seperated.
# # Can we draw multiple 2-D scatter plots for each combination of features?
# # How many cobinations exist? 4C2 = 6.

# #Observation(s):

#     #1=Using sepal_length and sepal_width features, we can distinguish Setosa flowers from others.
#     #2=Seperating Versicolor from Viginica is much harder as they have considerable overlap.

# #pair-plot

sns.set_style('whitegrid');
sns.pairplot(iris,hue='species',height=3);
plt.show()

# #Observations

#     #1=petal_length and petal_width are the most useful features to identify various flower types.
#     #2=While Setosa can be easily identified (linearly seperable), Virnica and Versicolor have some overlap (almost linearly seperable).
#     #3=We can find "lines" and "if-else" conditions to build a simple model to classify the flower types.

# #Histogram
#     #what about 1-D scatter plot using just one feature
#     #1-D scatter plot of petal length

iris_setosa=iris.loc[iris['species']=='Iris-setosa']
iris_virginica=iris.loc[iris['species']=='Iris-virginica']
iris_versicolor=iris.loc[iris['species']=='Iris-versicolor']

#print(iris_setosa["petal_length"])
plt.plot(iris_setosa['petal_length'],np.zeros_like(iris_setosa['petal_length']),'o')
plt.plot(iris_virginica['petal_length'],np.zeros_like(iris_virginica['petal_length']),'o')
plt.plot(iris_versicolor['petal_length'],np.zeros_like(iris_versicolor['petal_length']),'o')

plt.show()

#Disadvantage of 1-D scatter plot : Vertical y hard to make sense as points
#are overlapping a lot
#Are there better ways of visualizing 1-D scatter plot?
sns.set_style('whitegrid')
sns.FacetGrid(iris,hue='species',size=5).map(sns.distplot,'petal_length').add_legend()
plt.show()

sns.FacetGrid(iris,hue='species',size=5).map(sns.distplot,'sepal_length').add_legend()
plt.show()

sns.FacetGrid(iris,hue='species',size=5).map(sns.distplot,'petal_width').add_legend()
plt.show()

sns.FacetGrid(iris,hue='species',size=5).map(sns.distplot,'sepal_width').add_legend()
plt.show()


#Histogram and probability density function using KDF
#how to compute PDF using counts/frequencies of data points in each window.
#How  window width effects the PDF plot.

#Disadvantage of PDF
#can we say what percentage of versicolor points have a petal_length of less than 5?


#need of CDF :
    #we can visually see what percentage of versicolor flowers have a petal_length of less than 5?
    #How to construct a CDF?
    #How to read CDF?

    #plot CDF of petal_length

counts,bin_edges = np.histogram(iris_setosa['petal_length'],bins=10,density=True)

pdf=counts/(sum(counts))
print(pdf);
print(bin_edges)

cdf=np.cumsum(pdf)
plt.plot(bin_edges[1:],pdf)
plt.plot(bin_edges[1:],cdf)

#Virginica
counts,bin_edges=np.histogram(iris_virginica['petal_length'],bins=10,density=True)

pdf=counts/(sum(counts))
print(pdf);
print(bin_edges)

cdf=np.cumsum(pdf)
plt.plot(bin_edges[1:],pdf)
plt.plot(bin_edges[1:],cdf)

counts,bin_edges=np.histogram(iris_versicolor['petal_length'],bins=10,density=True)

pdf=counts/(sum(counts))
print(pdf);
print(bin_edges)

cdf=np.cumsum(pdf)
plt.plot(bin_edges[1:],pdf)
plt.plot(bin_edges[1:],cdf)

plt.show()

#Mean,Variance and Std-dev:-

print('means:')
print(np.mean(iris_setosa['petal_length']))

#mean with outlier.

print(np.mean(np.append(iris_setosa['petal_length'],50)))
print(np.mean(iris_virginica['petal_length']))
print(np.mean(iris_versicolor['petal_length']))


print('\nStd-dev:')

print(np.std(iris_setosa['petal_length']))
print(np.std(iris_virginica['petal_length']))
print(np.std(iris_versicolor['petal_length']))

#Median,Percentile,Quantile,IQR,MAD :-

print('\n','\n','\n')
print('Median :')

print(np.median(iris_setosa['petal_length']))
print(np.median(iris_virginica['petal_length']))
print(np.median(iris_versicolor['petal_length']))

print('\n','Quantiles:-')
print(np.percentile(iris_setosa['petal_length'],np.arange(0,100,25)))
print(np.percentile(iris_virginica['petal_length'],np.arange(0,100,25)))
print(np.percentile(iris_versicolor['petal_length'],np.arange(0,100,25)))

print('\n 90th percentile:-')

print(np.percentile(iris_setosa['petal_length'],90))
print(np.percentile(iris_virginica['petal_length'],90))
print(np.percentile(iris_versicolor['petal_length'],90))

#from statsmodels import robust
# print('\n Median Absolute Deviation')
# print(robust.mad(iris_setosa['petal_length']))
# print(robust.map(iris_virginica['petal_length']))
# print(robust.map(iris_versicolor['petal_length']))


#BOX PLOT AND WHISKERS:-
    #box plot with whiskers: another method of visualization the 1-D scatter plot more intuitively
    #The concept of median ,percentile , quantile .
    #How to draw the box in the box - plot?
    #How to draw whislers: [no standard way] could use min nd max or use other complex statistical techiques.
    #IQR like idea.

#NOTE : IN the plot below ,a technique call inter quantile range is used in plotting the whiskers.
       #Whiskers in the plot below dinot correspond to the min and max values.

       #Boz-plot can be visualized as a PDF on the side - ways.

sns.boxplot(x='species',y='petal_length',data=iris)
plt.show()


# VIOLIN PLOTS :-
    # A violin plot combines the benefits of the previous two plots and simplifies them
    # Denser regions of the data are fatter and sparser ones thinner in violin plot

sns.violinplot(x='species',y='petal_length',data=iris,size=8)
plt.show()



#UNIVARIATE ,BIVARIATE AND MULTIVARIATE ANALYSIS:-

    #multivariate probability density ,contour plot.

sns.jointplot(x='petal_length',y='petal_width',data='iris_setosa',kind='kde');
plt.show();


