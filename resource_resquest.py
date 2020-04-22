from banker import isSafe, is_lower, calculateNeed
import numpy as np 
from config import PROCESSES, AVAIL, MAXM,ALLOT, REQUEST, PROCESS_TH


def granted():
	need = calculateNeed(MAXM, ALLOT)
	if not is_lower(REQUEST, need[PROCESS_TH]):
		raise("Request > need")
	if not is_lower(REQUEST, AVAIL):
		raise("Request > available")
	
	avail = AVAIL
	request = REQUEST
	allot = ALLOT
	
	avail -= request
	allot[PROCESS_TH] += request

	return isSafe(PROCESSES, avail, MAXM, allot)

if __name__ == "__main__":
	granted()
	
		