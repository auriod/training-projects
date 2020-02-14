import tkinter as tk
#######################################
#            SETTING                  #
#######################################
main_color = '#2E9AFE'
btn_color = 'white'
font_select = 'Vernada 10'
font_main = 'Arial 14'


class MainWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg=main_color)

        guests_logo = tk.PhotoImage(file="img/guests.gif")
        hotels_logo = tk.PhotoImage(file="img/hotels.gif")
        orders_logo = tk.PhotoImage(file="img/orders.gif")

        btn_orders = tk.Button(self, width=130, height=130, image=orders_logo, bg=btn_color,
                               command=lambda: controller.show_frame('orders'))
        btn_orders.image = orders_logo
        btn_orders.grid(row=0, column=0, padx=20, pady=20)

        btn_hotels = tk.Button(self, width=130, height=130, image=hotels_logo, bg=btn_color,
                               command=lambda: controller.show_frame('hotels'))
        btn_hotels.image = hotels_logo
        btn_hotels.grid(row=0, column=1, padx=20, pady=20)

        btn_guests = tk.Button(self, width=130, height=130, image=guests_logo, bg=btn_color,
                               command=lambda: controller.show_frame('guests'))
        btn_guests.image = guests_logo
        btn_guests.grid(row=0, column=2, padx=20, pady=20)

        label_orders = tk.Label(self, text='ЗАКАЗЫ', bg=main_color, font=font_main, fg='white')
        label_orders.grid(row=1, column=0, padx=20)

        label_hotels = tk.Label(self, text='ОТЕЛИ', bg=main_color, font=font_main, fg='white')
        label_hotels.grid(row=1, column=1, padx=20)

        label_guests = tk.Label(self, text='ГОСТИ', bg=main_color, font=font_main, fg='white')
        label_guests.grid(row=1, column=2, padx=20)


if __name__ == '__main__':
    root = tk.Tk()
    frame = MainWindow(root, root)
    frame.grid(row=0, column=0)

    root.mainloop()



