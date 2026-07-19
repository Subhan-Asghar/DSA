from collections import deque
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        # r=fx+1
        # c=fy+1
        # grid=[[0]*c for _ in range(r)]
        # directions=[(1,0),(0,1),(1,1),(-1,-1),(1,-1),(-1,1),(-1,0),(0,-1)]
        # q=deque([(0,sx,sy)])
        # visited=set()
        # while q:
        #     time,qr,qc=q.popleft()
        #     if time>t:
        #         return False
        #     if time ==t and qr==fx and qc==fy:
        #         return True
        #     for dr,dc in directions:
        #         nr=qr+dr
        #         nc=qc+dc
        #         if 1<=nr<r and 1<=nc<c and time<t:
        #             q.append((1+time,nr,nc))
        # return False
        if (sx,sy)==(fx,fy) and t==1:
            return False
        max_val=max(abs(sx-fx),abs(fy-sy))
        if max_val<=t:
            return True
        return False