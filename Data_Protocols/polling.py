s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.bind((Local_IP, Port1))
s1.listen(5)

s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.bind((Local_IP, Port2))
s2.listen(5)

sockets_that_might_be_ready_to_read = [s1,s2]
sockets_that_might_be_ready_to_write_to = [s1,s2]
sockets_that_might_have_errors = [s1,s2]


([ready_to_read], [ready_to_write], [has_errors])  = 
       select.select([sockets_that_might_be_ready_to_read],
                     [sockets_that_might_be_ready_to_write_to], 
                     [sockets_that_might_have_errors],            timeout)


for sock in ready_to_read:
    c,a = sock.accept()
    data = sock.recv(128)
    ...
for sock in ready_to_write:
    #process writes
    ...
for sock in has_errors:
    #process errors