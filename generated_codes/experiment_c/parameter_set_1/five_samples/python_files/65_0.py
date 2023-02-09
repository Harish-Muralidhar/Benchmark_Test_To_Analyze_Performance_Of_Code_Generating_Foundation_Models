"""
"""
"""
Solution Outline:
	1. Sort the rectangles in descending order of area
	2. At each step, pick the rectangle with largest area,
	   intersect it with the rest.
	3. The intersection rectangle with the rectangle being dropped (if any) will be the same as the intersection rectangle with the rectangle being dropped,
	   and the remaining rectangles.
	4. Compute the area covered by the intersection rectangle at each step, return
	   the maximum among them.


Sample run:
	Rectangles:
		1: (2,2)
		2: (1,1)
		3: (5,5)
		4: (5,10)
		5: (10,10)
		M = 2
		
		Sort rectangles by area, in descending order
		5: (10,10)
		4: (5,10)
		3: (5,5)
		1: (2,2)
		2: (1,1)

		Pick the rectangle with largest area, and intersect it with the rest
		5: (10,10)
		5: (10,10) x (5,10) = (5,10)
		5: (10,10) x (5,5) = (5,5)
		5: (10,10) x (2,2) = (2,2)
		5: (10,10) x (1,1) = (1,1)
		Area covered = (5*10) + (5*5) + (2*2) + (1*1)

		Remove the rectangle at index 3
		4: (5,10)
		4: (5,10) x (5,5) = (5,5)
		4: (5,10) x (2,2) = (2,2)
		4: (5,10) x (1,1) = (1,1)
		Area covered = (5*5) + (2*2) + (1*1)

		Remove the rectangle at index 0
		3: (5,5)
		3: (5,5) x (2,2) = (2,2)
		3: (5,5) x (1,1) = (1,1)
		Area covered = (2*2) + (1*1)

		Remove the rectangle at index 1
		1: (2,2)
		1: (2,2) x (1,1) = (1,1)
		Area covered = (1*1)

		Remove the rectangle at index 2
		2: (1,1)
		Area covered = 0

		Return the maximum among all area covered: 100
		
"""

from collections import namedtuple

class Rectangle(object):
	def __init__(self, x, y):
		self.x, self.y = x, y
		self.area = x*y

	def __repr__(self):
		return "(%d, %d)" % (self.x, self.y)


def max_intersection_area(rectangles, m):
	if not rectangles:
		return 0

	# Sort the rectangles by area in descending order
	rectangles.sort(key=lambda r: r.area, reverse=True)
	max_area = 0

	for i in xrange(len(rectangles)):
		area = 0
		# Pick the rectangle with largest area
		# and intersect it with the rest
		for j in xrange(i+1, len(rectangles)):
			# Intersect rectangles[i] with rectangles[j]
			rx = min(rectangles[i].x, rectangles[j].x)
			ry = min(rectangles[i].y, rectangles[j].y)
			area += rx*ry
		
		max_area = max(max_area, area)

	return max_area


if __name__ == '__main__':
	rectangles = [Rectangle(10, 10), Rectangle(5, 10), Rectangle(5, 5), Rectangle(2,2), Rectangle(1,1)]
	assert max_intersection_area(rectangles, 2) == 100

	rectangles = [Rectangle(5, 5), Rectangle(5, 10), Rectangle(2,2), Rectangle(1,1)]
	assert max_intersection_area(rectangles, 2) == 25

	rectangles = [Rectangle(1, 1), Rectangle(2,2)]
	assert max_intersection_area(rectangles, 1) == 4