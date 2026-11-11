Tree problems can be categorized into 2 ways broadly: 
1. Traversal
2. Problem Decomposition
 
 1. Traversal 
 We use DFS , BFS to do the traversal 
 With DFS we can go with Inorder , Preorder , Postorder
 With BFS we do Level order traversal 
 Note that BFS is Iterative while DFS is recursive 
 
 We can also do Inorder , Preorder , Postorder iteratively but that might not be a good way With traversals we have 3 positions - InOrder , PreOrder , PostOrder 
 Speciality of Post Order position is that we have data from both left subtree and right subtree
 Any question which needs data from both left and right subtree we go with post order traversal

 2.Problem Decomposition

 In Problem Decompostion approach we trust the definition of our function
 We assume it does the task (declarative) and we write the code
 Why problem decomposition feels non intuitive is that we are making recursive call to a function which is not even fully written 

 But on a high level , we assume the function gets the task done and call the function for left and right and we get the desired result
 We need to define the return value of the function correctly , clearly

 So problem decomposition involves post order position work as we assume that left and right have done the task and now we are doing the task for the current node
 And problem decomposition is of 3 types :
 1) Aggregation (integers)
 2) Inspector (Boolean)
 3) Tracker (Tuples/Objects)

 
 
 
 
 
 
 
 
 
 
 
 
 Parallels between DFS,Backtracking and Dp with Tree problems :
 Traversal approach is akin to backtracking , Problem Decomposition is akin to dynamic programming 

 DP, DFS, and backtracking can all be viewed as extensions of binary tree problems. The difference is what they focus on:

Dynamic programming uses a decomposition (divide-and-conquer) approach, focusing on entire "subtrees."
Backtracking uses a traversal approach, focusing on the "edges" between nodes.
DFS uses a traversal approach, focusing on individual "nodes."
 
