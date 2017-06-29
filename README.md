# LineSweeper

(C) Keziah Milligan, 2017

GPL v3. See LICENSE or https://www.gnu.org/licenses/gpl-3.0.en.html for full details.


## What is it?

LineSweeper is a command line tool, which will remove errant whitespace 
characters from a csv (or similar tab delimited) file, e.g. new line 
characters in a address field.

For example, running LineSweeper on a csv file containing

    id, name, address, city, country
    345, Smith, 0/2\n34 Made Up Street, London, UK

would replace the new line character ``\n`` with a single space:

    id, name, address, city, country
    345, Smith, 0/2 34 Made Up Street, London, UK
    
This also works for Windows-style new line characters ``\r\n``.


You need Python 3 to use LineSweeper, as well as the 
[Pandas](http://pandas.pydata.org/index.html) package.
You can download Python 3 [here](https://www.python.org/downloads/)
or from your package manager or as part of a distribution such as [Anaconda](https://www.continuum.io/)
(which will automatically include Pandas).


## How do I use it?

To display the command line options, run

    $ python LineSweeper.py -h


LineSweeper takes an input file and optionally an output file (if no output file
is provided, the input will be overwritten). The default separator for both input
and output is a comma, but this can be changed with the ``--insep`` and ``--outsep`` 
flags (note that if you wish to specify a special character as the delimiter, it should
be enclosed in quotation marks, e.g. ``"\t"``).

The ``--field`` option can be used to specify which column of the csv file to check. 
If not included in the arguments, all fields will be checked. Multiple fields can
be specified by giving a comma-separated list, e.g. ``-f address1,address2``.

If the given output file already exists, to will be prompted to either overwrite or
provide a different name. The ``--auto_overwrite`` flag can be used if you want 
to overwrite the file without prompt.

For example, to check a file ``input.csv`` for errant whitespace in a field ``House number``
and write to a tab-delimited file ``output.txt``, run the command

    $ python LineSweeper.py input.csv -f "House number" -o output.txt -os "\t"


If you want to be able to call LineSweeper from anywhere in your system, without having
LineSweeper.py in the same directory as &mdash; or having long file paths to &mdash; the input, you
can put the command to call LineSweeper in a script (making sure your system PATH is set 
accordingly).

For example, in UNIX-based operating systems, this would be along the lines of:

    #!/bin/bash
    python ~/path/to/LineSweeper.py "@*"

or in Windows:

    python C:\path\to\LineSweeper.py %*
