import io
import time
import os
 
# Replace this with the path to your EQ logs file
LOG_LOCATION = '.\log_test_py.txt'

# Replace this with phrase to watch for in log file
WATCH_PHRASE = 'immolated in flame'
 
#Replace with number of seconds to count
SECONDS = 12
 
def main():

	#keepy copy to avoid duplicate timers
	line_compare = ''
	last_log_size = 0

	while True:
		#delay to allow OS time to open/close file between readings
		time.sleep(.1)

		#only test for immolate when log file size changes
		log_size = os.path.getsize(LOG_LOCATION)
		if log_size != last_log_size:
			last_log_size = log_size

			#open and close file
			with io.FileIO(LOG_LOCATION, 'r') as file:
				file.seek(-100, 2)						#-100 offset, end-of-file
				last_lines = file.readlines()	

			#search from bottom up
			for line in reversed(last_lines):
				#remove excess whitespace that throws off line-ending
				line = str(line).replace("\\r", "").replace("\\n","")

				#exec timer if 'immolated' is different from last
				if WATCH_PHRASE in line and line != line_compare:

					#keepy copy to avoid duplicate timers
					line_compare = line

					start_cd = time.time()		#start timer
					print('***', line, '***')
					for countdown in reversed(range(1, SECONDS+1)):
						time.sleep(1)
						print('\t',countdown)

					print(time.time()-start_cd)	#print timer
					break

				#if 'immolated' and same as last time, break the for loop
				elif 'immolated in flame' in line and line == line_compare:
					break
				else:
					continue
				break

if __name__ == '__main__':
	main()
