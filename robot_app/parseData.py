#!/usr/bin/env python3
import json

#reformat data before saving
def reformatData(inData):
    print('in reformat')
    #data = json.loads(inData['inData'])
    data = inData
    numWugs = 8
    numPairs = numWugs*2
    startIndex = 6
    #list of dictionaries, where each dictionary keeps the data for a single trial
    #Those dictionaries will become  rows in the data table
    trialIndex = startIndex
    botNames = {}
    tData = {}
    tData['turk_code'] = data[0]['turk_code']
    tData['subject_id'] = data[2]['response']['subject_id']
    tData['usefulFt1'] = data[0]['usefulFt1']
    tData['usefulFt2'] = data[0]['usefulFt2']
    tData['favoredEnd1'] = data[0]['favoredEnd1']
    tData['favoredEnd2'] = data[0]['favoredEnd2']
        
    #tempData.subject_id = tData.subject_id

    #first trial
    tData['round1rt'] = []
    tData['round1bot1'] = []
    tData['round1bot2'] = []
    tData['round1name1'] = []
    tData['round1name2'] = []
    tData['round1correct'] = []
    tData['wrong1firstBot'] = [] #if wrong in round 1, first bot displayed in learn trial
    tData['wrong1firstBotName'] = []
    tData['wrong1secondBot'] = []
    tData['wrong1secondBotName'] = []
    tData['wrong1firstAttempts'] = []
    tData['wrong1firstRt'] = []
    tData['wrong1secondAttempts'] = []
    tData['wrong1secondRt'] = []
    for i in range(numPairs*2):
        #tData.trial_order = i+1;
        #trial specific data
        trial = data[trialIndex]
        tData['round1rt'].append(trial['rt'])
        tData['round1bot1'].append(trial['namedWug'])
        tData['round1bot2'].append(trial['otherWug'])
        tData['round1name1'].append(trial['name'])
        tData['round1name2'].append(trial['otherName'])
        tData['round1correct'].append(trial['correct'])
        #if wrong, get learning data
        if(not(trial['correct'])):
            trialIndex=trialIndex+2
            trial = data[trialIndex]
            #get bot order
            if (trial['first']=='named'):
                tData['wrong1firstBot'].append(trial['namedWug'])
                tData['wrong1firstBotName'].append(trial['name'])
                tData['wrong1secondBot'].append(trial['otherWug'])
                tData['wrong1secondBotName'].append(trial['otherName'])
            else:
                tData['wrong1firstBot'].append(trial['otherWug'])
                tData['wrong1firstBotName'].append(trial['otherName'])
                tData['wrong1secondBot'].append(trial['namedWug'])
                tData['wrong1secondBotName'].append(trial['name'])
            botNames[trial['name']] = trial['namedWug']
            botNames[trial['otherName']] = trial['otherWug']
            #get num attempts and rt til correct
            attempts1=0
            rts1 = []
            correct = False
            while (not(correct)):
                rts1.append(trial['rt'])
                attempts1=attempts1+1
                if (trial['answer'] == trial['response']):
                    correct = True
                trialIndex=trialIndex+2
                trial=data[trialIndex]
            tData['wrong1firstAttempts'].append(attempts1)
            tData['wrong1firstRt'].append(rts1)
            #now get num attempts and rt for second bot
            attempts2=0
            rts2 = []
            correct = False
            while (not(correct)):
                rts2.append(trial['rt'])
                attempts2=attempts2+1
                if (trial['answer'] == trial['response']):
                    correct = True
                trialIndex=trialIndex+2
                trial=data[trialIndex]
            tData['wrong1secondAttempts'].append(attempts2)
            tData['wrong1secondRt'].append(rts2)
        else:
            tData['wrong1firstBot'].append(' ')
            tData['wrong1firstBotName'].append(' ')
            tData['wrong1secondBot'].append(' ')
            tData['wrong1secondBotName'].append(' ')
            tData['wrong1firstAttempts'].append(0)
            tData['wrong1firstRt'].append([])
            tData['wrong1secondAttempts'].append(0)
            tData['wrong1secondRt'].append([])
            botNames[trial['name']] = trial['namedWug']
            botNames[trial['otherName']] = trial['otherWug']
            trialIndex = trialIndex+2
    #print('after first trial:')
    #print(trialIndex)
    #memory test between trials 114-129
    #var tDict = tData;
    trial=data[trialIndex]
    memoryNames = []
    memoryBots = []
    memoryResponse = []
    memoryRts = []
    memoryCorrect = []
    #list of names, list of responses, list of correct, list of bots in same order as names
    for i in range(numWugs):
        correctName = trial['name']
        memoryNames.append(correctName)
        memoryBots.append(botNames[correctName])
        memoryResponse.append(trial['name_choices'][trial['response']])
        memoryRts.append(trial['rt'])
        memoryCorrect.append((trial['name_choices'][trial['response']]) == correctName)
        trialIndex=trialIndex+2;#skip feedback
        trial=data[trialIndex]
    tData['memoryNames'] = memoryNames
    tData['memoryBots'] = memoryBots
    tData['memoryResponse'] = memoryResponse
    tData['memoryRts'] = memoryRts
    tData['memoryCorrect'] = memoryCorrect
    tData['numMemoryCorrect'] = sum([r for r in memoryCorrect if r])
    #print('after first memory:')
    #print(trialIndex)
    #second trial
    tData['round2rt'] = []
    tData['round2bot1'] = []
    tData['round2bot2'] = []
    tData['round2name1'] = []
    tData['round2name2'] = []
    tData['round2correct'] = []
    tData['wrong2firstBot'] = []
    tData['wrong2firstBotName'] = []
    tData['wrong2secondBot'] = []
    tData['wrong2secondBotName'] = []
    tData['wrong2firstAttempts'] = []
    tData['wrong2firstRt'] = []
    tData['wrong2secondAttempts'] = []
    tData['wrong2secondRt'] = []
    for i2 in range(numPairs*2):
        #tData.trial_order = i2+i+1;
        #trial specific data
        trial = data[trialIndex]
        tData['round2rt'].append(trial['rt'])
        tData['round2bot1'].append(trial['namedWug'])
        tData['round2bot2'].append(trial['otherWug'])
        tData['round2name1'].append(trial['name'])
        tData['round2name2'].append(trial['otherName'])
        tData['round2correct'].append(trial['correct'])
        #if wrong, get learning data
        if(not(trial['correct'])):
            trialIndex=trialIndex+2
            trial = data[trialIndex]
            #get bot order
            if (trial['first']=='named'):
                tData['wrong2firstBot'].append(trial['namedWug'])
                tData['wrong2firstBotName'].append(trial['name'])
                tData['wrong2secondBot'].append(trial['otherWug'])
                tData['wrong2secondBotName'].append(trial['otherName'])
                botNames[trial['name']] = trial['namedWug']
                botNames[trial['otherName']] = trial['otherWug']
            else:
                tData['wrong2firstBot'].append(trial['otherWug'])
                tData['wrong2firstBotName'].append(trial['otherName'])
                tData['wrong2secondBot'].append(trial['namedWug'])
                tData['wrong2secondBotName'].append(trial['name'])
                botNames[trial['name']] = trial['namedWug']
                botNames[trial['otherName']] = trial['otherWug']
            #get num attempts and rt til correct
            attempts1=0
            rts1 = []
            correct = False
            while (not(correct)):
                rts2.append(trial['rt'])
                attempts1=attempts1+1
                if (trial['answer'] == trial['response']):
                    correct = True
                trialIndex=trialIndex+2
                trial=data[trialIndex]
            tData['wrong2firstAttempts'].append(attempts1)
            tData['wrong2firstRt'].append(rts1)
            #now get num attempts and rt for second bot
            #trialIndex=trialIndex+1
            #trial=data[trialIndex]
            #print(trial)
            attempts2=0
            
            rts2 = []
            correct=False
            while (not(correct)):
                rts2.append(trial['rt'])
                attempts2=attempts2+1
                if (trial['answer'] == trial['response']):
                    correct = True
                trialIndex=trialIndex+2
                trial=data[trialIndex]
            tData['wrong2secondAttempts'].append(attempts2)
            tData['wrong2secondRt'].append(rts2)
        else:
            tData['wrong2firstBot'].append(' ')
            tData['wrong2firstBotName'].append(' ')
            tData['wrong2secondBot'].append(' ')
            tData['wrong2secondBotName'].append(' ')
            tData['wrong2firstAttempts'].append(0)
            tData['wrong2firstRt'].append([])
            tData['wrong2secondAttempts'].append(0)
            tData['wrong2secondRt'].append([])
            trialIndex=trialIndex+2
    #print('after second trial:')
    #print(trialIndex)
    
    #memory test between trials 2-3
    trial=data[trialIndex]
    memoryNames2 = []
    memoryBots2 = []
    memoryResponse2 = []
    memoryRts2 = []
    memoryCorrect2 = []
    #print(botNames)
    #list of names, list of responses, list of correct, list of bots in same order as names
    for i in range(numWugs):
        correctName = trial['name']
        memoryNames2.append(correctName)
        memoryBots2.append(botNames[correctName])
        memoryResponse2.append(trial['name_choices'][trial['response']])
        memoryRts2.append(trial['rt'])
        memoryCorrect2.append((trial['name_choices'][trial['response']]) == correctName)
        trialIndex=trialIndex+2;#skip feedback
        trial=data[trialIndex]
    tData['memoryNames2'] = memoryNames2
    tData['memoryBots2'] = memoryBots2
    tData['memoryResponse2'] = memoryResponse2
    tData['memoryRts2'] = memoryRts2
    tData['memoryCorrect2'] = memoryCorrect2
    tData['numMemoryCorrect2'] = sum([r for r in memoryCorrect2 if r])

    #third trial
    tData['round3rt'] = []
    tData['round3bot1'] = []
    tData['round3bot2'] = []
    tData['round3name1'] = []
    tData['round3name2'] = []
    tData['round3correct'] = []
    tData['wrong3firstBot'] = []
    tData['wrong3firstBotName'] = []
    tData['wrong3secondBot'] = []
    tData['wrong3secondBotName'] = []
    tData['wrong3firstAttempts'] = []
    tData['wrong3firstRt'] = []
    tData['wrong3secondAttempts'] = []
    tData['wrong3secondRt'] = []
    for i2 in range(numPairs*2):
        #trial specific data
        trial = data[trialIndex]
        tData['round3rt'].append(trial['rt'])
        tData['round3bot1'].append(trial['namedWug'])
        tData['round3bot2'].append(trial['otherWug'])
        tData['round3name1'].append(trial['name'])
        tData['round3name2'].append(trial['otherName'])
        tData['round3correct'].append(trial['correct'])
        #if wrong, get learning data
        if(not(trial['correct'])):
            trialIndex=trialIndex+2
            trial = data[trialIndex]
            #get bot order
            if (trial['first']=='named'):
                tData['wrong3firstBot'].append(trial['namedWug'])
                tData['wrong3firstBotName'].append(trial['name'])
                tData['wrong3secondBot'].append(trial['otherWug'])
                tData['wrong3secondBotName'].append(trial['otherName'])
                botNames[trial['name']] = trial['namedWug']
                botNames[trial['otherName']] = trial['otherWug']
            else:
                tData['wrong3firstBot'].append(trial['otherWug'])
                tData['wrong3firstBotName'].append(trial['otherName'])
                tData['wrong3secondBot'].append(trial['namedWug'])
                tData['wrong3secondBotName'].append(trial['name'])
                botNames[trial['name']] = trial['namedWug']
                botNames[trial['otherName']] = trial['otherWug']
            #get num attempts and rt til correct
            attempts1=0
            rts1 = []
            correct = False
            while (not(correct)):
                rts2.append(trial['rt'])
                attempts1=attempts1+1
                if (trial['answer'] == trial['response']):
                    correct = True
                trialIndex=trialIndex+2
                trial=data[trialIndex]
            tData['wrong3firstAttempts'].append(attempts1)
            tData['wrong3firstRt'].append(rts1)
            attempts3=0 
            rts3 = []
            correct=False
            while (not(correct)):
                rts3.append(trial['rt'])
                attempts3=attempts3+1
                if (trial['answer'] == trial['response']):
                    correct = True
                trialIndex=trialIndex+2
                trial=data[trialIndex]
            tData['wrong3secondAttempts'].append(attempts2)
            tData['wrong3secondRt'].append(rts2)
        else:
            tData['wrong3firstBot'].append(' ')
            tData['wrong3firstBotName'].append(' ')
            tData['wrong3secondBot'].append(' ')
            tData['wrong3secondBotName'].append(' ')
            tData['wrong3firstAttempts'].append(0)
            tData['wrong3firstRt'].append([])
            tData['wrong3secondAttempts'].append(0)
            tData['wrong3secondRt'].append([])
            trialIndex=trialIndex+2
    
    #add demo info
    trialIndex=trialIndex+1 #skip instructions
    #print(data[trialIndex])
    demo1 = list(data[trialIndex]['response'].values())
    trialIndex = trialIndex + 1
    demo2 = list(data[trialIndex]['response'].values())
    tData['age'] = demo1[0]
    tData['language'] = demo1[1]
    tData['nationality'] = demo1[2]
    tData['country'] = demo1[3]
    tData['gender'] = demo2[0]
    tData['student'] = demo2[1]
    tData['education'] = demo2[2]
    #print('after demo:')
    #print(trialIndex)

    #generations
    trialIndex = trialIndex + 3
    trial=data[trialIndex]
    gen = []
    genRts = []
    while(trial['trial_type'] == 'survey-text'):
        if('response' in trial):
            res = trial['response']
            gen.append(list(res.values())[0])
            genRts.append(trial['rt'])
        trialIndex=trialIndex+1
        trial=data[trialIndex]
    tData['generations'] = gen
    tData['generationRts'] = genRts
    #print('after gen:')
    #print(trialIndex)
    
    #finally, memory test
    trialIndex=trialIndex+1#skip instructions
    trial=data[trialIndex]
    memoryNames3 = []
    memoryBots3 = []
    memoryResponse3 = []
    memoryRts3 = []
    memoryCorrect3 = []
    #list of names, list of responses, list of correct, list of bots in same order as names
    while(trial['trial_type'] == 'canvas-button-response'):
        #print(trial)
        correctName = trial['name']
        memoryNames3.append(correctName)
        memoryBots3.append(botNames[correctName])
        memoryResponse3.append(trial['name_choices'][trial['response']])
        memoryRts3.append(trial['rt'])
        memoryCorrect3.append((trial['name_choices'][trial['response']]) == correctName)
        trialIndex=trialIndex+1
        trial=data[trialIndex]
    tData['memoryNames3'] = memoryNames3
    tData['memoryBots3'] = memoryBots3
    tData['memoryResponse3'] = memoryResponse3
    tData['memoryRts3'] = memoryRts3
    tData['memoryCorrect3'] = memoryCorrect3
    tData['numMemoryCorrect3'] = sum([r for r in memoryCorrect3 if r])
    for k,v in tData.items():
        if type(v)!=str:
            tData[k] = repr(v)
    return tData

#print(reformatData(d))








"""
export function makeQuery(data) {
    data = json.parse(json.stringify(data));
    console.log('Parsing data');
    data = reformatData(data);
    console.log('done');
    var table = 'robots';
    var keys = '';
    var keyArr = Object.keys(data[0]);
    for(var i=0; i<keyArr.length; i++) {
        keys = keys.concat(keyArr[i] + ", ");
    }
    keys = "(" + keys.substring(0, keys.length-2) + ")";
    var valuesList = [];
    var x = 0;
    for(var i=0; i<data.length; i++) {
        var dict = data[i];
        valuesList[x] = "";
        var valArray = Object.values(dict);
        for(var j=0; j<valArray.length; j++) {
            valuesList[x] = valuesList[x].concat("'" + valArray[j] + "', ");
        }
        x++;
    }
    var valuesStr = "";
    for (var i=0; i<valuesList.length; i++) {
        var values = valuesList[i];
        values = "(" + values.substring(0, values.length-2) + ")";
        valuesStr = valuesStr + values + ", ";
    }
    valuesStr = valuesStr.substring(0, valuesStr.length-2);
    console.log("INSERT INTO " + table + keys + " " + "VALUES " + valuesStr + ";");
    return "INSERT INTO " + table + keys + " " + "VALUES " + valuesStr + ";";
}
"""