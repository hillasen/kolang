from function import function_manager
from base import variable
from library import parser, builder

b_i = builder.Builder()

code = "만약(\"헬로\"==\"헬로\"){ console.log(\"안녕\")}"
print(parser.code_parser(code))
print(b_i.startRun(parser.code_parser(code)))


