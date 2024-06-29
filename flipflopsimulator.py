import tkinter as tk
from tkinter import ttk

class FlipFlopSimulator:
    def __init__(self, master):
        self.master = master
        self.master.title("Flip-Flop Simulator")

        self.flipflop_type = tk.StringVar(value="D")

        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.master)
        frame.pack(padx=10, pady=10)


        ttk.Label(frame, text="Select Flip-Flop type:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        ttk.Radiobutton(frame, text="D Flip-Flop", variable=self.flipflop_type, value="D", command=self.reset_fields).grid(row=0, column=1, padx=5, pady=5)
        ttk.Radiobutton(frame, text="T Flip-Flop", variable=self.flipflop_type, value="T", command=self.reset_fields).grid(row=0, column=2, padx=5, pady=5)


        ttk.Label(frame, text="Set (S):").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.set_var = tk.IntVar()
        ttk.Checkbutton(frame, variable=self.set_var).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Reset (R):").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.reset_var = tk.IntVar()
        ttk.Checkbutton(frame, variable=self.reset_var).grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Clock (CLK):").grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.clock_var = tk.IntVar()
        ttk.Checkbutton(frame, variable=self.clock_var).grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Data (D):").grid(row=4, column=0, padx=5, pady=5, sticky='e')
        self.data_var = tk.IntVar()
        self.data_entry = ttk.Entry(frame, textvariable=self.data_var)
        self.data_entry.grid(row=4, column=1, padx=5, pady=5)


        ttk.Label(frame, text="Output Q:").grid(row=5, column=0, padx=5, pady=5, sticky='e')
        self.output_q_var = tk.StringVar(value="0")
        ttk.Label(frame, textvariable=self.output_q_var).grid(row=5, column=1, padx=5, pady=5, sticky='w')

        ttk.Label(frame, text="Output Q':").grid(row=6, column=0, padx=5, pady=5, sticky='e')
        self.output_qn_var = tk.StringVar(value="1")
        ttk.Label(frame, textvariable=self.output_qn_var).grid(row=6, column=1, padx=5, pady=5, sticky='w')

        # Simulate button
        self.simulate_button = ttk.Button(frame, text="Simulate", command=self.simulate_flipflop)
        self.simulate_button.grid(row=7, column=0, columnspan=2, padx=5, pady=10)

        self.reset_fields()

    def reset_fields(self):
        self.set_var.set(0)
        self.reset_var.set(0)
        self.clock_var.set(0)
        self.data_var.set(0)
        self.output_q_var.set("0")
        self.output_qn_var.set("1")
        if self.flipflop_type.get() == "D":
            self.data_entry.config(state='normal')
        else:
            self.data_entry.config(state='disabled')

    def simulate_flipflop(self):
        flipflop_type = self.flipflop_type.get()
        set_val = self.set_var.get()
        reset_val = self.reset_var.get()
        clock_val = self.clock_var.get()
        data_val = self.data_var.get()

        if set_val == 1 and reset_val == 0:
            q_val = 1
        elif set_val == 0 and reset_val == 1:
            q_val = 0
        elif set_val == 1 and reset_val == 1:
            q_val = 1
        else:
            if flipflop_type == "D":
                if clock_val == 1:
                    q_val = data_val
                else:
                    q_val = int(self.output_q_var.get())
            elif flipflop_type == "T":
                if clock_val == 1:
                    q_val = 1 - int(self.output_q_var.get())
                else:
                    q_val = int(self.output_q_var.get())

        self.output_q_var.set(str(q_val))
        self.output_qn_var.set(str(1 - q_val))


if __name__ == "__main__":
    root = tk.Tk()
    app = FlipFlopSimulator(root)
    root.mainloop()
