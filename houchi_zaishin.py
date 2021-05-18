import random
 
def CalcNum(s):
	num = 0
	for i in range(len(items_num)) :
		num += items_weight[s][i]*items_num[i]
	return num;
 
items_weight = [[0,100,300,1500],[30,100,300,1500]]
items_num = [1,3,3,5]
cnt_items = [0]*12
num_sim = 30000
 
for i in range(num_sim):
	items_num = [1,3,3,5]
	#print(cnt_items)
	flag=0
	for j in range(12):
		if j<5 :
			s=0
		else:
			s=1
		rand = random.randint(1,CalcNum(s))
		for k in range(len(items_num)) :
			if rand <= items_weight[s][k]*items_num[k] :
				items_num[k]-=1
				#print("No%d:%d"%(j, k))
				if k==0 :
					cnt_items[j] +=1
					flag=1
				break
			else:
				rand -= items_weight[s][k]*items_num[k]
    		if rand == 0:
    			print("error")
    			exit()
		if flag == 1 :
			break
print(cnt_items)
for i in range(12):
	print("%d: %f"%(i+1, float(cnt_items[i])/num_sim*100))