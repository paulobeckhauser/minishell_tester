import subprocess
import os


def compile_minishell():
    """Compile minishell using Makefile."""
    os.chdir('..')
    print("\nChecking compilation...\n")
    subprocess.run(["make", "clean"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    try:
        subprocess.run(["make"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        print("\033[92mCompilation successful\033[0m ✅\n")
    except subprocess.CalledProcessError:
        print("\033[91mCompilation failed\033[0m ❌\n")

def run_programm():
    """Run a command in minishell and return the output."""
    if os.path.isfile("./minishell"):
            print("\033[92mCorrect executable file 'minishell': \033[0m ✅" + "\n")
    else:
        print("\033[91mFile does not open\033[0m ❌\n")
        return None









def get_output_command(command):
    with subprocess.Popen([".././minishell"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True) as proc:
        stdout, stderr = proc.communicate(command + "\n")
        output_lines = [line.strip() for line in stdout.splitlines()]
        output_lines = output_lines[1:-1]
        return output_lines


def test_commands(commands):
    outputs = []
    for command in commands:
        output = get_output_command(command)
        outputs.append(output)
    return outputs



def run_tests(outputs, expected_outputs, commands, threshold):
    for i, (outputs, expected_outputs, command, threshold) in enumerate(zip(outputs, expected_outputs, commands, thresholds), start=1):
        # Calculate the percentage difference

        set_outputs = set(outputs)
        set_expected_outputs = set(expected_outputs)
        differences = set_outputs.symmetric_difference(set_expected_outputs)
        percentage_difference = len(differences) / len(outputs) * 100
        if percentage_difference <= threshold:
            print(f"Test {i} ✅\t\033[90m{command}\033[0m")
        else:
            print(f"Test {i} ❌\t\033[90m{command}\033[0m")










def ls_expected(directory='.'):
    """Get a list of files in the specified directory."""
    files = os.listdir(directory)
    files = [file for file in files if not file.startswith('.')]  # Ignore hidden files
    return sorted(files, key=str.lower)  # Sort the files in a case-insensitive manner

def pwd_expected():
    expected_output = []
    expected_output.append(str(os.getcwd()))
    return expected_output

def export_expected():
    expected_output = []
    for key, value in os.environ.items():
        expected_output.append(f"declare -x {key}=\"{value}\"")
        # print(f"declare -x {key}={value}")
    expected_output.sort()
    return (expected_output)






commands = []
commands.append("ls")
commands.append("pwd")
commands.append("export")

thresholds = []
thresholds.append(0)
thresholds.append(0)
thresholds.append(10)


outputs = []
outputs = test_commands(commands)

expected_outputs = []
expected_outputs.append(ls_expected())
expected_outputs.append(pwd_expected())
expected_outputs.append(export_expected())



  

if __name__ == "__main__":
    compile_minishell()
    run_programm()
    run_tests(outputs, expected_outputs, commands, thresholds)
    print("\n")
