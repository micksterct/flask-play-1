#
#
#  note: requires spark context
#
# see https://blog.sicara.com/get-started-pyspark-jupyter-guide-tutorial-ae2fe84f594f
#


import random
num_samples = 100000000
def inside(p):
  x, y = random.random(), random.random()
  return x*x + y*y < 1
count = sc.parallelize(range(0, num_samples)).filter(inside).count()
pi = 4 * count / num_samples
print(pi)
sc.stop()