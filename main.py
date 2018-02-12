#coding:utf8
from GaussCal import gausscal
from __builtin__ import int
print("何日後の貯金額が知りたいですか？1以上の正の数で入力してください")
input_num = raw_input()
sum = gausscal(int(input_num)) #gausscal関数に入力した値をint型で渡し、戻り値を変数sumに代入する
print "%s日後の貯金額は、%d円です" % (input_num,sum) #結果を表示する。変数input_numはstr型であるため、%sで出力させている