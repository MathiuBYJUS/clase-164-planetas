
from tkinter import * 
from PIL import ImageTk, Image
from tkinter import ttk


root = Tk()
root.title("Planet Encyclopedia")
root.geometry("500x500")
root.configure(background="lightblue")

imagen1= ImageTk.PhotoImage(Image.open("earth.jpg"))
imagen2 = ImageTk.PhotoImage(Image.open ("mercury.jpg"))
imagen3= ImageTk.PhotoImage(Image.open("venus.jpg"))

label_1=Label(root,text="Planetas :",bg="lightgreen",font=15)
label_1.place(relx=0.1 , rely=0.1, anchor=CENTER)
label_2=Label(root,text="Planeta", font=("courier",15))
label_2.place(relx=0.2 ,rely=0.3 , anchor=CENTER)
label_3=Label(root,text="",highlightthickness="5",borderwidth=1,bg="gold",relief="solid")
label_3.place(relx=0.5 , rely=0.5, anchor=CENTER)
label_4=Label(root,text="Informacion")
label_4.place(relx=0.5,rely=0.7 , anchor=CENTER)
label_5=Label(root,text="info",bg="lightgreen",font=("arial",10))
label_5.place(relx=0.5 , rely=0.9,anchor=CENTER)

array1=["Mercury","Earth","Venus"]
selectedval = StringVar()
dropdown = ttk.Combobox(root, values = array1, textvariable=selectedval)
dropdown.place(relx=0.4, rely=0.1,anchor=CENTER)
def a():
    b=selectedval.get()
    if b=="Mercury":
        label_2["text"]="Mercurio"
        label_3["image"]=imagen2
        label_4["text"]="Mercurio es el planeta inmediatamente más cercano al Sol y es también el más pequeño de todos los 8 grandes planetas; adquirió esta categoría después de la reclasificación de Plutón como un planeta enano.."
        label_5["text"]="Tiene una órbita muy inclinada y muy elíptica. Es visible desde la Tierra sin telescopio o binoculares, pero debido a su proximidad con el Sol, es realmente difícil identificarlo pese a su brillantez"
        
    if b=="Earth":
        label_2["text"]="Tierra"
        label_3["image"]=imagen1
        label_4["text"]="Hablar de la Tierra implica un número indefinido de palabras y una cantidad de tiempo impresionante. Se sabe mucho sobre ella, y aún así falta demasiado por aprender. Pero es posible condensar lo más importante que de ella se conoce. Los seres humanos necesitamos entender el lugar donde vivimos."
        label_5["text"]=" No solo por simple curiosidad, sino también para ayudarnos a sobrevivir. El planeta Tierra es un conglomerado de elementos dispuestos de tal forma que funcionan como un todo y se sirven entre sí. Los océanos albergan vida animal y vegetal, y al mismo tiempo influyen en el clima de una región. "
    
    if b=="Venus":
        label_2["text"]="Venus"
        label_3["image"]=imagen3
        label_4["text"]="A pesar de que Venus no es el planeta más cercano al Sol, es el más calientes de todos los planetas que conforman el Sistema Solar. "
        label_5["text"]=" Se caracteriza por ser un planta rocoso, sin satélites ni anillos y con una atmósfera muy densa compuesta en mayor proporción de dióxido de carbono."
            

button1=Button(root,text="Dame click para ver la informacion",command=a)
button1.place(relx=0.5,rely=1,anchor=CENTER)
    

root.mainloop()
