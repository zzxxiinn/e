## 二叉树
二叉树这种结构无非就是二叉链表。

### 遍历思想

1. 前序遍历: root -> left -> right
2. 中序遍历: root -> left -> right
3. 后序遍历: root -> left -> right
4. 层次遍历: 按层次遍历二叉树

```typescript
interface TreeNode {
  val?: string|number
  left?: TreeNode | null
  right?: TreeNode | null
}

function traverse(root: TreeNode): void {
  if (root == null) return

  // 前序位置
  traverse(root.left);
  // 中序位置
  traverse(root.right);
  // 后序位置
}
```
