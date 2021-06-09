import re
import random
from datetime import datetime
regex = re.compile('( *- )(@bot)(.*)')
candidates = ['@bot', '@Bot', '@bOt', '@boT', '@bOT', '@BoT', '@BOt', '@BOT']
random.seed(datetime.now())

f = open('nlu.yml', 'r')
lines = f.readlines()
f.close()

res = ''
for line in lines:
    m = regex.match(line)
    s = ''
    if (m):
        prefix = candidates[int(random.random() * 8)]
        res += m.group(1) + prefix + m.group(3) + '\n'
    else:
        res += line
        

wf = open('nlu_bak.yml', 'w')
wf.write(res)
wf.close()

