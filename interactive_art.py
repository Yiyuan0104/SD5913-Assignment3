"""
interactive_art.py - Enhanced generative drawing tool using tkinter.

Controls:
- Drag mouse to draw/erase.
- 'e': toggle between draw and erase mode.
- 'b': toggle between brush and pencil mode.
- Number keys 1-6: change color preset.
- '[' and ']': decrease/increase brush size.
- 'c': clear canvas.
- 'u': undo last stroke.
- 's': save canvas to PostScript file.
- 'r/g/b/w': change background to red/green/blue/white.
- Space: toggle help display.

No external packages required.
"""

import tkinter as tk
from tkinter import filedialog
import time

class InteractiveArt:
    def __init__(self, root):
        self.root = root
        root.title("Interactive Generative Art")
        self.width = 800
        self.height = 600
        root.geometry(f"{self.width}x{self.height}")

        self.canvas = tk.Canvas(root, bg="white", width=self.width, height=self.height)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # state
        self.brush_size = 6
        self.color_presets = ['#000000', '#e63946', '#f4a261', '#2a9d8f', '#264653', '#8d99ae']
        self.color_index = 0
        self.color = self.color_presets[self.color_index]
        self.current_stroke = []
        self.strokes = []
        self.is_eraser = False
        self.brush_mode = "brush"  # "brush" or "pencil"
        self.bg_color = "white"
        self.show_help = False

        # status
        self.status = tk.Label(root, text=self._status_text(), anchor='w')
        self.status.pack(fill=tk.X)

        # bindings
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.end_stroke)
        self.canvas.bind("<Button-1>", self.start_stroke)
        root.bind("<Key>", self.key_handler)
        root.focus_set()  # ensure window can receive key events

    def _status_text(self):
        mode = "ERASE" if self.is_eraser else "DRAW"
        return f"Mode: {mode} ({self.brush_mode})  Color: {self.color}  Brush: {self.brush_size}  Strokes: {len(self.strokes)}  BG: {self.bg_color}"

    def start_stroke(self, event):
        self.current_stroke = []

    def draw(self, event):
        x, y = event.x, event.y
        r = self.brush_size
        
        if self.is_eraser:
            # Erase by drawing with background color
            color = self.bg_color
            outline = self.bg_color
        else:
            color = self.color
            outline = '' if self.brush_mode == "brush" else self.color
        
        # Different shapes for different modes
        if self.brush_mode == "brush":
            item = self.canvas.create_oval(x-r, y-r, x+r, y+r, fill=color, outline=outline)
        else:  # pencil mode
            item = self.canvas.create_rectangle(x-r//2, y-r//2, x+r//2, y+r//2, fill=color, outline=outline)
        
        self.current_stroke.append(item)

    def end_stroke(self, event):
        if self.current_stroke:
            self.strokes.append(self.current_stroke)
            self.current_stroke = []
            self.update_status()

    def key_handler(self, event):
        key = event.keysym
        if key in ('c', 'C'):
            self.clear_canvas()
        elif key in ('u', 'U'):
            self.undo()
        elif key in ('s', 'S'):
            self.save_canvas()
        elif key in ('e', 'E'):
            self.toggle_eraser()
        elif key in ('b', 'B'):
            self.toggle_brush_mode()
        elif key == 'space':
            self.toggle_help()
        elif key == 'r':
            self.change_background('red')
        elif key == 'g':
            self.change_background('green')
        elif key in ('b', 'B') and event.state & 0x4:  # Ctrl+B for blue background
            self.change_background('blue')
        elif key == 'w':
            self.change_background('white')
        elif key == 'bracketleft':
            self.change_brush(-1)
        elif key == 'bracketright':
            self.change_brush(1)
        elif key.isdigit():
            n = int(key)
            if 1 <= n <= len(self.color_presets):
                self.color_index = n - 1
                self.color = self.color_presets[self.color_index]
                self.update_status()

    def toggle_eraser(self):
        self.is_eraser = not self.is_eraser
        self.update_status()

    def toggle_brush_mode(self):
        self.brush_mode = "pencil" if self.brush_mode == "brush" else "brush"
        self.update_status()

    def change_background(self, color):
        self.bg_color = color
        self.canvas.config(bg=color)
        self.update_status()

    def toggle_help(self):
        self.show_help = not self.show_help
        if self.show_help:
            self.show_help_overlay()
        else:
            self.hide_help_overlay()

    def show_help_overlay(self):
        help_text = """Controls:
e - Toggle erase mode
b - Toggle brush/pencil mode  
1-6 - Color presets
[ ] - Brush size
c - Clear canvas
u - Undo stroke
s - Save to file
r/g/w - Background color
Space - Toggle this help"""
        
        self.help_window = tk.Toplevel(self.root)
        self.help_window.title("Controls")
        self.help_window.geometry("300x250")
        label = tk.Label(self.help_window, text=help_text, justify='left', font=('monospace', 10))
        label.pack(padx=10, pady=10)

    def hide_help_overlay(self):
        if hasattr(self, 'help_window'):
            self.help_window.destroy()

    def change_brush(self, delta):
        self.brush_size = max(1, self.brush_size + delta)
        self.update_status()

    def clear_canvas(self):
        self.canvas.delete('all')
        self.strokes.clear()
        self.update_status()

    def undo(self):
        if self.strokes:
            last = self.strokes.pop()
            for item in last:
                try:
                    self.canvas.delete(item)
                except Exception:
                    pass
            self.update_status()

    def save_canvas(self):
        # Save as PostScript
        fname = filedialog.asksaveasfilename(defaultextension='.ps', filetypes=[('PostScript','*.ps')], title='Save Canvas')
        if fname:
            # give the canvas a moment to update
            self.root.update()
            self.canvas.postscript(file=fname)

    def update_status(self):
        self.status.config(text=self._status_text())

if __name__ == '__main__':
    root = tk.Tk()
    app = InteractiveArt(root)
    root.mainloop()
