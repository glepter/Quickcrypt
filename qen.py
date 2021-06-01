from tkinter import filedialog as fd
from tkinter import *
from cryptography.fernet import Fernet
import sys


def getAddress(object):
	fileAddress = fd.askopenfilename()
	if object == 'k':
		with open(fileAddress, "rb") as keyFile:
			key.set(keyFile.read())
		kLabel['text'] = fileAddress
	elif object == 'f':
		file = fileAddress
		print(file)
		fLabel['text'] = file


def encrypt():
	f = Fernet(key.get())
	with open(fLabel['text'], "rb") as file_d:
		e_data = f.encrypt(file_d.read())
	with open(fLabel['text'], "wb") as file_d:
		file_d.write(e_data)

def decrypt():
	f = Fernet(key.get())
	with open(file, "rb") as file_d:
		d_data = f.decrypt(file_d.read())
	with open(file, "wb") as file_d:
		file_d.write(d_data)
def generateKey():
	win = Toplevel(Root)
	name = Entry(win, show="Enter key name")
	name.grid(row=0, column=1)
	changeAddress = Checkbutton(win, text="Local folder", variable=changeAddressState, onvalue=1, offvalue=0, command=updateEntry)
	changeAddress.grid(row=2, column=0)
	address = Entry(win, state='disabled')
	address.grid(row=1, column=1)
	cancel = Button(win, text="Cancel", command=win.destroy)
	cancel.grid(row=0, column=3)
	generate = Button(win, text="Generate key", command=saveKey)
	win.grid()

def saveKey(condition):
	newKey = Fernet.generate_key()
	keyAddress = ""
	if changeAddressState.get():
		keyAddress += name.get()
	else:
		keyAddress += address.get() + name.get() + ".key"
	with open(keyAddress, "wb") as keyA:
		keyA.write(newKey)
	win.destroy()

def updateEntry():
	if changeAddressState.get():
		address.config(state='disabled')
	else:
		address.config(state='enabled')

class UI:
	def __init__(self, master):
		self.master = master
		Label(Root, text="Key: ").grid(row=1, column=0)
		Label(Root, text="File: ").grid(row=2, column=0)
		self.kLabel = Label(Root, text="No key file selected")
		self.kLabel.grid(row=1, column=2)
		self.fLabel = Label(Root, text="No input file selected")
		self.fLabel.grid(row=2, column=2)
		self.kButton = Button(Root, text="Open key", command=lambda: getAddress('k'))
		self.kButton.grid(row=1, column=3)
		self.fButton = Button(Root, text="Open file", command=lambda: getAddress('f'))
		self.fButton.grid(row=2, column=3)

		Button(Root, text="Encrypt", command=self.encrypt).grid(row=3, column=0)
		Button(Root, text="Generate key", command=self.generateKey).grid(row=3, column=1)
		Button(Root, text="Decrypt", command=self.decrypt).grid(row=3, column=2)




Root = Tk()

key = StringVar()
changeAddressState = BooleanVar()
changeAddressState.set(0)

gui = UI(Root)

Root.mainloop()
