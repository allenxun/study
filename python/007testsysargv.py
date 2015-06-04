import sys

def printmy(list):
	for i in list:
		print i

if __name__ == '__main__':
	list = sys.argv
	printmy(list)