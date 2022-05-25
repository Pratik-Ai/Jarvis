import time, socket, sys

from tkinter import *

main_window = Tk()
main_window.title("Jarvis Client")

#blank space
Label(main_window, text = "").grid(row=0, column=0, columnspan=2)

#Input Labels

#Label(main_window, text = "Name : ").grid(row=1,column=0)
Label(main_window, text = "IP : ").grid(row=2, column=0)
Label(main_window, text = "Name : ").grid(row=3, column=0)

#Input fields

ip_value = Entry(main_window, width=35, borderwidth=5)
ip_value.grid(row=2, column=1, columnspan=3)

name_value = Entry(main_window, width=35, borderwidth=5)
name_value.grid(row=3, column=1, columnspan=3)

command_value = Entry(main_window, width=35, borderwidth=5)

l_command_lbl = Label(main_window, text = f"Your Last Command : ")
l_response_lbl = Label(main_window, text = f"Server's Last Response : ")

#functions
# socket_server = None

def connect():
    global socket_server 
    socket_server = socket.socket()
    server_host = socket.gethostname()
    ip = socket.gethostbyname(server_host)
    sport = 8080

    server_host = ip_value.get()
    name = name_value.get()

    socket_server.connect((server_host, sport))

    socket_server.send(name.encode())
    server_name = socket_server.recv(1024)
    server_name = server_name.decode()

    Label(main_window, text = f"Connection Status : Connected to server_name ").grid(row=5,column=0, columnspan=2)

    Label(main_window, text = f"Your Command : ").grid(row=6, column=0)
    command_value.grid(row=6, column=1, columnspan=3)
    
    send_btn = Button(main_window, text="Send", padx=35, pady=10, command=send_command)
    send_btn.grid(row=7, column=1, columnspan=1)

    l_command_lbl.grid(row=8, column=0, columnspan=2)
    l_response_lbl.grid(row=9, column=0, columnspan=2)

 
def send_command():
    command_msg = command_value.get()
    l_command_lbl.configure(text = f"Your Last Command : {command_msg}")

    socket_server.send(command_msg.encode()) #command sent to server
    
    response_msg = (socket_server.recv(1024)).decode() #receiving response from server
    l_response_lbl.configure(text = f"Server's Last Response : {response_msg} ")
    
    command_value.delete(0,END)


#Button
connect_btn = Button(main_window, text="Connect", padx=40, pady=10, command=connect)
connect_btn.grid(row=4, column=1, columnspan=1)



main_window.mainloop()


