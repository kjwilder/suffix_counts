# Suffix Counts

## Example:

The sample `words.txt` file contains the following words:
```
A
ALL
BALL
CALL
DOLL
```

The output of running `words.py` is:
```
 1                        [A]
 1 LL                     [A]
 1 OLL                    [D]
 2 ALL                    [B C]
```

Word suffixes here are all the letters that follow the first letter of a word.
There are four suffixes, three of which occur once ('', 'LL' and 'OLL'), and
one of which occurs twice ('ALL'). The output is sorted ascendingly by how
often the suffix occurs. The most common suffix above is 'ALL' as it occurs
twice with the first letters 'B' and 'C'.

The sample `words.txt` can be replaced with any list of words including the
Project Gutenberg list from the `data` directory.
