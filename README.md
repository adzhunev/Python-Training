# Python training final task: concurrency

Task:
In this task I will test I/O functionallity with two different approaches: sequential and concurrent.

I/O tasks can take really long time mainly because the program sends a request and wait for it's responce. Only when the 
responce is received the next  request is sent and the program continues with the next one and so on. This may take long time 
expecially if we have to send many requests. There is no point to just stay and wait for response every time before sending the 
net request because this way the program is just staying not doing anything most of the time. We can use concurrent approach instead 
and send multiple requests at the same time without waiting for response. The program will receive the responses when they 
arrive and will continue sending requests and receiving responces inconsistently and will not spend time in waiting. This will 
improve the runtime performance significantly.

I will compare the times of execution and see how much concurrent approach improves the speed of execution.

test time to send 1000 requests without concurrency: around 45 seconds

test time to send 1000 requests with concurrency: around 9 seconds