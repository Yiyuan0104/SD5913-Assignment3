# SD5913-Assignment3

## Project Overview



This project contains three Python scripts:

- `main.py`: Greets the user by name in the terminal.
- `Calculator.py`: A GUI calculator with buttons and display.
- `Input_GUI.py`: A GUI tool for interactive input demos (word count, max/min, weekday, reverse, math).
 - `interactive_art.py`: A simple generative drawing tool that responds to mouse and keyboard input.

## Usage


### main.py (Greeting Script)

Run the following command and enter your name when prompted:

```sh
python3 main.py
```

Example output:
```
Please enter your name: Alice
Hello, Alice!
```



### Calculator.py (GUI Calculator)

Run the calculator with a graphical interface:

```sh
python3 Calculator.py
```



### Input_GUI.py (GUI Input Demos)

Run the interactive input demo GUI:

```sh
python3 Input_GUI.py
```
Click a button to select a demo, enter your input in the popup, and see the result.


### interactive_art.py (Generative Drawing)

Run the interactive drawing tool:

```sh
python3 interactive_art.py
```

Controls:
- Drag left mouse button to draw or erase.
- 'e': toggle between draw and erase mode.
- 'b': toggle between brush and pencil drawing modes.
- Number keys 1-6: switch color presets.
- '[' and ']': decrease/increase brush size.
- 'c': clear canvas.
- 'u': undo last stroke.
- 's': save canvas to a PostScript file.
- 'r/g/w': change background color to red/green/white.
- Space: toggle help window with all controls.

This script satisfies the assignment requirements:
- Written in Python and uses standard library (`tkinter`).
- Accepts mouse and keyboard input.
- Provides real-time visual feedback (drawing) and state management (strokes, undo).
- Can be extended as a generative artwork or interactive tool.


