'''
1. จงเขียน regular expression ที่ match กับข้อความต่อไปนี้
"pit, spot, spate, slap two, respit" 
แต่ไม่ match กับข้อความเหล่านี้ "pt, Pot, part, respect, populate" 
'''
import re
txt = "pit spot spate slap two respit pt Pot part respect populate"
pattern = '.*p[aeiou| ]t'
ans = re.match(pattern, txt)
print(ans)