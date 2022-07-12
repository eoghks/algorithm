import loadfile as ld
import dynamic as dy
import tree as tr
import backtracking as bt
import brand_and_bound as bb
#필요한 정보 upload
w,S,p,weight=ld.load()
#dyanmic apporach
dynamic_result, dyanmic_count=dy.knapsack(S,w,p,weight)
print("dynamic_result: ",dynamic_result,"  number of primitive operations: ", dyanmic_count)

#make tree
root=tr.mktree(weight,S,p,w)
#backtrking apporach
best=0
count=0
backtracking_reuslt, backtracking_count=bt.checknode(root, best, count,w)
print("backtracking_reuslt: ",backtracking_reuslt,"  number of primitive operations: ", backtracking_count)

#branch-and-bound apporach
best=0
count=0
branch_and_bound_result, branch_and_bound_count=bb.tree_bfs_brand_and_bound(root, best, count,w)
print("branch-and-bound apporach_reuslt: ",branch_and_bound_result,"  number of primitive operations: ", branch_and_bound_count)


