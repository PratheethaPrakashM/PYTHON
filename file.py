with open('text.txt','w') as f:
      c=f.write("My bestfriend name is Janaki. she is always trying to seduce me by showing some of her weird gestures." )
with open('text.txt','rb') as f:
    print(f.tell())
    f.seek(-1,2)
    print(f.tell())



