```typescript
/* 迭代遍历数组 */
function traverse(arr: []): void {
    for (const i = 0; i < arr.length; i++) {
      // ...
    }
}

/* 递归遍历数组 */
function traverse(arr: [], i: number): void {
    if (i == arr.length) {
        return;
    }
    // 前序位置
    traverse(arr, i + 1);
    // 后序位置
}

/* 迭代遍历单链表 */
function traverse(head: ListNode): void {
    for (const p = head; p != null; p = p.next) {

    }
}

/* 递归遍历单链表 */
function traverse(head: ListNode): void {
    if (head == null) {
        return;
    }
    // 前序位置
    traverse(head.next);
    // 后序位置
}


/* 递归遍历二叉树 */
function traverse(root: TreeNode): void {
  if (root == null) return

  // 前序位置
  traverse(root.left);
  // 中序位置
  traverse(root.right);
  // 后序位置
}
```
