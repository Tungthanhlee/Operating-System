import numpy as np
from config import PROCESSES, AVAIL, MAXM,ALLOT

# Function to find the need of each process 
def calculateNeed(maxm, allot): 
	return (maxm - allot)

def is_lower(a, b):
	"""
	Check elementwise array a < array b
	Return True if a < b else False
	"""
	checks = b-a
	# print(checks)
	for check in checks:
		if check < 0:
			return False
	return True

# Function to find the system is in 
# safe state or not 
def isSafe(processes, avail, maxm, allot): 

	# Calcualte num_process	
	num_process = processes.shape[0]

	# Function to calculate need matrix 
	need = calculateNeed(maxm, allot) 

	# Mark all processes as infinish 
	finish = np.zeros((processes.shape), dtype=bool)
	
	# To store safe sequence 
	safeSeq = np.zeros((processes.shape), dtype=int)

	# store work as avalable matrix
	work = avail

	count = 0
	while (count < num_process): 
		
		flag = False
		for i in range(num_process):
			# print(i)
			if finish[i] == False and is_lower(need[i], work):
				print("Process: ",i)
				# print(finish[i])
				# print(is_lower(need[i], work))
				print("Need: ", need[i])
				print("Work before: ", work)

				work += allot[i]
				print("Work after: ", work)
				print("#"*10)
				finish[i] = True
				flag = True
				safeSeq[count] = i
				count += 1
				
		# If we could not find a next process 
		# in safe sequence. 
		if (flag == False): 
			print("System is not in safe state") 
			return False
		
	# If system is in safe state then 
	# safe sequence will be as below 
	print(f"System is in safe state.\n Safe sequence is {safeSeq}.")
	return True

# Driver code 
if __name__ =="__main__": 
	
	isSafe(PROCESSES, AVAIL, MAXM, ALLOT)

