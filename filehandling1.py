#WRITE A PROGRAM THAT ACCEPTS A FILENAME AS INPUT FROM USER , OPEN THE FILE AND COUNT THE NUMBER OF TIMES A CHARACTER APPEARS IN THE FILE.

fn=input("ENTER FILENAME:")
print(fn)
fo=open("{fn}","w")
text=input("ENTER THE TEXT:")
fo.write(text)
fo=open("{fn}","r")
fo.read(text)