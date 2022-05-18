from tkinter import *

window = Tk()
window.geometry('363x311')
window.title('Calculator')
window.resizable(False, False)


def click(item):
	global expression
	expression += str(item)
	input_text.set(expression)


expression = ''
input_text = StringVar


def clear():
	global expression
	expression = ''
	input_text.set('')


def egalitate():
	try:
		global expression
		rezultat = str(eval(expression))
		input_text.set(rezultat)
		expression = ''
	except Exception:
		expression = ''
		input_text.set('Error! Please click C button')

expression = ''
input_text = StringVar()
input_frame = Frame(window, width=312, height=50)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg='#eee', bd=0,
                    justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack()

frame_butoane = Frame(window, width=500, height=300, bg='grey')
frame_butoane.pack()

buton_clear = Button(frame_butoane, text='C', width=39, height=3, bg='#eee', cursor='hand2', command=lambda: clear())
buton_clear.grid(row=0, column=0, columnspan=3)
impartit = Button(frame_butoane, text='/', width=10, height=3, bg='#FF0000', cursor='hand2', command=lambda: click('/'))
impartit.grid(row=0, column=3)
sapte = Button(frame_butoane, text='7', width=12, height=3, bg='#eee', cursor='hand2', command=lambda: click('7'))
sapte.grid(row=1, column=0)
opt = Button(frame_butoane, text='8', width=12, height=3, bg='#eee', cursor='hand2', command=lambda: click('8'))
opt.grid(row=1, column=1)
noua = Button(frame_butoane, text='9', width=12, height=3, bg='#eee', cursor='hand2', command=lambda: click('9'))
noua.grid(row=1, column=2)
inmultit = Button(frame_butoane, text='*', width=10, height=3, bg='#FF0000', cursor='hand2',command=lambda: click('*'))
inmultit.grid(row=1, column=3)
patru = Button(frame_butoane, text='4', width=12, height=3, bg='#eee', cursor='hand2', command=lambda: click('4'))
patru.grid(row=2, column=0)
cinci = Button(frame_butoane, text='5', width=12, height=3, bg='#eee', cursor='hand2', command=lambda: click('5'))
cinci.grid(row=2, column=1)
sase = Button(frame_butoane, text='6', width=12, height=3, bg='#eee', cursor='hand2', command=lambda: click('6'))
sase.grid(row=2, column=2)
minus = Button(frame_butoane, text='-', width=10, height=3, bg='#FF0000', cursor='hand2', command=lambda: click('-'))
minus.grid(row=2, column=3)
unu = Button(frame_butoane, text='1', width=12, height=3, bg='#eee', cursor='hand2', command=lambda: click('1'))
unu.grid(row=3, column=0)
doi = Button(frame_butoane, text='2', width=12, height=3, bg='#eee', cursor='hand2', command=lambda: click('2'))
doi.grid(row=3, column=1)
trei = Button(frame_butoane, text='3', width=12, height=3, bg='#eee', cursor='hand2', command=lambda: click('3'))
trei.grid(row=3, column=2)
plus = Button(frame_butoane, text='+', width=10, height=3, bg='#FF0000', cursor='hand2', command=lambda: click('+'))
plus.grid(row=3, column=3)
zero = Button(frame_butoane, text='0', width=12, height=3, bg='#eee', cursor='hand2', command=lambda: click('0'))
zero.grid(row=4, column=0)
zerozero = Button(frame_butoane, text='00', width=12, height=3, bg='#eee', cursor='hand2', command=lambda: click('00'))
zerozero.grid(row=4, column=1)
virgula = Button(frame_butoane, text='.', width=12, height=3, bg='#eee', cursor='hand2', command=lambda: click('.'))
virgula.grid(row=4, column=2)
egal = Button(frame_butoane, text='=', width=10, height=3, bg='#FF0000', cursor='hand2', command=lambda: egalitate())
egal.grid(row=4, column=3)
window.mainloop()
