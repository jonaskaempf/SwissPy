from itertools import groupby

def groupem(l):
	G=(list(x) for _,x in groupby(enumerate(l), lambda (i,x):i-x))
	return ",".join("-".join(map(str,(g[0][1],g[-1][1])[:len(g)])) for g in G)
    