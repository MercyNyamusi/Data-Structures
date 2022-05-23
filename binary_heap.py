def insert_heap(x,priority_queue):
    priority_queue.append(x)
    length=len(priority_queue)-1

    while length>0:
        if priority_queue[length//2]>priority_queue[length]:
            priority_queue[length // 2],priority_queue[length]=priority_queue[length],priority_queue[length//2]
        length//=2

    return priority_queue

if __name__=='__main__':
    input_arr=[0,5,9,11,14,18,19,21,33,17,27,12]
             # 0,1,2, 3, 4, 5, 6, 7, 8, 9,10,11
    priority_queue = []

    for i in input_arr:
        priority_queue=insert_heap(i,priority_queue)

    for i in priority_queue:
        print(i,end=" ")