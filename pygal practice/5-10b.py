from random_walk import RandomWalk
import pygal

#make a random walk and plot points
rw = RandomWalk()
rw.fill_walk()

#visualize the results
hist = pygal.Bar()

hist.title = "Results of a random walk"
hist.x_labels = rw.x_values
hist.x_title = "x values"
hist.y_title = 'y values'

hist.add('x and y random walk', rw.y_values)
hist.render_to_file('rw.svg')
