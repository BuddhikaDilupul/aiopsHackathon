import subprocess

for i in range(100):
    print(f"Running iteration {i+1}")
    subprocess.run(["python", "main.py"])
