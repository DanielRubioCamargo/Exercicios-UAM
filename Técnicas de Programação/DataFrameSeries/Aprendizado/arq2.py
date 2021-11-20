import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [5,3,7,1]

plt.pie(x,y,label = "Linha",ls = "dashed",color = "g") # marker = "..."
plt.title("Valores")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
#plt.xticks([1,2,3,4,5,6,7,8])
#plt.yticks([1,2,3,4,5,6,7,8])
plt.axis(xmin = 1,xmax = 4,ymin = 0,ymax = 7) # auto, square
plt.legend()
plt.show()