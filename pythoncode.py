from tkinter import *
def show1(val):
    g.set(val)
def show2(val):
    w.set(val)
def show3(val):
    h.set(val)
def show4(val):
    b1.set(val)
    if b1.get()>=70 and b1.get()<=90:
        slider4.configure(from_=40,to=60)
    if b1.get()>90 and b1.get()<=120:
        slider4.configure(from_=61,to=80)
    if b1.get()>120:
        slider4.configure(from_=81,to=120)
def show5(val):
    b2.set(val)

def report():
    root3=Tk()
    #for gender
    if v.get()==1:
        m="Male"
    else:
        m="Female"
    #for BMI
    z=IntVar()
    a=w.get()
    b=h.get()
    b=b*((10)**(-2))
    b=b*b
    z=a/b
    s=StringVar()
    if z<18.5:
        s="Underweight"
    elif z<25:
        s="Normal Weight"
    elif z<30:
        s="Overweight"
    elif z<35:
        s="Grade I Obesity"
    elif z<=40:
        s="Grade II Obesity"
    else:
        if z>40:
            s="Grade III Obesity"
    #BP
    if b1.get()<=90:
        BB="Low"
    elif b1.get()>90 and b1.get()<=120:
        BB="Normal"
    else:
        BB="High"
    #hb
    c1=hb1.get()
    if v.get()==1:
        #male
        if c1>=14 and c1<=18:
            c2="Normal"
        elif c1<14:
            c2="Low"
        else:
            c2="high"
    else:
        #female
        if c1>=12 and c1<=16:
            c2="Normal"
        elif c1<12:
            c2="Low"
        else:
            c2="high"
    #pulse rate
    if p1.get()>=60 and p1.get()<=100:
        c3="Normal"
    elif p1.get()<60:
        c3="Low"
    else:
        c3="High"
    #chalestrol
    if ch1.get()<100:
        c4="Optimal"
    elif ch1.get()>=100 and ch1.get()<=129:
        c4="Near Optimal/above Optimal"
    elif ch1.get()>=130 and ch1.get()<=159:
        c4="Borderline High"
    elif ch1.get()>=160 and ch1.get()<=189:
        c4="High"
    else:
        c4="Very High"
    #platelets
    if pl.get()>=150000 and pl.get()<=450000:
        c5="Normal"
    elif pl.get()>450000:
        c5="Thrombocytosis"
    else:
        c5="Thrombocytopenia"
    #wbc
    if wbc1.get()>=4000 and wbc1.get()<=11000:
        c6="Normal"
    elif wbc1.get()<4000:
        c6="Low"
    else:
        c6="High"
        
    #rbc
    M=10**6
    if v.get()==1:
        #male
        if rbc1.get()<4.7*M:
            c7="Low"
        elif rbc1.get()<=6.1*M:
            c7="Normal"
        else:
            c7="high"
    else:
        #female
        if rbc1.get()<4.2*M:
            c7="Low"
        elif rbc1.get()<=5.4*M:
            c7="Normal"
        else:
            c7="high"
    
    l1=Label(root3,text="Report").grid(row=0,column=0)
    l2=Label(root3,text="name").grid(row=1,column=10)
    l3=Label(root3,text=n.get()).grid(row=1,column=12)
    l4=Label(root3,text="Gender").grid(row=2,column=10)
    l5=Label(root3,text=m).grid(row=2,column=12)
    l6=Label(root3,text="BMI").grid(row=3,column=10)
    l7=Label(root3,text=s).grid(row=3,column=12)
    l8=Label(root3,text="BP").grid(row=4,column=10)
    l9=Label(root3,text=BB).grid(row=4,column=12)
    l10=Label(root3,text="Pulse Rate").grid(row=5,column=10)
    l11=Label(root3,text=c3).grid(row=5,column=12)
    l12=Label(root3,text="WBC").grid(row=6,column=10)
    l13=Label(root3,text=c6).grid(row=6,column=12)
    l12=Label(root3,text="RBC").grid(row=7,column=10)
    l15=Label(root3,text=c7).grid(row=7,column=12)
    l16=Label(root3,text="Platelets").grid(row=8,column=10)
    l17=Label(root3,text=c5).grid(row=8,column=12)
    l18=Label(root3,text="HB").grid(row=9,column=10)
    l19=Label(root3,text=c2).grid(row=9,column=12)
    l20=Label(root3,text="Cholestrol").grid(row=10,column=10)
    l21=Label(root3,text=c4).grid(row=10,column=12)
    
    root3.mainloop()
    
    
root1=Tk()
#frames
frame0=Frame(root1)
frame1=Frame(root1)
frame2=Frame(root1)
frame3=Frame(root1)
frame4=Frame(root1)
frame5=Frame(root1)


t=Label(frame0,text='fiTneSS_cALcULATOr',fg='green')
t.configure(font='impact 20 bold')

#name
name=Label(frame1,text='Name')
n=StringVar()
n.set("Shailendra Sahu")
ename=Entry(frame1,textvariable=n)
g=IntVar()
g.set(18)
age=Label(frame1,text='Age')
eage=Entry(frame1,textvariable=g)
slider_age=Scale(frame1, from_=18, to=100, orient=HORIZONTAL,showvalue=NO,command=show1,length=130)
gender=Label(frame1,text="Gender")
v=IntVar()
v.set(1)
r1=Radiobutton(frame1,text="Male",value=1,variable=v)
r2=Radiobutton(frame1,text="Female",value=2,variable=v)



#weight
weight=Label(frame1,text='Weight(in Kg)')
w=IntVar()
w.set(60)
e1=Entry(frame1,textvariable=w)
slider1= Scale(frame1, from_=1, to=300, orient=HORIZONTAL,showvalue=NO,command=show2,length=130)

#height
height=Label(frame1,text='Height(in cms)')
h=IntVar()
h.set(170)
e2=Entry(frame1,textvariable=h)
slider2= Scale(frame1, from_=10, to=200, orient=HORIZONTAL,showvalue=NO,command=show3,length=130)

#blood
bpu=Label(frame1,text="BP Upper(in mmHg)")
b1=IntVar()
b1.set(120)
ebpu=Entry(frame1,textvariable=b1)
bpl=Label(frame1,text="BP Lower(in mmHg)")
slider3= Scale(frame1, from_=70, to=200, orient=HORIZONTAL,showvalue=NO,command=show4,length=130)
b2=IntVar()
b2.set(80)
ebpl=Entry(frame1,textvariable=b2)
slider4= Scale(frame1, from_=40, to=120, orient=HORIZONTAL,showvalue=NO,command=show5,length=130)

pulse=Label(frame1,text="Pulse rate (in bpm)")
p1=IntVar()
p1.set(134)
epulse=Entry(frame1,textvariable=p1)

rbc=Label(frame1,text="RBC Count (cells/mcl)")
rbc1=IntVar()
rbc1.set(4700000)
erbc=Entry(frame1,textvariable=rbc1)

wbc=Label(frame1,text="WBC Count")
wbc1=IntVar()
wbc1.set(100)
ewbc=Entry(frame1,textvariable=wbc1)

plate=Label(frame1,text="Platelets (per microliter)")
pl=IntVar()
pl.set(150000)
eplate=Entry(frame1,textvariable=pl)

hb=Label(frame1,text=" Hemoglobin (in g/dl)")
hb1=IntVar()
hb1.set(12)
ehb=Entry(frame1,textvariable=hb1)

ch=Label(frame1,text="Cholestrol")
ch1=IntVar()
ch1.set(100)
ech=Entry(frame1,textvariable=ch1)

#button
btn=Button(frame1,text="Genarate Report",command=report)

#placing
t.pack()

name.grid(row=0,column=0)
ename.grid(row=0,column=1)
age.grid(row=1,column=0)
eage.grid(row=1,column=1)
slider_age.grid(row=2,column=1)
gender.grid(row=3,column=0,pady=30)
r1.grid(row=3,column=1)
r2.grid(row=3,column=2)


weight.grid(row=5,column=0)
e1.grid(row=5,column=1)
slider1.grid(row=6,column=1)

height.grid(row=7,column=0)
e2.grid(row=7,column=1)
slider2.grid(row=8,column=1)

bpu.grid(row=9,column=0)
ebpu.grid(row=9,column=1)
slider3.grid(row=10,column=1)
bpl.grid(row=11,column=0)
ebpl.grid(row=11,column=1)
slider4.grid(row=12,column=1)

pulse.grid(row=13,column=0)
epulse.grid(row=13,column=1)

rbc.grid(row=14,column=0)
erbc.grid(row=14,column=1)

wbc.grid(row=15,column=0)
ewbc.grid(row=15,column=1)

plate.grid(row=16,column=0)
eplate.grid(row=16,column=1)

hb.grid(row=17,column=0)
ehb.grid(row=17,column=1)

ch.grid(row=18,column=0)
ech.grid(row=18,column=1)

#placing button
btn.grid(row=19,column=5)

frame0.pack(side=TOP,fill=X)
frame1.pack(fill=X)
root1.mainloop()
