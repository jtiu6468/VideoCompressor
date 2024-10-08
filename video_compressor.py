# Compresses a video file by reducing its bitrate and changing its frame rate
import ffmpeg
import os

def reduce_video(input_file, output_file, bitrate='750K'):
    print(f"Compressing {input_file} to {output_file}")
    # Use ffmpeg to change bitrate to 750K and frame rate to 23.976 
    ffmpeg.input(input_file).output(output_file, video_bitrate=bitrate, r=23.976).run()

    print(f"Video saved to {output_file} with reduced size.")

if __name__ == "__main__":
    input_file = "Replace with path of video you want to compress (ex: original_video.mp4)" 
    output_file = "Enter Desired Video Name (ex: compress_video.mp4)"
    # Check to see if file exists
    if not os.path.isfile(input_file):
        print(f"The file '{input_file}' does not exist.")
    else:
        reduce_video(input_file, output_file)
