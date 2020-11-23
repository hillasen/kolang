from function import function_manager
from base import variable
from library import parser, builder

b_i = builder.Builder()

code = "변수 변수_1 = 1 \n만약(\"헬로\"==\"헬로\"){ \n 출력하기(변수_1)\n}"
#print(parser.code_parser(code))
print(b_i.startRun(parser.code_parser(code)))


