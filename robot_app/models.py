from . import db

#need secret code at end of experiment?
#do they have a prolific id?

#not using this
"""
class Subject(db.Model):
    __tablename__ = 'subjects'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    jspsychID = db.Column(db.String, unique=True)
    prolificID = db.Column(db.String)
    completion = db.Column(db.Boolean)
    trials = db.relationship('Trial', backref='subject', lazy='dynamic', cascade="all, delete-orphan")

    def __repr__(self):
        return '<Subject %r>' % self.id
"""

class Trial(db.Model):
    __tablename__ = 'trials'
    
    subject_id = db.Column(db.String, primary_key=True)
    turk_code = db.Column(db.String)
    
    usefulFt1 = db.Column(db.String)
    usefulFt2 = db.Column(db.String)
    favoredEnd1 = db.Column(db.String)
    favoredEnd2 = db.Column(db.String)
    
    round1rt = db.Column(db.String)
    round1bot1 = db.Column(db.String)
    round1bot2 = db.Column(db.String)
    round1name1 = db.Column(db.String)
    round1name2 = db.Column(db.String)
    round1correct = db.Column(db.String)
    wrong1firstBot = db.Column(db.String)
    wrong1firstBotName = db.Column(db.String)
    wrong1secondBot = db.Column(db.String)
    wrong1secondBotName = db.Column(db.String)
    wrong1firstAttempts = db.Column(db.String)
    wrong1secondAttempts = db.Column(db.String)
    wrong1firstRt = db.Column(db.String)
    wrong1secondRt = db.Column(db.String)
    
    memoryNames = db.Column(db.String)
    memoryBots = db.Column(db.String)
    memoryResponse = db.Column(db.String)
    memoryRts = db.Column(db.String)
    memoryCorrect = db.Column(db.String)
    numMemoryCorrect = db.Column(db.String)
    
    round2rt = db.Column(db.String)
    round2bot1 = db.Column(db.String)
    round2bot2 = db.Column(db.String)
    round2name1 = db.Column(db.String)
    round2name2 = db.Column(db.String)
    wrong2firstBot = db.Column(db.String)
    wrong2firstBotName = db.Column(db.String)
    wrong2secondBot = db.Column(db.String)
    wrong2secondBotName = db.Column(db.String)
    wrong2firstAttempts = db.Column(db.String)
    wrong2firstRt = db.Column(db.String)
    wrong2secondAttempts = db.Column(db.String)
    wrong2secondRt = db.Column(db.String)
    
    memoryNames2 = db.Column(db.String)
    memoryBots2 = db.Column(db.String)
    memoryResponse2 = db.Column(db.String)
    memoryRts2 = db.Column(db.String)
    memoryCorrect2 = db.Column(db.String)
    numMemoryCorrect2 = db.Column(db.String)

    round3rt = db.Column(db.String)
    round3bot1 = db.Column(db.String)
    round3bot2 = db.Column(db.String)
    round3name1 = db.Column(db.String)
    round3name2 = db.Column(db.String)
    round3correct = db.Column(db.String)
    wrong3firstBot = db.Column(db.String)
    wrong3firstBotName = db.Column(db.String)
    wrong3secondBot = db.Column(db.String)
    wrong3secondBotName = db.Column(db.String)
    wrong3firstAttempts = db.Column(db.String)
    wrong3secondAttempts = db.Column(db.String)
    wrong3firstRt = db.Column(db.String)
    wrong3secondRt = db.Column(db.String)
    
    age = db.Column(db.String)
    language = db.Column(db.String)
    nationality = db.Column(db.String)
    country = db.Column(db.String)
    gender = db.Column(db.String)
    student = db.Column(db.String)
    education = db.Column(db.String)
    
    generations = db.Column(db.String)
    generationRts = db.Column(db.String)
    
    memoryResponse3 = db.Column(db.String)
    memoryRts3 = db.Column(db.String)
    numMemoryCorrect3 = db.Column(db.String)
    memoryNames3 = db.Column(db.String)
    memoryBots3 = db.Column(db.String)
    memoryCorrect3 = db.Column(db.String)

    def __repr__(self):
        return '<Subject %r>' % self.id

