from tkinter import *
from tkinter import Canvas, messagebox
import random
import math

def create_square(canvas: Canvas, top_left: tuple,  pixel:int=25,  color:str='light gray' ):
    canvas.create_rectangle(top_left[0], top_left[1], top_left[0] + pixel, top_left[1] + pixel, fill= color)
    # square.place( x = top_left[0], y= top_left[1])


def create_25_boxes(canvas: Canvas, top_left: tuple, num:int, canvas_width:int,  color:str = 'light gray'):
    x = top_left[0]
    orig_x = top_left[0]
    y = top_left[1]
    orig_y = top_left[1]
    pixel = canvas_width/((num*2)+1)
    while y < (orig_y + ((num+1)*pixel)):
        create_square(canvas, (x, y), pixel, color="white")
        x += pixel
        create_square(canvas, (x, y), pixel, color)
        x += pixel 
        if x >= (((num*2)+1)*pixel):
            create_square(canvas, (x, y), pixel, color = "white" )
            x = orig_x
            y += pixel

def count_letter_occurence(letter:str, wordle_word: str):
    count = 0
    for character in wordle_word:
        if character == letter:
            count += 1

    return count



def grade_word(canvas: Canvas, guess:str, wordle_word:str, num:int, row: int, canvas_width:int):
    list_of_letters = []
    # ocurr_of_letters = []
    if guess == wordle_word:
        win_game(canvas, guess, num, row, canvas_width)
    if guess != wordle_word and row == num+1:
        lose_game(canvas, guess, num, row, canvas_width, wordle_word)
    for index, character in enumerate(guess):
        if character in wordle_word and wordle_word[index] == guess[index] and character not in list_of_letters:
            green_box(canvas, guess, index, num, row, canvas_width)
            if count_letter_occurence(character, wordle_word) == 1:
                list_of_letters.append(character)
                # ocurr_of_letters.append(count_letter_occurence(character))
        elif character in wordle_word and wordle_word[index] != guess[index] and character not in list_of_letters:
            yellow_box(canvas, guess, index, num, row, canvas_width)
            if count_letter_occurence(character, wordle_word) == 1:
                list_of_letters.append(character)
                # ocurr_of_letters.append(count_letter_occurence(character))
        else:
            gray_box(canvas, guess, index, num, row, canvas_width)






def green_box(canvas:Canvas, guess:str, index:int, num:int, row:int, canvas_width:int):
    pixel = canvas_width/((num*2)+1)
    x = pixel + (index*(2*pixel))
    y = row * pixel
    pixel_floor = math.floor(pixel)
    half_pixel = math.floor(pixel/2)
    create_square(canvas, (x, y), pixel, color = "green")
    canvas.create_text(x+half_pixel, y+half_pixel, text="" + guess[index], font = ("Times", -pixel_floor))


def yellow_box(canvas:Canvas, guess:str, index:int, num:int, row:int, canvas_width:int):
    pixel = canvas_width/((num*2)+1)
    x = pixel + (index*(2*pixel))
    y = row * pixel
    pixel_floor = math.floor(pixel)
    half_pixel = math.floor(pixel/2)
    create_square(canvas, (x, y), pixel, color = "yellow")
    canvas.create_text(x+half_pixel, y+half_pixel, text="" + guess[index].lower(), font = ("Times", -pixel_floor))


def gray_box(canvas:Canvas, guess:str, index:int, num:int, row:int, canvas_width:int):
    pixel = canvas_width/((num*2)+1)
    x = pixel + (index*(2*pixel))
    y = row * pixel
    pixel_floor = math.floor(pixel)
    half_pixel = math.floor(pixel/2)
    canvas.create_text(x+half_pixel, y+half_pixel, text="" + guess[index].lower(), font = ("Times", -pixel_floor))


def win_game(canvas:Canvas, guess:str, num:int, row:int, canvas_width:int):
    for index, character in enumerate(guess.lower()):
        green_box(canvas, guess, index, num, row, canvas_width)
    messagebox.showinfo("showinfo", "Congrats!!! You got the correct answer :). Click OK to play again :)")
    
    
def lose_game(canvas: Canvas, guess:str, num:int, row:int, canvas_width:int, wordle_word: str):
    for index, character in enumerate(guess.lower()):
        gray_box(canvas, guess, index, num, row, canvas_width)
    messagebox.showerror("showerror", "Nice Try!! Correct word was " + str(wordle_word))

def restart_game(canvas: Canvas, num:int, row:int, canvas_width:int):
    pass
    




