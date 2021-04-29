from vidstream import AudioSender, AudioReceiver, ScreenShareClient, CameraClient, StreamingServer
import tkinter as tk
import socket
import threading

# getIp
local_ip = socket.gethostbyname(socket.gethostname())
#public_ip = requests.get('https://api.ipify.org').text
print(local_ip)

server = StreamingServer(local_ip, 5555)
receiver = AudioReceiver(local_ip, 4444)


# listening
def start_listening():
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=receiver.start_server)
    t1.start()
    t2.start()


def start_camara():
    camara_client = CameraClient(text_ip.get(1.0, 'end-1c'), 5555)
    t3 = threading.Thread(target=camara_client.start_stream)
    t3.start()


def screen_shearing():
    screen_client = ScreenShareClient(text_ip.get(1.0, 'end-1c'), 4444)
    t4 = threading.Thread(target=screen_client.start_stream)
    t4.start()

def audio_stream():
    audio_client = AudioSender(text_ip.get(1.0, 'end-1c'),5555)
    t5 = threading.Thread(target=audio_client.start_stream)
    t5.start()


# gui
wd = tk.Tk()
wd.title("VideoSteam")
wd.geometry('300x200')

label_ip = tk.Label(wd, text="IP: ")

text_ip = tk.Text(wd, height=1)
text_ip.pack()

btn_st = tk.Button(wd, text="Start Listening", width=50,command=start_listening)
btn_st.pack(anchor=tk.CENTER, expand=True)

btn_cam = tk.Button(wd, text="Start camara Stream", width=50, command=start_camara)
btn_cam.pack(anchor=tk.CENTER, expand=True)

btn_stream = tk.Button(wd, text="Start Screen Sharing", width=50, command=audio_stream)
btn_stream.pack(anchor=tk.CENTER, expand=True)
btn_audio = tk.Button(wd, text="Start audio Stream", width=50, command=audio_stream)
btn_audio.pack(anchor=tk.CENTER, expand=True)

wd.mainloop()
