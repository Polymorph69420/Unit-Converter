# Imports
import tkinter as tk
from tkinter import ttk

# Conversion factors dictionary
conversion_factors = {
    # Length
    ("meters", "kilometers"): 0.001,
    ("meters", "feet"): 3.28084,
    ("meters", "inches"): 39.3701,
    ("meters", "miles"): 0.000621371,
    ("meters", "centimeters"): 100,
    ("meters", "millimeters"): 1000,
    ("meters", "yards"): 1.09361,

    ("kilometers", "meters"): 1000,
    ("kilometers", "feet"): 3280.84,
    ("kilometers", "inches"): 39370.1,
    ("kilometers", "miles"): 0.621371,
    ("kilometers", "centimeters"): 100000,
    ("kilometers", "millimeters"): 1_000_000,
    ("kilometers", "yards"): 1093.61,

    ("feet", "meters"): 0.3048,
    ("feet", "kilometers"): 0.0003048,
    ("feet", "inches"): 12,
    ("feet", "miles"): 0.000189394,
    ("feet", "centimeters"): 30.48,
    ("feet", "millimeters"): 304.8,
    ("feet", "yards"): 1/3,

    ("inches", "meters"): 0.0254,
    ("inches", "kilometers"): 0.0000254,
    ("inches", "feet"): 1/12,
    ("inches", "miles"): 0.000015783,
    ("inches", "centimeters"): 2.54,
    ("inches", "millimeters"): 25.4,
    ("inches", "yards"): 1/36,

    ("miles", "meters"): 1609.34,
    ("miles", "kilometers"): 1.60934,
    ("miles", "feet"): 5280,
    ("miles", "inches"): 63360,
    ("miles", "centimeters"): 160934,
    ("miles", "millimeters"): 1609340,
    ("miles", "yards"): 1760,

    ("centimeters", "meters"): 0.01,
    ("centimeters", "kilometers"): 0.00001,
    ("centimeters", "feet"): 0.0328084,
    ("centimeters", "inches"): 0.393701,
    ("centimeters", "miles"): 0.0000062137,
    ("centimeters", "millimeters"): 10,
    ("centimeters", "yards"): 0.0109361,

    ("millimeters", "meters"): 0.001,
    ("millimeters", "kilometers"): 0.000001,
    ("millimeters", "feet"): 0.00328084,
    ("millimeters", "inches"): 0.0393701,
    ("millimeters", "miles"): 0.000000621371,
    ("millimeters", "centimeters"): 0.1,
    ("millimeters", "yards"): 0.00109361,

    ("yards", "meters"): 0.9144,
    ("yards", "kilometers"): 0.0009144,
    ("yards", "feet"): 3,
    ("yards", "inches"): 36,
    ("yards", "miles"): 0.000568182,
    ("yards", "centimeters"): 91.44,
    ("yards", "millimeters"): 914.4,

    # Temperature
    ("celsius", "fahrenheit"): "CtoF",
    ("fahrenheit", "celsius"): "FtoC",
    ("celsius", "kelvin"): "CtoK",
    ("kelvin", "celsius"): "KtoC",
    ("fahrenheit", "kelvin"): "FtoK",
    ("kelvin", "fahrenheit"): "KtoF",

    # Mass
    ("kilograms", "grams"): 1000,
    ("kilograms", "milligrams"): 1000000,
    ("kilograms", "pounds"): 2.20462,
    ("kilograms", "ounces"): 35.274,

    ("grams", "kilograms"): 0.001,
    ("grams", "milligrams"): 1000,
    ("grams", "pounds"): 0.00220462,
    ("grams", "ounces"): 0.035274,

    ("milligrams", "kilograms"): 0.000001,
    ("milligrams", "grams"): 0.001,
    ("milligrams", "pounds"): 0.0000022046,
    ("milligrams", "ounces"): 0.000035274,

    ("pounds", "kilograms"): 0.453592,
    ("pounds", "grams"): 453.592,
    ("pounds", "milligrams"): 453592,
    ("pounds", "ounces"): 16,

    ("ounces", "kilograms"): 0.0283495,
    ("ounces", "grams"): 28.3495,
    ("ounces", "milligrams"): 28349.5,
    ("ounces", "pounds"): 1/16,

    # Time
    ("seconds", "minutes"): 1/60,
    ("seconds", "hours"): 1/3600,
    ("seconds", "days"): 1/86400,

    ("minutes", "seconds"): 60,
    ("minutes", "hours"): 1/60,
    ("minutes", "days"): 1/1440,

    ("hours", "seconds"): 3600,
    ("hours", "minutes"): 60,
    ("hours", "days"): 1/24,

    ("days", "seconds"): 86400,
    ("days", "minutes"): 1440,
    ("days", "hours"): 24,
}

# Conversion function
def convert():
    try:
        amount = float(entry_amount.get())
    except ValueError:
        update_answer("Input a number")
        return

    unit_from = combo_from.get()
    unit_to = combo_to.get()

    entry_amount.delete(0, 'end')
    combo_from.set('')
    combo_to.set('')

    if unit_from == unit_to:
        update_answer("Different units, please")
    elif (unit_from, unit_to) not in conversion_factors:
        update_answer("Can't convert")
    else:
        factor = conversion_factors[(unit_from, unit_to)]
        if factor == "CtoF":
            answer = 1.8 * amount + 32
        elif factor == "FtoC":
            answer = (amount - 32) * 5/9
        elif factor == "CtoK":
            answer = amount + 273.15
        elif factor == "KtoC":
            answer = amount - 273.15
        elif factor == "KtoF":
            answer = 1.8 * (amount - 273.15) + 32
        elif factor == "FtoK":
            answer = ((amount - 32) * 5/9) + 273.15
        else:
            answer = amount * float(factor)

        update_answer(round(answer, 4))

# Helper to update the answer entry
def update_answer(text):
    entry_answer.config(state="normal")
    entry_answer.delete(0, 'end')
    entry_answer.insert(0, str(text))
    entry_answer.config(state="readonly")

# GUI setup
root = tk.Tk()
root.geometry("400x300")
root.title("Unit Converter 1.0")
root.config(bg="#f0f2f5")
root.resizable(False, False)

# Widgets
label_title = tk.Label(root, text="UNIT CONVERTER", font=("Helvetica", 16, "bold"), fg="#333333")
label_amount = tk.Label(root, text="Amount:", font=("Helvetica", 15), fg="#333333")
label_from = tk.Label(root, text="Convert From:", font=("Helvetica", 15), fg="#333333")
label_to = tk.Label(root, text="Convert To:", font=("Helvetica", 15), fg="#333333")

entry_amount = tk.Entry(root)

combo_from = ttk.Combobox(root)
combo_from['values'] = (
    'meters', 'kilometers', 'feet', 'inches', 'miles', 'centimeters', 'millimeters', 'yards',
    'celsius', 'fahrenheit', 'kelvin',
    'kilograms', 'grams', 'milligrams', 'pounds', 'ounces',
    'seconds', 'minutes', 'hours', 'days'
)

combo_to = ttk.Combobox(root)
combo_to['values'] = combo_from['values']

button_convert = tk.Button(
    root, text="Convert", command=convert,
    bg="#007acc", fg="white", activebackground="#005f99"
)

entry_answer = tk.Entry(root, bg="#ffffff")
entry_answer.config(state="readonly")

# Layout
label_title.grid(row=0, column=0, columnspan=2, pady=10)
label_amount.grid(row=1, column=0, sticky="w", padx=10)
entry_amount.grid(row=1, column=1, padx=10, pady=5)

label_from.grid(row=2, column=0, sticky="w", padx=10)
combo_from.grid(row=2, column=1, padx=10, pady=5)

label_to.grid(row=3, column=0, sticky="w", padx=10)
combo_to.grid(row=3, column=1, padx=10, pady=5)

button_convert.grid(row=4, column=0, columnspan=2, pady=10)
entry_answer.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Run the application
root.mainloop()



