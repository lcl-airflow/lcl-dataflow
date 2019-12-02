import io

with open('../../MARA_20191007190003_0001.txt') as f:
    first_line = f.readline()
    v= first_line.split('|')
    #print (v)


f = open("../../schema.txt", "a", encoding='utf-8')
f.write('[ ')
f.write('\n')
f.write('{')
f.write('\n')
f.write('"discription":' + '"'+ v[0] + '"' +','+'\n')
f.write('"mode": "REQUIRED",\n')
f.write('"name":' + '"'+ v[0] + '"' +','+'\n')
f.write('"type": "STRING"\n')
f.write('}')
for vs in v:
    f.write(',')
    f.write('\n')
    f.write('{')
    f.write('\n')
    f.write('"discription":' + '"'+ vs + '"' +',' +'\n')
    f.write('"mode": "REQUIRED",\n')
    f.write('"name":' + '"'+ vs + '"' +','+'\n')
    f.write('"type": "STRING"\n')
    f.write('}')
f.write('\n')
f.write(']')
