from flask import render_template, request, make_response
from . import app, db
from .models import Subject, Trial
import datetime



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
        return render_template('templates/experiment.html')
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



#if __name__ == '__main__':
#    app.run()
