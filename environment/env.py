import subprocess

env = "env-py38"
libs = "tensorflow|numpy|matplotlib|pandas|scikit-learn|pexpect|seaborn|pillow"

# Comando a ejecutar
command = f"conda activate {env} && conda list | grep -E '{libs}'"

# Ejecutar el comando en un subproceso de la terminal
process = subprocess.Popen(
    ["bash", "-c", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE
)

# Capturar la salida y el error
output, error = process.communicate()

# Imprimir la salida o el error si hubo alguno
if output:
    print(output.decode())
else:
    print(error.decode())
