from pylab import imshow, show, get_cmap
from numpy import random
import matplotlib.pyplot as plt
import pprint

colors_dic = {}
colors = ['Accent', 'Blues', 'BrBG', 'BuGn', 'BuPu', 'CMRmap',
'Dark2', 'GnBu', 'Greens', 'Greys', 'OrRd', 'Oranges',
'PRGn', 'Paired', 'Pastel1', 'Pastel2', 'PiYG',
'PuBu', 'PuBuGn', 'PuOr', 'PuRd', 'Purples', 'RdBu',
'RdGy', 'RdPu', 'RdYlBu', 'RdYlGn', 'Reds', 'Set1',
'Set2', 'Set3', 'Spectral', 'Wistia', 'YlGn', 'YlGnBu',
'YlOrBr', 'YlOrRd', 'afmhot', 'autumn', 'binary',
'bone', 'brg', 'bwr', 'cool', 'coolwarm', 'copper',
'cubehelix', 'flag', 'gist_earth', 'gist_gray', 'gist_heat',
'gist_ncar', 'gist_rainbow', 'gist_stern', 'gist_yarg',
'gnuplot', 'gnuplot2', 'gray', 'hot', 'hsv', 'inferno',
'jet', 'magma', 'nipy_spectral', 'ocean', 'pink',
'plasma', 'prism', 'rainbow', 'seismic', 'spring', 'summer',
'tab10', 'tab20', 'tab20b', 'tab20c', 'terrain',
'viridis', 'winter']
counter = 1
for i in colors:
    colors_dic[counter] = i
    counter += 1

print('********Pixel Canvas********')
print('Colors :')
for i in sorted(colors_dic):
    print(str(i) + ' --> ' + str(colors_dic[i]))

color = int(input('Pick a color : '))
x_dimension = input('Enter x dimension (Default = 10):')
y_dimension = input('Enter y dimension (Default = 10):')
save_file = input('Do you want to save the image? [Y/n] :')


if(x_dimension != '' and y_dimension !=  ''):
    Z = random.random((int(x_dimension),int(y_dimension)))
else:
    Z = random.random((10,10))
fig = plt.figure(frameon=False)
ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
fig.add_axes(ax)
if(save_file == 'Y' or save_file == 'y' or save_file == ''):
    file_format = input('Enter file format : ')
    path = input('Enter Path to save file : ')
    dpi = int(input('Enter dpi : '))
    imshow(Z, cmap=get_cmap(colors_dic[color]), interpolation='nearest')
    fig.savefig('{}.{}'.format(path,file_format), format='{}'.format(file_format), dpi=dpi)
    show()
else:
    imshow(Z, cmap=get_cmap(colors_dic[color]), interpolation='nearest')
    show()
