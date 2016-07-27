def _odd_iter():
	n=1
	while True:
		n=n+2
		yield n
def _not_divisible(n):
	return lambda x:x % n>0
