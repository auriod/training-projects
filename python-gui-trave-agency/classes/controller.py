import tkinter as tk
import classes.main_window as mw
import classes.orders_window as rw
import classes.hotels_window as hw
import classes.guests_window as gw

main_color = '#2E9AFE'


class Controller(tk.Tk):
    def __init__(self,  *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('TravelAgency')
        self.geometry('+50+50')
        container = tk.Frame(self, bg=main_color, padx=20, pady=20)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {
            'main': mw.MainWindow(parent=container, controller=self),
            'orders': rw.OrdersWindow(parent=container, controller=self),
            'hotels': hw.HotelsWindow(parent=container, controller=self),
            'guests': gw.GuestsWindow(parent=container, controller=self)
        }

        for frame in self.frames.values():
            frame.grid(row=0, column=0)

        self.show_frame('main')

    def show_frame(self, frame):
        for f in self.frames.values():
            f.grid_remove()
        self.frames[frame].grid()


if __name__ == '__main__':
    app = Controller()
    app.mainloop()



