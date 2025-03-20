import tkinter as tk
fenetre=tk.Tk()
fenetre.title("Testing")

def cliqueCalculer():
    lblReponse1['text'] = "Hey Stop Clicking!"

lblReponse1 = tk.Label(fenetre)
lblReponse1["text"] = "Hello There."
lblReponse1.pack()

btnCalculer1 = tk.Button(fenetre)
btnCalculer1["text"] = " Click Me"
btnCalculer1["font"] = "Arial 11"
btnCalculer1["command"] = cliqueCalculer
btnCalculer1.pack()

fenetre.mainloop()
