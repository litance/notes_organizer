import tkinter as tk
import tkinter as ttk
from tkinter import messagebox, Label
from tkinter import simpledialog
from tkinter.messagebox import showinfo
from PIL import Image
import datetime

# Initialize global variables
MAX = 100
NOTES = 0  # Note counter
notes_ary = [""] * MAX
notes_title = [""] * MAX
notes_time = [""] * MAX
notes_category = [""] * MAX

# Functions for GUI actions
def save_notes():
    with open("save.txt", "w", encoding="utf-8") as file:  # Open file in write mode
        for i in range(NOTES):
            file.write(f"Title: {notes_title[i]}\n")
            file.write(f"Time: {notes_time[i]}\n")
            file.write(f"Content: {notes_ary[i]}\n")
            file.write("---\n")  # Separator for each note


def load_notes():
    global NOTES
    try:
        with open("save.txt", "r", encoding="utf-8") as file:  # Open file in read mode
            notes_title.clear()
            notes_ary.clear()
            notes_time.clear()
            notes_category.clear()
            NOTES = 0

            lines = file.readlines()
            title, category, time, content = "", "", "", ""
            for line in lines:
                line = line.strip()
                if line.startswith("Title:"):
                    title = line.replace("Title: ", "")
                elif line.startswith("Category:"):
                    category = line.replace("Category: ", "")
                elif line.startswith("Time:"):
                    time = line.replace("Time: ", "")
                elif line.startswith("Content:"):
                    content = line.replace("Content: ", "")
                elif line == "---":  # End of one note
                    if title and time and content:
                        notes_title.append(title)
                        notes_category.append(category)
                        notes_time.append(time)
                        notes_ary.append(content)
                        NOTES += 1
                    title, category, time, content = (
                        "",
                        "",
                        "",
                        "",
                    )  # Reset for the next note

            update_list()
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No saved notes file found.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load notes: {e}")


def add_note():
    global NOTES
    if NOTES < MAX:
        title = simpledialog.askstring("Add Note", "Enter Note Title:")
        if not title:
            return

        category = simpledialog.askstring("Add Note", "Enter Note Category:")
        if not category:
            return

        note = custom_text_dialog("Add Note", "Enter Note Content:")
        if not note:
            return

        time = datetime.datetime.now().strftime("%D-%H:%M:%S")

        notes_title.append(title)
        notes_ary.append(note)
        notes_time.append(time)
        notes_category.append(category)
        NOTES += 1
        update_list()
        save_notes()
        messagebox.showinfo("Success", "Note added successfully!")
    else:
        messagebox.showerror("Error", "Note limit reached!")


def view_note():
    selected = note_list.curselection()
    if not selected:
        messagebox.showwarning("Warning", "No note selected!")
        return

    note_id = selected[0]
    title = notes_title[note_id]
    category = notes_category[note_id]
    content = notes_ary[note_id]
    time = notes_time[note_id]
    messagebox.showinfo(
        "View Note",
        f"Title: {title}\n\nCategory: {category}\n\nContent: {content}\n\nTime: {time}",
    )


def search_note():
    query = simpledialog.askstring("Search Note", "Enter title to search:")
    if not query:
        return

    results = []
    for i in range(NOTES):
        if query.lower() in notes_title[i].lower():
            results.append((i, notes_title[i]))

    if results:
        result_str = "\n".join([f"{i}. {title}" for i, title in results])
        messagebox.showinfo("Search Results", f"Matching Notes:\n\n{result_str}")
    else:
        messagebox.showinfo("No Results", "No notes match your search.")


def edit_note():
    selected = note_list.curselection()
    if not selected:
        messagebox.showwarning("Warning", "No note selected!")
        return

    note_id = selected[0]
    new_title = simpledialog.askstring(
        "Edit Note", "Edit Note Title:", initialvalue=notes_title[note_id]
    )
    if new_title is None:
        return

    new_category = simpledialog.askstring(
        "Edit Note", "Edit Note Category:", initialvalue=notes_category[note_id]
    )
    if new_category is None:
        return

    new_content = custom_text_dialog(
        "Edit Note", "Edit Note Content:", initialvalue=notes_ary[note_id]
    )
    if new_content is None:
        return

    notes_title[note_id] = new_title
    notes_category[note_id] = new_category
    notes_ary[note_id] = new_content
    update_list()
    save_notes()
    messagebox.showinfo("Success", "Note edited successfully!")


def delete_note():
    global NOTES
    selected = note_list.curselection()
    if not selected:
        messagebox.showwarning("Warning", "No note selected!")
        return

    note_id = selected[0]
    confirm = messagebox.askyesno(
        "Confirm Delete", "Are you sure you want to delete this note?"
    )
    if confirm:
        notes_ary.pop(note_id)
        notes_title.pop(note_id)
        notes_category.pop(note_id)
        notes_time.pop(note_id)
        NOTES -= 1
        update_list()


def clear_notes():
    global NOTES
    confirm = messagebox.askyesno(
        "Confirm Clear", "Are you sure you want to clear all notes?"
    )
    if confirm:
        notes_ary[:] = [""] * MAX
        notes_title[:] = [""] * MAX
        notes_category[:] = [""] * MAX
        notes_time[:] = [""] * MAX
        NOTES = 0
        update_list()
        save_notes()


def update_list():
    note_list.delete(0, tk.END)
    for i in range(NOTES):
        note_list.insert(
            tk.END, f"{i}      |    {notes_category[i]}    |    {notes_title[i]}"
        )


# Custom text dialog for multi-line input
def custom_text_dialog(title, prompt, initialvalue=""):
    dialog = tk.Toplevel(root)
    dialog.title(title)
    dialog.geometry("400x300")

    tk.Label(dialog, text=prompt).pack(pady=10)

    text_area = tk.Text(dialog, wrap=tk.WORD, height=10, width=40)
    text_area.pack(pady=10, padx=10)
    text_area.insert(tk.END, initialvalue)

    result = {"value": None}

    def submit():
        result["value"] = text_area.get("1.0", tk.END).strip()
        dialog.destroy()

    def cancel():
        dialog.destroy()

    btn_frame = tk.Frame(dialog)
    btn_frame.pack(pady=10)
    tk.Button(btn_frame, text="OK", command=submit).pack(side=tk.LEFT, padx=5)
    tk.Button(btn_frame, text="Cancel", command=cancel).pack(side=tk.RIGHT, padx=5)

    dialog.transient(root)
    dialog.grab_set()
    root.wait_window(dialog)

    return result["value"]


# GUI section
# Initialize the main application window
root = tk.Tk()
root.geometry("800x500")
root.title("Notes Organizer")

# Create background
img = tk.PhotoImage(
    file="C:\\Users\\User\\Downloads\\jeremy-thomas-E0AHdsENmDg-unsplash.png"
)
label1 = Label(root, image=img)
label1.place(x=0, y=0)

# Create frames for layout
frame_top = tk.Frame(root)
frame_top.pack(pady=10)

frame_side = tk.Frame(root, width=20, height=250)
frame_side.pack(side=tk.LEFT, padx=5, pady=10, fill=tk.Y, expand=True)

frame_middle = tk.Frame(root)
frame_middle.pack(pady=10)

frame_bottom = tk.Frame(root)
frame_bottom.pack(pady=10)

# Create widgets
bck_img = Image.open(
    "C:\\Users\\User\\Downloads\\jeremy-thomas-E0AHdsENmDg-unsplash.png"
)
bg_color = bck_img.getpixel((269, 54))
bg_color_hex = "#%02x%02x%02x" % bg_color[:3]
note_tt = tk.Label(
    frame_top,
    text="NOTES ORGANIZER",
    width=20,
    height=1,
    font=("Times New Roman", 20),
    bg=bg_color_hex,
    fg="WHITE",
)
note_tt.pack()

note_list = tk.Listbox(
    frame_middle,
    width=50,
    height=15,
    font=("Times New Roman", 16),
    bg="#3c495e",
    fg="#dcdee6",
)
note_list.pack()


def show_preview(event):
    selected = note_list.curselection()
    if not selected:
        return
    note_id = selected[0]
    content = notes_ary[note_id]
    messagebox.showinfo("Note Preview", f"Content:\n\n{content}")


note_list.bind("<Double-1>", show_preview)

btn_add = tk.Button(
    frame_side,
    background="WHITE",
    foreground="BLACK",
    activebackground="GREY",
    activeforeground="BLACK",
    highlightthickness=2,
    highlightbackground="BLACK",
    highlightcolor="BLACK",
    width=15,
    height=2,
    border=0,
    cursor="hand1",
    text="Add Note",
    command=add_note,
)
btn_add.grid(row=1, column=0, padx=30, pady=10)

btn_view = tk.Button(
    frame_side,
    background="WHITE",
    foreground="BLACK",
    activebackground="GREY",
    activeforeground="BLACK",
    highlightthickness=2,
    highlightbackground="BLACK",
    highlightcolor="BLACK",
    width=15,
    height=2,
    border=0,
    cursor="hand1",
    text="View Note",
    command=view_note,
)
btn_view.grid(row=2, column=0, padx=30, pady=10)

btn_search = tk.Button(
    frame_side,
    background="WHITE",
    foreground="BLACK",
    activebackground="GREY",
    activeforeground="BLACK",
    highlightthickness=2,
    width=15,
    height=2,
    border=0,
    cursor="hand1",
    text="Search Note",
    command=search_note,
)
btn_search.grid(row=3, column=0, padx=30, pady=10)

btn_edit = tk.Button(
    frame_side,
    background="WHITE",
    foreground="BLACK",
    activebackground="GREY",
    activeforeground="BLACK",
    highlightthickness=2,
    highlightbackground="BLACK",
    highlightcolor="BLACK",
    width=15,
    height=2,
    border=0,
    cursor="hand1",
    text="Edit Note",
    command=edit_note,
)
btn_edit.grid(row=4, column=0, padx=30, pady=10)

btn_delete = tk.Button(
    frame_side,
    background="WHITE",
    foreground="BLACK",
    activebackground="GREY",
    activeforeground="BLACK",
    highlightthickness=2,
    highlightbackground="BLACK",
    highlightcolor="BLACK",
    width=15,
    height=2,
    border=0,
    cursor="hand1",
    text="Delete Note",
    command=delete_note,
)
btn_delete.grid(row=5, column=0, padx=30, pady=10)

btn_clear = tk.Button(
    frame_side,
    background="WHITE",
    foreground="BLACK",
    activebackground="GREY",
    activeforeground="BLACK",
    highlightthickness=2,
    highlightbackground="BLACK",
    highlightcolor="BLACK",
    width=15,
    height=2,
    border=0,
    cursor="hand1",
    text="Clear Note",
    command=clear_notes,
)
btn_clear.grid(row=6, column=0, padx=30, pady=10)

btn_exit = tk.Button(
    frame_side,
    background="WHITE",
    foreground="BLACK",
    activebackground="GREY",
    activeforeground="BLACK",
    highlightthickness=2,
    highlightbackground="BLACK",
    highlightcolor="BLACK",
    width=15,
    height=2,
    border=0,
    cursor="hand1",
    text="Exit",
    command=root.destroy,
)
btn_exit.grid(row=7, column=0, padx=30, pady=10, sticky="n")

# Run
load_notes()
root.mainloop()
