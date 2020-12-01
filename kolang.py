from function import function_manager
from base import variable
from library import parser, builder
import sys


b_i = builder.Builder()

f = open(sys.argv[1], 'r')
code = f.read()
f.close()



compiled_code = b_i.startRun(parser.code_parser(code))
#print(compiled_code)


f = open(sys.argv[2], 'w')
f.write(compiled_code)
f.close()
print("Finish")
print(sys.argv[1] + " --> " + sys.argv[2])