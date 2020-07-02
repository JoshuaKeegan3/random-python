# assesment.py
# Display maori names of nz places and a short discription
# Created: 21/06/2019
# Last Edited: 21/06/2019
# Author: Joshua Keegan
##

import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile

class App(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Maori Place Names')
        self.container = tk.Frame(self)
        self.geometry("550x300+400+200")

        self.__get_places()

        self.container.pack(side ="top", fill = "both", expand = True)

        self.LARGE_FONT = ("Arial", 18)

        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)
        
        self.frames = {}
        
        for Page in (Home,
                     new_place_entry_page,
                     find_maori_name_and_discription_page,
                     find_english_name_and_discription_page,
                     english_names_in_order_page,
                     edit_entry_page,
                     delete_entry_page):
            frame = Page(self.container,self)

            self.frames[Page] = frame
            frame.grid(row = 0, column=0, sticky="nsew")

        self.show_frame(Home)


    def show_frame(self, page):

        frame = self.frames[page]
        frame.tkraise()

    def __get_places(self):
        valid = False
        while not valid:
            try:
                self.places = []
                self.file_name = askopenfilename()
                buffer = open(self.file_name, "r")
                for line in buffer:
                    exec("Place(self,{})".format(str(line[:-1].split(','))[:-1][1:]))
                buffer.close()
                valid = True
            except:
                print("Error Opening File")
            


class Home(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        page_name_label = tk.Label(self, text = "Home Page", font = controller.LARGE_FONT)
        page_name_label.grid(row = 0, column =0)

        # Create Buttons
        self.command_frame = tk.Frame(self)
        self.command_frame.grid(row=1,column=0)
        # Enter a new place
        self.new_place_entry_button = tk.Button(self.command_frame,
                                                text='Enter new place',
                                                command =
                                                lambda: controller.show_frame(new_place_entry_page))
        
        self.new_place_entry_button.grid(row=0,column=0,sticky="NESW")
        # Find maori name and discription
        self.find_maori_name_and_discription_button = tk.Button(self.command_frame,
                                        text='Find maori name and discription',
                                        command =
                                        lambda: controller.show_frame(
                                            find_maori_name_and_discription_page))
        
        self.find_maori_name_and_discription_button.grid(row=0,column=1)
        # Find english_name_and discription
        self.find_english_name_and_discription_button = tk.Button(self.command_frame,
                                text='Find english name and discription',
                                command =
                                lambda: controller.show_frame(find_english_name_and_discription_page))
        
        self.find_english_name_and_discription_button.grid(row=0,column=2,sticky="NESW")
        # List english names in order
        self.english_names_in_order_button = tk.Button(self.command_frame,
                                text='List english names in order',
                                command =
                                lambda: controller.show_frame(english_names_in_order_page))
        
        self.english_names_in_order_button.grid(row=1,column=0,sticky="NESW")
        # Edit entry
        self.edit_entry_button = tk.Button(self.command_frame,
                        text='Edit entry',
                        command =
                        lambda: controller.show_frame(edit_entry_page))
        
        self.edit_entry_button.grid(row=1,column=1,sticky="NESW")
        # Delete entry
        self.delete_entry_button = tk.Button(self.command_frame,
                        text='Delete entry',
                        command =
                        lambda: controller.show_frame(delete_entry_page))
        
        self.delete_entry_button.grid(row=1,column=2,sticky="NESW")

        self.quit_button = tk.Button(self.command_frame, command = controller.destroy, text = "Quit")
        self.quit_button.grid(row = 2, column = 1,sticky="NESW")

        
    
class default_page(tk.Frame):       ## Might be util

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        self.back_button = tk.Button(self, text = "Back", command = lambda: controller.show_frame(Home))
        self.back_button.grid(row=0,column =0)

class new_place_entry_page(default_page):

    def __init__(self, parent, controller):

        default_page.__init__(self,parent, controller)

        self.controller = controller

        english_name_label = tk.Label(self, text = "Enter the English name")
        maori_name_label = tk.Label(self, text = "Enter the Maori name")
        discription_label = tk.Label(self, text = "Enter the disciption")
        
        english_name_label.grid(row=1,column=0)
        maori_name_label.grid(row=1,column=1)
        discription_label.grid(row=1,column=2)

        self.english_name = tk.StringVar()
        self.maori_name = tk.StringVar()
        self.discription = tk.StringVar()

        
        english_name_entry = tk.Entry(self, textvariable = self.english_name)
        english_name_entry.grid(row=2,column=0)
        maori_name_entry = tk.Entry(self, textvariable = self.maori_name)
        maori_name_entry.grid(row=2,column=1)
        discription_entry = tk.Entry(self, textvariable = self.discription)
        discription_entry.grid(row=2,column=2)

        submit_button = tk.Button(self, text = "Submit", command = self.submit)
        submit_button.grid(row=3,column=1)## Make a event <<return>>

    def submit(self):
        
        text = self.english_name.get()+","+self.maori_name.get()+","+self.discription.get()+"\n"
        with open(self.controller.file_name, "a") as myfile:
            myfile.write(text)
            
        #Show confirmation
        confirm_window = tk.Tk()
        confirm_window.title("Success!")
        confirmation_text = "A new place with the english name {}, the maori name {}, and the discription {}, has been added to the file {}".format(
            self.english_name.get(),self.maori_name.get(),self.discription.get(),self.controller.file_name)
        tk.Label(confirm_window, text = confirmation_text).pack()
        tk.Button(confirm_window, command=confirm_window.destroy, text = "Close").pack()
        confirm_window.lift()
##        confirm_window.attributes('-topmost', True)
##        confirm_window.attributes('-topmost', False)
        confirm_window.mainloop()


class find_maori_name_and_discription_page(default_page):
    
    def __init__(self, parent, controller):

        default_page.__init__(self,parent, controller)

        self.controller = controller
        # Get English Name
        english_names = []
        self.english_name = tk.StringVar()
        
        for place in controller.places:
            english_names.append(place.get_english_name())

        self.english_name.set(english_names[0])
        
        english_name_options = tk.OptionMenu(self, self.english_name, *english_names)
        english_name_options.grid(row=1,column=0)
        
        self.english_name.trace("w", self.find_maori_name_and_description)

        self.output_frame = tk.Frame(self)
        self.output_frame.grid(row=2,column=0)


    def find_maori_name_and_description(self, *args):
        print(*args) # StringVar '' w
        # Find maori Name and description
        for place in self.controller.places:
            if self.english_name in place.english_name:
                # Display them
                maori_name_label = Label(self.output_frame, text = "Maori Name: "+ place.maori_name)
                maori_name_label.pack()

                discription_label = Label(self.output_frame, text = "Discription: "+ place.discription)
                discription_label.pack()
                
                
                
        # Show Message if it can't be found

class find_english_name_and_discription_page(default_page):
    pass

class english_names_in_order_page(default_page):
    pass

class edit_entry_page(default_page):
    pass

class delete_entry_page(default_page):
    pass

class Place(): 

    def __init__(self,controller, __english_name = '', __maori_name= '', __discription=''):
        self.__english_name = __english_name
        self.__maori_name = __maori_name
        self.__discription = __discription
        controller.places.append(self)

    def get_english_name(self):
        return self.__english_name

    def get_maori_name(self):
        return self.__maori_name

    def get_discription(self):
        return self.__discription
    
    def change_english_name(self, changed_english_name):
        self.__english_name = changed_english_name
        
    def change_discription(self, changed_maori_name):
        self.__maori_name = changed_maori_name

    def change_discription(self, changed_discription):
        self.__discription = changed_discription
        
    

if __name__ == "__main__":
    gui = App()
    gui.mainloop()
    
        
## allow the user to enter the English and Māori names for a place, along with a short
##description;
## allow the user to find the Māori name and the description, given the English name;
## allow the user to find the English name and the description, given the Māori name;
## allow the user to list all the names, in alphabetical order of the English names;
## allow the user to edit an entry;
## allow the user to delete an entry;
## possibly use an external file to store the data.
