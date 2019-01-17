#coding=utf-8

name = str(input("输入姓名："))
hight = input("身高:米")
isinstance(hight,float)
if True:
    pass
    while False:
        print("请重新输入数字")
        hight = float(input("身高:米"))

weight = float(input("体重:"))
BMI = weight / (hight ** 2)
#BMI = float(input(isinstance("体重:",(int,float))))/(float(input(isinstance("身高:",(int,float))))**2)    #计算BMI值；
BMImodel = ['BMI标准如下:',
'==========================',
'BMI <= 18.5 体重过轻',
'BMI <= 25 体重正常',
'BMI <= 28 体重过重',
'BMI <= 32 体重肥胖',
'BMI > 32 严重肥胖',
'==========================']
for model in BMImodel:
    print(model)    #输出BMI对照表；
if 	BMI <= 18.5:
    print("%s 您的体重"%name,"过轻!!")
elif BMI <= 25:
    print("%s 您的体重"%name,"正常~")
elif BMI <= 28:
    print("%s 您的体重"%name,"过重!")
elif BMI <= 32:
    print("%s 您的体重"%name,"肥胖!!")
elif BMI > 32:
    print("%s 您的体重"%name,"严重肥胖!!!")
