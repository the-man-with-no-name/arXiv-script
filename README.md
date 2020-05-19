# arXiv-script
Retrieve the new articles from arXiv in a user given subject.

This script requires the modules ```sys```, ```requests```, and ```bs4``` (BeautifulSoup).

To run the script, cd to the directory containing ```arXivscript.py``` and run:

```python arXivscript.py SUBJECT```

where ```SUBJECT``` is the subject for which you wish to view the new submissions.

For example, if I wish to view articles on Combinatorics, I type:

```python arXivscript.py math.CO```

or

```python arXivscript.py cs.DS```

for articles on Data Structures and Algorithms.
