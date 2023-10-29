class Graph:
	def __init__(self, number_of_verts):
			self.vertices = number_of_verts
			self.adj_list = [[] for _ in range(number_of_verts)]
			self.edges = 0

	def add_vertex(self):
			self.vertices += 1
			self.adj_list.append([])

	def add_edge(self, from_idx, to_idx, weight=1):
		if from_idx < 0 or from_idx >= self.vertices or to_idx < 0 or to_idx >= self.vertices:
			return False
			
		for edge in self.adj_list[from_idx]:
			if edge[0] == to_idx:
				return False
			
		self.adj_list[from_idx].append((to_idx, weight))
		self.edges += 1
		return True

	def num_edges(self):
		return self.edges

	def num_verts(self):
		return self.vertices

	def has_edge(self, from_idx, to_idx):
		if from_idx < 0 or from_idx >= self.vertices or to_idx < 0 or to_idx >= self.vertices:
			return False

		for edge in self.adj_list[from_idx]:
			if edge[0] == to_idx:
				return True
		return False

	def edge_weight(self, from_idx, to_idx):
		if from_idx < 0 or from_idx >= self.vertices or to_idx < 0 or to_idx >= self.vertices:
			return None

		for edge in self.adj_list[from_idx]:
			if edge[0] == to_idx:
				return edge[1]
		return None

	def get_connected(self, v):
		if v < 0 or v >= self.vertices:
			return []
		return self.adj_list[v]
	