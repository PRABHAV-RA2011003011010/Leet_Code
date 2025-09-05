class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        def calculate_nextgain(pass_students,total_pass):
            return ((pass_students+1)/(total_pass+1))-(pass_students/total_pass)
        max_heap=[]
        for pass_stu, tot in classes:
            gain=calculate_nextgain(pass_stu,tot)
            max_heap.append((-gain,pass_stu,tot))

        heapq.heapify(max_heap)

        for _ in range(extraStudents):

            gain,p,t=heapq.heappop(max_heap)
            heapq.heappush(max_heap,(-calculate_nextgain(p+1,t+1),p+1,t+1))
        
        total_ratio=sum(pass_stu/tot for _,pass_stu,tot in max_heap )

        return (total_ratio)/len(classes)




            
        