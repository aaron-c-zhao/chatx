import re
import random
from datetime import datetime
regex = re.compile('- (.*)')
# candidates = ['@bot', '@Bot', '@bOt', '@boT', '@bOT', '@BoT', '@BOt', '@BOT']
candidates = ['@', '@b', '@ ', '@b ', '@B ', '@B', '@bo', '@bo ', '@bt', '@BT ', '@Bt', '@Bo ', '@bO', '@oT', '@ot ']
random.seed(datetime.now())

f = open('text.txt', 'r')
lines = f.readlines()
f.close()

res = ''
for line in lines:
    m = regex.match(line)
    s = ''
    if (m):
        prefix = candidates[int(random.random() * 15)]
        res += '- ' + prefix + m.group(1) + '\n'
    else:
        res += line
        

wf = open('nlu_bak.yml', 'w')
wf.write(res)
wf.close()

