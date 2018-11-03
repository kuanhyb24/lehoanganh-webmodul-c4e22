from poll import Poll
from random import choice # từ ... lấy ra ...
import mlab

# 1. connect to database
mlab.connect()

# 2.prepare data
q = "Hackathon ăn gì?"
opts = [
    "pizza"
    "bánh mì"
    "phở xào"
]
alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
c = ""
for _ in range(6):
    c+= choice(alphabet)
print(c)
# 3. create document
p = Poll(question=q, option=opts, code=c)

#  4. save
p.save()