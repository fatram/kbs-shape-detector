import tkinter as tk
import tkinter.ttk as ttk

# TODO buttons mechanism
def open_rule_editor():
    print("Open rule editor")

def open_image():
    print("Open image")

def show_rules():
    print("Show rules")

def show_facts():
    print("Show facts")

root = tk.Tk()

# Upper Frame
frame_upper = tk.Frame(root)
frame_upper.grid(column=0, row=0)

# Upper Frame Elements
label_frame_image_source = tk.LabelFrame(frame_upper, text="Source Image")
label_frame_image_source.grid(column=0, row=0, padx=(10, 10), pady=(10, 10))
frame_image_source = tk.Frame(label_frame_image_source, bg="white", height=300, width=300)
frame_image_source.pack()
frame_image_source.pack_propagate(False)
message_image_source = tk.Message(frame_image_source, text="Please open an image", bg="white")
message_image_source.pack()

label_frame_image_detection = tk.LabelFrame(frame_upper, text="Detection Image")
label_frame_image_detection.grid(column=1, row=0, padx=(10, 10), pady=(10, 10))
frame_image_detection = tk.Frame(label_frame_image_detection, bg="white", height=300, width=300)
frame_image_detection.pack()
frame_image_detection.pack_propagate(False)
message_image_detection = tk.Message(frame_image_detection, text="Please choose a shape", bg="white")
message_image_detection.pack()

# Frame which contains buttons
frame_button = tk.Frame(frame_upper)
frame_button.grid(column=2, row=0, padx=(0,10), pady=(10, 10))

button_open_image = tk.Button(frame_button, 
                   text="Open Image",
                   command=open_image)
button_open_image.grid(column=0, row=0, pady=(4, 4))

button_open_rule_editor = tk.Button(frame_button,
                   text="Open Rule Editor",
                   command=open_rule_editor)
button_open_rule_editor.grid(column=0, row=1, pady=(4, 4))

button_show_rules = tk.Button(frame_button,
                    text="Show Rules",
                    command=show_rules)
button_show_rules.grid(column=0, row=2, pady=(4, 4))

button_show_facts = tk.Button(frame_button,
                    text="Show Facts",
                    command=show_facts)
button_show_facts.grid(column=0, row=3, pady=(4, 4))

label_shape = tk.Label(frame_button, text="What shape do you want")
label_shape.grid(column=0, row=4, pady=(10, 0))
treeview_shapes = ttk.Treeview(frame_button)
treeview_shapes.grid(column=0, row=5)

allshapes = treeview_shapes.insert("", 1, text="All Shapes")
treeview_shapes.insert(allshapes, "end", text="triangle")
treeview_shapes.insert(allshapes, "end", text="quadrilateral")
treeview_shapes.insert(allshapes, "end", text="pentagon")
treeview_shapes.insert(allshapes, "end", text="hexagon")

# Lower Frame
frame_lower = tk.Frame(root)
frame_lower.grid(column=0, row=1)

# Lower Frame Elements
label_frame_detection_result = tk.LabelFrame(frame_lower, text="Detection Result")
label_frame_detection_result.grid(column=0, row=0, padx=(10, 10), pady=(10, 10))
frame_detection_result = tk.Frame(label_frame_detection_result, bg="white", height=200, width=200)
frame_detection_result.pack()
frame_detection_result.pack_propagate(False)

label_frame_matched_facts = tk.LabelFrame(frame_lower, text="Matched Facts")
label_frame_matched_facts.grid(column=1, row=0, padx=(10, 10), pady=(10, 10))
frame_matched_facts = tk.Frame(label_frame_matched_facts, bg="white", height=200, width=200)
frame_matched_facts.pack()
frame_matched_facts.pack_propagate(False)

label_frame_hit_rules = tk.LabelFrame(frame_lower, text="Hit Rules")
label_frame_hit_rules.grid(column=2, row=0, padx=(10, 10), pady=(10, 10))
frame_hit_rules = tk.Frame(label_frame_hit_rules, bg="white", height=200, width=200)
frame_hit_rules.pack()
frame_hit_rules.pack_propagate(False)

root.mainloop()