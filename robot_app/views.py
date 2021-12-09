from flask import render_template, request, make_response, session
from . import app, db
from .models import Trial
from .parseData import reformatData
import datetime
import json


# Views
#@app.route('/botstudy', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def experiment():
    if request.method == 'GET':
        return render_template('experiment.html')
    if request.method == 'POST':
        data = request.get_json(force=True)
        tdata = reformatData(data)
        print(tdata)
        trial = Trial(subject_id=tdata['subject_id'], turk_code = tdata['turk_code'], usefulFt1 = tdata['usefulFt1'], usefulFt2 = tdata['usefulFt2'], favoredEnd1 = tdata['favoredEnd1'], favoredEnd2 = tdata['favoredEnd2'], round1rt = tdata['round1rt'], round1bot1 = tdata['round1bot1'], round1bot2 = tdata['round1bot2'], round1name1 = tdata['round1name1'], round1name2 = tdata['round1name2'], round1correct = tdata['round1correct'], wrong1firstBot = tdata['wrong1firstBot'], wrong1firstBotName = tdata['wrong1firstBotName'], wrong1secondBot = tdata['wrong1secondBot'], wrong1secondBotName = tdata['wrong1secondBotName'], wrong1firstAttempts = tdata['wrong1firstAttempts'], wrong1secondAttempts = tdata['wrong1secondAttempts'], wrong1firstRt = tdata['wrong1firstRt'], wrong1secondRt = tdata['wrong1secondRt'], numMemoryCorrect = tdata['numMemoryCorrect'], memoryNames = tdata['memoryNames'], memoryBots = tdata['memoryBots'], memoryResponse = tdata['memoryResponse'], memoryRts = tdata['memoryRts'], memoryCorrect = tdata['memoryCorrect'], round2rt = tdata['round2rt'], round2bot1 = tdata['round2bot1'], round2bot2 = tdata['round2bot2'], round2name1 = tdata['round2name1'], round2name2 = tdata['round2name2'], wrong2firstBot = tdata['wrong2firstBot'], wrong2firstBotName = tdata['wrong2firstBotName'], wrong2secondBot = tdata['wrong2secondBot'], wrong2secondBotName = tdata['wrong2secondBotName'], wrong2firstAttempts = tdata['wrong2firstAttempts'], wrong2firstRt = tdata['wrong2firstRt'], wrong2secondAttempts = tdata['wrong2secondAttempts'], wrong2secondRt = tdata['wrong2secondRt'], memoryNames2 = tdata['memoryNames2'], memoryBots2 = tdata['memoryBots2'], memoryCorrect2 = tdata['memoryCorrect2'], memoryResponse2 = tdata['memoryResponse2'], memoryRts2 = tdata['memoryRts2'], numMemoryCorrect2 = tdata['numMemoryCorrect2'], round3rt = tdata['round3rt'], round3bot1 = tdata['round3bot1'], round3bot2 = tdata['round3bot2'], round3name1 = tdata['round3name1'], round3name2 = tdata['round3name2'], wrong3firstBot = tdata['wrong3firstBot'], wrong3firstBotName = tdata['wrong3firstBotName'], wrong3secondBot = tdata['wrong3secondBot'], wrong3secondBotName = tdata['wrong3secondBotName'], wrong3firstAttempts = tdata['wrong3firstAttempts'], wrong3firstRt = tdata['wrong3firstRt'], wrong3secondAttempts = tdata['wrong3secondAttempts'], wrong3secondRt = tdata['wrong3secondRt'], age = tdata['age'], language = tdata['language'], nationality = tdata['nationality'], country = tdata['country'], gender = tdata['gender'], student = tdata['student'], education = tdata['education'], generations = tdata['generations'], generationRts = tdata['generationRts'], memoryNames3 = tdata['memoryNames3'], memoryBots3 = tdata['memoryBots3'], memoryCorrect3 = tdata['memoryCorrect3'], memoryResponse3 = tdata['memoryResponse3'], memoryRts3 = tdata['memoryRts3'], numMemoryCorrect3 = tdata['numMemoryCorrect3'])
        #db.session.add(trial)
        #db.session.commit()
        return make_response("", 200)
        

