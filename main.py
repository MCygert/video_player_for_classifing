import tkinter
import tkinter as ttk, threading
import cv2


class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title = window_title
        self.window.columnconfigure(1, minsize=300)
        self.window.rowconfigure(1, minsize=300)

        self.vid = MyVideoCapture(video_source)
        btn_choose_video = ttk.Button(text="Choose video")
        btn_choose_video.grid(column=0, row=2)
        btn_quit = ttk.Button(text="Quit", command=self.window.destroy)
        self.canvas = tkinter.Canvas(window, width=vid.width, height=vid.height).grid(column=0, row=1, sticky='nsew')
        btn_quit.grid(column=0, row=0)
        self.window.mainloop()


class MyVideoCapture:
    def __init__(self, video_source=0):
        self.vid = cv2.VideoCapture
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
        self.window.mainloop()
    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB),)
            else:
                return (ret, None)
        else:
            return (None, None)



if __name__ == '__main__':
    App(ttk.Tk(), 'Video player', 'sample-mp4-file-small.mp4')
    # lbl_video_placeholder = ttk.Label(text="Video placeholder", bg='black', fg='white')
    # lbl_video_placeholder.grid(column=0, row=1, sticky='nsew')
    # root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
