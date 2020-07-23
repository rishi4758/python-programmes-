import tkinter as Tk
import random
import math
def ok():
 optimized_root = Tk.Tk()
 optimized_canvas = Tk.Canvas(optimized_root)

 optimized_root.pack(fill=Tk.BOTH, expand=1)
 optimized_image = second.create_image(0, 0, anchor=Tk.NW, image=background_image)
 optimized_root.wm_geometry("794x370")
 optimized_root.title('Optimized Map')
 optimized_root.mainloop()



root = Tk.Tk()
canvas = Tk.Canvas(root)
background_image=Tk.PhotoImage(file="Screenshot (122).gif")
canvas.pack(fill=Tk.BOTH, expand=1) # Stretch canvas to root window size.
image = canvas.create_image(0, 0, anchor=Tk.NW, image=background_image)
root.wm_geometry("794x370")
root.title('First')

ok=Tk.Button(root,text='ok',command=ok)
cancel=Tk.Button(root,text='Cancel')
cancel.Tk.pack()
ok.Tk.pack()

root.mainloop()

