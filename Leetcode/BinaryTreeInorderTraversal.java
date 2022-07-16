/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        class Helper{
            public void preorderHelper(TreeNode helperRoot){
                if (helperRoot != null){
                    answer.add(helperRoot.val);
                    this.preorderHelper(helperRoot.left);
                    this.preorderHelper(helperRoot.right);
                }
            }
        }
        
        new Helper().preorderHelper(root);
        return answer;
    }
}
