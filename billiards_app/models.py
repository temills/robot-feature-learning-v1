from . import db


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


class Trial(db.Model):
    __tablename__ = 'trials'
    id = db.Column(db.Integer, primary_key=True)
    trial_num = db.Column(db.Integer)
    jspsychID = db.Column(db.String)
    stimulus = db.Column(db.String)
    agent = db.Column(db.Boolean)
    time_elapse = db.Column(db.Float)
    stim_outcome = db.Column(db.Boolean)
    stim_cf = db.Column(db.Boolean)
    cause_resp = db.Column(db.Integer)
    cf_resp = db.Column(db.Integer)
    agent_resp = db.Column(db.Integer)
    rt_1 = db.Column(db.Float)
    rt_2 = db.Column(db.Float)
    rt_3 = db.Column(db.Float)
    trial_rt = db.Column(db.Float)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'))

    def __repr__(self):
        return '<Subject %r>' % self.id

