# python-examples
This repository covers python basic foundations with examples and helps to understand the nuts and bolts of the language.

#Test Github PR Using API
### The examples are based on 3.8.2 version

# How to execute a python file from bash
python ./name_of_python_file.py 

## More detailed info on several different ways to execute the python from bash
   * https://stackoverflow.com/questions/4377109/shell-script-execute-a-python-program-from-within-a-shell-script
   
## Why do we need a virtual environment and how to create virtual environment
###### If you want your code to run in it's own virtual environment without depending on the OS virtual env or on other python interpreters then in those scenarios you need a virtual environment.
    * python -m venv new_virt_env
### Activate virtual environment 
  *  source new_virt_env/bin/activate ( In Mac as /bin folder doesn't exists in windows)
  *  new_virt_env/Scripts/activate ( In windows - Just run this path to activate the virtual environment)
### Deactivate virtual environment and Destroy virtual environment
  * deactivate
  * rm -rf new_virt_env/ ( Clean up all the files in the folder)  
  
###### Pip installing and uninstalling new packages
    * pip install selenium --user ( pass --user if pip install selenium fails)
    * pip uninstall selenium
    * pip uninstall selenium urllib3 ( to uninstall multiple packages)
   
###### Upgrading pip
Upgrade pip if any of the package doesn't get installed in the virtual env

    * python -m pip install --upgrade pip

###### Other pip commands
    * pip --help
    * pip freeze ( Outputs the installed packages using pip)
    * pip freeze > requirements.txt
    * pip install -r requirements.txt ( Install required packages)


