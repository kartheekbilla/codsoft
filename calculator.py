import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x600")
        self.root.configure(bg="#f0f0f0") 

        self.reset_next = False  

        
        self.entry = tk.Entry(root, font=("Arial", 32), justify="right", bg="white", fg="black", bd=0, relief="flat")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

       
        self.button_colors = {
            'numbers': "#e0e0e0",  
            'operators': "#f0a500",  
            'special': "#d3d3d3",  
            'equals': "#f0a500"  
        }

        
        self.buttons = [
            ('AC', 'special'), ('+/-', 'special'), ('%', 'special'), ('÷', 'operators'),
            ('7', 'numbers'), ('8', 'numbers'), ('9', 'numbers'), ('×', 'operators'),
            ('4', 'numbers'), ('5', 'numbers'), ('6', 'numbers'), ('-', 'operators'),
            ('1', 'numbers'), ('2', 'numbers'), ('3', 'numbers'), ('+', 'operators'),
            ('0', 'numbers'), ('.', 'numbers'), ('←', 'special'), ('=', 'equals')
        ]

    
        row = 1
        col = 0
        for (button, category) in self.buttons:
            action = lambda x=button: self.on_button_click(x)
            color = self.button_colors[category]
            btn = tk.Button(root, text=button, command=action, width=5, height=2, bg=color, fg="black", font=("Arial", 20), bd=1, relief="solid")
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

      
        for i in range(6):
            root.rowconfigure(i, weight=1)
        for i in range(4):
            root.columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == '=':
            try:
                expression = self.entry.get().replace('÷', '/').replace('×', '*')
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
                self.reset_next = True 
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif char == 'AC':
            self.entry.delete(0, tk.END)
            self.reset_next = False 
        elif char == '+/-':
            current_text = self.entry.get()
            if current_text:
                if current_text[0] == '-':
                    self.entry.delete(0)
                else:
                    self.entry.insert(0, '-')
        elif char == '←':
            current_text = self.entry.get()
            if current_text:
                self.entry.delete(len(current_text)-1, tk.END)
        else:
            if self.reset_next:
                if char in '0123456789.':
                    self.entry.delete(0, tk.END)
                self.reset_next = False  
            self.entry.insert(tk.END, char)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
