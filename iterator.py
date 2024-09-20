#iterator are some methods used to iterate collection like list, tuples
p_list=[1,3,5,7,11,17]
p_iterator=iter[p_list]
print(next[p_list])
print(next[p_list]
for num in p_iterator:
      print(num)

#generator is a function that retun an iterator that produce sequence of values whenever iterated is over

      def custom_generator(n):
          value=0
          while value<n:
              yield value
              value+=1
      value=custom_generator(10)
      print(next(value))
      print(next(value))
      
      
