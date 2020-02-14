### Controller(tk.Tk)
класс основного окна, служит контроллером для переключения фреймов(tk.Frame) с помощью метода show_frame(frame)

------------

### MainWindow(tk.Frame)
класс окна навигации между окнами.

------------


### OrdersWindow(tk.Frame)
класс окна заказов.
##### class.select_data(guest='', hotel='') 
метод формирует таблицу с даннами заказов. Если переданы данные гостя guest или отеля hotel формируется выборка данных заказа по гостю и/или отелю

#### AddOrdersWindow(tk.Toplevel)
класс окна (tk.Toplevel) для добавления данных нового заказа. 
##### class.get_guests_name()
стат.метод возвращает список имен гостей
##### class.get_hotels_name()
стат.метод возвращает список имен отелей
##### add_order()
метод добавляет введенные данные в БД

#### DeleteOrdersWindow(tk.Toplevel)
класс окна (tk.Toplevel) для удаления заказа. 
##### delete_order(id)
метод удаляет заказ из БД по id

------------


### HotelsWindow(tk.Frame)
класс окна заказов.
#### class.select_data()
метод формирует таблицу с даннами отелей

#### AddHotelWindow(tk.Toplevel)
 окна (tk.Toplevel) для добавления данных нового отеля. 
##### add_hotel()
метод добавляет введенные данные в БД

------------


### GuestsWindow(tk.Frame)
класс окна гостей.
#### class.select_data()
метод формирует таблицу с даннами гостей

#### AddGuestsWindow(tk.Toplevel)
класс окна (tk.Toplevel) для добавления данных нового гостя. 
##### add_hotel()
метод добавляет введенные данные в БД