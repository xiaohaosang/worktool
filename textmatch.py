pattern='jsonCallBack'
directory_path='F:\每日_月度统计 _ 上海证券交易所_files'
#directory_path='F:\meiri'
match_results=[]

import os,re

def match(path,pattern):
	#print(path)
	filetype =path.split('.')[-1]
	#print(filetype)
	if filetype not in ('png'):
		try:
			with open(path,"r",encoding='utf-8') as f:
				text=f.read()
				#print(text)
			#result=re.search(pattern,text,re.I)
			result=re.compile(pattern,re.I).search(text)	
			#print(result)
			if result!=None:
				match_results.append(path)				
		except Exception as e:  #IOError:
			print('{} open is fail'.format(path))
			print(e)

		
assert os.path.isdir(directory_path)
directory_paths_list=[directory_path]
while directory_paths_list!=[]:
	directory_path=directory_paths_list[0]
	for x in os.listdir(directory_path):
		path=os.path.join(directory_path,x)
		if os.path.isdir(path):
			directory_paths_list.append(path)	
		else:
			match(path,pattern)
	directory_paths_list.remove(directory_path)		

'''
print('**********')
print('match_results:')
for i in match_results:
	print(i)
'''	