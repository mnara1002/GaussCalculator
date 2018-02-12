#coding:utf8
"""
ガウス少年の数式で計算する
n:1以上の正の数
"""

def gausscal(n):
    sum = 0 #答えを格納する変数sumを初期化する
    sum = ((n + 1) * n ) /2
    return sum #計算結果を返却する