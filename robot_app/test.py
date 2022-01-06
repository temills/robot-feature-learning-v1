#!/usr/bin/env python3

from parseData import *

data = {"data":[{"rt":1346.5799999999035,"stimulus":"<h4>Please consider this information carefully before deciding whether to participate in this research.</h4><h4>The purpose of this research is to examine how people consider possibilities. We are simply interested in your thought process. The study will take less than 10 minutes to complete, and you will receive $2.00 on Amazon Mechanical Turk. There are no anticipated risks associated with participating in this study. The effects of participating should be comparable to those you would ordinarily experience from viewing a computer monitor and using a mouse or keyboard for a similar amount of time.</h4> <h4>Your participation in this study is completely voluntary and you may refuse to participate or you may choose to withdraw at any time without penalty or loss of benefits to which you are otherwise entitled. Your participation in this study will remain confidential. No personally identifiable information will be associated with your data. Also, all analyses of the data will be averaged across all the participants, so your individual responses will never be specifically analyzed. </h4> <h4>Agreement: The nature and purpose of this research have been sufficiently explained and I agree to participate in this study. I understand that I am free to withdraw at any time without incurring any penalty. Please consent by clicking the button below to continue. Otherwise, please exit the study at this time.</h4>","button_pressed":"0","trial_type":"html-button-response","trial_index":0,"time_elapsed":1372,"internal_node_id":"0.0-0.0"}]}

print(reformatData(data))