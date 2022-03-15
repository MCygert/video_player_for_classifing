import tkinter
import tkinter as ttk, threading
import datetime
import os

import PIL.ImageTk
import cv2
from FramesCache import FramesCache


class App:
    def __init__(self, window, window_title, video_source=0):
        # Setting up window
        self.window = window
        self.window.title = window_title
        self.window.columnconfigure(1, minsize=300)
        self.window.rowconfigure(1, minsize=300)
        self.vid = MyVideoCapture(video_source)
        self._number_of_frames = self.vid.fps * 5
        self.cache = FramesCache(self._number_of_frames)

        btn_pass = ttk.Button(text="Pass", command= lambda: self.save_video("pass"))
        btn_pass.grid(column=1, row=2)
        btn_shot = ttk.Button(text="Shot")
        btn_shot.grid(column=2, row=2)
        btn_save = ttk.Button(text="Save")
        btn_save.grid(column=3, row=2)


        self.canvas = tkinter.Canvas(self.window, width=self.vid.width, height=self.vid.height)
        self.canvas.grid(column=0, row=1, sticky='nsew')

        btn_choose_video = ttk.Button(text="Choose video")
        btn_choose_video.grid(column=0, row=2)
        btn_quit = ttk.Button(text="Quit", command=self.window.destroy)
        btn_quit.grid(column=0, row=0)
        # Capturing video

        self.delay = 25
        self.update()
        self.window.mainloop()

    def update(self):
        ret, frame = self.vid.get_frame()
        if ret:
            self.cache.append(frame)
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
        self.window.after(self.delay, self.update)

    def save_video(self, label):
        time = datetime.datetime.now()
        root_path = "data"
        os.makedirs(root_path, exist_ok=True)
        if label == "pass":
            path = root_path + "/pass/"
            os.makedirs(path, exist_ok=True)
        if label == "shot":
            path = root_path + "/shot/"
            os.makedirs(path, exist_ok=True)
        if label == "save":
            path = root_path + "/save/"
            os.makedirs(path, exist_ok=True)
        print(path + str(time) + ".mp4")
        out = cv2.VideoWriter(path + str(time) + ".mp4", cv2.VideoWriter_fourcc(*'mp4v'), 30, (720, 1080))
        for frame in self.cache.dump():
            out.write(frame)
        out.release()



class MyVideoCapture:
    def __init__(self, video_source=0):
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.fps = self.vid.get(cv2.CAP_PROP_FPS)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                return ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            else:
                return ret, None
        else:
            return None, None


if __name__ == '__main__':
    App(ttk.Tk(), 'Video player', 'sample-mp4-file-small.mp4')
    # lbl_video_placeholder = ttk.Label(text="Video placeholder", bg='black', fg='white')
    # lbl_video_placeholder.grid(column=0, row=1, sticky='nsew')
    # root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
