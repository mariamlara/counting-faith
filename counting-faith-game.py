

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
# please install pillow on your laptop to run this using the below command -Lara
# pip install pillow
#############################################################################
class StoryGame:
    def __init__(self, master):
        self.master = master
        master.title("Interactive Space Adventure")
        master.geometry("800x600")

        # Top frame for images
        self.image_frame = tk.Frame(master, height=400, width=800, bg='black')
        self.image_frame.pack(side=tk.TOP, fill=tk.X)
        
        # Label for displaying images
        self.image_label = tk.Label(self.image_frame, bg='black')
        self.image_label.pack(expand=True)

        # Bottom frame for dialog and input
        self.dialog_frame = tk.Frame(master, height=200, width=800, bg='gray')
        self.dialog_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Dialog text
        self.dialog_text = tk.Label(self.dialog_frame, text="", wraplength=700, font=("Arial", 12))
        self.dialog_text.pack(pady=10)

        # User input
        self.input_var = tk.StringVar()
        self.input_entry = tk.Entry(self.dialog_frame, textvariable=self.input_var, width=50)
        self.input_entry.pack(pady=10)

        # Submit button
        self.submit_button = tk.Button(self.dialog_frame, text="Submit", command=self.process_input)
        self.submit_button.pack(pady=10)

        # Game state variables
        self.player_name = ""
        self.friend_name = ""
        self.current_stage = ""
        self.tries = 5

        # Starting the game
        self.start_game()
##################################################################################################################

    def load_image(self, image_path):
        """Dynamically load and display an image"""
        try:
            
            original_image = Image.open(image_path)
            original_image = original_image.resize((600, 350), Image.LANCZOS)
            photo = ImageTk.PhotoImage(original_image)
            self.image_label.config(image=photo)
            self.image_label.image = photo  
        except Exception as e:
            print(f"Error loading image: {e}")
            self.image_label.config(image='')

    def start_game(self):
        """Initial game setup"""
        self.dialog_text.config(text="The interdimensional police station buzzed with strange energy as you arrived.\n"
                                "You are here to find your friend and bring them back to Earth.\n"
                                "You suspect that your friend got lost in time-dilation during their mission near the black-hole.\n"
                                "The police asks your name: ")
        self.current_stage = "get_player_name"
        self.load_image("assets/pic1.JPG")  

    def process_input(self):
        """Process user input based on current game stage"""
        user_input = self.input_var.get().strip()
        
        if self.current_stage == "get_player_name":
            if user_input:
                self.player_name = user_input
                self.dialog_text.config(text=f"Hi {self.player_name}! What is your friend's name:")
                self.current_stage = "get_friend_name"
                self.input_var.set("")
                self.load_image("assets/pic2.jpg")

        elif self.current_stage == "get_friend_name":
            if user_input:
                self.load_image("")
                self.friend_name = user_input
                self.dialog_text.config(text=f"The officer tells you that {self.friend_name} is at a restaurant located somewhere in the “✨7th Starlit Labyrinth” galaxy, which is currently out of their jurisdiction."
                                        "So you have to take matters into your own hands.\n"
                                        "Before you leave, the officer hands you a note and tells you to keep count of EVERYTHING.\n"
                                        "Type “open” to read it:")
                self.current_stage = "note"
                self.input_var.set("")
                self.load_image("assets/pic4.jpg")


        elif self.current_stage == "note":
            self.load_image("")
            if user_input.lower() == "open":
                self.dialog_text.config(text=f"The note says the following: there are ✨3 rules; \n- don't drink the water,\n- dont order off the menu,\n- don't talk to anyone....your friend is in the kitchen\nType “okay” to continue:")
                self.current_stage = "post_note"
                self.input_var.set("")
                self.load_image("assets/pic3.jpg")
            else:
                self.dialog_text.config(text="Please type 'open'")
                self.input_var.set("")
                self.load_image("assets/pic13.jpg")

        elif self.current_stage == "post_note":
            self.load_image("assets/pic12.jpg")
            if user_input.lower() == "okay":
                self.dialog_text.config(text=f"You arrive at the '✨Nine Planets Cafe'.\n"
                                        "Type 'go' to step inside or 'nope' to leave:")
                self.current_stage = "first_scene"
                self.input_var.set("")
            else:
                self.dialog_text.config(text="Please type 'okay'")
                self.input_var.set("")
                self.load_image("assets/pic9.jpg")

        elif self.current_stage == "first_scene":
            self.load_image("")
            if user_input.lower() == "go":
                self.dialog_text.config(text="The waiter at the diner has no face, only a mouth full of ✨2 sharp and shiny teeth."
                                        "He hands you the menu. What do you do?"
                                        "(a) eat\n"
                                        "(b) say you don't want it\n"
                                        "(c) smile and keep the food but don’t eat it\n")
                self.current_stage = "diner_scene"
                self.input_var.set("")
                self.load_image("assets/pic8.jpg")

            elif user_input.lower() == "nope":
                self.dialog_text.config(text="wow your friend must be proud :< go leave\nGAME OVER")
                self.current_stage = "quit"
                self.input_var.set("")
                self.load_image("assets/pic10.jpg")
            else:
                self.dialog_text.config(text="Please choose 'go' or 'nope'.")
                self.input_var.set("")
                self.load_image("assets/pic8.jpg")
            

        elif self.current_stage == "diner_scene":
            self.load_image("")
            if user_input.lower() == "a":
                self.dialog_text.config(text="As you’re eating the food, you see some eyeballs pop up in your soup but you survive ^o^.\n Press submit to proceed")
                self.current_stage = "pre_spider_scene"
                
                
            elif user_input.lower() == "b":
                self.dialog_text.config(text="They suspect you and capture you. You failed your mission X_X\n")
                self.current_stage = "pre_spider_scene"
            elif user_input.lower() == "c":
                self.dialog_text.config(text="The waiter is getting suspicious but you survived for now ;_;\n press submit to proceed")
                self.current_stage = "pre_spider_scene"
            else:
                self.dialog_text.config(text="Please choose 'a', 'b', 'c'.")
            self.input_var.set("")
            self.load_image("assets/pic5.png")

        elif self.current_stage == "pre_spider_scene":
            self.load_image("")
            if user_input.lower() == "":
                self.dialog_text.config(text="You see another customer, which is a spider with ✨5 legs, walking toward the kitchen.\n"
                                        "The waiter’s back is turned.\n What do you do?\n"
                                        "(a) stay in your seat\n "
                                        "(b) ask the spider if it knows where your friend is\n"
                                        "(c) follow the spider to the kitchen\n")
            else:
                self.dialog_text.config(text="Please choose 'a', 'b', 'c'.")
            self.current_stage = "spider_scene"
            self.input_var.set("")
            self.load_image("assets/pic6.jpg")

        elif self.current_stage == "spider_scene":
            self.load_image("")
            if user_input.lower() == "a":
                self.dialog_text.config(text="The spider came back to get you.\n The waiter saw this and got suspicious and captured both of you.\n Game over\n")
                self.current_stage = "quit"
                self.load_image("assets/pic14.jpg")
            elif user_input.lower() == "b":
                self.dialog_text.config(text="Everyone in the diner heard it and they captured you. Game over X_X")
                self.current_stage = "quit"
                self.load_image("assets/pic14.jpg")
            elif user_input.lower() == "c":
                self.dialog_text.config(text=f"Congrats! You made it to the kitchen.\n You see your friend trapped in a cage with other animals.\n The cage requires a 5 digit pin.\n What do you think the pin is?(5 tries):\n")
                self.current_stage = "code_game"
                self.load_image("assets/pic11.jpg")
            else:
                self.dialog_text.config(text="Please choose 'a', 'b', 'c'.")
                self.current_stage = "spider_scene"
                self.load_image("assets/pic11.jpg")
            self.input_var.set("")

        elif self.current_stage == "code_game":
            self.load_image("")
            if user_input.lower() == "73925":
                self.dialog_text.config(text="Yay you have found your friend\n YOU WON!")
                self.current_stage = "quit"
                
            else:
                self.tries= self.tries - 1
                if self.tries == 0:
                    self.dialog_text.config(text="NO more tries\n GAME OVER")
                    self.current_stage = "quit"
                else:
                    self.dialog_text.config(text=f"you have {self.tries} more tires left. Think harder!")
                    self.current_stage = "code_game"
            self.input_var.set("")
            self.load_image("assets/pic7.jpg")
    
        elif self.current_stage == "quit":
            raise SystemExit
        
        elif self.current_stage == "pre_quit":
            self.load_image("")
            self.dialog_text.config(text="close the window")
            self.current_stage = "quit"
            raise SystemExit

def main():
    root = tk.Tk()
    game = StoryGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()

