##List of numbers :: in dictionary :: prod ()
##We need to do operations on dictionary 


#-------------------------------------------------------------------------------------------------------------#

def start():
	num=dict()
	d=int(raw_input("Enter number of input  : "))
	i=0
	print "\n\n"
	while True :
		if i <d :
			num[i]=convert()
			i=i+1
		else :
			break 
	return  num

def split(d) :
	data=[]
	
	if d :
		i=0
		for a in d :
			data+=a
		return  data
	else :
		return 0


def convert():
	d=raw_input("Enter number : ")
	if d == "" :
		d='FF'
		print "\nInvalid input taking d default as " + d 
		
	n=split(d)
	n.reverse()
	ba=raw_input("Enter Base: ")
	if not ba :
		base=16 
		print "\nInvalid input taking base as default 16\n"
	else :
		base=int (ba)
	num=0
	i=0 
	count=0
	for i in n :
		i=ord(i)
		if i >=48 and i<=57:
			i=i-48
			num=num+i*(base**count)
			count=count+1
		else :
			if i >=65 and i <=90 :
				i=i-65+10
				num=num+int(i)*(base**count)
				count=count+1
			if i >=97 and i <=122:
				i=i-97+10+26
				num=num+int(i)*(base**count)
				count=count+1	
	#print "Number in base 10 -> " +str(num)
	l=[]
	l.append(d)
	l.append(str(base))
	l.append(str(num))
	print "\n\n"
	return l


def convert_to_bin(pro):
	for i in pro.keys():
			r = pro[i]
			temp=r[2]
			pro[i].append( "{0:b}".format(int(temp)))
			pro[i].append(convert_base(str(pro[i][1]),str(pro[i][2])))
	return pro

def display(pro):
	for i in pro.keys():
			print "\n"+str(i)+"-> "+str(pro[i])
		       
		
def convert_base(base,num):
	num=int(num)
	base=int(base)
	l=''
	while True :
		if num == 0:
			break 
		if not num :
			break 
		rem=num%base
		#print rem
		if rem > 9 :
			rem=rem+55
			if rem > 90 :
				rem=rem+7
				
		
		if rem >=65 and rem <=90 :
			l+=chr(rem)
		
		if rem >=97 and rem <=122 : 
				l+=chr(rem)		
		
		if rem <= 9 :
			l+=str(rem)
		
		num=num/base 
		#print num
		l=''.join(reversed(l))
	return l
			
	
#------------------------------------------------------------------------------#

prod1=start()
prod=convert_to_bin(prod1)
print "\n\n\nNumber || orignal base || decimal form || Binary form"
display(prod) 






















