import re
import sys
import os
from subprocess import run

def create_virtual_environment(venv_dir, activate_script):
    # Create a new virtual environment

    python_executable = sys.executable

    create_env = f'''
        {python_executable} -m venv {venv_dir}
    '''
    
    run(f'''
        {create_env}
    ''', shell=True)

    if os.name == "posix":
        # Fix permissions
        permissions = f'''
            chmod 755 {activate_script}
        '''

        run(f'''
            {permissions}
        ''', shell=True)

def install_requirements(activate_script, requirements_file):
    # Activate the virtual environment
    
    
    pip_install = f'''
        source {activate_script};
        pip install -r {requirements_file};
    '''

    run(pip_install, shell=True)

def main():

    # Set variables
    virtual_environment_directory_name = 'env'
    current_path = os.getcwd()
    venv_dir = os.path.join(current_path, virtual_environment_directory_name)
    activate_script = os.path.join(venv_dir, 'bin', 'activate')
    
     # Create Virtual environment
    create_virtual_environment(venv_dir, activate_script)

    # Install requirements in the virtual environmentquit
    requirements_file = sys.argv[1]
    install_requirements(activate_script, requirements_file)

    # run Jupyter
    run(f'''
        source {activate_script};
        jupyter lab;
    ''', shell=True)


if __name__ == "__main__":
    main()
