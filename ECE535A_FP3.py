import random
import math
from numpy import random
import matplotlib.pyplot as plt

def viterbi(inputBit):
    graph = {"S0_0": [["S0_1", [1,1], "0", 0, ["0", "S0_0"]], ["S1_1", [1,-1], "1", 0, ["1", "S0_0"]]],#0
             "S0_1": [["S0_2", [1,1], "0", 0, ["0", "S0_1"]], ["S1_2", [1,-1], "1", 0, ["1", "S0_1"]]],
             "S1_1": [["S2_2", [-1,-1], "0", 0, ["0", "S1_1"]], ["S3_2", [-1,1], "1", 0, ["1", "S1_1"]]],#1
             "S0_2": [["S0_3", [1,1], "0", 0, ["0", "S0_2"]], ["S1_3", [1,-1], "1", 0, ["1", "S0_2"]]],
             "S1_2": [["S2_3", [-1,-1], "0", 0, ["0", "S1_2"]], ["S3_3", [-1,1], "1", 0, ["1", "S1_2"]]],
             "S2_2": [["S4_3", [-1,-1], "0", 0, ["0", "S2_2"]], ["S5_3", [-1,1], "1", 0, ["1", "S2_2"]]],
             "S3_2": [["S6_3", [1,1], "0", 0, ["0", "S3_2"]], ["S7_3", [1,-1], "1", 0, ["1", "S3_2"]]],#2
             "S0_3": [["S0_4", [1,1], "0", 0, []], ["S1_4", [1,-1], "1", 0, []]],
             "S1_3": [["S2_4", [-1,-1], "0", 0, []], ["S3_4", [-1,1], "1", 0, []]],
             "S2_3": [["S4_4", [-1,-1], "0", 0, []], ["S5_4", [-1,1], "1", 0, []]],
             "S3_3": [["S6_4", [1,1], "0", 0, []], ["S7_4", [1,-1], "1", 0, []]],
             "S4_3": [["S0_4", [-1,1], "0", 0, []], ["S1_4", [-1,-1], "1", 0, []]],
             "S5_3": [["S2_4", [1,-1], "0", 0, []], ["S3_4", [1,1], "1", 0, []]],
             "S6_3": [["S4_4", [1,-1], "0", 0, []], ["S5_4", [1,1], "1", 0, []]],
             "S7_3": [["S6_4", [-1,1], "0", 0, []], ["S7_4", [-1,-1], "1", 0, []]],#3
             "S0_4": [["S0_5", [1,1], "0", 0, []], ["S1_5", [1,-1], "1", 0, []]],
             "S1_4": [["S2_5", [-1,-1], "0", 0, []], ["S3_5", [-1,1], "1", 0, []]],
             "S2_4": [["S4_5", [-1,-1], "0", 0, []], ["S5_5", [-1,1], "1", 0, []]],
             "S3_4": [["S6_5", [1,1], "0", 0, []], ["S7_5", [1,-1], "1", 0, []]],
             "S4_4": [["S0_5", [-1,1], "0", 0, []], ["S1_5", [-1,-1], "1", 0, []]],
             "S5_4": [["S2_5", [1,-1], "0", 0, []], ["S3_5", [1,1], "1", 0, []]],
             "S6_4": [["S4_5", [1,-1], "0", 0, []], ["S5_5", [1,1], "1", 0, []]],
             "S7_4": [["S6_5", [-1,1], "0", 0, []], ["S7_5", [-1,-1], "1", 0, []]],#4
             "S0_5": [["S0_6", [1,1], "0", 0, []], ["S1_6", [1,-1], "1", 0, []]],
             "S1_5": [["S2_6", [-1,-1], "0", 0, []], ["S3_6", [-1,1], "1", 0, []]],
             "S2_5": [["S4_6", [-1,-1], "0", 0, []], ["S5_6", [-1,1], "1", 0, []]],
             "S3_5": [["S6_6", [1,1], "0", 0, []], ["S7_6", [1,-1], "1", 0, []]],
             "S4_5": [["S0_6", [-1,1], "0", 0, []], ["S1_6", [-1,-1], "1", 0, []]],
             "S5_5": [["S2_6", [1,-1], "0", 0, []], ["S3_6", [1,1], "1", 0, []]],
             "S6_5": [["S4_6", [1,-1], "0", 0, []], ["S5_6", [1,1], "1", 0, []]],
             "S7_5": [["S6_6", [-1,1], "0", 0, []], ["S7_6", [-1,-1], "1", 0, []]],#5
             "S0_6": [["S0_7", [1,1], "0", 0, []], ["S1_7", [1,-1], "1", 0, []]],
             "S1_6": [["S2_7", [-1,-1], "0", 0, []], ["S3_7", [-1,1], "1", 0, []]],
             "S2_6": [["S4_7", [-1,-1], "0", 0, []], ["S5_7", [-1,1], "1", 0, []]],
             "S3_6": [["S6_7", [1,1], "0", 0, []], ["S7_7", [1,-1], "1", 0, []]],
             "S4_6": [["S0_7", [-1,1], "0", 0, []], ["S1_7", [-1,-1], "1", 0, []]],
             "S5_6": [["S2_7", [1,-1], "0", 0, []], ["S3_7", [1,1], "1", 0, []]],
             "S6_6": [["S4_7", [1,-1], "0", 0, []], ["S5_7", [1,1], "1", 0, []]],
             "S7_6": [["S6_7", [-1,1], "0", 0, []], ["S7_7", [-1,-1], "1", 0, []]],#6
             "S0_7": [["S0_8", [1,1], "0", 0, []], ["S1_8", [1,-1], "1", 0, []]],
             "S1_7": [["S2_8", [-1,-1], "0", 0, []], ["S3_8", [-1,1], "1", 0, []]],
             "S2_7": [["S4_8", [-1,-1], "0", 0, []], ["S5_8", [-1,1], "1", 0, []]],
             "S3_7": [["S6_8", [1,1], "0", 0, []], ["S7_8", [1,-1], "1", 0, []]],
             "S4_7": [["S0_8", [-1,1], "0", 0, []], ["S1_8", [-1,-1], "1", 0, []]],
             "S5_7": [["S2_8", [1,-1], "0", 0, []], ["S3_8", [1,1], "1", 0, []]],
             "S6_7": [["S4_8", [1,-1], "0", 0, []], ["S5_8", [1,1], "1", 0, []]],
             "S7_7": [["S6_8", [-1,1], "0", 0, []], ["S7_8", [-1,-1], "1", 0, []]],#7
             "S0_8": [["S0_9", [1,1], "0", 0, []], ["S1_9", [1,-1], "1", 0, []]],
             "S1_8": [["S2_9", [-1,-1], "0", 0, []], ["S3_9", [-1,1], "1", 0, []]],
             "S2_8": [["S4_9", [-1,-1], "0", 0, []], ["S5_9", [-1,1], "1", 0, []]],
             "S3_8": [["S6_9", [1,1], "0", 0, []], ["S7_9", [1,-1], "1", 0, []]],
             "S4_8": [["S0_9", [-1,1], "0", 0, []], ["S1_9", [-1,-1], "1", 0, []]],
             "S5_8": [["S2_9", [1,-1], "0", 0, []], ["S3_9", [1,1], "1", 0, []]],
             "S6_8": [["S4_9", [1,-1], "0", 0, []], ["S5_9", [1,1], "1", 0, []]],
             "S7_8": [["S6_9", [-1,1], "0", 0, []], ["S7_9", [-1,-1], "1", 0, []]],#8
             "S0_9": [["S0_10", [1,1], "0", 0, []], ["S1_10", [1,-1], "1", 0, []]],
             "S1_9": [["S2_10", [-1,-1], "0", 0, []], ["S3_10", [-1,1], "1", 0, []]],
             "S2_9": [["S4_10", [-1,-1], "0", 0, []], ["S5_10", [-1,1], "1", 0, []]],
             "S3_9": [["S6_10", [1,1], "0", 0, []], ["S7_10", [1,-1], "1", 0, []]],
             "S4_9": [["S0_10", [-1,1], "0", 0, []], ["S1_10", [-1,-1], "1", 0, []]],
             "S5_9": [["S2_10", [1,-1], "0", 0, []], ["S3_10", [1,1], "1", 0, []]],
             "S6_9": [["S4_10", [1,-1], "0", 0, []], ["S5_10", [1,1], "1", 0, []]],
             "S7_9": [["S6_10", [-1,1], "0", 0, []], ["S7_10", [-1,-1], "1", 0, []]],#9
             }


    FSMOut = []
    keyList = []
    itemList = []
    nodePath = ["S0_0"]
    for key in graph:
        keyList.append(key)
    for item in graph.values():
        itemList.append(item)
    #print("graph items: ", end = "")
    #print(itemList)
    if inputBit[0] == "1":    # 0
        FSMOut.append([1,1])
        nodePath.append("S0_1")
        #print(nodePath)
    if inputBit[0] == "2":    # 1
        FSMOut.append([-1,-1])
        nodePath.append("S1_1")
        #print(nodePath)
    for i in range(1, len(inputBit), 1):
        if inputBit[i] == "1": # 0
            tempItem = graph[nodePath[-1]]
            #print(tempItem)
            FSMOut.append(tempItem[0][1])
            nodePath.append(tempItem[0][0])
        if inputBit[i] == "2": # 1
            tempItem = graph[nodePath[-1]]
            #print(tempItem)
            FSMOut.append(tempItem[1][1])
            nodePath.append(tempItem[1][0])

    FSMOutMap = []
    for i in range(0, len(FSMOut), 1):
        FSMOutMap.append(FSMOut[i][0])
        FSMOutMap.append(FSMOut[i][1])

    #print(nodePath)
    #print(FSMOut)
    #print(FSMOutMap)

    """
    noise = []
    for i in range(0, len(FSMOut), 1):
        noise.append(random.randint(-10, 10) / 10)
    #print("generate random noise: ", end = '')
    #print(noise)
    """

    noise = random.normal(loc=0, scale=0.7, size=(1, 20))
    #print(noise)

    noiseOut = []
    for i in range(0, len(FSMOutMap), 1):
        noiseOut.append(FSMOutMap[i] + noise[0][i])
    #print("FSM output added with noise: ", end = '')
    #print(noiseOut)
    """
    list1 = []
    list2 = []
    for i in range(0, len(noiseOut), 1):
        list1.append(noiseOut[i])
        list2.append(noiseOut[i])
    print(list1)
    print(list2)

    distU = 0
    distU1 = 0
    distU2 = 0

    distL = 0
    distL1 = 0
    distL2 = 0
    """


    graph["S0_0"][0][3] = (int(graph["S0_0"][0][1][0])-noiseOut[0])**2 + (int(graph["S0_0"][0][1][1])-noiseOut[1])**2
    graph["S0_0"][1][3] = (int(graph["S0_0"][1][1][0])-noiseOut[0])**2 + (int(graph["S0_0"][1][1][1])-noiseOut[1])**2 #0


    graph["S0_1"][0][3] = (int(graph["S0_1"][0][1][0])-noiseOut[2])**2 + (int(graph["S0_1"][0][1][1])-noiseOut[3])**2 + graph["S0_0"][0][3]
    graph["S0_1"][1][3] = (int(graph["S0_1"][1][1][0])-noiseOut[2])**2 + (int(graph["S0_1"][1][1][1])-noiseOut[3])**2 + graph["S0_0"][0][3]
    graph["S1_1"][0][3] = (int(graph["S1_1"][0][1][0])-noiseOut[2])**2 + (int(graph["S1_1"][0][1][1])-noiseOut[3])**2 + graph["S0_0"][1][3]
    graph["S1_1"][1][3] = (int(graph["S1_1"][1][1][0])-noiseOut[2])**2 + (int(graph["S1_1"][1][1][1])-noiseOut[3])**2 + graph["S0_0"][1][3]#1

    graph["S0_2"][0][3] = (int(graph["S0_2"][0][1][0])-noiseOut[4])**2 + (int(graph["S0_2"][0][1][1])-noiseOut[5])**2 + graph["S0_1"][0][3]
    graph["S0_2"][1][3] = (int(graph["S0_2"][1][1][0])-noiseOut[4])**2 + (int(graph["S0_2"][1][1][1])-noiseOut[5])**2 + graph["S0_1"][0][3]
    graph["S1_2"][0][3] = (int(graph["S1_2"][0][1][0])-noiseOut[4])**2 + (int(graph["S1_2"][0][1][1])-noiseOut[5])**2 + graph["S0_1"][1][3]
    graph["S1_2"][1][3] = (int(graph["S1_2"][1][1][0])-noiseOut[4])**2 + (int(graph["S1_2"][1][1][1])-noiseOut[5])**2 + graph["S0_1"][1][3]
    graph["S2_2"][0][3] = (int(graph["S2_2"][0][1][0])-noiseOut[4])**2 + (int(graph["S2_2"][0][1][1])-noiseOut[5])**2 + graph["S1_1"][0][3]
    graph["S2_2"][1][3] = (int(graph["S2_2"][1][1][0])-noiseOut[4])**2 + (int(graph["S2_2"][1][1][1])-noiseOut[5])**2 + graph["S1_1"][0][3]
    graph["S3_2"][0][3] = (int(graph["S3_2"][0][1][0])-noiseOut[4])**2 + (int(graph["S3_2"][0][1][1])-noiseOut[5])**2 + graph["S1_1"][1][3]
    graph["S3_2"][1][3] = (int(graph["S3_2"][1][1][0])-noiseOut[4])**2 + (int(graph["S3_2"][1][1][1])-noiseOut[5])**2 + graph["S1_1"][1][3]#2

    graph["S0_3"][0][3] = (int(graph["S0_3"][0][1][0])-noiseOut[6])**2 + (int(graph["S0_3"][0][1][1])-noiseOut[7])**2
    graph["S0_3"][1][3] = (int(graph["S0_3"][1][1][0])-noiseOut[6])**2 + (int(graph["S0_3"][1][1][1])-noiseOut[7])**2
    s0_1_3 = graph["S0_3"][0][3] + graph["S0_2"][0][3]
    s1_1_3 = graph["S0_3"][1][3] + graph["S0_2"][0][3]
    graph["S1_3"][0][3] = (int(graph["S1_3"][0][1][0])-noiseOut[6])**2 + (int(graph["S1_3"][0][1][1])-noiseOut[7])**2
    graph["S1_3"][1][3] = (int(graph["S1_3"][1][1][0])-noiseOut[6])**2 + (int(graph["S1_3"][1][1][1])-noiseOut[7])**2
    s2_1_3 = graph["S1_3"][0][3] + graph["S0_2"][1][3]
    s3_1_3 = graph["S1_3"][1][3] + graph["S0_2"][1][3]
    graph["S2_3"][0][3] = (int(graph["S2_3"][0][1][0])-noiseOut[6])**2 + (int(graph["S2_3"][0][1][1])-noiseOut[7])**2
    graph["S2_3"][1][3] = (int(graph["S2_3"][1][1][0])-noiseOut[6])**2 + (int(graph["S2_3"][1][1][1])-noiseOut[7])**2
    s4_1_3 = graph["S2_3"][0][3] + graph["S1_2"][0][3]
    s5_1_3 = graph["S2_3"][1][3] + graph["S1_2"][0][3]
    graph["S3_3"][0][3] = (int(graph["S3_3"][0][1][0])-noiseOut[6])**2 + (int(graph["S3_3"][0][1][1])-noiseOut[7])**2
    graph["S3_3"][1][3] = (int(graph["S3_3"][1][1][0])-noiseOut[6])**2 + (int(graph["S3_3"][1][1][1])-noiseOut[7])**2
    s6_1_3 = graph["S3_3"][0][3] + graph["S1_2"][1][3]
    s7_1_3 = graph["S3_3"][1][3] + graph["S1_2"][1][3]
    graph["S4_3"][0][3] = (int(graph["S4_3"][0][1][0])-noiseOut[6])**2 + (int(graph["S4_3"][0][1][1])-noiseOut[7])**2
    graph["S4_3"][1][3] = (int(graph["S4_3"][1][1][0])-noiseOut[6])**2 + (int(graph["S4_3"][1][1][1])-noiseOut[7])**2
    s0_2_3 = graph["S4_3"][0][3] + graph["S2_2"][0][3]
    s1_2_3 = graph["S4_3"][1][3] + graph["S2_2"][0][3]
    graph["S5_3"][0][3] = (int(graph["S5_3"][0][1][0])-noiseOut[6])**2 + (int(graph["S5_3"][0][1][1])-noiseOut[7])**2
    graph["S5_3"][1][3] = (int(graph["S5_3"][1][1][0])-noiseOut[6])**2 + (int(graph["S5_3"][1][1][1])-noiseOut[7])**2
    s2_2_3 = graph["S5_3"][0][3] + graph["S2_2"][1][3]
    s3_2_3 = graph["S5_3"][1][3] + graph["S2_2"][1][3]
    graph["S6_3"][0][3] = (int(graph["S6_3"][0][1][0])-noiseOut[6])**2 + (int(graph["S6_3"][0][1][1])-noiseOut[7])**2
    graph["S6_3"][1][3] = (int(graph["S6_3"][1][1][0])-noiseOut[6])**2 + (int(graph["S6_3"][1][1][1])-noiseOut[7])**2
    s4_2_3 = graph["S6_3"][0][3] + graph["S3_2"][0][3]
    s5_2_3 = graph["S6_3"][1][3] + graph["S3_2"][0][3]
    graph["S7_3"][0][3] = (int(graph["S7_3"][0][1][0])-noiseOut[6])**2 + (int(graph["S7_3"][0][1][1])-noiseOut[7])**2
    graph["S7_3"][1][3] = (int(graph["S7_3"][1][1][0])-noiseOut[6])**2 + (int(graph["S7_3"][1][1][1])-noiseOut[7])**2 #3
    s6_2_3 = graph["S7_3"][0][3] + graph["S3_2"][1][3]
    s7_2_3 = graph["S7_3"][1][3] + graph["S3_2"][1][3]
    if s0_1_3 <= s0_2_3:
        graph["S0_3"][0][3] = s0_1_3
        graph["S0_3"][0][4] = ["0", "S0_3"]
    else:
        graph["S0_3"][0][3] = s0_2_3
        graph["S0_3"][0][4] = ["0", "S4_3"]

    if s1_1_3 <= s1_2_3:
        graph["S0_3"][1][3] = s1_1_3
        graph["S0_3"][1][4] = ["1", "S0_3"]
    else:
        graph["S0_3"][1][3] = s1_2_3
        graph["S0_3"][1][4] = ["1", "S4_3"]

    if s2_1_3 <= s2_2_3:
        graph["S1_3"][0][3] = s2_1_3
        graph["S1_3"][0][4] = ["0", "S1_3"]
    else:
        graph["S1_3"][0][3] = s2_2_3
        graph["S1_3"][0][4] = ["0", "S5_3"]

    if s3_1_3 <= s3_2_3:
        graph["S1_3"][1][3] = s3_1_3
        graph["S1_3"][1][4] = ["1", "S1_3"]
    else:
        graph["S1_3"][1][3] = s3_2_3
        graph["S1_3"][1][4] = ["1", "S5_3"]

    if s4_1_3 <= s4_2_3:
        graph["S2_3"][0][3] = s4_1_3
        graph["S2_3"][0][4] = ["0", "S2_3"]
    else:
        graph["S2_3"][0][3] = s4_2_3
        graph["S2_3"][0][4] = ["0", "S6_3"]

    if s5_1_3 <= s5_2_3:
        graph["S2_3"][1][3] = s5_1_3
        graph["S2_3"][1][4] = ["1", "S2_3"]
    else:
        graph["S2_3"][1][3] = s5_2_3
        graph["S2_3"][1][4] = ["1", "S6_3"]

    if s6_1_3 <= s6_2_3:
        graph["S3_3"][0][3] = s6_1_3
        graph["S3_3"][0][4] = ["0", "S3_3"]
    else:
        graph["S3_3"][0][3] = s6_2_3
        graph["S3_3"][0][4] = ["0", "S7_3"]

    if s7_1_3 <= s7_2_3:
        graph["S3_3"][1][3] = s7_1_3
        graph["S3_3"][1][4] = ["1", "S3_3"]
    else:
        graph["S3_3"][1][3] = s7_2_3
        graph["S3_3"][1][4] = ["1", "S7_3"]

    graph["S0_4"][0][3] = (int(graph["S0_4"][0][1][0])-noiseOut[8])**2 + (int(graph["S0_4"][0][1][1])-noiseOut[9])**2
    graph["S0_4"][1][3] = (int(graph["S0_4"][1][1][0])-noiseOut[8])**2 + (int(graph["S0_4"][1][1][1])-noiseOut[9])**2
    s0_1_4 = graph["S0_4"][0][3] + graph["S0_3"][0][3]
    s1_1_4 = graph["S0_4"][1][3] + graph["S0_3"][0][3]
    graph["S1_4"][0][3] = (int(graph["S1_4"][0][1][0])-noiseOut[8])**2 + (int(graph["S1_4"][0][1][1])-noiseOut[9])**2
    graph["S1_4"][1][3] = (int(graph["S1_4"][1][1][0])-noiseOut[8])**2 + (int(graph["S1_4"][1][1][1])-noiseOut[9])**2
    s2_1_4 = graph["S1_4"][0][3] + graph["S0_3"][1][3]
    s3_1_4 = graph["S1_4"][1][3] + graph["S0_3"][1][3]
    graph["S2_4"][0][3] = (int(graph["S2_4"][0][1][0])-noiseOut[8])**2 + (int(graph["S2_4"][0][1][1])-noiseOut[9])**2
    graph["S2_4"][1][3] = (int(graph["S2_4"][1][1][0])-noiseOut[8])**2 + (int(graph["S2_4"][1][1][1])-noiseOut[9])**2
    s4_1_4 = graph["S2_4"][0][3] + graph["S1_3"][0][3]
    s5_1_4 = graph["S2_4"][1][3] + graph["S1_3"][0][3]
    graph["S3_4"][0][3] = (int(graph["S3_4"][0][1][0])-noiseOut[8])**2 + (int(graph["S3_4"][0][1][1])-noiseOut[9])**2
    graph["S3_4"][1][3] = (int(graph["S3_4"][1][1][0])-noiseOut[8])**2 + (int(graph["S3_4"][1][1][1])-noiseOut[9])**2
    s6_1_4 = graph["S3_4"][0][3] + graph["S1_3"][1][3]
    s7_1_4 = graph["S3_4"][1][3] + graph["S1_3"][1][3]
    graph["S4_4"][0][3] = (int(graph["S4_4"][0][1][0])-noiseOut[8])**2 + (int(graph["S4_4"][0][1][1])-noiseOut[9])**2
    graph["S4_4"][1][3] = (int(graph["S4_4"][1][1][0])-noiseOut[8])**2 + (int(graph["S4_4"][1][1][1])-noiseOut[9])**2
    s0_2_4 = graph["S4_4"][0][3] + graph["S2_3"][0][3]
    s1_2_4 = graph["S4_4"][1][3] + graph["S2_3"][0][3]
    graph["S5_4"][0][3] = (int(graph["S5_4"][0][1][0])-noiseOut[8])**2 + (int(graph["S5_4"][0][1][1])-noiseOut[9])**2
    graph["S5_4"][1][3] = (int(graph["S5_4"][1][1][0])-noiseOut[8])**2 + (int(graph["S5_4"][1][1][1])-noiseOut[9])**2
    s2_2_4 = graph["S5_4"][0][3] + graph["S2_3"][1][3]
    s3_2_4 = graph["S5_4"][1][3] + graph["S2_3"][1][3]
    graph["S6_4"][0][3] = (int(graph["S6_4"][0][1][0])-noiseOut[8])**2 + (int(graph["S6_4"][0][1][1])-noiseOut[9])**2
    graph["S6_4"][1][3] = (int(graph["S6_4"][1][1][0])-noiseOut[8])**2 + (int(graph["S6_4"][1][1][1])-noiseOut[9])**2
    s4_2_4 = graph["S6_4"][0][3] + graph["S3_3"][0][3]
    s5_2_4 = graph["S6_4"][1][3] + graph["S3_3"][0][3]
    graph["S7_4"][0][3] = (int(graph["S7_4"][0][1][0])-noiseOut[8])**2 + (int(graph["S7_4"][0][1][1])-noiseOut[9])**2
    graph["S7_4"][1][3] = (int(graph["S7_4"][1][1][0])-noiseOut[8])**2 + (int(graph["S7_4"][1][1][1])-noiseOut[9])**2 #4
    s6_2_4 = graph["S7_4"][0][3] + graph["S3_3"][1][3]
    s7_2_4 = graph["S7_4"][1][3] + graph["S3_3"][1][3]
    if s0_1_4 <= s0_2_4:
        graph["S0_4"][0][3] = s0_1_4
        graph["S0_4"][0][4] = ["0", "S0_4"]
    else:
        graph["S0_4"][0][3] = s0_2_4
        graph["S0_4"][0][4] = ["0", "S4_4"]

    if s1_1_4 <= s1_2_4:
        graph["S0_4"][1][3] = s1_1_4
        graph["S0_4"][1][4] = ["1", "S0_4"]
    else:
        graph["S0_4"][1][3] = s1_2_4
        graph["S0_4"][1][4] = ["1", "S4_4"]

    if s2_1_4 <= s2_2_4:
        graph["S1_4"][0][3] = s2_1_4
        graph["S1_4"][0][4] = ["0", "S1_4"]
    else:
        graph["S1_4"][0][3] = s2_2_4
        graph["S1_4"][0][4] = ["0", "S5_4"]

    if s3_1_4 <= s3_2_4:
        graph["S1_4"][1][3] = s3_1_4
        graph["S1_4"][1][4] = ["1", "S1_4"]
    else:
        graph["S1_4"][1][3] = s3_2_4
        graph["S1_4"][1][4] = ["1", "S5_4"]

    if s4_1_4 <= s4_2_4:
        graph["S2_4"][0][3] = s4_1_4
        graph["S2_4"][0][4] = ["0", "S2_4"]
    else:
        graph["S2_4"][0][3] = s4_2_4
        graph["S2_4"][0][4] = ["0", "S6_4"]

    if s5_1_4 <= s5_2_4:
        graph["S2_4"][1][3] = s5_1_4
        graph["S2_4"][1][4] = ["1", "S2_4"]
    else:
        graph["S2_4"][1][3] = s5_2_4
        graph["S2_4"][1][4] = ["1", "S6_4"]

    if s6_1_4 <= s6_2_4:
        graph["S3_4"][0][3] = s6_1_4
        graph["S3_4"][0][4] = ["0", "S3_4"]
    else:
        graph["S3_4"][0][3] = s6_2_4
        graph["S3_4"][0][4] = ["0", "S7_4"]

    if s7_1_4 <= s7_2_4:
        graph["S3_4"][1][3] = s7_1_4
        graph["S3_4"][1][4] = ["1", "S3_4"]
    else:
        graph["S3_4"][1][3] = s7_2_4
        graph["S3_4"][1][4] = ["1", "S7_4"]


    graph["S0_5"][0][3] = (int(graph["S0_5"][0][1][0])-noiseOut[10])**2 + (int(graph["S0_5"][0][1][1])-noiseOut[11])**2
    graph["S0_5"][1][3] = (int(graph["S0_5"][1][1][0])-noiseOut[10])**2 + (int(graph["S0_5"][1][1][1])-noiseOut[11])**2
    s0_1_5 = graph["S0_5"][0][3] + graph["S0_4"][0][3]
    s1_1_5 = graph["S0_5"][1][3] + graph["S0_4"][0][3]
    graph["S1_5"][0][3] = (int(graph["S1_5"][0][1][0])-noiseOut[10])**2 + (int(graph["S1_5"][0][1][1])-noiseOut[11])**2
    graph["S1_5"][1][3] = (int(graph["S1_5"][1][1][0])-noiseOut[10])**2 + (int(graph["S1_5"][1][1][1])-noiseOut[11])**2
    s2_1_5 = graph["S1_5"][0][3] + graph["S0_4"][1][3]
    s3_1_5 = graph["S1_5"][1][3] + graph["S0_4"][1][3]
    graph["S2_5"][0][3] = (int(graph["S2_5"][0][1][0])-noiseOut[10])**2 + (int(graph["S2_5"][0][1][1])-noiseOut[11])**2
    graph["S2_5"][1][3] = (int(graph["S2_5"][1][1][0])-noiseOut[10])**2 + (int(graph["S2_5"][1][1][1])-noiseOut[11])**2
    s4_1_5 = graph["S2_5"][0][3] + graph["S1_4"][0][3]
    s5_1_5 = graph["S2_5"][1][3] + graph["S1_4"][0][3]
    graph["S3_5"][0][3] = (int(graph["S3_5"][0][1][0])-noiseOut[10])**2 + (int(graph["S3_5"][0][1][1])-noiseOut[11])**2
    graph["S3_5"][1][3] = (int(graph["S3_5"][1][1][0])-noiseOut[10])**2 + (int(graph["S3_5"][1][1][1])-noiseOut[11])**2
    s6_1_5 = graph["S3_5"][0][3] + graph["S1_4"][1][3]
    s7_1_5 = graph["S3_5"][1][3] + graph["S1_4"][1][3]
    graph["S4_5"][0][3] = (int(graph["S4_5"][0][1][0])-noiseOut[10])**2 + (int(graph["S4_5"][0][1][1])-noiseOut[11])**2
    graph["S4_5"][1][3] = (int(graph["S4_5"][1][1][0])-noiseOut[10])**2 + (int(graph["S4_5"][1][1][1])-noiseOut[11])**2
    s0_2_5 = graph["S4_5"][0][3] + graph["S2_4"][0][3]
    s1_2_5 = graph["S4_5"][1][3] + graph["S2_4"][0][3]
    graph["S5_5"][0][3] = (int(graph["S5_5"][0][1][0])-noiseOut[10])**2 + (int(graph["S5_5"][0][1][1])-noiseOut[11])**2
    graph["S5_5"][1][3] = (int(graph["S5_5"][1][1][0])-noiseOut[10])**2 + (int(graph["S5_5"][1][1][1])-noiseOut[11])**2
    s2_2_5 = graph["S5_5"][0][3] + graph["S2_4"][1][3]
    s3_2_5 = graph["S5_5"][1][3] + graph["S2_4"][1][3]
    graph["S6_5"][0][3] = (int(graph["S6_5"][0][1][0])-noiseOut[10])**2 + (int(graph["S6_5"][0][1][1])-noiseOut[11])**2
    graph["S6_5"][1][3] = (int(graph["S6_5"][1][1][0])-noiseOut[10])**2 + (int(graph["S6_5"][1][1][1])-noiseOut[11])**2
    s4_2_5 = graph["S6_5"][0][3] + graph["S3_4"][0][3]
    s5_2_5 = graph["S6_5"][1][3] + graph["S3_4"][0][3]
    graph["S7_5"][0][3] = (int(graph["S7_5"][0][1][0])-noiseOut[10])**2 + (int(graph["S7_5"][0][1][1])-noiseOut[11])**2
    graph["S7_5"][1][3] = (int(graph["S7_5"][1][1][0])-noiseOut[10])**2 + (int(graph["S7_5"][1][1][1])-noiseOut[11])**2 #5
    s6_2_5 = graph["S7_5"][0][3] + graph["S3_4"][1][3]
    s7_2_5 = graph["S7_5"][1][3] + graph["S3_4"][1][3]
    if s0_1_5 <= s0_2_5:
        graph["S0_5"][0][3] = s0_1_5
        graph["S0_5"][0][4] = ["0", "S0_5"]
    else:
        graph["S0_5"][0][3] = s0_2_5
        graph["S0_5"][0][4] = ["0", "S4_5"]

    if s1_1_5 <= s1_2_5:
        graph["S0_5"][1][3] = s1_1_5
        graph["S0_5"][1][4] = ["1", "S0_5"]
    else:
        graph["S0_5"][1][3] = s1_2_5
        graph["S0_5"][1][4] = ["1", "S4_5"]

    if s2_1_5 <= s2_2_5:
        graph["S1_5"][0][3] = s2_1_5
        graph["S1_5"][0][4] = ["0", "S1_5"]
    else:
        graph["S1_5"][0][3] = s2_2_5
        graph["S1_5"][0][4] = ["0", "S5_5"]

    if s3_1_5 <= s3_2_5:
        graph["S1_5"][1][3] = s3_1_5
        graph["S1_5"][1][4] = ["1", "S1_5"]
    else:
        graph["S1_5"][1][3] = s3_2_5
        graph["S1_5"][1][4] = ["1", "S5_5"]

    if s4_1_5 <= s4_2_5:
        graph["S2_5"][0][3] = s4_1_5
        graph["S2_5"][0][4] = ["0", "S2_5"]
    else:
        graph["S2_5"][0][3] = s4_2_5
        graph["S2_5"][0][4] = ["0", "S6_5"]

    if s5_1_5 <= s5_2_5:
        graph["S2_5"][1][3] = s5_1_5
        graph["S2_5"][1][4] = ["1", "S2_5"]
    else:
        graph["S2_5"][1][3] = s5_2_5
        graph["S2_5"][1][4] = ["1", "S6_5"]

    if s6_1_5 <= s6_2_5:
        graph["S3_5"][0][3] = s6_1_5
        graph["S3_5"][0][4] = ["0", "S3_5"]
    else:
        graph["S3_5"][0][3] = s6_2_5
        graph["S3_5"][0][4] = ["0", "S7_5"]

    if s7_1_5 <= s7_2_5:
        graph["S3_5"][1][3] = s7_1_5
        graph["S3_5"][1][4] = ["1", "S3_5"]
    else:
        graph["S3_5"][1][3] = s7_2_5
        graph["S3_5"][1][4] = ["1", "S7_5"]




    graph["S0_6"][0][3] = (int(graph["S0_6"][0][1][0])-noiseOut[12])**2 + (int(graph["S0_6"][0][1][1])-noiseOut[13])**2
    graph["S0_6"][1][3] = (int(graph["S0_6"][1][1][0])-noiseOut[12])**2 + (int(graph["S0_6"][1][1][1])-noiseOut[13])**2
    s0_1_6 = graph["S0_6"][0][3] + graph["S0_5"][0][3]
    s1_1_6 = graph["S0_6"][1][3] + graph["S0_5"][0][3]
    graph["S1_6"][0][3] = (int(graph["S1_6"][0][1][0])-noiseOut[12])**2 + (int(graph["S1_6"][0][1][1])-noiseOut[13])**2
    graph["S1_6"][1][3] = (int(graph["S1_6"][1][1][0])-noiseOut[12])**2 + (int(graph["S1_6"][1][1][1])-noiseOut[13])**2
    s2_1_6 = graph["S1_6"][0][3] + graph["S0_5"][1][3]
    s3_1_6 = graph["S1_6"][1][3] + graph["S0_5"][1][3]
    graph["S2_6"][0][3] = (int(graph["S2_6"][0][1][0])-noiseOut[12])**2 + (int(graph["S2_6"][0][1][1])-noiseOut[13])**2
    graph["S2_6"][1][3] = (int(graph["S2_6"][1][1][0])-noiseOut[12])**2 + (int(graph["S2_6"][1][1][1])-noiseOut[13])**2
    s4_1_6 = graph["S2_6"][0][3] + graph["S1_5"][0][3]
    s5_1_6 = graph["S2_6"][1][3] + graph["S1_5"][0][3]
    graph["S3_6"][0][3] = (int(graph["S3_6"][0][1][0])-noiseOut[12])**2 + (int(graph["S3_6"][0][1][1])-noiseOut[13])**2
    graph["S3_6"][1][3] = (int(graph["S3_6"][1][1][0])-noiseOut[12])**2 + (int(graph["S3_6"][1][1][1])-noiseOut[13])**2
    s6_1_6 = graph["S3_6"][0][3] + graph["S1_5"][1][3]
    s7_1_6 = graph["S3_6"][1][3] + graph["S1_5"][1][3]
    graph["S4_6"][0][3] = (int(graph["S4_6"][0][1][0])-noiseOut[12])**2 + (int(graph["S4_6"][0][1][1])-noiseOut[13])**2
    graph["S4_6"][1][3] = (int(graph["S4_6"][1][1][0])-noiseOut[12])**2 + (int(graph["S4_6"][1][1][1])-noiseOut[13])**2
    s0_2_6 = graph["S4_6"][0][3] + graph["S2_5"][0][3]
    s1_2_6 = graph["S4_6"][1][3] + graph["S2_5"][0][3]
    graph["S5_6"][0][3] = (int(graph["S5_6"][0][1][0])-noiseOut[12])**2 + (int(graph["S5_6"][0][1][1])-noiseOut[13])**2
    graph["S5_6"][1][3] = (int(graph["S5_6"][1][1][0])-noiseOut[12])**2 + (int(graph["S5_6"][1][1][1])-noiseOut[13])**2
    s2_2_6 = graph["S5_6"][0][3] + graph["S2_5"][1][3]
    s3_2_6 = graph["S5_6"][1][3] + graph["S2_5"][1][3]
    graph["S6_6"][0][3] = (int(graph["S6_6"][0][1][0])-noiseOut[12])**2 + (int(graph["S6_6"][0][1][1])-noiseOut[13])**2
    graph["S6_6"][1][3] = (int(graph["S6_6"][1][1][0])-noiseOut[12])**2 + (int(graph["S6_6"][1][1][1])-noiseOut[13])**2
    s4_2_6 = graph["S6_6"][0][3] + graph["S3_5"][0][3]
    s5_2_6 = graph["S6_6"][1][3] + graph["S3_5"][0][3]
    graph["S7_6"][0][3] = (int(graph["S7_6"][0][1][0])-noiseOut[12])**2 + (int(graph["S7_6"][0][1][1])-noiseOut[13])**2
    graph["S7_6"][1][3] = (int(graph["S7_6"][1][1][0])-noiseOut[12])**2 + (int(graph["S7_6"][1][1][1])-noiseOut[13])**2 #6
    s6_2_6 = graph["S7_6"][0][3] + graph["S3_5"][1][3]
    s7_2_6 = graph["S7_6"][1][3] + graph["S3_5"][1][3]
    if s0_1_6 <= s0_2_6:
        graph["S0_6"][0][3] = s0_1_6
        graph["S0_6"][0][4] = ["0", "S0_6"]
    else:
        graph["S0_6"][0][3] = s0_2_6
        graph["S0_6"][0][4] = ["0", "S4_6"]

    if s1_1_6 <= s1_2_6:
        graph["S0_6"][1][3] = s1_1_6
        graph["S0_6"][1][4] = ["1", "S0_6"]
    else:
        graph["S0_6"][1][3] = s1_2_6
        graph["S0_6"][1][4] = ["1", "S4_6"]

    if s2_1_6 <= s2_2_6:
        graph["S1_6"][0][3] = s2_1_6
        graph["S1_6"][0][4] = ["0", "S1_6"]
    else:
        graph["S1_6"][0][3] = s2_2_6
        graph["S1_6"][0][4] = ["0", "S5_6"]

    if s3_1_6 <= s3_2_6:
        graph["S1_6"][1][3] = s3_1_6
        graph["S1_6"][1][4] = ["1", "S1_6"]
    else:
        graph["S1_6"][1][3] = s3_2_6
        graph["S1_6"][1][4] = ["1", "S5_6"]

    if s4_1_6 <= s4_2_6:
        graph["S2_6"][0][3] = s4_1_6
        graph["S2_6"][0][4] = ["0", "S2_6"]
    else:
        graph["S2_6"][0][3] = s4_2_6
        graph["S2_6"][0][4] = ["0", "S6_6"]

    if s5_1_6 <= s5_2_6:
        graph["S2_6"][1][3] = s5_1_6
        graph["S2_6"][1][4] = ["1", "S2_6"]
    else:
        graph["S2_6"][1][3] = s5_2_6
        graph["S2_6"][1][4] = ["1", "S6_6"]

    if s6_1_6 <= s6_2_6:
        graph["S3_6"][0][3] = s6_1_6
        graph["S3_6"][0][4] = ["0", "S3_6"]
    else:
        graph["S3_6"][0][3] = s6_2_6
        graph["S3_6"][0][4] = ["0", "S7_6"]

    if s7_1_6 <= s7_2_6:
        graph["S3_6"][1][3] = s7_1_6
        graph["S3_6"][1][4] = ["1", "S3_6"]
    else:
        graph["S3_6"][1][3] = s7_2_6
        graph["S3_6"][1][4] = ["1", "S7_6"]


    graph["S0_7"][0][3] = (int(graph["S0_7"][0][1][0])-noiseOut[14])**2 + (int(graph["S0_7"][0][1][1])-noiseOut[15])**2
    graph["S0_7"][1][3] = (int(graph["S0_7"][1][1][0])-noiseOut[14])**2 + (int(graph["S0_7"][1][1][1])-noiseOut[15])**2
    s0_1_7 = graph["S0_7"][0][3] + graph["S0_6"][0][3]
    s1_1_7 = graph["S0_7"][1][3] + graph["S0_6"][0][3]
    graph["S1_7"][0][3] = (int(graph["S1_7"][0][1][0])-noiseOut[14])**2 + (int(graph["S1_7"][0][1][1])-noiseOut[15])**2
    graph["S1_7"][1][3] = (int(graph["S1_7"][1][1][0])-noiseOut[14])**2 + (int(graph["S1_7"][1][1][1])-noiseOut[15])**2
    s2_1_7 = graph["S1_7"][0][3] + graph["S0_6"][1][3]
    s3_1_7 = graph["S1_7"][1][3] + graph["S0_6"][1][3]
    graph["S2_7"][0][3] = (int(graph["S2_7"][0][1][0])-noiseOut[14])**2 + (int(graph["S2_7"][0][1][1])-noiseOut[15])**2
    graph["S2_7"][1][3] = (int(graph["S2_7"][1][1][0])-noiseOut[14])**2 + (int(graph["S2_7"][1][1][1])-noiseOut[15])**2
    s4_1_7 = graph["S2_7"][0][3] + graph["S1_6"][0][3]
    s5_1_7 = graph["S2_7"][1][3] + graph["S1_6"][0][3]
    graph["S3_7"][0][3] = (int(graph["S3_7"][0][1][0])-noiseOut[14])**2 + (int(graph["S3_7"][0][1][1])-noiseOut[15])**2
    graph["S3_7"][1][3] = (int(graph["S3_7"][1][1][0])-noiseOut[14])**2 + (int(graph["S3_7"][1][1][1])-noiseOut[15])**2
    s6_1_7 = graph["S3_7"][0][3] + graph["S1_6"][1][3]
    s7_1_7 = graph["S3_7"][1][3] + graph["S1_6"][1][3]
    graph["S4_7"][0][3] = (int(graph["S4_7"][0][1][0])-noiseOut[14])**2 + (int(graph["S4_7"][0][1][1])-noiseOut[15])**2
    graph["S4_7"][1][3] = (int(graph["S4_7"][1][1][0])-noiseOut[14])**2 + (int(graph["S4_7"][1][1][1])-noiseOut[15])**2
    s0_2_7 = graph["S4_7"][0][3] + graph["S2_6"][0][3]
    s1_2_7 = graph["S4_7"][1][3] + graph["S2_6"][0][3]
    graph["S5_7"][0][3] = (int(graph["S5_7"][0][1][0])-noiseOut[14])**2 + (int(graph["S5_7"][0][1][1])-noiseOut[15])**2
    graph["S5_7"][1][3] = (int(graph["S5_7"][1][1][0])-noiseOut[14])**2 + (int(graph["S5_7"][1][1][1])-noiseOut[15])**2
    s2_2_7 = graph["S5_7"][0][3] + graph["S2_6"][1][3]
    s3_2_7 = graph["S5_7"][1][3] + graph["S2_6"][1][3]
    graph["S6_7"][0][3] = (int(graph["S6_7"][0][1][0])-noiseOut[14])**2 + (int(graph["S6_7"][0][1][1])-noiseOut[15])**2
    graph["S6_7"][1][3] = (int(graph["S6_7"][1][1][0])-noiseOut[14])**2 + (int(graph["S6_7"][1][1][1])-noiseOut[15])**2
    s4_2_7 = graph["S6_7"][0][3] + graph["S3_6"][0][3]
    s5_2_7 = graph["S6_7"][1][3] + graph["S3_6"][0][3]
    graph["S7_7"][0][3] = (int(graph["S7_7"][0][1][0])-noiseOut[14])**2 + (int(graph["S7_7"][0][1][1])-noiseOut[15])**2
    graph["S7_7"][1][3] = (int(graph["S7_7"][1][1][0])-noiseOut[14])**2 + (int(graph["S7_7"][1][1][1])-noiseOut[15])**2 #7
    s6_2_7 = graph["S7_7"][0][3] + graph["S3_6"][1][3]
    s7_2_7 = graph["S7_7"][1][3] + graph["S3_6"][1][3]
    if s0_1_7 <= s0_2_7:
        graph["S0_7"][0][3] = s0_1_7
        graph["S0_7"][0][4] = ["0", "S0_7"]
    else:
        graph["S0_7"][0][3] = s0_2_7
        graph["S0_7"][0][4] = ["0", "S4_7"]

    if s1_1_7 <= s1_2_7:
        graph["S0_7"][1][3] = s1_1_7
        graph["S0_7"][1][4] = ["1", "S0_7"]
    else:
        graph["S0_7"][1][3] = s1_2_7
        graph["S0_7"][1][4] = ["1", "S4_7"]

    if s2_1_7 <= s2_2_7:
        graph["S1_7"][0][3] = s2_1_7
        graph["S1_7"][0][4] = ["0", "S1_7"]
    else:
        graph["S1_7"][0][3] = s2_2_7
        graph["S1_7"][0][4] = ["0", "S5_7"]

    if s3_1_7 <= s3_2_7:
        graph["S1_7"][1][3] = s3_1_7
        graph["S1_7"][1][4] = ["1", "S1_7"]
    else:
        graph["S1_7"][1][3] = s3_2_7
        graph["S1_7"][1][4] = ["1", "S5_7"]

    if s4_1_7 <= s4_2_7:
        graph["S2_7"][0][3] = s4_1_7
        graph["S2_7"][0][4] = ["0", "S2_7"]
    else:
        graph["S2_7"][0][3] = s4_2_7
        graph["S2_7"][0][4] = ["0", "S6_7"]

    if s5_1_7 <= s5_2_7:
        graph["S2_7"][1][3] = s5_1_7
        graph["S2_7"][1][4] = ["1", "S2_7"]
    else:
        graph["S2_7"][1][3] = s5_2_7
        graph["S2_7"][1][4] = ["1", "S6_7"]

    if s6_1_7 <= s6_2_7:
        graph["S3_7"][0][3] = s6_1_7
        graph["S3_7"][0][4] = ["0", "S3_7"]
    else:
        graph["S3_7"][0][3] = s6_2_7
        graph["S3_7"][0][4] = ["0", "S7_7"]

    if s7_1_7 <= s7_2_7:
        graph["S3_7"][1][3] = s7_1_7
        graph["S3_7"][1][4] = ["1", "S3_7"]
    else:
        graph["S3_7"][1][3] = s7_2_7
        graph["S3_7"][1][4] = ["1", "S7_7"]


    graph["S0_8"][0][3] = (int(graph["S0_8"][0][1][0])-noiseOut[16])**2 + (int(graph["S0_8"][0][1][1])-noiseOut[17])**2
    graph["S0_8"][1][3] = (int(graph["S0_8"][1][1][0])-noiseOut[16])**2 + (int(graph["S0_8"][1][1][1])-noiseOut[17])**2
    s0_1_8 = graph["S0_8"][0][3] + graph["S0_7"][0][3]
    s1_1_8 = graph["S0_8"][1][3] + graph["S0_7"][0][3]
    graph["S1_8"][0][3] = (int(graph["S1_8"][0][1][0])-noiseOut[16])**2 + (int(graph["S1_8"][0][1][1])-noiseOut[17])**2
    graph["S1_8"][1][3] = (int(graph["S1_8"][1][1][0])-noiseOut[16])**2 + (int(graph["S1_8"][1][1][1])-noiseOut[17])**2
    s2_1_8 = graph["S1_8"][0][3] + graph["S0_7"][1][3]
    s3_1_8 = graph["S1_8"][1][3] + graph["S0_7"][1][3]
    graph["S2_8"][0][3] = (int(graph["S2_8"][0][1][0])-noiseOut[16])**2 + (int(graph["S2_8"][0][1][1])-noiseOut[17])**2
    graph["S2_8"][1][3] = (int(graph["S2_8"][1][1][0])-noiseOut[16])**2 + (int(graph["S2_8"][1][1][1])-noiseOut[17])**2
    s4_1_8 = graph["S2_8"][0][3] + graph["S1_7"][0][3]
    s5_1_8 = graph["S2_8"][1][3] + graph["S1_7"][0][3]
    graph["S3_8"][0][3] = (int(graph["S3_8"][0][1][0])-noiseOut[16])**2 + (int(graph["S3_8"][0][1][1])-noiseOut[17])**2
    graph["S3_8"][1][3] = (int(graph["S3_8"][1][1][0])-noiseOut[16])**2 + (int(graph["S3_8"][1][1][1])-noiseOut[17])**2
    s6_1_8 = graph["S3_8"][0][3] + graph["S1_7"][1][3]
    s7_1_8 = graph["S3_8"][1][3] + graph["S1_7"][1][3]
    graph["S4_8"][0][3] = (int(graph["S4_8"][0][1][0])-noiseOut[16])**2 + (int(graph["S4_8"][0][1][1])-noiseOut[17])**2
    graph["S4_8"][1][3] = (int(graph["S4_8"][1][1][0])-noiseOut[16])**2 + (int(graph["S4_8"][1][1][1])-noiseOut[17])**2
    s0_2_8 = graph["S4_8"][0][3] + graph["S2_7"][0][3]
    s1_2_8 = graph["S4_8"][1][3] + graph["S2_7"][0][3]
    graph["S5_8"][0][3] = (int(graph["S5_8"][0][1][0])-noiseOut[16])**2 + (int(graph["S5_8"][0][1][1])-noiseOut[17])**2
    graph["S5_8"][1][3] = (int(graph["S5_8"][1][1][0])-noiseOut[16])**2 + (int(graph["S5_8"][1][1][1])-noiseOut[17])**2
    s2_2_8 = graph["S5_8"][0][3] + graph["S2_7"][1][3]
    s3_2_8 = graph["S5_8"][1][3] + graph["S2_7"][1][3]
    graph["S6_8"][0][3] = (int(graph["S6_8"][0][1][0])-noiseOut[16])**2 + (int(graph["S6_8"][0][1][1])-noiseOut[17])**2
    graph["S6_8"][1][3] = (int(graph["S6_8"][1][1][0])-noiseOut[16])**2 + (int(graph["S6_8"][1][1][1])-noiseOut[17])**2
    s4_2_8 = graph["S6_8"][0][3] + graph["S3_7"][0][3]
    s5_2_8 = graph["S6_8"][1][3] + graph["S3_7"][0][3]
    graph["S7_8"][0][3] = (int(graph["S7_8"][0][1][0])-noiseOut[16])**2 + (int(graph["S7_8"][0][1][1])-noiseOut[17])**2
    graph["S7_8"][1][3] = (int(graph["S7_8"][1][1][0])-noiseOut[16])**2 + (int(graph["S7_8"][1][1][1])-noiseOut[17])**2 #8
    s6_2_8 = graph["S7_8"][0][3] + graph["S3_7"][1][3]
    s7_2_8 = graph["S7_8"][1][3] + graph["S3_7"][1][3]
    if s0_1_8 <= s0_2_8:
        graph["S0_8"][0][3] = s0_1_8
        graph["S0_8"][0][4] = ["0", "S0_8"]
    else:
        graph["S0_8"][0][3] = s0_2_8
        graph["S0_8"][0][4] = ["0", "S4_8"]

    if s1_1_8 <= s1_2_8:
        graph["S0_8"][1][3] = s1_1_8
        graph["S0_8"][1][4] = ["1", "S0_8"]
    else:
        graph["S0_8"][1][3] = s1_2_8
        graph["S0_8"][1][4] = ["1", "S4_8"]

    if s2_1_8 <= s2_2_8:
        graph["S1_8"][0][3] = s2_1_8
        graph["S1_8"][0][4] = ["0", "S1_8"]
    else:
        graph["S1_8"][0][3] = s2_2_8
        graph["S1_8"][0][4] = ["0", "S5_8"]

    if s3_1_8 <= s3_2_8:
        graph["S1_8"][1][3] = s3_1_8
        graph["S1_8"][1][4] = ["1", "S1_8"]
    else:
        graph["S1_8"][1][3] = s3_2_8
        graph["S1_8"][1][4] = ["1", "S5_8"]

    if s4_1_8 <= s4_2_8:
        graph["S2_8"][0][3] = s4_1_8
        graph["S2_8"][0][4] = ["0", "S2_8"]
    else:
        graph["S2_8"][0][3] = s4_2_8
        graph["S2_8"][0][4] = ["0", "S6_8"]

    if s5_1_8 <= s5_2_8:
        graph["S2_8"][1][3] = s5_1_8
        graph["S2_8"][1][4] = ["1", "S2_8"]
    else:
        graph["S2_8"][1][3] = s5_2_8
        graph["S2_8"][1][4] = ["1", "S6_8"]

    if s6_1_8 <= s6_2_8:
        graph["S3_8"][0][3] = s6_1_8
        graph["S3_8"][0][4] = ["0", "S3_8"]
    else:
        graph["S3_8"][0][3] = s6_2_8
        graph["S3_8"][0][4] = ["0", "S7_8"]

    if s7_1_8 <= s7_2_8:
        graph["S3_8"][1][3] = s7_1_8
        graph["S3_8"][1][4] = ["1", "S3_8"]
    else:
        graph["S3_8"][1][3] = s7_2_8
        graph["S3_8"][1][4] = ["1", "S7_8"]



    graph["S0_9"][0][3] = (int(graph["S0_9"][0][1][0])-noiseOut[18])**2 + (int(graph["S0_9"][0][1][1])-noiseOut[19])**2
    graph["S0_9"][1][3] = (int(graph["S0_9"][1][1][0])-noiseOut[18])**2 + (int(graph["S0_9"][1][1][1])-noiseOut[19])**2
    s0_1_9 = graph["S0_9"][0][3] + graph["S0_8"][0][3]
    s1_1_9 = graph["S0_9"][1][3] + graph["S0_8"][0][3]
    graph["S1_9"][0][3] = (int(graph["S1_9"][0][1][0])-noiseOut[18])**2 + (int(graph["S1_9"][0][1][1])-noiseOut[19])**2
    graph["S1_9"][1][3] = (int(graph["S1_9"][1][1][0])-noiseOut[18])**2 + (int(graph["S1_9"][1][1][1])-noiseOut[19])**2
    s2_1_9 = graph["S1_9"][0][3] + graph["S0_8"][1][3]
    s3_1_9 = graph["S1_9"][1][3] + graph["S0_8"][1][3]
    graph["S2_9"][0][3] = (int(graph["S2_9"][0][1][0])-noiseOut[18])**2 + (int(graph["S2_9"][0][1][1])-noiseOut[19])**2
    graph["S2_9"][1][3] = (int(graph["S2_9"][1][1][0])-noiseOut[18])**2 + (int(graph["S2_9"][1][1][1])-noiseOut[19])**2
    s4_1_9 = graph["S2_9"][0][3] + graph["S1_8"][0][3]
    s5_1_9 = graph["S2_9"][1][3] + graph["S1_8"][0][3]
    graph["S3_9"][0][3] = (int(graph["S3_9"][0][1][0])-noiseOut[18])**2 + (int(graph["S3_9"][0][1][1])-noiseOut[19])**2
    graph["S3_9"][1][3] = (int(graph["S3_9"][1][1][0])-noiseOut[18])**2 + (int(graph["S3_9"][1][1][1])-noiseOut[19])**2
    s6_1_9 = graph["S3_9"][0][3] + graph["S1_8"][1][3]
    s7_1_9 = graph["S3_9"][1][3] + graph["S1_8"][1][3]
    graph["S4_9"][0][3] = (int(graph["S4_9"][0][1][0])-noiseOut[18])**2 + (int(graph["S4_9"][0][1][1])-noiseOut[19])**2
    graph["S4_9"][1][3] = (int(graph["S4_9"][1][1][0])-noiseOut[18])**2 + (int(graph["S4_9"][1][1][1])-noiseOut[19])**2
    s0_2_9 = graph["S4_9"][0][3] + graph["S2_8"][0][3]
    s1_2_9 = graph["S4_9"][1][3] + graph["S2_8"][0][3]
    graph["S5_9"][0][3] = (int(graph["S5_9"][0][1][0])-noiseOut[18])**2 + (int(graph["S5_9"][0][1][1])-noiseOut[19])**2
    graph["S5_9"][1][3] = (int(graph["S5_9"][1][1][0])-noiseOut[18])**2 + (int(graph["S5_9"][1][1][1])-noiseOut[19])**2
    s2_2_9 = graph["S5_9"][0][3] + graph["S2_8"][1][3]
    s3_2_9 = graph["S5_9"][1][3] + graph["S2_8"][1][3]
    graph["S6_9"][0][3] = (int(graph["S6_9"][0][1][0])-noiseOut[18])**2 + (int(graph["S6_9"][0][1][1])-noiseOut[19])**2
    graph["S6_9"][1][3] = (int(graph["S6_9"][1][1][0])-noiseOut[18])**2 + (int(graph["S6_9"][1][1][1])-noiseOut[19])**2
    s4_2_9 = graph["S6_9"][0][3] + graph["S3_8"][0][3]
    s5_2_9 = graph["S6_9"][1][3] + graph["S3_8"][0][3]
    graph["S7_9"][0][3] = (int(graph["S7_9"][0][1][0])-noiseOut[18])**2 + (int(graph["S7_9"][0][1][1])-noiseOut[19])**2
    graph["S7_9"][1][3] = (int(graph["S7_9"][1][1][0])-noiseOut[18])**2 + (int(graph["S7_9"][1][1][1])-noiseOut[19])**2 #9
    s6_2_9 = graph["S7_9"][0][3] + graph["S3_8"][1][3]
    s7_2_9 = graph["S7_9"][1][3] + graph["S3_8"][1][3]
    if s0_1_9 <= s0_2_9:
        graph["S0_9"][0][3] = s0_1_9
        graph["S0_9"][0][4] = ["0", "S0_9"]
    else:
        graph["S0_9"][0][3] = s0_2_9
        graph["S0_9"][0][4] = ["0", "S4_9"]

    if s1_1_9 <= s1_2_9:
        graph["S0_9"][1][3] = s1_1_9
        graph["S0_9"][1][4] = ["1", "S0_9"]
    else:
        graph["S0_9"][1][3] = s1_2_9
        graph["S0_9"][1][4] = ["1", "S4_9"]

    if s2_1_9 <= s2_2_9:
        graph["S1_9"][0][3] = s2_1_9
        graph["S1_9"][0][4] = ["0", "S1_9"]
    else:
        graph["S1_9"][0][3] = s2_2_9
        graph["S1_9"][0][4] = ["0", "S5_9"]

    if s3_1_9 <= s3_2_9:
        graph["S1_9"][1][3] = s3_1_9
        graph["S1_9"][1][4] = ["1", "S1_9"]
    else:
        graph["S1_9"][1][3] = s3_2_9
        graph["S1_9"][1][4] = ["1", "S5_9"]

    if s4_1_9 <= s4_2_9:
        graph["S2_9"][0][3] = s4_1_9
        graph["S2_9"][0][4] = ["0", "S2_9"]
    else:
        graph["S2_9"][0][3] = s4_2_9
        graph["S2_9"][0][4] = ["0", "S6_9"]

    if s5_1_9 <= s5_2_9:
        graph["S2_9"][1][3] = s5_1_9
        graph["S2_9"][1][4] = ["1", "S2_9"]
    else:
        graph["S2_9"][1][3] = s5_2_9
        graph["S2_9"][1][4] = ["1", "S6_9"]

    if s6_1_9 <= s6_2_9:
        graph["S3_9"][0][3] = s6_1_9
        graph["S3_9"][0][4] = ["0", "S3_9"]
    else:
        graph["S3_9"][0][3] = s6_2_9
        graph["S3_9"][0][4] = ["0", "S7_9"]

    if s7_1_9 <= s7_2_9:
        graph["S3_9"][1][3] = s7_1_9
        graph["S3_9"][1][4] = ["1", "S3_9"]
    else:
        graph["S3_9"][1][3] = s7_2_9
        graph["S3_9"][1][4] = ["1", "S7_9"]


    """
    print(graph["S0_9"][0][3])
    print(graph["S0_9"][1][3])
    print(graph["S1_9"][0][3])
    print(graph["S1_9"][1][3])
    print(graph["S2_9"][0][3])
    print(graph["S2_9"][1][3])
    print(graph["S3_9"][0][3])
    print(graph["S3_9"][1][3])

    print("------")
    """
    val1 = graph["S0_9"][0][3]
    val2 = graph["S0_9"][1][3]
    val3 = graph["S1_9"][0][3]
    val4 = graph["S1_9"][1][3]
    val5 = graph["S2_9"][0][3]
    val6 = graph["S2_9"][1][3]
    val7 = graph["S3_9"][0][3]
    val8 = graph["S3_9"][1][3]

    lastList = [val1, val2, val3, val4, val5, val6, val7, val8]
    minVal = min(lastList)
    #print(minVal)

    for i in range(0, len(lastList), 1):
        if minVal == lastList[i]:
            indexNum = i
    #print(indexNum)

    lastNodePre = ""
    outputBit = ""
    if indexNum == 0:
        outputBit = graph["S0_9"][0][4][0]
        lastNodePre = graph["S0_9"][0][4][1]
    elif indexNum == 1:
        outputBit = graph["S0_9"][1][4][0]
        lastNodePre = graph["S0_9"][1][4][1]
    elif indexNum == 2:
        outputBit = graph["S1_9"][0][4][0]
        lastNodePre = graph["S1_9"][0][4][1]
    elif indexNum == 3:
        outputBit = graph["S1_9"][1][4][0]
        lastNodePre = graph["S1_9"][1][4][1]
    elif indexNum == 4:
        outputBit = graph["S2_9"][0][4][0]
        lastNodePre = graph["S2_9"][0][4][1]
    elif indexNum == 5:
        outputBit = graph["S2_9"][1][4][0]
        lastNodePre = graph["S2_9"][1][4][1]
    elif indexNum == 6:
        outputBit = graph["S3_9"][0][4][0]
        lastNodePre = graph["S3_9"][0][4][1]
    elif indexNum == 7:
        outputBit = graph["S3_9"][1][4][0]
        lastNodePre = graph["S3_9"][1][4][1]

    #print(graph["S4_9"][0][4]) []
    #print(graph["S4_9"][1][4]) []
    #print(graph["S4_5"][1][4]) []
    """
    for item in graph.values():
        if item[0][0] == lastNodePre and len(item[0][4]) == 2:
            outputBit = outputBit + item[0][4][0]
            lastNodePre = item[0][4][1]
        if item[1][0] == lastNodePre and len(item[0][4]) == 2:
            outputBit = outputBit + item[1][4][0]
            lastNodePre = item[1][4][1]
    print(outputBit)
    """

    for i in range(0, 9, 1):
        for item in graph.values():
            if item[0][0] == lastNodePre and len(item[0][4]) == 2:
                outputBit = outputBit + item[0][4][0]
                lastNodePre = item[0][4][1]
            if item[1][0] == lastNodePre and len(item[0][4]) == 2:
                outputBit = outputBit + item[1][4][0]
                lastNodePre = item[1][4][1]

    finalOutputBit = outputBit[::-1]
    #print(outputBit)
    #print(finalOutputBit)
    finalOutputBitMap = ""
    for i in range(0, len(finalOutputBit), 1):
        if finalOutputBit[i] == "0":
            finalOutputBitMap = finalOutputBitMap + "1"
        if finalOutputBit[i] == "1":
            finalOutputBitMap = finalOutputBitMap + "2"

    return finalOutputBitMap

def viterbiRun(theInput):
    bitError = 0
    cnt = 0

    while bitError < 25600:
        cnt = cnt + 1
        theOutput = viterbi(theInput)
        print("Output Bit: ", end = "")
        print(theOutput)

        for i in range(0, len(theInput), 1):
            if theInput[i] != theOutput[i]:
                bitError = bitError + 1
        print("Bit Error: ", end = "")
        print(bitError)
        print("---")

    totBit = cnt * 10
    bitErrorRate = bitError / totBit
    print("Total Bit: ", end="")
    print(totBit)
    print("Bit Error Rate: ", end="")
    print(bitErrorRate)

    SNR = -10*math.log(0.7*0.5, 10)

    print(SNR)


def plotFunc():
    N0 = [0.70, 0.65, 0.60, 0.55, 0.50, 0.45, 0.40, 0.38]

    SNR1 = [4.559, 4.8812, 5.2288, 5.6067, 6.0206, 6.4782, 6.9897, 7.2125]
    BER1 = [0.0144168, 0.008536, 0.00445, 0.00194, 0.000723, 0.000253, 0.0000607076, 0.0000258598]

    SNR2 = [4.559, 4.8812, 5.2288, 5.6067, 6.0206, 6.4782, 6.9897, 7.2125]
    BER2 = [0.0842043, 0.061306, 0.040921, 0.023801, 0.0114725, 0.004953, 0.0014292, 0.0006955]


    plt.semilogy(SNR1, BER1, label = "FSM 1")
    plt.semilogy(SNR2, BER2, label = "FSM 2")

    plt.xlabel("SNR(dB)")
    plt.ylabel("BER")

    plt.title("Viterbi Project(FSM 1 and FSM 2)")
    plt.legend()
    plt.show()



