def get_top_k_element(l, k):
	"""
	This function return the top k elements of the given list 
	"""
	if k > len(l):
		raise ValueError("k should be lesssthan or equal to lenngth of list l")
	sorted_list = sorted(l, reverse = True)
	top_k_list = sorted_list[:k]
	return top_k_list


sample_list = [4,8,2,5,1,9,3,7]
k = 4
print("The top K elements are:")
print(get_top_k_element(sample_list, k))

