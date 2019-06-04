import unittest
from bin_search_tree import BST

class BSTTestcase(unittest.TestCase):
        
        def test_bstTest(self):
            bst = BST()

            bst.add_node(7,"Seven")
            self.assertEqual(bst.size(),1)

            bst.add_node(47,"47 ronin")
            self.assertEqual(bst.size(),2)

            bst.add_node(15,"ok")
            self.assertEqual(bst.size(),3)

            bst.add_node(39,"Good")
            self.assertEqual(bst.size(),4)

            self.assertListEqual(bst.inorder_traverse(),[7,15,39,47])

            self.assertListEqual(bst.preorder_traverse(),[7,47,15,39])

            self.assertListEqual(bst.postorder_traverse(),[39,15,47,7])



if __name__ == "__main__":
    unittest.main()