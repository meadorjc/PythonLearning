#calebmeador 1/18/2014 meadorjc at gmail.com
#Algorithm practice
#taken from http://community.topcoder.com/stat?c=problem_statement&pm=7558

"""
Problem definition:
You are working in an advertising agency.
There are 100 billboards owned by your agency, numbered from 1 to 100.

You clients send you requests, one after another.
Each request is the number of the billboard on which the client would like to place his advertisement.

Initially all billboards are empty. Each time you receive a request, you act as follows.
If the corresponding billboard is empty, you satisfy the request and occupy the billboard with the client's advertisement.
If the corresponding billboard is occupied, you reject the request.

You are given a int[] requests containing the requests in the order you receive them. Return the number of rejected requests.
"""

class AdvertisingAgency:
	def numberOfRejections(self, requests):
		req_dict = {}
		total = 0
		for num in requests:
			req_dict[num] = (requests.count(num)-1)
		for index in req_dict:
			total += req_dict[index]
		return total 


ad = AdvertisingAgency()

#returns 0
requests = [1, 2, 3]
print ("Requests: ", requests, "\nRejections: ", ad.numberOfRejections(requests), end="\n\n")

#returns 2
requests = [1, 1, 1]
print ("Requests: ", requests, "\nRejections: ", ad.numberOfRejections(requests), end="\n\n")

#returns 2
requests = [1, 2, 1, 2]
print ("Requests: ", requests, "\nRejections: ", ad.numberOfRejections(requests), end="\n\n")

#returns 49
requests = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
print ("Requests: ", requests, "\nRejections: ", ad.numberOfRejections(requests), end="\n\n")

