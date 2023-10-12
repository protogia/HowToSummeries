# python-projects-1x1 in vscode

This how-to describes some common problems when creating python-projects in vscode and how to solve them

## project-structure

The easiest way to prevent importing- and dependecy-issues for custom modules is to follow the classical-module-structure:
- create `setup.py` like in this example

```py
from setuptools import setup, find_packages


setup(
    name="foo",
    version="1.0",
    packages=find_packages(),
)
```

- Create projectstructure like classical [python-module/package-structure](https://stackoverflow.com/questions/53154159/importing-python-modules-from-different-levels-of-hierarchy): 

# prepare for errorhandling and debuggin

- Create .vscode/launch.json for debugging
- Add `pretty_errors` to project to [colorize python-error-console-output](https://pypi.org/project/pretty-errors/)

# prepare for autocomplete-functionality of custom classes

 - Add TypeHint-Functionality

Example-definition of CustomClass:

```py
class CustomClass:
  def __init__(self, name: str) -> None:
    self.name: str = name

  def print_name(self) -> None:
    print(self.name)

```

Try to call functions or vars of CustomClass-object

```py
from typing import Type  # you have to import Type

def foo(arg: Type[CustomClass]):
    arg. 
       #^print_name()
       # ...
``` 
