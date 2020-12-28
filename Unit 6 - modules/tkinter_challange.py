import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.image_hidden = True

    def create_widgets(self):
        self.question = tk.Label(self, text="What Framework in the image?")
        self.question.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

        self.show = tk.Button(self, text="SHOW IMAGE",
                              fg="blue", command=self.toggle_image)
        self.show.pack(side="bottom")

        self.image = tk.PhotoImage(file="Unit 6 - modules/flutter.png")
        self.lable_image = tk.Label(
            self, image=self.image, width=500, height=500)

    def toggle_image(self):
        if self.image_hidden:
            self.lable_image.pack()
        else:
            self.lable_image.pack_forget()
        self.image_hidden = not self.image_hidden


def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
