import os
import shutil

print(os.getcwd())

os.chdir('/tmp')
os.system('mkdir today')

shutil.copytree('/tmp/today', '/tmp/tomorrow')

shutil.move('foo.txt', 'bar.txt')
