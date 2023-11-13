import tkinter as tk

def convert_temperature():
    try:
        temperature = float(entry.get())
    except ValueError:
        result_label.config(text="Invalid input", fg="red")
        return

    if var.get() == 1:  # Celsius to Kelvin
        result = temperature + 273.15
    elif var.get() == 2:  # Celsius to Fahrenheit
        result = (temperature * 9/5) + 32
    elif var.get() == 3:  # Kelvin to Celsius
        result = temperature - 273.15
    elif var.get() == 4:  # Kelvin to Fahrenheit
        result = (temperature - 273.15) * 9/5 + 32
    elif var.get() == 5:  # Fahrenheit to Celsius
        result = (temperature - 32) * 5/9
    else:  # Fahrenheit to Kelvin
        result = (temperature - 32) * 5/9 + 273.15

    result_label.config(text=f"Result: {result:.2f}", fg="white")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")
root.configure(bg="black")

# Set the window size and position
window_width = 500
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Create and configure the UI elements
frame = tk.Frame(root, bg="black")
frame.place(relx=0.5, rely=0.5, anchor="center")

label = tk.Label(frame, text="Enter Temperature:", fg="white", bg="black")
label.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(frame, width=15)
entry.grid(row=0, column=1, padx=10, pady=10)

var = tk.IntVar()
var.set(1)  # Default selection

options = [
    ("Celsius to Kelvin", 1),
    ("Celsius to Fahrenheit", 2),
    ("Kelvin to Celsius", 3),
    ("Kelvin to Fahrenheit", 4),
    ("Fahrenheit to Celsius", 5),
    ("Fahrenheit to Kelvin", 6)
]

for i, (text, value) in enumerate(options):
    tk.Radiobutton(frame, text=text, variable=var, value=value, bg="black", fg="white",
                   selectcolor="black", activebackground="black", activeforeground="white").grid(row=i+1, column=0, columnspan=2, pady=5)

convert_button = tk.Button(frame, text="Convert", command=convert_temperature, bg="green", fg="white")
convert_button.grid(row=len(options)+1, column=0, columnspan=2, pady=10)

result_label = tk.Label(frame, text="Result after conversion: ", fg="white", bg="black")
result_label.grid(row=len(options)+2, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
