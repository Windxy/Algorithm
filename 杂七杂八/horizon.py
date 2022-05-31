# ACIoU = Area + 长宽 + 对角线距离 + IoU
import math
# IoU
def IoU_cal(box1,box2):
    # b1 [x1,y1,w1,h1] b2[]
    box1 = [box1[0]-box1[2]//2,box1[1]-box1[3]//2,box1[0]+box1[2]//2,box1[1]+box1[3]//2]    # [x1,y1,x2,y2]
    box2 = [box2[0]-box2[2]//2,box2[1]-box2[3]//2,box2[0]+box2[2]//2,box2[1]+box2[3]//2]
    # 交集+并集
    s1 = (abs(max(box1[2],box2[0]) - min(box1[0],box2[2]))) * (abs(min(box1[1],box2[3])-max(box1[3],box2[1])))
    s2 = (box1[2]-box1[0])*(box1[3]-box1[1]) + (box2[3]-box2[1])*(box2[2]-box1[0]) - s1
    return s1*1.0 / (s2+1e-5)

# Area
def IoU_area(box1,box2):
    box1 = [box1[0]-box1[2]//2,box1[1]-box1[3]//2,box1[0]+box1[2]//2,box1[1]+box1[3]//2]    # [x1,y1,x2,y2]
    box2 = [box2[0]-box2[2]//2,box2[1]-box2[3]//2,box2[0]+box2[2]//2,box2[1]+box2[3]//2]
    s1 = (box1[2]-box1[0])*(box1[3]-box1[1])
    s2 = (box2[3]-box2[1])*(box2[2]-box1[0])
    return min(s1,s2)*1.0/(1e-5+max(s1,s2))

# 长宽
def IoU_ck(box1,box2):
    # b1 [x1,y1,w1,h1] b2[]
    return box1[3] * 1.0 / (box2[3]+1e-5) + box1[2] * 1.0 / (box2[2]+1e-5)

# 对角线
def IoU_djx(box1,box2):
    # b1 [x1,y1,w1,h1] b2[]
    box1 = [box1[0]-box1[2]//2,box1[1]-box1[3]//2,box1[0]+box1[2]//2,box1[1]+box1[3]//2]    # [x1,y1,x2,y2]
    box2 = [box2[0]-box2[2]//2,box2[1]-box2[3]//2,box2[0]+box2[2]//2,box2[1]+box2[3]//2]
    center1 = [(box1[2]+box1[0])/2,(box1[3]+box1[1])/2]
    center2 = [(box2[2]+box1[0])/2,(box2[3]+box2[1])/2]
    distance1 = math.sqrt((center1[0]-center2[0])*(center1[0]-center2[0]) + (center1[1]-center2[1])*(center1[1]-center2[1]))
    tmp_w = max(box1[2],box2[2])-min(box1[0],box2[0])
    tmp_h = max(box1[3],box2[3])-min(box1[1],box2[1])
    distance2 = math.sqrt(tmp_w*tmp_w+tmp_h*tmp_h)
    return distance1 * 1.0 / (distance2 + 1e-5)

box1 = []
box2 = []
a,b,c,d = 0.1,0.1,0.1,0.1
print(a*IoU_ck(box1,box2)+IoU_area(box1,box2)+IoU_cal(box1,box2)+IoU_djx(box1,box2))

# yi = e**(xi) / Σj(e**(xj))  softmax

import numpy as np

arr = np.array([0.3,0.3,0.2,0.1])
y0 = np.exp(arr[0]) / np.sum([np.exp(arr[i]) for i in range(len(arr))])
