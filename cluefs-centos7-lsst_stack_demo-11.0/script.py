import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcol
import math
counter = 0
xData = []#read bandwidth slow
yData = []#read bandwidth fast
zData = []#executing time
for line in open("gettime.txt"):
	print line,
	counter=counter+1;
        if counter > 1:
	    if counter%2 == 0:
                  newline = line.rstrip('\n')
                  line_split = newline.split('_')
		  xData.append(int(line_split[1]))
		  yData.append(int(line_split[3]))
	    else:
		  zData.append(float(line.rstrip('\n')))
         
print xData
print yData
print zData
minima = min(yData)
maxima = max(yData)
#cm = plt.cm.get_cmap('RdYlBu')

#norm = mcol.Normalize(vmin=minima, vmax=maxima, clip=True)
#mapper = cm.ScalarMappable(norm=norm, cmap=cm.Greys)

#for v in yData:
 #   print(mapper.to_rgba(v))

# really simple grayscale answer
#algebra_list = [(x-minima)/(maxima-minima) for x in yData]
# let's compare the mapper and the algebra
#mapper_list = [mapper.to_rgba(x)[0] for x in yData]

plt.figure(num=1, figsize=(8, 6))
plt.title('Plot 1', size=14)
plt.xlabel('Read Bandwidth(slow)', size=14)
plt.ylabel('Executing time', size=14)
#plt.plot(yData, mapper_list, color='red', label='ScalarMappable')
#plt.plot(yData, algebra_list, color='blue', label='Algebra')

sc=plt.scatter(xData,zData,c=yData,vmin=minima,vmax=maxima,label="time",s=50,cmap=cm.Greys)
cbar=plt.colorbar(sc)
cbar.set_label('Read Bandwidth(fast)',size=14)
#plt.plot(xData, yData, color='b', linestyle='--', marker='o', label='Time')
#plt.legend(loc='upper left')
plt.savefig('images/plot1.png', format='png')
