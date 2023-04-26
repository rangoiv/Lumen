import subprocess
from pathlib import Path

for path, _, files in os.walk(str(noise_path)):
     for i, file in enumerate(files):
             if file.endswith('.mp3'):
                     subprocess.call(['ffmpeg', '-i', noise_path/file, str(noise_path/f"{i}.wav")])