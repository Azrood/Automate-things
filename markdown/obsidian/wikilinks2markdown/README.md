# wiki2mrkdown

Obsidian wikilinks are in the form `![[page name]]` or `[[page name]]` but this syntax isn't supported everywhere, for example on github. SO if you have your notes on Obsidian with attachments linked as Wikilinks, you will need to convert them to standard Markdown links. `[page name](url_or_path)`. This can be quite tedious to do by hand, so I made this script to convert all wikilinks in a file to markdown links.

# Example

Consider this file structure :
```
folder/
├── Main_menu.png
├── Screenshot from 2020-12-11 02-38-19.png
├── Notes.md
```

Let's look at the content of `Notes.md`.

**Notes.md**
```
Lorem ipsum dolor sit amet, consectetur adipiscing elit. In turpis libero, ullamcorper eu commodo quis, varius non urna.
![[ Main_menu.png ]]
Integer sodales, lorem sit amet fermentum rutrum, risus leo auctor magna, non efficitur nulla leo ut nisl. Aliquam erat volutpat. Quisque id mollis magna, eu tristique ante. Phasellus eget ipsum turpis. Mauris. 
[[ Screenshot from 2020-12-11 02-38-19.png ]]
```
If you want to upload this file to Github for example, the images won't be displayed.

After converting to markdown links
**Notes.md**
```
Lorem ipsum dolor sit amet, consectetur adipiscing elit. In turpis libero, ullamcorper eu commodo quis, varius non urna.
[Main_menu](folder/Main_menu.png)
Integer sodales, lorem sit amet fermentum rutrum, risus leo auctor magna, non efficitur nulla leo ut nisl. Aliquam erat volutpat. Quisque id mollis magna, eu tristique ante. Phasellus eget ipsum turpis. Mauris. 
[Screenshot from 2020-12-11 02-38-19](folder/Screenshot%20from%202020-12-11%2002-38-19.png)
```

### **N.B** :
* You need to have python >= 3.6 installed

# How to use :


