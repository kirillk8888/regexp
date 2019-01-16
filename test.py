import re
from regexp import calculate


def findall(regexp):
    text = """a=1a=+1a=-1a=ba=b+100a=b-100b+=10b+=+10b+=-10b+=bb+=b+100b+=b-100c-=101c-=+101c-=-101c-=bc-=b+101c-=b-101"""

    return re.findall(regexp, text)


result = calculate({'a': 1, 'b': 2, 'c': 3}, findall)
correct = {"a": -98, "b": 196, "c": -686}
if result == correct:
    print ("Correct")
else:
    print ("Incorrect: %s != %s" % (result, correct))
