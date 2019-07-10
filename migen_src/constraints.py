
# This class is to be used when any module set a constraints
# on the frame.
class Constraints():

	def __init__(self):

		self.height_min = ["Default", 1]
		self.width_min = ["Default", 1]
		self.bit_depth_min = ["Default", 2]

		self.height_max = ["Default", 65535]
		self.width_max = ["Default", 65535]
		self.bit_depth_max = ["Default", 16]

		self.height_multiple = ["Default", 1]
		self.width_multiple = ["Default", 1]


	def update_height(self, new_height, component):
		if new_height > self.height_min[1]:
			self.height_min[1] = new_height
			self.height_min[0] = component
		if new_height < self.height_max[1]:
			self.height_max[1] = new_height
			self.height_max[0] = component


	def update_width(self, new_width, component):
		if new_width > self.width_min[1]:
			self.width_min[1] = new_width
			self.width_min[0] = component
		if new_width < self.width_max[1]:
			self.width_max[1] = new_width
			self.width_max[0] = component


	def update_bit_depth(self, new_bit_depth, component):
		if new_bit_depth > self.bit_depth_min[1]:
			self.bit_depth_min[1] = new_bit_depth
			self.bit_depth_min[0] = component
		if new_bit_depth < self.bit_depth_max[1]:
			self.bit_depth_max[1] = new_bit_depth
			self.bit_depth_max[0] = component


	def update_height_multiple(self, new_multiple, component):
		if(new_multiple > self.height_multiple[1]):
			self.height_multiple[1] = new_multiple
			self.height_multiple[0] = component


	def update_width_multiple(self, new_multiple, component):
		if(new_multiple > self.width_multiple[1]):
			self.width_multiple[1] = new_multiple
			self.width_multiple[0] = component