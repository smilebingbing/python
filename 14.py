from functools import reduce
def str2float(s):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    strs=s.split('.')
	return reduce(lambda x,y:x*10+y,map(str2float,strs[0]))
print('str2float(\'123.456\')=',str2int('123.456'))