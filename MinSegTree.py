class MinSegmentTree:
    def buildSegTree(self,arr,seg,idx,low,high):
        if low==high:
            seg[idx]=arr[low]
            return
        mid=(low+high)//2
        self.buildSegTree(arr,seg,2*idx+1,low,mid)
        self.buildSegTree(arr,seg,2*idx+2,mid+1,high)
        seg[idx]=min(seg[2*idx+1],seg[2*idx+2])

    def rangeQuery(self,seg,l,r,low,high,idx):
        if r<low or l>high:
            return float('inf')
        if low>=l and high<=r:
            return seg[idx]
        mid=(low+high)//2
        left = self.rangeQuery(seg,l,r,low,mid,2*idx+1)
        right = self.rangeQuery(seg,l,r,mid+1,high,2*idx+2)
        return min(left,right)

    def updateQuery(self,seg,low,high,idx,i,val):
        if low==high:
            seg[idx]=val
            return
        mid=(low+high)//2
        if i<=mid:
            self.updateQuery(seg,low,mid,2*idx+1,i,val)
        else:
            self.updateQuery(seg,mid+1,high,2*idx+2,i,val)
        seg[idx]=min(seg[2*idx+1],seg[2*idx+2])



n=int(input())
a=list(map(int,input().split()))

seg=[0]*(4*n)

tree = MinSegmentTree()
tree.buildSegTree(a,seg,0,0,n-1)

# Update Query
print("Update Query :")
i,val=map(int,input().split())
tree.updateQuery(seg,0,n-1,0,i,val)

# Minimum Range Query
print("Range Query :")
l,r=map(int,input().split())
print(tree.rangeQuery(seg,l,r,0,n-1,0))