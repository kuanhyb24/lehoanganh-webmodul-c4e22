from poll import Poll
import mlab

# 1. connect4
mlab.connect()

# 2. read all
poll_list = Poll.objects() #page, lazy, loading
for p in poll_list:
    print(p.question)
    print(p.options)
    print(p.code)
    print("************")