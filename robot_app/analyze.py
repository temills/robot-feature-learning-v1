#!/usr/bin/env python3
import json

#get data
with open('out2.json') as f:
  data = json.load(f)        

#takes subject response dict
#returns list of num correct responses for
#all pairs, pairs round 1, pairs round 2, pairs round 3, memory test 1, memory test 2, memory test 3
def getNumCorrect(subj):
    r1, r2, r3 = 0, 0, 0
    for name in eval(subj["wrong1firstBotName"]):
        if name==' ':
            r1 = r1 + 1
    for name in eval(subj["wrong2firstBotName"]):
        if name==' ':
            r2 = r2 + 1
    for name in eval(subj["wrong3firstBotName"]):
        if name==' ':
            r3 = r3 + 1
    s = r1+r2+r3
    return [s, r1, r2, r3, subj["numMemoryCorrect"], subj["numMemoryCorrect2"], subj["numMemoryCorrect3"]]
    

omit = []
#for generations, see which robot that is, get its features
for i in range(len(data)):
    if (i < 8) or (i in omit):
        continue
    subj = data[i]
    print("Subject: " + subj["subject_id"])
    #print("Correct: " + str(getNumCorrect(subj)))
    c = getNumCorrect(subj)
    print("Correct: " + str(c[0]) + "(all pairs), " + str(c[1]) + "(round 1 pairs), " + str(c[2]) + "(round 2 pairs), " + str(c[3]) + "(round 3 pairs), ", str(c[4]) + "(memory test 1), ", str(c[5]) + "(memory test 2), " +  str(c[1]) + "(memory test 3)")
    #get useful features (often distinguishes robot pair)
    #and favored version of useful features (in these pairs, asked for robot often has that version of the feature)
    i1 = int(subj["usefulFt1"])
    v1 = int(subj["favoredEnd1"])
    i2 = int(subj["usefulFt2"])
    v2 = int(subj["favoredEnd2"])

    round1name1 = eval(subj['round1name1'])
    #map bot names to features
    botDict = {}
    names = list(set(round1name1))
    for name in names:
        idx = round1name1.index(name)
        botDict[name.lower()] = subj["round1bot1"][idx]

    #how we lookin
    generations = eval(subj['generations'])
    print("Generations: " + str(generations))

    #print("useful feature, end: " + str(i1) + ", " + str(v1))
    #print("useful feature, end: " + str(i2) + ", " + str(v2))
    print("Task favored bots with " + str(v1) + " for feature " + str(i1+1) + ", " + str(v2) + " for feature " + str(i2+1))
    print("Features of bots generated:")
    for g in generations:
        #if g not in names:
            #l = get_close_matches(g, names, 1, 0.9)
            #if len(l)==1:
                #g = l[0]
            #else:
                #print("dafuk is dis: " + g)
                #continue
        g = g.lower()
        bot = botDict[g]
        print(bot)
    print(" ")

#then look at useful features. A
