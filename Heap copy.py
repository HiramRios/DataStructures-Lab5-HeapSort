
# Hiram Rios 80552404 the purpose of this lab is to practise heap methods 

class Heap:
    def __init__(self):
        self.heap_array = []
        
        
    def insert(self,k): 
        self.heap_array.append(k)
        
    #after it inserts the value it starts comparing it with the other elements by perculating up
        i = len(self.heap_array)-1
        while (i-1) // 2 >= 0:
            if self.heap_array[i] < self.heap_array[(i-1) // 2]:
                temp = self.heap_array[(i-1) // 2]
                self.heap_array[(i-1) // 2] = self.heap_array[i]
                self.heap_array[i] = temp
            i = i // 2        
        return self.heap_array
    # what extract min does is it gets rid of the first index and replace it with the last index  
    def extract_min(self):
        if self.is_empty():
            return None 
        # this replaces haep arry[0] with the last index in the array then pops the last one     
        min_elem= self.heap_array[0]
        self.heap_array[0]= self.heap_array[len(self.heap_array)-1]
        self.heap_array.pop(len(self.heap_array)-1)
        i =0
        print(min_elem + " just got extracted ")
        # this compares the children finds which one is the smallest then compares it the parent  
        while (i * 2+2) < len(self.heap_array)-1:
            # compares the child 
            if self.heap_array[i*2+1] > self.heap_array[i*2+2]:
                mic= i *2+2
            else:
                mic= i * 2 +1
                    
            #compares the parent with the smallest child 
            if self.heap_array[i] > self.heap_array[mic]:
                tmp = self.heap_array[i]
                self.heap_array[i] = self.heap_array[mic]
                self.heap_array[mic] = tmp
            i = mic

        return self.heap_array
        
    
    
    def is_empty(self):
        return len(self.heap_array)==0



def main():
    text_file = open("file.txt", "r")
    lines = text_file.read().split(',')
    h = Heap()
    #input_list= [23,70,46,20,67,35,72,59]
    for k in lines:
        print(h.insert(k))

        
    for k in lines:
        print(h.extract_min())
    
    
main() 






