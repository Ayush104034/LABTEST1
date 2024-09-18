import numpy as np


products= np.array([[120,500,230,75,45],[130,520,210,80,49],[125,530,220,70,50],[140,540,200,90,60]])
print (products)
totals(products)
totals2(products)


def totals(products):
    summ=0
    print("TOTAL SOLD ITEMS ACCROSS ALL WEEK:")
    for i in products:
        summ=summ+i[0]
    print("item 1",summ)
    sum2=np.sum(products[:,1])
    sum3=np.sum(products[:,2])
    sum4=np.sum(products[:,3])
    sum5=np.sum(products[:,4])
    
    print("item 2",sum2)
    print("item 3",sum3)
    print("item 4",sum4)
    print("item 5",sum5)

def totals2(products):
    i=1
    for j in products:
        summ2=np.sum(j)
        print("week",i)
        print (summ2)
        i=i+1
    print ("AVERAGE SALES PER PRODUCT:")
    avg1=np.mean(products[:,0])
    avg2=np.mean(products[:,1])
    avg3=np.mean(products[:,2])
    avg4=np.mean(products[:,3])
    avg5=np.mean(products[:,4])
    print("item 1",avg1)
    print("item 2",avg2)
    print("item 3",avg3)
    print("item 4",avg4)
    print("item 5",avg5)


import matplotlib.pyplot as plt
y=[1,2,3,4]
for i in range(0,5):
    x1=products[:,i]
    plt.plot(y,x1)
    
plt.xlabel('week')
plt.ylabel("item")
plt.show()


y=[1,2,3,4]
for i in range(0,4):
    x1=products[:,i]
    plt.bar(y,x1)
    

plt.show()

