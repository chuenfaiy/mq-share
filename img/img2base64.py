import base64
for i in range(5):
    f=open(str(i+1) + '.png','rb')
    ls_f=base64.b64encode(f.read())
    f.close()
    print(i+1, ls_f)