#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 18:41:55 2020

@author: arthur
"""   
def knn():
    bd = [[0,250,36,"A"],
          [10,150,34,"B"],
          [2,90,10,"A"],
          [6,78,8,"B"],
          [4,20,1,"A"],
          [1,170,70,"B"],
          [8,160,41,"A"],
          [10,180,38,"B"],
          [6,200,45,""]]
    l = []
    k_max = len(bd)-1
    for i in range(k_max):
        d = 0
        for j in range(3):
            d += abs(bd[8][j] - bd[i][j])
        l.append(d)
        print(d)
    k = 1
    inf = 10000
    while k <= k_max:
        aux = l.copy()
        print("-------------------------------")
        print("K = ", k)
        print("NN's: ", end ="")
        pred = []
        for n in range(k):
            nearest = aux.index(min(aux))
            dist = aux.pop(nearest)
            aux.insert(nearest, inf)
            pred.append((bd[nearest][3], dist))
            print(nearest+1, end = " ")
        print(pred)
        counterA = 0
        counterB = 0
        resultado = None
        for classe in pred:
            if classe == "A":
                counterA += 1
            else: counterB += 1
        if counterA > counterB: resultado = "A"
        elif counterA < counterB: resultado = "B"
        else:
            soma_distA = 0
            soma_distB = 0
            for i in range(k):
                if pred[i][0] == "A": 
                    soma_distA += 1/pred[i][1]
                else:
                    soma_distB += 1/pred[i][1]
            if soma_distA > soma_distB: resultado = "A"
            else: resultado = "B" 
        print("Predição: ", resultado)
        k += 1
knn()
