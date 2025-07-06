from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox

root = Tk()
root.geometry('1600x1000')

customer_name = StringVar()
customer_phone = StringVar()
bill_no = StringVar()


Bath_Soap =IntVar()
Face_Cream=IntVar()
Face_Wash=IntVar()
Hair_Spray=IntVar()
Body_Lotion=IntVar()
Rice=IntVar()
Food_Oil=IntVar()
Daal=IntVar()
Wheat=IntVar()
Sugar=IntVar()
Maza=IntVar()
Coke=IntVar()
Frooti=IntVar()
Nimkos=IntVar()
Biscuits=IntVar()

total_cosmetics=IntVar()
total_grocery=IntVar()
other_total=IntVar()
cosmetics_tax=IntVar()
grocery_tax=IntVar()
other_tax=IntVar()


# Bath_Soap= 40
# Face_Cream=140
# Face_Wash=240
# Hair_Spray=160
# Body_Lotion=260
# Rice=80
# Food_Oil=360
# Daal=90
# Wheat=60
# Sugar=170
# Maza = 70
# Coke = 60
# Frooti = 50
# Nimkos = 30
# Biscuits = 25

PRICES = {
    "Bath_Soap": 40,
    "Face_Cream": 140,
    "Face_Wash": 240,
    "Hair_Spray": 160,
    "Body_Lotion": 260,
    "Rice": 80,
    "Food_Oil": 360,
    "Daal": 90,
    "Wheat": 60,
    "Sugar": 170,
    "Maza": 70,
    "Coke": 60,
    "Frooti": 50,
    "Nimkos": 30,
    "Biscuits": 25
}

bg_color = '#003366'
fg_color = 'white'
entry_bg = '#e6f2ff'
btn_color = '#0059b3'

def safe_int(var):
    try:
        return int(str(var.get()).lstrip('0') or '0')
    except:
        return 0

def calculate_total():
    cosmetic_sum = (
        safe_int(Bath_Soap) * PRICES["Bath_Soap"] +
        safe_int(Face_Cream) * PRICES["Face_Cream"] +
        safe_int(Face_Wash) * PRICES["Face_Wash"] +
        safe_int(Hair_Spray) * PRICES["Hair_Spray"] +
        safe_int(Body_Lotion) * PRICES["Body_Lotion"]
    )
    tax_cos = round(cosmetic_sum * 0.05)

    grocery_sum = (
        safe_int(Rice) * PRICES["Rice"] +
        safe_int(Food_Oil) * PRICES["Food_Oil"] +
        safe_int(Daal) * PRICES["Daal"] +
        safe_int(Wheat) * PRICES["Wheat"] +
        safe_int(Sugar) * PRICES["Sugar"]
    )
    tax_groc = round(grocery_sum * 0.05)

    snack_sum = (
        safe_int(Maza) * PRICES["Maza"] +
        safe_int(Coke) * PRICES["Coke"] +
        safe_int(Frooti) * PRICES["Frooti"] +
        safe_int(Nimkos) * PRICES["Nimkos"] +
        safe_int(Biscuits) * PRICES["Biscuits"]
    )
    tax_snack = round(snack_sum * 0.05)

    total_cosmetics.set(f"{cosmetic_sum} Rs")
    cosmetics_tax.set(f"{tax_cos} Rs")
    total_grocery.set(f"{grocery_sum} Rs")
    grocery_tax.set(f"{tax_groc} Rs")
    other_total.set(f"{snack_sum} Rs")
    other_tax.set(f"{tax_snack} Rs")

    
    
    
def clear_data():
    # Clear all product quantities
    product_vars = [
        Bath_Soap, Face_Cream, Face_Wash, Hair_Spray, Body_Lotion,
        Rice, Food_Oil, Daal, Wheat, Sugar,
        Maza, Coke, Frooti, Nimkos, Biscuits
    ]
    
    for var in product_vars:
        var.set(0)

    # Clear totals and taxes
    bill_vars = [
        total_cosmetics, cosmetics_tax,
        total_grocery, grocery_tax,
        other_total, other_tax
    ]
    
    for var in bill_vars:
        var.set("")

    # Clear customer info and bill area
    customer_name.set("")
    customer_phone.set("")
    bill_no.set("")
    bill_text.delete('1.0', END)

    
frame1 = Frame(root, background='#003366', height=80, bd=7, relief=GROOVE)
frame1.pack(side=TOP, fill=X)
Label(frame1, text="BILLING SOFTWARE", font=('Arial', 20, 'bold'), bg='#003366', fg='white').pack()


cust_frame = LabelFrame(root, text="Customer Details", font=('Arial', 12, 'bold'), bg=bg_color, fg=fg_color, bd=5, relief=GROOVE)
cust_frame.pack(fill=X, padx=20, pady=5)

Label(cust_frame, text="Customer Name", bg=bg_color, fg=fg_color, font=('Arial', 12)).grid(row=0, column=0, padx=10, pady=5)
Entry(cust_frame, textvariable=customer_name, font=('Arial', 12), bg=entry_bg, width=20).grid(row=0, column=1, padx=10)

Label(cust_frame, text="Phone No", bg=bg_color, fg=fg_color, font=('Arial', 12)).grid(row=0, column=2, padx=10)
Entry(cust_frame, textvariable=customer_phone, font=('Arial', 12), bg=entry_bg, width=20).grid(row=0, column=3, padx=10)

Label(cust_frame, text="Bill No", bg=bg_color, fg=fg_color, font=('Arial', 12)).grid(row=0, column=4, padx=10)
Entry(cust_frame, textvariable=bill_no, font=('Arial', 12), bg=entry_bg, width=20).grid(row=0, column=5, padx=10)

# Main Frame for product categories
main = Frame(root, bg='#003366', bd=10, relief=GROOVE)
main.pack(fill=BOTH)

# Cosmetic frame
cosmetic_frame = Frame(main, bg='#003366', bd=8, relief=GROOVE, height=450)
cosmetic_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")
# cosmetic_frame.pack(side=LEFT)

Label(cosmetic_frame, text="Bath Soap", font=('Arial', 12), bg='#003366', fg='white').grid(row=0, column=0, padx=10, pady=8)
Entry(cosmetic_frame, textvariable=Bath_Soap, width=15, font=('Arial', 20), bg='#f1f3f5', bd=2, relief=SOLID).grid(row=0, column=1, padx=10, pady=8)

Label(cosmetic_frame, text="Face Cream", font=('Arial', 12), bg='#003366', fg='white').grid(row=1, column=0, padx=10, pady=8)
Entry(cosmetic_frame, textvariable=Face_Cream, width=15, font=('Arial', 20), bg='#f1f3f5', bd=2, relief=SOLID).grid(row=1, column=1, padx=10, pady=8)

Label(cosmetic_frame, text="Face Wash", font=('Arial', 12), bg='#003366', fg='white').grid(row=2, column=0, padx=10, pady=8)
Entry(cosmetic_frame, textvariable=Face_Wash, width=15, font=('Arial', 20), bg='#f1f3f5', bd=2, relief=SOLID).grid(row=2, column=1, padx=10, pady=8)

Label(cosmetic_frame, text="Hair Spray", font=('Arial', 12), bg='#003366', fg='white').grid(row=3, column=0, padx=10, pady=8)
Entry(cosmetic_frame, textvariable=Hair_Spray, width=15, font=('Arial', 20), bg='#f1f3f5', bd=2, relief=SOLID).grid(row=3, column=1, padx=10, pady=8)

Label(cosmetic_frame, text="Body Lotion", font=('Arial', 12), bg='#003366', fg='white').grid(row=4, column=0, padx=10, pady=8)
Entry(cosmetic_frame, textvariable=Body_Lotion, width=15, font=('Arial', 20), bg='#f1f3f5', bd=2, relief=SOLID).grid(row=4, column=1, padx=10, pady=8)

# Grocery frame
grocery_frame = Frame(main, bg='#003366', bd=8, relief=GROOVE, height=450)
grocery_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")
# grocery_frame.pack(side=LEFT)

Label(grocery_frame, text="Rice", font=('Arial', 12), bg='#003366', fg='white').grid(row=0, column=0, padx=10, pady=8)
Entry(grocery_frame, textvariable=Rice, width=15, font=('Arial', 20), bd=2, relief=SOLID).grid(row=0, column=1, padx=10, pady=8)

Label(grocery_frame, text="Food Oil", font=('Arial', 12), bg='#003366', fg='white').grid(row=1, column=0, padx=10, pady=8)
Entry(grocery_frame, textvariable=Food_Oil, width=15, font=('Arial', 20), bd=2, relief=SOLID).grid(row=1, column=1, padx=10, pady=8)

Label(grocery_frame, text="Daal", font=('Arial', 12), bg='#003366', fg='white').grid(row=2, column=0, padx=10, pady=8)
Entry(grocery_frame, textvariable=Daal, width=15, font=('Arial', 20), bd=2, relief=SOLID).grid(row=2, column=1, padx=10, pady=8)

Label(grocery_frame, text="Wheat", font=('Arial', 12), bg='#003366', fg='white').grid(row=3, column=0, padx=10, pady=8)
Entry(grocery_frame, textvariable=Wheat, width=15, font=('Arial', 20), bd=2, relief=SOLID).grid(row=3, column=1, padx=10, pady=8)

Label(grocery_frame, text="Sugar", font=('Arial', 12), bg='#003366', fg='white').grid(row=4, column=0, padx=10, pady=8)
Entry(grocery_frame, textvariable=Sugar, width=15, font=('Arial', 20), bd=2, relief=SOLID).grid(row=4, column=1, padx=10, pady=8)

# Snack frame
snack_frame = Frame(main, bg='#003366', bd=8, relief=GROOVE, height=450)
snack_frame.grid(row=0, column=2, padx=10, pady=10, sticky="n")
# snack_frame.pack(side=LEFT)

Label(snack_frame, text="Maza", font=('Arial', 12), bg='#003366', fg='white').grid(row=0, column=0, padx=10, pady=8, sticky='w')
Entry(snack_frame, textvariable=Maza, width=15, font=('Arial', 20), bd=2, relief=SOLID).grid(row=0, column=1, padx=10, pady=8)

Label(snack_frame, text="Coke", font=('Arial', 12), bg='#003366', fg='white').grid(row=1, column=0, padx=10, pady=8, sticky='w')
Entry(snack_frame, textvariable=Coke, width=15, font=('Arial', 20), bd=2, relief=SOLID).grid(row=1, column=1, padx=10, pady=8)

Label(snack_frame, text="Frooti", font=('Arial', 12), bg='#003366', fg='white').grid(row=2, column=0, padx=10, pady=8, sticky='w')
Entry(snack_frame, textvariable=Frooti, width=15, font=('Arial', 20), bd=2, relief=SOLID).grid(row=2, column=1, padx=10, pady=8)

Label(snack_frame, text="Nimkos", font=('Arial', 12), bg='#003366', fg='white').grid(row=3, column=0, padx=10, pady=8, sticky='w')
Entry(snack_frame, textvariable=Nimkos, width=15, font=('Arial', 20), bd=2, relief=SOLID).grid(row=3, column=1, padx=10, pady=8)

Label(snack_frame, text="Biscuits", font=('Arial', 12), bg='#003366', fg='white').grid(row=4, column=0, padx=10, pady=8, sticky='w')
Entry(snack_frame, textvariable=Biscuits, width=15, font=('Arial', 20), bd=2, relief=SOLID).grid(row=4, column=1, padx=10, pady=8)

bill_frame = Frame(main, bg='#003366', bd=8, relief=GROOVE, height=450)
bill_frame.grid(row=0, column=3, padx=10, pady=10, sticky="n")
# bill_frame.pack(side=LEFT)

bill_text = scrolledtext.ScrolledText(bill_frame, width=40, height=27, font=('Courier New', 10), bg='white')
bill_text.pack(padx=5, pady=2)

def bill():
    if customer_name.get() == "" or customer_phone.get() == "":
        messagebox.showerror("Error", "Customer details are required")
        return

    calculate_total()

    bill_text.delete('1.0', END)
    bill_text.insert(END, '\t  *** Welcome to Billing Software ***\n')
    bill_text.insert(END, '=' * 50 + '\n')
    bill_text.insert(END, f'Bill No       : {bill_no.get()}\n')
    bill_text.insert(END, f'Customer Name : {customer_name.get()}\n')
    bill_text.insert(END, f'Phone Number  : {customer_phone.get()}\n')
    bill_text.insert(END, '=' * 50 + '\n')
    bill_text.insert(END, f'{"Product":20}{"Qty":>7}{"Price":>10}\n')
    bill_text.insert(END, '-' * 50 + '\n')

    total_bill = 0
    cosmetic_subtotal = 0
    grocery_subtotal = 0
    snack_subtotal = 0

    product_groups = {
        "Cosmetics": [
            ("Bath Soap", Bath_Soap, PRICES["Bath_Soap"]),
            ("Face Cream", Face_Cream, PRICES["Face_Cream"]),
            ("Face Wash", Face_Wash, PRICES["Face_Wash"]),
            ("Hair Spray", Hair_Spray, PRICES["Hair_Spray"]),
            ("Body Lotion", Body_Lotion, PRICES["Body_Lotion"]),
        ],
        "Grocery": [
            ("Rice", Rice, PRICES["Rice"]),
            ("Food Oil", Food_Oil, PRICES["Food_Oil"]),
            ("Daal", Daal, PRICES["Daal"]),
            ("Wheat", Wheat, PRICES["Wheat"]),
            ("Sugar", Sugar, PRICES["Sugar"]),
        ],
        "Snacks & Drinks": [
            ("Maza", Maza, PRICES["Maza"]),
            ("Coke", Coke, PRICES["Coke"]),
            ("Frooti", Frooti, PRICES["Frooti"]),
            ("Nimkos", Nimkos, PRICES["Nimkos"]),
            ("Biscuits", Biscuits, PRICES["Biscuits"]),
        ]
    }

    for category, items in product_groups.items():
        printed_header = False
        for name, var, price in items:
            qty = var.get()
            if qty > 0:
                if not printed_header:
                    bill_text.insert(END, f"\n-- {category} --\n")
                    printed_header = True
                total_price = qty * price
                bill_text.insert(END, f"{name:20}{qty:>7}{total_price:>10} Rs\n")
                total_bill += total_price
                if category == "Cosmetics":
                    cosmetic_subtotal += total_price
                elif category == "Grocery":
                    grocery_subtotal += total_price
                elif category == "Snacks & Drinks":
                    snack_subtotal += total_price

    # Taxes
    tax_cos = int(cosmetics_tax.get().split()[0]) if cosmetics_tax.get() else 0
    tax_groc = int(grocery_tax.get().split()[0]) if grocery_tax.get() else 0
    tax_snack = int(other_tax.get().split()[0]) if other_tax.get() else 0
    grand_total = total_bill + tax_cos + tax_groc + tax_snack

    # Subtotals and taxes
    bill_text.insert(END, '\n' + '-' * 50 + '\n')
    bill_text.insert(END, f"{'Cosmetics Subtotal':30}{cosmetic_subtotal:>10} Rs\n")
    bill_text.insert(END, f"{'Cosmetics Tax':30}{tax_cos:>10} Rs\n")
    bill_text.insert(END, f"{'Grocery Subtotal':30}{grocery_subtotal:>10} Rs\n")
    bill_text.insert(END, f"{'Grocery Tax':30}{tax_groc:>10} Rs\n")
    bill_text.insert(END, f"{'Snacks Subtotal':30}{snack_subtotal:>10} Rs\n")
    bill_text.insert(END, f"{'Snacks Tax':30}{tax_snack:>10} Rs\n")
    bill_text.insert(END, '=' * 50 + '\n')
    bill_text.insert(END, f"{'GRAND TOTAL':30}{grand_total:>10} Rs\n")
    bill_text.insert(END, '=' * 50 + '\n')
    bill_text.insert(END, '\n\tThank you for shopping with us!\n')
       
bottom_frame = Frame(root, bg='#003366', bd=8, relief=GROOVE,height=300)
bottom_frame.pack(fill=BOTH,expand=TRUE)

Label(bottom_frame, text="Total Cosmetics", font=('Arial', 12), bg='#003366', fg='white').grid(row=0, column=0,pady=6)
Entry(bottom_frame, textvariable=total_cosmetics, width=20, font=('Arial', 18)).grid(row=0, column=1, padx=10,pady=6)

Label(bottom_frame, text="Cosmetics Tax", font=('Arial', 12), bg='#003366', fg='white').grid(row=0, column=2,pady=6)
Entry(bottom_frame, textvariable=cosmetics_tax, width=20, font=('Arial', 18)).grid(row=0, column=3, padx=10,pady=6)

Label(bottom_frame, text="Total Grocery", font=('Arial', 12), bg='#003366', fg='white').grid(row=1, column=0)
Entry(bottom_frame, textvariable=total_grocery, width=20, font=('Arial', 18)).grid(row=1, column=1, padx=10)

Label(bottom_frame, text="Grocery Tax", font=('Arial', 12), bg='#003366', fg='white').grid(row=1, column=2)
Entry(bottom_frame, textvariable=grocery_tax, width=20, font=('Arial', 18)).grid(row=1, column=3, padx=10)

Label(bottom_frame, text="Other Total", font=('Arial', 12), bg='#003366', fg='white').grid(row=2, column=0)
Entry(bottom_frame, textvariable=other_total, width=20, font=('Arial', 18)).grid(row=2, column=1, padx=10)

Label(bottom_frame, text="Other Tax", font=('Arial', 12), bg='#003366', fg='white').grid(row=2, column=2)
Entry(bottom_frame, textvariable=other_tax, width=20, font=('Arial', 18)).grid(row=2, column=3, padx=10)


Button(bottom_frame, text='Total', font=('Arial', 12), fg='white', bg=btn_color, width=15, command=calculate_total).grid(row=1, column=4, padx=18, pady=20)
Button(bottom_frame, text='Generate Bill', font=('Arial', 12), fg='white', bg=btn_color, width=15,command=bill).grid(row=1, column=5, padx=18, pady=20)
Button(bottom_frame, text='Clear', font=('Arial', 12), fg='white', bg=btn_color, width=15, command=clear_data).grid(row=1, column=6, padx=18, pady=20)
Button(bottom_frame, text='Exit', font=('Arial', 12), fg='white', bg=btn_color, width=15, command=root.quit).grid(row=1, column=7, padx=18, pady=20)

root.mainloop()