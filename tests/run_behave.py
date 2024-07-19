import sys
import os
from behave import __main__ as behave_executable

# اضافه کردن مسیر src به PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# تنظیم مسیرها
features_directory = os.path.join(os.path.dirname(__file__), 'features')

# اجرای behave
sys.argv = ['behave', features_directory]
behave_executable.main()
