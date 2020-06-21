from sklearn.linear_model import LinearRegression
import numpy as np
from matplotlib import pyplot
import sqlite3
import pandas as pd
def mean(tupe):

    famn = 0
    for add in tupe[0:]:
        famn = int(famn) + int(add)
    numper=len(tupe)
    val=int(float(famn))/int(float(numper))
    return val
########### math with gender
##
def google_student_data(name_of_sub):
    total_result=[]
    fig = pyplot.figure()
    total_result.append(name_of_sub)

    deg_math_male=[]
    deg_math_female=[]
    ax1 = fig.add_subplot(111)
    fig.suptitle('{} with gender'.format(name_of_sub), fontsize=16)
    ax1.set_xlabel("gender")
    con=sqlite3.connect("..\\dataset\\student.db")
    exe=con.cursor()
#study of math degree
    exe.execute("SELECT {},gender FROM students ".format(name_of_sub))
    for math_dg in exe.fetchall():
        if math_dg[1]=="female":
            deg_math_female.append(int(float(math_dg[0])))
        if math_dg[1]=="male":
            deg_math_male.append(int(float(math_dg[0])))
    con.close()

    con=sqlite3.connect("..\\dataset\\student.db")
    exe=con.cursor()
#study of math degree
#اmean of female
    famn=0
    for add in deg_math_female[0:]:
        famn=int(famn)+int(add)

    maln=0
    for add2 in deg_math_male[0:]:
        maln=int(maln)+int(add2)
    mean_fm=int(famn/len(deg_math_female))
    mean_man=int(maln/len(deg_math_male))
    if float(mean_fm) > float(mean_man):
        total_result.append("female")
    else:
        total_result.append("male")

    x=["male \n {}".format(mean_man),"female \n {}".format(mean_fm)]
    y=[mean_man,mean_fm]
    ax1.set_ylabel("{} degree".format(name_of_sub))
    pl=ax1.bar(x,y)

###########################################################################################
####################
#####################
#### math with group
########### math with group
    fig2= pyplot.figure()
    group_a=[]
    group_b=[]
    group_c=[]
    group_d=[]
    group_e=[]

    ax2 = fig2.add_subplot(211)
    math=[]
    group=[]
    con=sqlite3.connect("..\\dataset\\student.db")
    exe=con.cursor()
    #study of math degree
    exe.execute("SELECT {},race FROM students".format(name_of_sub))
    for math_dg in exe.fetchall():
        if math_dg[1] == "group A":
            group_a.append(int(float(math_dg[0])))
        if math_dg[1] == "group B":
            group_b.append(int(float(math_dg[0])))
        if math_dg[1] == "group C":
            group_c.append(int(float(math_dg[0])))
        if math_dg[1] == "group D":
            group_d.append(int(float(math_dg[0])))
        if math_dg[1] == "group E":
            group_e.append(int(float(math_dg[0])))
#mean1
    gr_1=mean(group_a)
    gr_2=mean(group_b)
    gr_3=mean(group_c)
    gr_4=mean(group_d)
    gr_5=mean(group_e)
    con.close()
    dg_mean=[gr_1,gr_2,gr_3,gr_4,gr_5]
    total_result.append(max(dg_mean))
    classes=["A \n {}".format(gr_1),"B \n {}".format(gr_2),"C \n {}".format(gr_3),"D \n {}".format(gr_4),"E \n {}".format(gr_5)]
    pl=ax2.bar(classes,dg_mean)
    ax2.set_title("{} with group ".format(name_of_sub))
######
#########
######### math with lunch

    fig3= pyplot.figure()
    group_a=[]
    group_b=[]

    ax3 = fig3.add_subplot(211)
    math=[]
    group=[]
    con=sqlite3.connect("..\\dataset\\student.db")
    exe=con.cursor()
#study of math degree
    exe.execute("SELECT {},launch FROM students".format(name_of_sub))
    for math_dg in exe.fetchall():
        if math_dg[1] == "standard":
            group_a.append(int(float(math_dg[0])))
        if math_dg[1] == "free/reduced":
            group_b.append(int(float(math_dg[0])))

#mean1
    gr_1=mean(group_a)
    gr_2=mean(group_b)
    if gr_1>gr_2:
        total_result.append("standard")
    else:
        total_result.append("free/reduced")
    con.close()
    dg_mean=[gr_1,gr_2]
    classes=["standard \n {}".format(gr_1),"free/reduced \n {}".format(gr_2)]
    pl=ax3.bar(classes,dg_mean)
    ax3.set_title("{} with lunch ".format(name_of_sub))
    ######
    #########
    ######### math with test preparation


    fig4= pyplot.figure()
    group_a=[]
    group_b=[]

    ax4 = fig4.add_subplot(211)
    math=[]
    group=[]
    con=sqlite3.connect("..\\dataset\\student.db")
    exe=con.cursor()
    #study of math degree
    exe.execute("SELECT {},test_prep FROM students".format(name_of_sub))
    for math_dg in exe.fetchall():
        if math_dg[1] == "completed":
            group_a.append(int(float(math_dg[0])))
        if math_dg[1] == "none":
            group_b.append(int(float(math_dg[0])))
    if gr_1>gr_2:
        total_result.append("completed")
    else:
        total_result.append("none")
    #mean1
    gr_1=mean(group_a)
    gr_2=mean(group_b)

    con.close()
    dg_mean=[gr_1,gr_2]
    classes=["completed \n {}".format(gr_1),"none \n {}".format(gr_2)]
    pl=ax4.bar(classes,dg_mean)
    ax4.set_title("{} with test preparation ".format(name_of_sub))

    ##################
    ################
    ###############math with education

    fig5= pyplot.figure()
    group_a=[]
    group_b=[]
    group_c=[]
    group_d=[]
    group_e=[]
    group_f=[]

    ax5 = fig5.add_subplot(211)
    math=[]
    group=[]
    con=sqlite3.connect("..\\dataset\\student.db")
    exe=con.cursor()
    #study of math degree
    exe.execute("SELECT {},eductation FROM students".format(name_of_sub))
    for math_dg in exe.fetchall():
        if math_dg[1] == "some high school":
            group_a.append(int(float(math_dg[0])))
        if math_dg[1] == "some college":
            group_b.append(int(float(math_dg[0])))
        if math_dg[1] == "master's degree":
            group_c.append(int(float(math_dg[0])))
        if math_dg[1] == "high school":
            group_d.append(int(float(math_dg[0])))
        if math_dg[1] == "bachelor's degree":
            group_e.append(int(float(math_dg[0])))
        if math_dg[1] == "associate's degree":
            group_f.append(int(float(math_dg[0])))
    #mean1

    gr_1=mean(group_a)
    gr_2=mean(group_b)
    gr_3=mean(group_c)
    gr_4=mean(group_d)
    gr_5=mean(group_e)
    gr_6=mean(group_f)
    con.close()
    dg_mean=[gr_1,gr_2,gr_3,gr_4,gr_5,gr_6]
    total_result.append(max(dg_mean))


    classes=["some high school \n {}".format(gr_1),"some college\n {}".format(gr_2),"master's degree\n {}".format(gr_3),"high school\n {}".format(gr_4),"bachelor's degree\n {}".format(gr_5),"associate's degree\n {}".format(gr_6)]
    pl=ax5.bar(classes,dg_mean)
    ax5.set_title("{} with education lvl ".format(name_of_sub))
    pyplot.show()
    return total_result