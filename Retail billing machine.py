from tkinter import*
from tkinter import messagebox
import random,os,tempfile,smtplib
# functionality Part
def clear():
    bathsoapEntry.delete(0,END)
    bodylotionEntry.delete(0,END)
    facecreamEntry.delete(0,END)
    facewashEntry.delete(0,END)
    hairgelEntry.delete(0,END)
    perfumeEntry.delete(0,END)
    
    daalEntry.delete(0,END)
    oilEntry.delete(0,END)
    riceEntry.delete(0,END)
    sugarEntry.delete(0,END)
    teaEntry.delete(0,END)
    WheatEntry.delete(0,END)
    
    cococolaEntry.delete(0,END)
    dewEntry.delete(0,END)
    frootiEntry.delete(0,END)
    maazaEntry.delete(0,END)
    pepsiEntry.delete(0,END)
    spriteEntry.delete(0,END)
    
    bathsoapEntry.insert(0,0)
    bodylotionEntry.insert(0,0)
    facecreamEntry.insert(0,0)
    facewashEntry.insert(0,0)
    hairgelEntry.insert(0,0)
    perfumeEntry.insert(0,0)
    
    daalEntry.insert(0,0)
    oilEntry.insert(0,0)
    riceEntry.insert(0,0)
    sugarEntry.insert(0,0)
    teaEntry.insert(0,0)
    WheatEntry.insert(0,0)

    cococolaEntry.insert(0,0)
    dewEntry.insert(0,0)
    frootiEntry.insert(0,0)
    maazaEntry.insert(0,0)
    pepsiEntry.insert(0,0)
    spriteEntry.insert(0,0)
    cosmeticpriceEntry.delete(0,END)
    grocerypriceEntry.delete(0,END)
    drinkspriceEntry.delete(0,END)
    
    cosmetictaxEntry.delete(0,END)
    grocerytaxEntry.delete(0,END)
    drinkstaxEntry.delete(0,END)
    
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billnumberEntry.delete(0,END)
    
    textarea.delete(0,END)
    

def send_email():
    def send_gmail():
        try:
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(senderEntry.get(),passwordEntry.get())
            message=email_textarea.get(1.0,END)
            ob.sendmail(senderEntry.get(),recieverEntry.get(),message)
            ob.quit()
            messagebox.showinfo('Success','Bill is successfully sent')
            root1.destroy()
        except:    
            messagebox.showerror('Error','Something went wrong, Please try again',parent=root1)
        
    if textarea.get(1.0,END)=='\n':
      messagebox.showerror('Error','Bill is empty')
    else:
        root1=Toplevel()
        root1.grab_set()
        root1.title('send gmail')
        root1.config(bg='gray20')
        root1.resizable(0,0) 
        
        senderFrame=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        senderFrame.grid(row=0,column=0,padx=40,pady=20)
        
        senderLabel=Label(senderFrame,text="Sender's Email",font=('arial',14,'bold'),bg='gray20',fg='white')
        senderLabel.grid(row=0,column=0,padx=10,pady=8)   
        
        senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10,pady=8)
        
        passwordLabel=Label(senderFrame,text="Password",font=('arial',14,'bold'),bg='gray20',fg='white')
        passwordLabel.grid(row=1,column=0,padx=10,pady=8)   
        
        passwordEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE,show='*')
        passwordEntry.grid(row=1,column=1,padx=10,pady=8)
        
        recipientFrame=LabelFrame(root1,text='RECIPIENT',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        recipientFrame.grid(row=1,column=0,padx=40,pady=20)
        
        recieverLabel=Label(recipientFrame,text="Email Address",font=('arial',14,'bold'),bg='gray20',fg='white')
        recieverLabel.grid(row=0,column=0,padx=10,pady=8)   
        
        recieverEntry=Entry(recipientFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        recieverEntry.grid(row=0,column=1,padx=10,pady=8)
        
        messageLabel=Label(recipientFrame,text="Message",font=('arial',14,'bold'),bg='gray20',fg='white')
        messageLabel.grid(row=1, column=0, padx=10, pady=8)   
        
        email_textarea=Text(recipientFrame,font=('arial',14,'bold'),bd=2,relief=SUNKEN,width=42,height=11)
        email_textarea.grid(row=2, column=0, columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))
        
        sendButton=Button(root1,text='SEND',font=('arial',16,'bold'),width=12,command=send_gmail)
        sendButton.grid(row=2,column=0, pady=30)
        root.mainloop()
        
    

def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')
       


def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==billnumberEntry.get():
           f=open(f'bills/{i}','r')
           textarea.delete(1.0,END)
           for data in f:
               textarea.insert(END,data)
           f.close()
           break
    else:
        messagebox.showerror('Error','Invalid Bill Number')
           

if not os.path.exists('bills'):
    os.mkdir('bills')


def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirm','Do you want to save the bill?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'bill number {billnumber} is saved successfully')
        billnumber=random.randint(500,1000)


billnumber=random.randint(500,1000)

def bill_area():
    if nameEntry.get() == '' or phoneEntry.get() == '':
        messagebox.showerror('Error', 'Customer Details Are Required')
        return

    if cosmeticpriceEntry.get() == '' and grocerypriceEntry.get() == '' and drinkspriceEntry.get() == '':
        messagebox.showerror('Error', 'No Products Are Selected')
        return

    if cosmeticpriceEntry.get() == '0 Rs' and grocerypriceEntry.get() == '0 Rs' and drinkspriceEntry.get() == '0 Rs':
        messagebox.showerror('Error', 'No Products Are Selected')
        return

    # ✅ Clear old text and start fresh
    textarea.delete(1.0, END)
    textarea.insert(END, '\t\t**Welcome Customer**\n')
    textarea.insert(END, f'\nBill Number: {billnumber}')
    textarea.insert(END, f'\nCustomer Name: {nameEntry.get()}')
    textarea.insert(END, f'\nCustomer Phone Number: {phoneEntry.get()}\n')
    textarea.insert(END, '\n=======================================================')
    textarea.insert(END, 'Product\t\t\tQuantity\t\t\tPrice')
    textarea.insert(END, '\n=======================================================')

    # ✅ Cosmetics
    if bathsoapEntry.get() != '0':
        textarea.insert(END, f'\nBath Soap\t\t\t{bathsoapEntry.get()}\t\t\t{soapprice} Rs')
    if bodylotionEntry.get() != '0':
        textarea.insert(END, f'\nBody Lotion\t\t\t{bodylotionEntry.get()}\t\t\t{bodylotionprice} Rs')
    if facecreamEntry.get() != '0':
        textarea.insert(END, f'\nFace Cream\t\t\t{facecreamEntry.get()}\t\t\t{facecreamprice} Rs')
    if facewashEntry.get() != '0':
        textarea.insert(END, f'\nFace Wash\t\t\t{facewashEntry.get()}\t\t\t{facewashprice} Rs')
    if hairgelEntry.get() != '0':
        textarea.insert(END, f'\nHair Gel\t\t\t{hairgelEntry.get()}\t\t\t{hairgelprice} Rs')
    if perfumeEntry.get() != '0':
        textarea.insert(END, f'\nPerfume\t\t\t{perfumeEntry.get()}\t\t\t{perfumeprice} Rs')

    # ✅ Grocery
    if daalEntry.get() != '0':
        textarea.insert(END, f'\nDaal\t\t\t{daalEntry.get()}\t\t\t{daalprice} Rs')
    if oilEntry.get() != '0':
        textarea.insert(END, f'\nOil\t\t\t{oilEntry.get()}\t\t\t{oilprice} Rs')
    if riceEntry.get() != '0':
        textarea.insert(END, f'\nRice\t\t\t{riceEntry.get()}\t\t\t{riceprice} Rs')
    if sugarEntry.get() != '0':
        textarea.insert(END, f'\nSugar\t\t\t{sugarEntry.get()}\t\t\t{sugarprice} Rs')
    if teaEntry.get() != '0':
        textarea.insert(END, f'\nTea\t\t\t{teaEntry.get()}\t\t\t{teaprice} Rs')
    if WheatEntry.get() != '0':
        textarea.insert(END, f'\nWheat\t\t\t{WheatEntry.get()}\t\t\t{Wheatprice} Rs')

    # ✅ Drinks
    if cococolaEntry.get() != '0':
        textarea.insert(END, f'\nCoco Cola\t\t\t{cococolaEntry.get()}\t\t\t{cococolaprice} Rs')
    if dewEntry.get() != '0':
        textarea.insert(END, f'\nDew\t\t\t{dewEntry.get()}\t\t\t{dewprice} Rs')
    if frootiEntry.get() != '0':
        textarea.insert(END, f'\nFrooti\t\t\t{frootiEntry.get()}\t\t\t{frootiprice} Rs')
    if maazaEntry.get() != '0':
        textarea.insert(END, f'\nMazza\t\t\t{maazaEntry.get()}\t\t\t{maazaprice} Rs')
    if pepsiEntry.get() != '0':
        textarea.insert(END, f'\nPepsi\t\t\t{pepsiEntry.get()}\t\t\t{pepsiprice} Rs')
    if spriteEntry.get() != '0':
        textarea.insert(END, f'\nSprite\t\t\t{spriteEntry.get()}\t\t\t{spriteprice} Rs')

    textarea.insert(END, '\n-------------------------------------------------------')

    # ✅ Add Taxes
    if cosmetictaxEntry.get() != '0.0 Rs':
        textarea.insert(END, f'\nCosmetic Tax\t\t\t\t{cosmetictaxEntry.get()}')
    if grocerytaxEntry.get() != '0.0 Rs':
        textarea.insert(END, f'\nGrocery Tax\t\t\t\t{grocerytaxEntry.get()}')
    if drinkstaxEntry.get() != '0.0 Rs':
        textarea.insert(END, f'\nSoft Drinks Tax\t\t\t\t{drinkstaxEntry.get()}')

    textarea.insert(END, f'\n\nTotal Bill \t\t\t\t {totalbill} Rs')
    textarea.insert(END, '\n-------------------------------------------------------')

    # ✅ Save automatically
    save_bill()
            
def get_value(value):
        if value == '' or not value.isdigit():
           return 0
        return int(value)


def total():
    global soapprice,bodylotionprice,facecreamprice,facewashprice,hairgelprice,perfumeprice
    global daalprice,oilprice,riceprice,sugarprice,teaprice,Wheatprice
    global cococolaprice,dewprice,frootiprice,maazaprice,pepsiprice,spriteprice
    global totalbill
    # cosmetic price calculation
    soapprice=get_value(bathsoapEntry.get())*20
    bodylotionprice=get_value(bodylotionEntry.get())*60                 
    facecreamprice=get_value(facecreamEntry.get())*50                  
    facewashprice=get_value(facewashEntry.get())*100                   
    hairgelprice=get_value(hairgelEntry.get())*80
    perfumeprice=get_value(perfumeEntry.get())*180
    
    totalcosmeticprice=soapprice+bodylotionprice+facecreamprice+facewashprice+hairgelprice+perfumeprice
    cosmeticpriceEntry.delete(0,END)
    cosmeticpriceEntry.insert(0,f'{totalcosmeticprice} Rs')
    
    cosmetictax=totalcosmeticprice*0.12
    cosmetictaxEntry.delete(0,END)
    cosmetictaxEntry.insert(0,str(cosmetictax)+' Rs')
    
    # grocery price calculation
    daalprice=int(daalEntry.get())*100
    oilprice=int(oilEntry.get())*120
    riceprice=int(riceEntry.get())*50
    sugarprice=int(sugarEntry.get())*80
    teaprice=int(teaEntry.get())*140
    Wheatprice=int(WheatEntry.get())*90
    
    totalgroceryprice=daalprice+oilprice+riceprice+sugarprice+teaprice+Wheatprice
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,f'{totalgroceryprice} Rs')
    
    grocerytax=totalgroceryprice*0.05
    grocerytaxEntry.delete(0,END)
    grocerytaxEntry.insert(0,str(grocerytax)+' Rs')
    
    # drinks price calculation
    cococolaprice=int(cococolaEntry.get())*100
    dewprice=int(dewEntry.get())*120
    frootiprice=int(frootiEntry.get())*50
    maazaprice=int(maazaEntry.get())*80
    pepsiprice=int(pepsiEntry.get())*140
    spriteprice=int(spriteEntry.get())*90
    
    totaldrinksprice=cococolaprice+dewprice+frootiprice+maazaprice+pepsiprice+spriteprice
    drinkspriceEntry.delete(0,END)
    drinkspriceEntry.insert(0,f'{totaldrinksprice} Rs')
    
    drinkstax=totaldrinksprice*0.08
    drinkstaxEntry.delete(0,END)
    drinkstaxEntry.insert(0,str(drinkstax)+' Rs')

    totalbill=totalcosmeticprice+totalgroceryprice+totaldrinksprice+cosmetictax+grocerytax+drinkstax


# GUI Part
root=Tk()
root.title('RETAIL BILLING SYSTEM')
root.geometry('1270x685')
root.iconbitmap('icon-ico.ico')
headinglabel=Label(root,text='RETAIL BILLING SYSTEM',font=('times new roman',50,'bold'),bg='grey20',fg='white',bd=12,relief=RIDGE)
headinglabel.pack(fill=X)
   

customer_details_frame=LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
customer_details_frame.pack(fill=X,pady=5)

namelabel=Label(customer_details_frame,text='Name',font=('times new roman',15,'bold'),bg='grey20',fg='white')
namelabel.grid(row=0,column=0,padx=20)

nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phonelabel=Label(customer_details_frame,text='Phone Number',font=('times new roman',15,'bold'),bg='grey20',fg='white')
phonelabel.grid(row=0,column=2,padx=20,pady=5)

phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberlabel=Label(customer_details_frame,text='Bill Number',font=('times new roman',15,'bold'),bg='grey20',fg='white')
billnumberlabel.grid(row=0,column=4,padx=20,pady=5)

billnumberEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,width=10,command=search_bill)
searchButton.grid(row=0,column=6,padx=20,pady=8)

productsFrame=Frame(root)
productsFrame.pack(pady=2)

cosmeticsFrame=LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
cosmeticsFrame.grid(row=0,column=0)

bathsoaplabel=Label(cosmeticsFrame,text='Bath Soap',font=('times new roman',15,'bold'),bg='grey20',fg='white')
bathsoaplabel.grid(row=0,column=0,pady=5,padx=10,sticky='w')

bathsoapEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=5,padx=10)
bathsoapEntry.insert(0,0)

bodylotionlabel=Label(cosmeticsFrame,text='Body Lotion',font=('times new roman',15,'bold'),bg='grey20',fg='white')
bodylotionlabel.grid(row=1,column=0,pady=5,padx=10,sticky='w')

bodylotionEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bodylotionEntry.grid(row=1,column=1,pady=5,padx=10)
bodylotionEntry.insert(0,0)

facecreamlabel=Label(cosmeticsFrame,text='Face Cream',font=('times new roman',15,'bold'),bg='grey20',fg='white')
facecreamlabel.grid(row=2,column=0,pady=5,padx=10,sticky='w')

facecreamEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facecreamEntry.grid(row=2,column=1,pady=5,padx=10)
facecreamEntry.insert(0,0)

facewashlabel=Label(cosmeticsFrame,text='Face Wash',font=('times new roman',15,'bold'),bg='grey20',fg='white')
facewashlabel.grid(row=3,column=0,pady=5,padx=10,sticky='w')

facewashEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facewashEntry.grid(row=3,column=1,pady=5,padx=10)
facewashEntry.insert(0,0)

hairgellabel=Label(cosmeticsFrame,text='Hair Gel',font=('times new roman',15,'bold'),bg='grey20',fg='white')
hairgellabel.grid(row=4,column=0,pady=5,padx=10,sticky='w')

hairgelEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairgelEntry.grid(row=4,column=1,pady=5,padx=10)
hairgelEntry.insert(0,0)

perfumelabel=Label(cosmeticsFrame,text='Perfume',font=('times new roman',15,'bold'),bg='grey20',fg='white')
perfumelabel.grid(row=5,column=0,pady=5,padx=10,sticky='w')

perfumeEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
perfumeEntry.grid(row=5,column=1,pady=5,padx=10)
perfumeEntry.insert(0,0)

groceryFrame=LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
groceryFrame.grid(row=0,column=1)

daallabel=Label(groceryFrame,text='Daal',font=('times new roman',15,'bold'),bg='grey20',fg='white')
daallabel.grid(row=0,column=0,pady=5,padx=10,sticky='w')

daalEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
daalEntry.grid(row=0,column=1,pady=5,padx=10)
daalEntry.insert(0,0)

oillabel=Label(groceryFrame,text='Oil',font=('times new roman',15,'bold'),bg='grey20',fg='white')
oillabel.grid(row=1,column=0,pady=5,padx=10,sticky='w')

oilEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
oilEntry.grid(row=1,column=1,pady=5,padx=10)
oilEntry.insert(0,0)

ricelabel=Label(groceryFrame,text='Rice',font=('times new roman',15,'bold'),bg='grey20',fg='white')
ricelabel.grid(row=2,column=0,pady=5,padx=10,sticky='w')

riceEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
riceEntry.grid(row=2,column=1,pady=5,padx=10)
riceEntry.insert(0,0)

sugarlabel=Label(groceryFrame,text='Sugar',font=('times new roman',15,'bold'),bg='grey20',fg='white')
sugarlabel.grid(row=3,column=0,pady=5,padx=10,sticky='w')

sugarEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
sugarEntry.grid(row=3,column=1,pady=5,padx=10)
sugarEntry.insert(0,0)

tealabel=Label(groceryFrame,text='Tea',font=('times new roman',15,'bold'),bg='grey20',fg='white')
tealabel.grid(row=4,column=0,pady=5,padx=10,sticky='w')

teaEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
teaEntry.grid(row=4,column=1,pady=5,padx=10)
teaEntry.insert(0,0)

Wheatlabel=Label(groceryFrame,text='Wheat',font=('times new roman',15,'bold'),bg='grey20',fg='white')
Wheatlabel.grid(row=5,column=0,pady=5,padx=10,sticky='w')

WheatEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
WheatEntry.grid(row=5,column=1,pady=5,padx=10)
WheatEntry.insert(0,0)

drinksFrame=LabelFrame(productsFrame,text='Soft Drinks',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
drinksFrame.grid(row=0,column=2)

cococolalabel=Label(drinksFrame,text='Coco Cola',font=('times new roman',15,'bold'),bg='grey20',fg='white')
cococolalabel.grid(row=0,column=0,pady=5,padx=10,sticky='w')

cococolaEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
cococolaEntry.grid(row=0,column=1,pady=5,padx=10)
cococolaEntry.insert(0,0)

dewlabel=Label(drinksFrame,text='Dew',font=('times new roman',15,'bold'),bg='grey20',fg='white')
dewlabel.grid(row=1,column=0,pady=5,padx=10,sticky='w')

dewEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
dewEntry.grid(row=1,column=1,pady=5,padx=10)
dewEntry.insert(0,0)

frootilabel=Label(drinksFrame,text='Frooti',font=('times new roman',15,'bold'),bg='grey20',fg='white')
frootilabel.grid(row=2,column=0,pady=5,padx=10,sticky='w')

frootiEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
frootiEntry.grid(row=2,column=1,pady=5,padx=10)
frootiEntry.insert(0,0)

mazzalabel=Label(drinksFrame,text='Mazza',font=('times new roman',15,'bold'),bg='grey20',fg='white')
mazzalabel.grid(row=3,column=0,pady=5,padx=10,sticky='w')

maazaEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
maazaEntry.grid(row=3,column=1,pady=5,padx=10)
maazaEntry.insert(0,0)

pepsilabel=Label(drinksFrame,text='Pepsi',font=('times new roman',15,'bold'),bg='grey20',fg='white')
pepsilabel.grid(row=4,column=0,pady=5,padx=10,sticky='w')

pepsiEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
pepsiEntry.grid(row=4,column=1,pady=5,padx=10)
pepsiEntry.insert(0,0)

spritelabel=Label(drinksFrame,text='Sprite',font=('times new roman',15,'bold'),bg='grey20',fg='white')
spritelabel.grid(row=5,column=0,pady=5,padx=10,sticky='w')

spriteEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
spriteEntry.grid(row=5,column=1,pady=5,padx=10)
spriteEntry.insert(0,0)

billframe=Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3)

billarealabel=Label(billframe,text='Bill Area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billarealabel.pack(fill=BOTH,expand=True)

scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

textarea=Text(billframe,height=15,width=55,yscrollcommand=scrollbar.set)
textarea.pack(side=LEFT ,fill=BOTH, expand=True)
scrollbar.config(command=textarea.yview)

billmenuFrame=LabelFrame(root,text='Bill Menu',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
billmenuFrame.pack()

cosmeticpricelabel=Label(billmenuFrame,text='Cosmetic Price',font=('times new roman',13,'bold'),bg='grey20',fg='white')
cosmeticpricelabel.grid(row=0,column=0,pady=3,padx=10,sticky='w')

cosmeticpriceEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=12,bd=5)
cosmeticpriceEntry.grid(row=0,column=1,pady=3,padx=10)

grocerypricelabel=Label(billmenuFrame,text='Grocery Price',font=('times new roman',13,'bold'),bg='grey20',fg='white')
grocerypricelabel.grid(row=1,column=0,pady=3,padx=10,sticky='w')

grocerypriceEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=12,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=3,padx=10)

drinkspricelabel=Label(billmenuFrame,text='Soft Drinks Price',font=('times new roman',13,'bold'),bg='grey20',fg='white')
drinkspricelabel.grid(row=2,column=0,pady=3,padx=10,sticky='w')

drinkspriceEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=12,bd=5)
drinkspriceEntry.grid(row=2,column=1,pady=3,padx=10)

cosmetictaxlabel=Label(billmenuFrame,text='Cosmetic Tax',font=('times new roman',13,'bold'),bg='grey20',fg='white')
cosmetictaxlabel.grid(row=0,column=2,pady=3,padx=10,sticky='w')

cosmetictaxEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=12,bd=5)
cosmetictaxEntry.grid(row=0,column=3,pady=3,padx=10)

grocerytaxlabel=Label(billmenuFrame,text='Grocery Tax',font=('times new roman',13,'bold'),bg='grey20',fg='white')
grocerytaxlabel.grid(row=1,column=2,pady=3,padx=10,sticky='w')

grocerytaxEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=12,bd=5)
grocerytaxEntry.grid(row=1,column=3,pady=3,padx=10)

drinkstaxlabel=Label(billmenuFrame,text='Soft Drinks Tax',font=('times new roman',13,'bold'),bg='grey20',fg='white')
drinkstaxlabel.grid(row=2,column=2,pady=3,padx=10,sticky='w')

drinkstaxEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=12,bd=5)
drinkstaxEntry.grid(row=2,column=3,pady=3,padx=10)

buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton=Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='grey20',fg='white',bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)

billButton=Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='grey20',fg='white',bd=5,width=8,pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=5)

emailButton=Button(buttonFrame,text='Email',font=('arial',16,'bold'),bg='grey20',fg='white',bd=5,width=8,pady=10,command=send_email)
emailButton.grid(row=0,column=2,pady=20,padx=5)

printButton=Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='grey20',fg='white',bd=5,width=8,pady=10,command=print_bill)
printButton.grid(row=0,column=3,pady=20,padx=5)

clearButton=Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='grey20',fg='white',bd=5,width=8,pady=10,command=clear)
clearButton.grid(row=0,column=4,pady=20,padx=5)

root.mainloop()