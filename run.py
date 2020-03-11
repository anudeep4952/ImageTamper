from detection import detection
from susbtitute import substitute
from tamper import tamper

while True:
    ch=int(input("1.WaterMark Image 2.Tamper Detection 3.Tamper 4.Exit"))
    if ch==1:
        substitute()
        print("watermark generated\n")
    elif ch==2:
        detection()
        print("detected and recovered\n")
    elif ch==3:
        tamper()
        print("image tampered")
    elif ch==4:
        break
    else:
        print("please enter correct choice")
    print()
