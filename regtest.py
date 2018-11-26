import re

# line = 'bobby123'
# regex_str = "(bobby|bobby123)"
# regex_str = "([abcd]obby123)"

line = '131223454567'
regex_str = "(1[4835][0-9][^1]{9})"
"""
中括号用法
    1. 表示某一个值
    2. 表示某个范围
    3. [^1]不等于 1
    4. [.*] . 和 * 不再有特殊含义了
"""

"""
\s 空格
\S
"""
line1 = "你 好"
regex_str1 = "(你\s好)"

"""
[A-Za-z0-9]
"""
match_obj = re.match(regex_str, line)

if match_obj:
    print(match_obj.group(1))