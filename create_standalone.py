import os

# Requires Nuitka
os.system("""py -m nuitka --mingw64 "Windows 11 Context Menu Editor.pyw" --onefile --enable-plugin=tk-inter""")
