from collections import defaultdict
from codename import codename
import random

counts = defaultdict(lambda: 0)
for i in range (0, 2760*1000):
  val = random.randint(0, 999999999999)
  res = codename(val, 1, 3, '', True)
  #print "%s %s" % (val, res)
  counts[res] = counts[res] + 1
  
for k,v in counts.items():
  print "%s %s" % (k, v)
  
  
   