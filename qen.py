from tkinter import filedialog as fd
from tkinter import *
from cryptography.fernet import Fernet
import os
import sys

class UI:
	def __init__(self, master):
		self.master = master
		self.key = ""
		self.file = ""
		Label(self.master, text="Key: ").grid(row=0, column=0, padx=5, pady=10)
		Label(self.master, text="File: ").grid(row=1, column=0, padx=5, pady=10)
		self.kLabel = Label(self.master, text="No key file selected")
		self.kLabel.grid(row=0, column=1, padx=5, pady=10)
		self.fLabel = Label(self.master, text="No input file selected")
		self.fLabel.grid(row=1, column=1, padx=5, pady=10)
		self.kButton = Button(self.master, text="Open key", height = 2, width = 10, command=lambda: self.getAddress('k'))
		self.kButton.grid(row=0, column=2, padx=5, pady=10)
		self.fButton = Button(self.master, text="Open file", height = 2, width = 10, command=lambda: self.getAddress('f'))
		self.fButton.grid(row=1, column=2, padx=5, pady=10)

		Button(self.master, text="Encrypt", height = 2, width = 10, command=self.encrypt).grid(row=3, column=0, padx=5, pady=10)
		Button(self.master, text="Generate key", height = 2, width = 10, command=self.generateKey).grid(row=3, column=1, padx=5, pady=10)
		Button(self.master, text="Decrypt", height = 2, width = 10, command=self.decrypt).grid(row=3, column=2, padx=5, pady=10)


	def getAddress(self, object):
		fileAddress = fd.askopenfilename()
		if object == 'k':
			with open(fileAddress, "rb") as keyFile:
				self.key = keyFile.read()
			self.f = Fernet(self.key)
			self.kLabel['text'] = fileAddress
		
		elif object == 'f':
			self.file = fileAddress
			self.fLabel['text'] = fileAddress


	def encrypt(self):
		f = Fernet(self.key)
		with open(self.fLabel['text'], "rb") as file_d:
			e_data = f.encrypt(file_d.read())
		with open(self.fLabel['text'], "wb") as file_d:
			file_d.write(e_data)

	def decrypt(self):
		f = Fernet(self.key)
		with open(self.file, "rb") as file_d:
			d_data = f.decrypt(file_d.read())
		with open(self.file, "wb") as file_d:
			file_d.write(d_data)

	def generateKey(self):
		self.win = Toplevel(self.master)
		self.name = Entry(self.win)
		self.name.grid(row=0, column=1)
		Label(self.win, text="New keys name: ").grid(row=0, column=0)
		self.changeAddress = Checkbutton(self.win, text="Local folder", variable=changeAddressState, onvalue=1, offvalue=0, command=self.updateEntry)
		changeAddressState.set(1)
		self.changeAddress.grid(row=2, column=0)
		self.address = Entry(self.win, state='disabled')
		self.address.grid(row=1, column=1)
		Label(self.win, text="New keys location: ").grid(row=1, column=0)
		self.cancel = Button(self.win, text="Cancel", command=self.win.destroy)
		self.cancel.grid(row=3, column=0)
		self.generate = Button(self.win, text="Generate key", command=self.saveKey)
		self.generate.grid(row=3, column=1)
		self.win.grid()

	def saveKey(self):
		newKey = Fernet.generate_key()
		keyAddress = ""
		if changeAddressState.get():
			keyAddress += self.name.get() + ".key"
		else:
			keyAddress += self.address.get() + "/" + self.name.get() + ".key"
			if not os.path.exists(self.address.get()):
				os.mkdir(os.getcwd()+ "\\"  + self.address.get() + "\\" )

		with open(keyAddress, "wb") as keyA:
			keyA.write(newKey)
		
		self.win.destroy()

	def updateEntry(self):
		if changeAddressState.get() == 1:
			self.address.config(state='disabled')
		else:
			self.address.config(state='normal')



Root = Tk()

changeAddressState = BooleanVar()
changeAddressState.set(0)

gui = UI(Root)

Root.mainloop()
