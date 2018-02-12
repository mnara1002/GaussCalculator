#coding:utf8
from GaussCal import gausscal
from __builtin__ import int
print("1～nまでの和で求めたい範囲を指定してください。")
input_num = raw_input()

sum = gausscal(int(input_num))

print "1から%sまでのすべての和は、%dです" % (input_num,sum)

