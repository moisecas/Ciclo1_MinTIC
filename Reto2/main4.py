grupo=[]
promedio=0
cont=0 
fid=[]
sid=[]
tid=[]
    
    
    
for d in grupo:
    promedio += d['nota_fundamentos']
    cont += 1
promedio /= cont
    
primero= 0
segundo= 0
tercero= 0
cuadro_honor = {}
    
for d in grupo:
    if d['nota_fundamentos'] > primero:
        primero = d ['nota_fundamentos']
        fid = [d['cédula']]
    elif d['nota_fundamentos'] == primero:
        fid += [d['cédula']]
    
cuadro_honor[1] = fid
    
for d in grupo:
    if d['nota_fundamentos'] > segundo and d ['nota_fundamentos'] != primero:
        segundo = d['nota_fundamentos']
        sid = [d['cédula']]
    elif d['nota_fundamentos'] == segundo:
        sid += [d['cédula']]
cuadro_honor[2] = sid 
    
for d in grupo:
    if d['nota_fundamentos'] > tercero and d ['nota_fundamentos'] not in [primero,segundo]:
        tercero = d['nota_fundamentos']
        tid = [d['cédula']]
    elif d['nota_fundamentos'] == tercero:
        tid+=[d['cédula']]
            
cuadro_honor[3] = tid 
        