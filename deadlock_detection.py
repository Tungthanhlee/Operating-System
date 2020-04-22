import numpy as np
from config import DL_PROCESSES, DL_AVAIL, DL_REQUEST, DL_ALLOT
from banker import is_lower


def is_zeros(arr):
	"""
	Return True if all the element in the arr is zero else return False
	"""
	for i in arr:
		if i != 0:
			return False 
	return True

def is_deadlock(processes, avail, request, allot): 

	# Calcualte num_process	
	num_process = processes.shape[0]

	# Mark all processes as False  
	finish = np.zeros((processes.shape), dtype=bool)

	# store work as avalable matrix
	work = avail

	#check if allocation or request is zero or not
	for i in range(num_process):
		if not is_zeros(allot[i]) or not is_zeros(request[i]):
			finish[i] = False
		else:
			finish[i] = True

	count = 0
	while (count < num_process): 
		
		flag = False
		for i in range(num_process):
			# print(i)
			if finish[i] == False:
				if is_lower(request[i], work):
					print("Process: ",i)
					# print(finish[i])
					# print(is_lower(need[i], work))
					print("Request: ", request[i])
					print("Work before: ", work)

					work += allot[i]
					print("Work after: ", work)
					finish[i] = True
					print(f"Finish vector: {finish}")
					print("#"*10)
					flag = True
					count += 1
				
		# If we could not find a next process 
		# in safe sequence. 
		if (flag == False): 
			break
	
	deadlock = False
	for f in range(len(finish)):
		if finish[f] == False:
			print(f"Deadlock at process {f}")
			deadlock = True
			break
	
	if deadlock == False:
		print("There is no deadlock")
		
# Driver code 
if __name__ =="__main__": 
	is_deadlock(DL_PROCESSES, DL_AVAIL, DL_REQUEST, DL_ALLOT)

