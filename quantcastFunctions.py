def increment_count(counts_list, key):
	if key in counts_list:
		counts_list[key] += 1
	else:
		counts_list[key] = 1

def correct_date(timestamp, date):
	if timestamp.startswith(date):
		return True
	else:
		return False
		
def find_max_cookie(counts_list):
	current_max = 0
	max_list = []
	for cookie in counts_list:
		if counts_list[cookie] > current_max:
			max_list = [cookie]
			current_max = counts_list[cookie]
		elif counts_list[cookie] == current_max:
			max_list.append(cookie)
	return max_list