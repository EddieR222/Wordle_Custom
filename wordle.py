from email.mime import image
from tkinter import *
from tkinter.ttk import *
from tkinter import Canvas, messagebox
# from PIL import ImageTk, Image
import wordleFunc as c
import requests
import random

# Initialize the window
window = Tk()

#This starts the game at row zero of 6
global row
row = 0
global curr_word_list
curr_word_list = []
global num 
num = 5

#Code to place icon
# image1 = Image.open('wordle.png')
# icon = ImageTk.PhotoImage(image1)
# window.iconphoto(False, icon)


#Gather information about the user's screen pixel size and decrease height a bit
window_height = window.winfo_screenheight()
window_width = window.winfo_screenwidth()
window_height -= 100
window.geometry(str(window_width) + 'x' + str(window_height))


# Calucluate the widht and height of canvas in relation to the window
canvas_height = window_height - (window_height*0.2)
canvas_width = window_width - (window_width*0.4)
canvas = Canvas(window, bg = "white", width = canvas_width, height = canvas_height)

window.title("Wordle")

Title =  Label(window, text="Wordle", font = ("Times", -80)).place(relx = 0.5, rely = 0, anchor = N)

# This function creates 25 boxes, with white ones in between the light gray ones
c.create_25_boxes(canvas, (0, 0), num, canvas_width, color = "light gray")

word_site = "http://www.mieliestronk.com/corncob_lowercase.txt"

response = requests.get(word_site)
WORDS = response.content.splitlines()


# Since I only want words from 4 to 8 letters long, I will 
# iter through the WORDs list and filter them
WORDS3 = []
WORDS4 = []
WORDS5 = []
WORDS6 = []
WORDS7 = []
WORDS8 = []
def filterwords(WORD_LIST:tuple, num: int, WORDS:tuple):

    for word in WORDS:
        if len(word) == num:
            WORD_LIST.append(word)
    return WORD_LIST

WORDS3 = filterwords(WORDS3, 3, WORDS)
WORDS4 = filterwords(WORDS4, 4,  WORDS)
WORDS5 = filterwords(WORDS5, 5,  WORDS)
WORDS6 = filterwords(WORDS6, 6,  WORDS)
WORDS7 = filterwords(WORDS7, 7,  WORDS)
WORDS8 = filterwords(WORDS8, 8,  WORDS)

def current_word_list(num: int):
    if num == 3:
        return WORDS3
    elif num == 4:
        return WORDS4
    elif num == 5:
        return  WORDS5
    elif num == 6:
        return  WORDS6
    elif num == 7:
        return  WORDS7
    else:
        return WORDS8

#This picks a random word of desired size
def choose_wordle_word():
    global wordle_word
    wordle_word = random.choice(current_word_list(num)).decode("utf-8")
    return wordle_word



global wordle_word
wordle_word = choose_wordle_word()






# This checks if word is correct length and is in the word bank
def submit():
    global row
    global num
    global wordle_word
    input_word = input_text.get()
    print(num)
    print(wordle_word)
    curr_word_list = current_word_list(num)
    input_text.set("")
    if row == num and input_word != wordle_word:
        c.lose_game(canvas, input_word, num, row, canvas_width, wordle_word)
        selected_item()
    elif row <= num+1 and input_word == wordle_word:
        c.win_game(canvas, input_word, num, row, canvas_width)
        selected_item()
    elif row < num+1:
        if len(input_word) > num or len(input_word) < num:
            messagebox.showerror("showerror", "Error: Please input " + str(num) + " letter word!!")
        elif len(input_word) == num and (input_word.lower().encode("utf-8")) not in curr_word_list:
            messagebox.showerror("showerror", "Error: Word not in word bank, try again")
        elif len(input_word) == num and (input_word.lower().encode("utf-8")) in curr_word_list:
            c.grade_word(canvas, input_word, wordle_word, num, row, canvas_width)
            row += 1
    
    


canvas.place(relx = 0.2, y=100)
# This will put the button to submit the word and call the function submit which checks if word is acceptable
input_text = StringVar()
entry1 = Entry(window, textvariable = input_text, font = ("Times", 15)).place(relx = 0.5, rely = 0.9, anchor = S)
sub_btn = Button(window, text="Submit", command =submit).place(relx = 0.5, rely = 0.95, anchor=S)

# # Creates listbox so that we can set the length of words in wordle 
listbox = Listbox(window, selectmode = SINGLE)
listbox.place(relx = 0.9, rely = 0.5, anchor = E)
for values in range(3, 9):
    listbox.insert(END, values)

# Will be called when we press "choose number" button and it will restart the game with choosen number
number = StringVar()
def selected_item():
    global num 
    global wordle_word
    global row 
    number = listbox.get(ACTIVE)
    num = number
    row = 0
    canvas.delete('all')
    wordle_word  = choose_wordle_word()
    c.create_25_boxes(canvas, (0,0), num, canvas_width, color = 'light gray')
 
# Create a button widget and
# map the command parameter to
# selected_item function
btn = Button(window, textvariable = 'number', text='Choose Number', command=selected_item).place(relx = 0.89, rely = 0.6, anchor = E)


# input_word = Entry(window).place(relx = 0.45, rely = 0.75)
# c.win_game(canvas, guess = "Vincent", num=7, row=5, canvas_width=canvas_width)

# guess = b'apple'
# if guess in WORDS5:
#     print(guess.decode('utf-8').upper())
# else:
#     print("NOT IN LIST")

    

         


window.mainloop()

