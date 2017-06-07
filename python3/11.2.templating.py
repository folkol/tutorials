from string import Template
t = Template('${village}folk send $$10 to $cause.')
print(t.substitute(village='Nottingham', cause='the ditch fund'))

t.safe_substitute()  # Leaves template placeholders unchanged instead of KeyError


import time, os.path

photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    delimiter = '%'

# fmt = input('Enter rename style (%{d}-date, %{n}-seqnum, %{f}-format): ')
fmt = 'lollers_%{d}_%{n}%f'
t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))

"""
img_1074.jpg --> lollers_05Jun17_0.jpg
img_1076.jpg --> lollers_05Jun17_1.jpg
img_1077.jpg --> lollers_05Jun17_2.jpg
"""
