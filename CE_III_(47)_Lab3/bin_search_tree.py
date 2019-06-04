class BST:
	def __init__(self):
		self._size = 0
		self._root = None #type bstnode

	class _BSTNode:
		def __init__(self, key, value):
			self.key = key
			self.value = value
			self.left = None
			self.right = None

	def add_node(self, key, value):
		z = self._BSTNode(key, value)
		y =None
		x = self._root
		while (x != None):
			y = x
			if (key < x.key):
				x = x.left
			else:
				x = x.right
		if (y == None):
			self._root = z
		elif (z.key < y.key):
			y.left = z
		else:
			y.right = z
		self._size += 1

	def is_empty(self):
		return self._size == 0

	def size(self):
		return self._size

	def inorder_traverse(self):
		nodes = []
		self._inorder_traverse(self._root, nodes)
		return nodes

	def _inorder_traverse(self, subtree, nodes):
		if(subtree):
			self._inorder_traverse(subtree.left, nodes)
			nodes.append(subtree.key)
			self._inorder_traverse(subtree.right, nodes)

	def preorder_traverse(self):
		nodes = []
		self._preorder_traverse(self._root, nodes)
		return nodes

	def _preorder_traverse(self, subtree, nodes):
		if(subtree):
			nodes.append(subtree.key)
			self._preorder_traverse(subtree.left, nodes)
			self._preorder_traverse(subtree.right, nodes)

	def postorder_traverse(self):
		nodes = []
		self._postorder_traverse(self._root, nodes)
		return nodes

	def _postorder_traverse(self, subtree, nodes):
		if(subtree):
			self._postorder_traverse(subtree.left, nodes)
			self._postorder_traverse(subtree.right, nodes)
			nodes.append(subtree.key)

	def search_for_node(self, key):
		found = []
		self._search_for_node(self._root, key, found)
		return found

	def _search_for_node(self, subtree, key, found):
		if(subtree):
			if(key == subtree.key):
				found.append(1)
			elif(key < subtree.key):
				self._search_for_node(subtree.left, key, found)
			elif(key > subtree.key):
				self._search_for_node(subtree.right, key, found)

	def search_smallest_key(self):
		nodes = []
		self._search_smallest_key(self._root, nodes)
		return nodes

	def _search_smallest_key(self, subtree, nodes):
		if(subtree):
			if(subtree.left == None):
				nodes.append(subtree.key)
			self._search_smallest_key(subtree.left, nodes)

	def _search_largest_key(self):
		nodes = []
		self.__search_largest_key(self._root, nodes)
		return nodes

	def __search_largest_key(self, subtree, nodes):
		if(subtree):
			if(subtree.right == None):
				nodes.append(subtree.key)
			self._search_largest_key(subtree.right, nodes)