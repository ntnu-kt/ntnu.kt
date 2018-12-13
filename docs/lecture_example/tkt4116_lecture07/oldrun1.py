# Can I access the NTNU lib now?

import ntnu.kt

print(ntnu.kt.__file__)

# prints /home/teodorlu/.local/lib/python3.7/site-packages/ntnu/kt/__init__.py
# So this is installed locally, somehow.

# What does this contain? Let's find out.
#
# $ tree /home/teodorlu/.local/lib/python3.7/site-packages/ntnu
#    /home/teodorlu/.local/lib/python3.7/site-packages/ntnu
#    └── kt
#        ├── course
#        │   ├── __init__.py
#        │   ├── __pycache__
#        │   │   ├── __init__.cpython-37.pyc
#        │   │   └── tkt4116.cpython-37.pyc
#        │   └── tkt4116.py
#        ├── __init__.py
#        └── __pycache__
#            └── __init__.cpython-37.pyc

# There seems to be our files. What about version?


# ================================================================================

# But is there hotloading? Yes.

# import ntnu.kt.tkt4116
# from ntnu.kt import tkt4116 as mek1
import ntnu.kt.course.tkt4116 as mek1

print(mek1.__file__)
print(mek1.__package__)
print(mek1.__name__)

# What about lecture07?

import ntnu.kt.course.tkt4116.lecture07 as lecture

print(lecture.hello)

