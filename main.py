from function import function_manager
from base import variable
from library import parser, builder

b_i = builder.Builder()

f = open("hello.kol", 'r')
code = f.read()
f.close()
#code = "함수 안녕(){} \n 변수 = 1 \n만약(\"헬로\"==\"헬로\"){ \n 출력하기(변수_1)\n}"
#print(parser.code_parser(code))
compiled_code = b_i.startRun(parser.code_parser(code))
print(compiled_code)


f = open("hello.js", 'w')
f.write(compiled_code)
f.close()