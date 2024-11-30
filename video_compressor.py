import ffmpeg
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to compress a video using FFmpeg
def reduce_video(input_file, output_file, bitrate='500K'):
    ''''
    Compresses a video file to reduce its size.
    Parameters:
    - input_file: path of input video file
    - output_file: path to save the compressed video
    - bitrate (optional): target bitrate is '500K'
    '''
    try:
        print(f"Compressing {input_file} to {output_file}")
        ffmpeg.input(input_file).output(output_file, video_bitrate=bitrate, r=23.976).run()
        print(f"Video saved to {output_file} with reduced size.")
        messagebox.showinfo("Success", f"Video saved to {output_file} with reduced size.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to compress video: {str(e)}")

# Opens a file dialog for selecting the video file
def browse_file(entry):
    '''
    Opens a file dialog to let the user select a video file, 
    and inserts the selected file's path into the given entry widget. 
    '''
    filename = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.mov;*.avi;*.mkv")])
    entry.delete(0, tk.END)
    entry.insert(0, filename)

#Validates input entry and starts the video compression
def start_compression(input_entry, output_entry, bitrate_entry):
    '''
    Reads user input from the GUI, validates it, and then starts the video compression.
    '''
    input_file = input_entry.get()
    output_file = output_entry.get()
    bitrate = bitrate_entry.get() if bitrate_entry.get() else '500K'

    if not input_file or not os.path.isfile(input_file):
        messagebox.showerror("Error", "Invalid input file. Please select a valid video file.")
        return

    if not output_file:
        messagebox.showerror("Error", "Please specify an output file name.")
        return

    reduce_video(input_file, output_file, bitrate)

# Create the main GUI window
root = tk.Tk()
root.title("Video Compressor")

# GUI components for input file
tk.Label(root, text="Input File:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
input_entry = tk.Entry(root, width=40)
input_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=lambda: browse_file(input_entry)).grid(row=0, column=2, padx=5, pady=5)

# GUI components for output file
tk.Label(root, text="Output File:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
output_entry = tk.Entry(root, width=40)
output_entry.grid(row=1, column=1, padx=5, pady=5)

# GUI components for bitrate field
tk.Label(root, text="Bitrate (optional):").grid(row=2, column=0, padx=5, pady=5, sticky='e')
bitrate_entry = tk.Entry(root, width=20)
bitrate_entry.grid(row=2, column=1, padx=5, pady=5)

# Button to start compression in the GUI
tk.Button(root, text="Compress Video", command=lambda: start_compression(input_entry, output_entry, bitrate_entry)).grid(row=3, column=1, pady=10)

# Start the GUI main event loop
root.mainloop()
