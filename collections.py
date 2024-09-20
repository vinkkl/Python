from collections import namedtuple, deque,ChainMap,Counter, defaultdict
''', 
courses = namedtuple('course',['name','tech'])
clist=courses(name='data Science', tech='web dev')
print(clist)
print(clist.name)
course_list=['webdevelopment', 'html']
print(courses._make(course_list)) #convert list into tuples

#deque - it is optimized list to perform insertion and deltion (list have no left option to insert but deque have)
t_list=['rohit','virat','mohit']
t_queue = deque(t_list)
print(t_queue)
t_queue.popleft()
print(t_queue)
t_queue.appendleft('rohit')
print(t_queue)

#chainmap - it is dictionary like class able to make a single view
tmod_1={1:'Angular',2:'python'}
tmod_2={3:'react',4:'cloud'}
mlist=ChainMap(tmod_1, tmod_2)
print(mlist)

#Counter - dict subclass which is used to count hastable object
rohit_score = [70,100,70,100,200]
score_count = Counter(rohit_score)
print(score_count.keys())
print(score_count.values())
print(score_count.items())
'''
temp=defaultdict(int)
temp[1]="te"
temp[2]="the"
print(temp[3])


item= OrderedDict()
