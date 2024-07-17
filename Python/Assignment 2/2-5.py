seconds=int(input("seconds: "))
h,m,s=0,0,0
while seconds>60:
    if seconds>3600:
        h=int(seconds/3600)
        seconds=seconds-int((h*3600))
    if seconds<3600 and seconds>60:
        m=int(seconds/60)
        seconds=seconds-int((m*60))
    if seconds<60:
        s=seconds
    
print(h,":",m,":",s)