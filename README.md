# Accessible Trees

This tool creates accessible trees in HTML.
It automatically adds `aria-role="tree"` and `aria-role="treeitem"` to the relevant items.

## Usage

To change the output of the tree, read the `data.py` file.
Many, *many* examples are laid out in there.
You do not need to create a tuple if there are no children.

Install one (optional) package: `bs4` (Beautiful Soup 4), with `pip install -r requirements.txt`.
This will make the output "pretty" (i.e. indented).

To print the output to terminal, run `python tree.py`

To save to a file, run `python tree.py file.html`.

To append to an already existing file, run `python tree.py >> file.html`
