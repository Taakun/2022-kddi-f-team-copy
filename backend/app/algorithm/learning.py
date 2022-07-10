import matplotlib.pyplot as plt
import pandas as pd
import random

# いいね率を更新するプログラム
# q[0]がquestion1の答え(0ならスポドリ,1なら紅茶), q[1]がquestion2の答え(0ならきのこ,1ならたけのこ) 
# ansはYes or No
def update(q,ans,y,n):
    S=''.join(map(str, q))
    t=int(S,2)
    if ans=="No":
        n[t]+=1
    else:
        y[t]+=1
    return y,n

# いいね率が１番低いものを入れ替えるプログラム
def change(place,sub,y,n):
    min_p=1.0 # いいね率
    min_cnt=0 # いいね率が低い場所
    for i in range(len(place)):
        if place[i][1]<min_p:
            min_p=place[i][1]
            min_cnt=i
    if min_p!=1.0:
        y[min_cnt],n[min_cnt]=1,0
        X=place[min_cnt]
        place[min_cnt]=[sub.pop(0),y[min_cnt]/(y[min_cnt]+n[min_cnt])]
        sub.append(X[0])
    
    return place,sub,y,n

def place_point(place,y,n):
    pl=[]
    for i in range(len(place)):
        pl.append([place[i],y[i]/(n[i]+y[i])])
    return pl

# これを呼び出す
def natu(q,ans,y,n,place,sub):
    A=list(update(q,"No",y,n)) # 更新
    y=A[0]
    n=A[1]
    
    place_p=place_point(place,y,n) # 点数化
    
    if random.randint(1,3)==1: # 1/3の確率で交換する
        place_p=list(change(place_p,sub,y,n))[0]
        sub=list(change(place_p,sub,y,n))[1]
        y=list(change(place_p,sub,y,n))[2]
        n=list(change(place_p,sub,y,n))[3]
        place=[]
        for i in range(len(place_p)):
            place.append(place_p[i][0])
    
    return y,n,place,sub

# natsuのテスト
def test:
  # 質問が3パターンの時
  # 初期条件
  y=[1 for _ in range(8)]
  n=[0 for _ in range(8)]
  place=[["山登り"],["BBQ"],["花火"],["川遊び"],["海"],["キャンプ"],["水族館"],["映画館"]]
  sub=["釣り","ボーリング"]
  print(place)

  # 質問結果
  q=[0,0,1]
  ans="No"
  # 更新
  X=list(natu(q,ans,y,n,place,sub))
  y=X[0]
  n=X[1]
  place=X[2]
  sub=X[3]
  print(place_point(place,y,n))

  # 質問結果
  q=[0,0,1]
  ans="No"
  # 更新
  X=list(natu(q,ans,y,n,place,sub))
  y=X[0]
  n=X[1]
  place=X[2]
  sub=X[3]
  print(place_point(place,y,n))

  # 質問結果
  q=[0,0,1]
  ans="No"
  # 更新
  X=list(natu(q,ans,y,n,place,sub))
  y=X[0]
  n=X[1]
  place=X[2]
  sub=X[3]
  print(place_point(place,y,n))
