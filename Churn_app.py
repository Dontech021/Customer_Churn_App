import os
import sys
import subprocess
import subprocess
import os

filename = "rescale.dill.gz"
result = subprocess.run(['find', '.', '-name', filename], stdout=subprocess.PIPE)

if result.returncode == 0:
    filepath = result.stdout.decode().strip()
    print("The file is located at: ", filepath)
else:
    print("Error: File not found")

