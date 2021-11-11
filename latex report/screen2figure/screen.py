#!/usr/bin/env python3

import os
import sys
from pathlib import Path

template = r""" \begin{figure}[H]
    \centering
    \includegraphics[width=0.9\linewidth]{screens/$FILENAME}
    $CAPTION
\end{figure}"""

path = "." if len(sys.argv)==1 else sys.argv[1]
files = [os.path.basename(str(p)) 
         for p in Path(path).iterdir() 
         if p.is_file() and str(p).rsplit(".", 1)[-1].lower() in ("png", "jpg", "jpeg", "eps", "bmp")]
files.sort(key=os.path.getmtime)
for p in files:
    print(template.replace("$FILENAME", p).replace("$CAPTION", (r"\caption{"+str(p).rsplit(".",1)[0]+"}").replace("_"," ")
                                                                if any(x not in p.lower() for x in ("capture","screenshot")) else ""))
