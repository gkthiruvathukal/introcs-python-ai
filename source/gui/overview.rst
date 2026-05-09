.. index:: GUI, Tkinter, graphical user interface, widgets, events

.. _Graphical-User-Interfaces-With-Tkinter:

Graphical User Interfaces with Tkinter
=======================================

.. note::
   *Source:* Contributed by PhD students in COMP 501 at Loyola University Chicago.

.. todo::
   This chapter covers Tkinter, Python's classic built-in GUI library. While Tkinter
   remains fully functional and widely taught, the Python GUI landscape has evolved.
   Modern alternatives (e.g., PyQt, PySide, Dear PyGui, or web-based interfaces)
   may be more appropriate for production work. Consider modernizing this chapter
   in a future revision to survey current options or to replace Tkinter examples
   with a more contemporary toolkit.

A **Graphical User Interface (GUI)** lets users interact with a program using visual
elements — windows, buttons, text boxes, and menus — rather than typing commands.
GUIs make software more accessible and intuitive, especially for users who are not
comfortable with the command line.

You encounter GUIs every day: the desktop environment, web browsers, file explorers,
calculators, and games all use them.

.. index:: Tkinter; overview, tk.Tk(), mainloop(), event loop; Tkinter

What Is Tkinter?
----------------

**Tkinter** is Python's built-in library for creating desktop GUIs. It comes
pre-installed with Python, so no extra installation is required. Tkinter acts as a
bridge between Python and the Tcl/Tk GUI toolkit.

The simplest possible Tkinter program:

.. code-block:: python

   import tkinter as tk

   root = tk.Tk()
   root.title("My First GUI")

   label = tk.Label(root, text="Hello, Tkinter!")
   label.pack()

   root.mainloop()

- ``tk.Tk()`` creates the main application window.
- ``Label`` is a widget that displays text.
- ``pack()`` places the widget inside the window.
- ``mainloop()`` starts the event loop — it keeps the window open and listens for
  user actions until the window is closed.

.. index:: widgets; Tkinter, Label widget, Button widget, Entry widget, Text widget, Frame widget, Canvas widget, Listbox widget, Checkbutton widget

Widgets
-------

Widgets are the building blocks of a Tkinter GUI.

.. list-table::
   :header-rows: 1

   * - Widget
     - Purpose
   * - ``Label``
     - Display text or an image.
   * - ``Button``
     - Perform an action when clicked.
   * - ``Entry``
     - Accept a single line of text input.
   * - ``Text``
     - Accept multiple lines of text input.
   * - ``Frame``
     - Container for grouping other widgets.
   * - ``Listbox``
     - Display a scrollable list of items.
   * - ``Canvas``
     - Draw shapes, lines, or custom graphics.
   * - ``Checkbutton``
     - A checkbox that can be on or off.

Example — a button that reacts to a click:

.. code-block:: python

   import tkinter as tk

   def on_click():
       print("Button clicked!")

   root = tk.Tk()
   btn = tk.Button(root, text="Click Me", command=on_click)
   btn.pack()
   root.mainloop()

The ``command`` attribute points to a function that is called when the button is
clicked.

.. index:: Entry widget; user input, entry.get(), label.config(); dynamic update

Handling User Input
-------------------

Use an ``Entry`` widget to collect text from the user, and ``entry.get()`` to
retrieve what they typed:

.. code-block:: python

   import tkinter as tk

   def show_greeting():
       name = entry.get()
       label.config(text=f"Hello, {name}!")

   root = tk.Tk()

   entry = tk.Entry(root)
   entry.pack()

   btn = tk.Button(root, text="Submit", command=show_greeting)
   btn.pack()

   label = tk.Label(root, text="")
   label.pack()

   root.mainloop()

``label.config(text=...)`` updates the label's text dynamically without
recreating the widget.

.. index:: layout managers; Tkinter, pack(); Tkinter, grid(); Tkinter, place(); Tkinter

Layout Managers
---------------

Tkinter offers three geometry managers for positioning widgets:

.. list-table::
   :header-rows: 1

   * - Manager
     - Description
   * - ``pack()``
     - Stacks widgets vertically or horizontally; simplest to use.
   * - ``grid()``
     - Arranges widgets in a table of rows and columns.
   * - ``place()``
     - Positions widgets at exact pixel coordinates.

For most programs, ``pack()`` or ``grid()`` is sufficient. ``place()`` is useful
when you need precise control over widget positions.

.. index:: messagebox; Tkinter, messagebox.showerror(), messagebox.showinfo(), messagebox.askyesno()

Error Messages with ``messagebox``
------------------------------------

Display pop-up dialogs for errors or confirmations:

.. code-block:: python

   from tkinter import messagebox

   messagebox.showerror("Error", "Invalid input. Please try again.")
   messagebox.showinfo("Success", "Data saved successfully.")
   messagebox.askyesno("Confirm", "Are you sure you want to delete this?")

.. index:: Tkinter; API integration, requests; Tkinter example, GUI; API data display

Integrating an API with a GUI
------------------------------

Tkinter and the ``requests`` module can be combined to build interactive data apps.
Here is a minimal weather-lookup window:

.. code-block:: python

   import tkinter as tk
   from tkinter import messagebox
   import requests

   def fetch_weather():
       city = entry.get().strip()
       if not city:
           messagebox.showerror("Error", "Please enter a city name.")
           return
       url = f"https://wttr.in/{city}?format=3"
       try:
           response = requests.get(url, timeout=5)
           if response.status_code == 200:
               result_label.config(text=response.text)
           else:
               result_label.config(text="City not found.")
       except requests.exceptions.ConnectionError:
           messagebox.showerror("Error", "No internet connection.")

   root = tk.Tk()
   root.title("Weather Lookup")

   tk.Label(root, text="City:").pack()
   entry = tk.Entry(root)
   entry.pack()

   tk.Button(root, text="Get Weather", command=fetch_weather).pack()
   result_label = tk.Label(root, text="")
   result_label.pack()

   root.mainloop()

Exercises
---------

1. Create a Tkinter window that displays "Welcome to Tkinter!" and a button that
   closes the application when clicked.
2. Build a greeting app with an ``Entry`` for the user's name and a ``Button``
   that updates a ``Label`` to say ``"Hello, <name>!"``.
3. Create a simple counter app with "+" and "−" buttons and a label that shows
   the current count.
4. Build a color-changer: three buttons ("Red", "Green", "Blue") that each change
   the window's background color when clicked.
5. Create a GUI calculator that adds two numbers entered in ``Entry`` widgets and
   displays the result in a ``Label`` when a "Calculate" button is clicked.
6. Extend one of the exercises above to display a pop-up error message if the
   user provides invalid input (e.g., non-numeric values in the calculator).
