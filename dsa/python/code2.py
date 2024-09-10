from cx_Freeze import *
includefiles = ["iconfinder-499-student-education-graduate-learning-4212915_114945.ico"]
excludes = []
packages = []
base = None
if sys.platform == "win32":
    base = "Win32GUI"

shortcut_table = [
    ("DesktopShortcut",
     "DesktopFolder",
     "Student Management System",
     "TARGETDIR",
     "[TARGETDIR]\Student Management System.exe",
     None,
     None,
     None,
     None,
     None,
     None,
     "TARGETDIR",
     )
]

msi_data = {"Shortcut": Shortcut_table}

bdist_msi_options = {'data': msi_data}
setup(
    version="0.1",
    description="Student Management System Developed By Shourav Kumar",
    author="Shourav Kumar",
    name="Student Management system",
    options={'build_exe':{'include_files': includefiles}, "bdist_msi": bdist_msi_options, },
    executables=[
        Executables(
            script="Student Mangement System.py",
            base=base,
            icon='iconfinder-499-student-education-graduate-learning-4212915_114945.ico'

        )
    ]
)