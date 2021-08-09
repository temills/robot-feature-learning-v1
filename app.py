from flask import Flask, render_template, request, make_response, session
import os
from flask_sqlalchemy import SQLAlchemy
import datetime
import json

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models


class Subject(db.Model):
    __tablename__ = 'subjects'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    jspsychID = db.Column(db.String, unique=True)
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
    rt_1 = db.Column(db.Float)
    rt_2 = db.Column(db.Float)
    trial_rt = db.Column(db.Float)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'))

    def __repr__(self):
        return '<Subject %r>' % self.id


# Views
@app.route('/', methods=['GET', 'POST'])
def intro():
    if request.method == 'GET':
        return render_template('intro.html')
    if request.method == 'POST':
        d = request.get_json()[1]
        subj = Subject(jspsychID=d['subjectID'], date=datetime.datetime.now())
        db.session.add(subj)
        db.session.commit()
        return make_response("", 200)


@app.route('/experiment', methods=['POST', 'GET'])
def experiment():
    if request.method == 'GET':
        return render_template('experiment.html')
    if request.method == 'POST':
        d = request.get_json(force=True)[0]
        vid = d['stimulus'][0].split('/')[2]
        agent = False
        outcome = False
        cf = False
        if 'a' in vid:
            agent = True
        if vid.split('_')[1] == 'in':
            outcome = True
        if vid.split('_')[2] == 'in':
            cf = True

        subj = Subject.query.filter_by(jspsychID=d['subjectID']).first()

        trial_dat = Trial(trial_num=d['trial_index'],
                          jspsychID=d['subjectID'],
                          stimulus=d['stimulus'][0],
                          agent=agent,
                          time_elapse=d['time_elapsed'],
                          stim_outcome=outcome,
                          stim_cf=cf,
                          cause_resp=d['response_1'],
                          cf_resp=d['response_2'],
                          rt_1=d['rt_1'],
                          rt_2=d['rt_2'],
                          trial_rt=d['rt'],
                          subject_id=subj.id)
        db.session.add(trial_dat)
        db.session.commit()
        return make_response("", 200)



if __name__ == '__main__':
    app.run()
