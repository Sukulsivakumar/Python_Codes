with open('D:/first.txt','r') as fs, open('D:/second.txt','w') as sf:
    for line in fs:
             sf.write(line)