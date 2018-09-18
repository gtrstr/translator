#! python3
from tkinter import *
from tkinter import ttk
from googletrans import Translator, constants


#Function identifies the selected destination language and returns the two-character code for that language
def constants_link():
    lang_choice = langvar.get()
    lang_list = constants.LANGCODES
    return lang_list[lang_choice.lower()]
    #TODO: Write an exception to handle in case user does not select a language from the Combobox

#Function translates user inputted text from textbox and displays it in the Translation box
def translation():
    translator = Translator()
    trans_text = translator.translate(text=t.get(1.0, 'end-1c'), dest=constants_link())
    resultContent.set(trans_text.text)

root = Tk()
root.title('Translation App')

mainframe = ttk.Frame(root, padding="3 3 12 12")  #TODO: Assign minimum size
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

lang_label = ttk.Label(mainframe, text='Destination language').grid(column=2, row=1, sticky="NW")

#Combobox for language selection
langvar = StringVar()
langvar.set('Select language')
language = ttk.Combobox(mainframe, textvariable=langvar, state='readonly',
                        values=['Spanish', 'German']).grid(column=2, row=1, sticky='SE')  #TODO: Populate the values list using constants.py

t = Text(mainframe, width=20, height=5)  #TODO: Add a scroll bar to the text box
t.grid(column=1, row=1, rowspan=2, sticky='NE')

ttk.Button(mainframe, text='Translate', command=translation).grid(column=2, row=2) #Don't pass arg to command here

lf = ttk.LabelFrame(mainframe, text='Translation', height=100, width=300, padding=50)  #TODO: Expand the size of the Translation box
lf.grid(column=1, columnspan=2, row=3)
lf.columnconfigure(0, weight=1)
lf.rowconfigure(0, weight=1)

resultContent = StringVar()
end_result = ttk.Label(master=lf, textvariable=resultContent).grid(column=0, row=0)  #TODO: Test character limit, keep centered

root.mainloop()