
Stu=[]
def main():
    while True:
        MenuOutput()
        key=input('请输入功能对应字母:')
        if key=='A':
            AddStudent()
        elif key=='D':
            Display()





def MenuOutput():  
    print('主菜单')
    print('A.添加学生')
    print('B.删除学生')
    print('C.修改学生')
    print('D.显示所有学生信息')
    print('E.退出系统')

def AddStudent():
    new_name=input('请输入新学生的名字:')
    new_class=input('请输入新学生的班级')
    new_information={}
    new_information['name']=new_name
    new_information['class']=new_class
    new_information['math']=0
    new_information['chinese']=0
    new_information['english']=0
    new_information['computer']=0
    Stu.append(new_information)

def Display():
    print('学生信息如下:')
    i=1
    for temp in Stu:
        print('编号%d 姓名%s 班级%s 数学成绩%d 语文成绩%d 英语成绩%d 专业成绩%d'%(i,temp['name'],temp['class'],temp['math'],temp['chinese'],temp['english'],temp['computer']))
        i=i+1
