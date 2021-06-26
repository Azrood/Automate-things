# screen2figure
Convert all images of a folder to LaTeX figures. 

This is useful if you just want to put a number of images in a LaTeX report.

## Example
```
folder/
├── Main_menu.png
├── Screenshot from 2020-12-11 02-38-19.png
├── Example.jpg

```

```latex
\begin{figure}[H]
    \centering
    \includegraphics[width=0.9\linewidth]{screens/Main_menu.png}
    \caption{Main menu}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.9\linewidth]{screens/Screenshot from 2020-12-11 02-38-19.png}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.9\linewidth]{screens/Example.png}
    \caption{Example}
\end{figure}
```

## Note :
* Captions are removed if the file contains `screenshot` or `capture` in the filename.
* Captions have all `_` in filename are replaced with a space and extension removed.
* Figures are ordered by time of modification of the image files.

# Run

* Copy the file `screen.py` in your screens folder locally, or you can pass the path as argument.
```
python3 screen.py <PATH>
```
## Linux
Install xclip (useful if you want to copy the output to clipboard) then execute:
```bash
python3 screen.py <PATH> | xclip -sel clip
```
or (don't forget to `chmod +x screen.py`)
```bash
./screen.py <PATH> | xclip -sel clip
```
You can execute the script by itself but you will have to manually select and copy the output if you don't use `xclip`
## Windows
Check your python alias ( if it's `python3` or `python` or `py`)
```
python3 screen.py <PATH> | clip.exe
```
* **clip.exe** is the executable that manages your clipboard in windows
#### Note:
`clip.exe` is available in WSL, you don't need `xclip`

