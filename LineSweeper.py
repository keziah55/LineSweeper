#!/usr/bin/env python3
# Copyright (C) 2017, Keziah Milligan
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# The GNU General Public License can be found at: https://www.gnu.org/licenses/
"""
Replace any whitespace characters with a single space in a given field in a csv
file.
"""

import argparse
import os
import sys
import re
import pandas as pd
from codecs import decode


def remove_chars(in_file, out_file=None, insep=',', outsep=',', field=None, 
                 auto_overwrite=False):
        
    # if no out_file provided, overwrite input
    if out_file is None:
        out_file = in_file
        auto_overwrite = True

    df = pd.read_csv(in_file, sep=insep) 
    
    if not isinstance(field, (list,tuple)):
        if field is None:
            field = df.columns
        else:
            field = list(f.strip() for f in field.split(','))
        
    for f in field:
        for i in range(len(df[f])):
            
            entry = df[f][i]
            
            if isinstance(entry, str):
                # replace any whitespace character (that isn't just a space) 
                # with a single space
                if re.search(r'[^ \S]+', entry):
                    
                    new = re.sub(r'[^ \S]+', ' ', entry)
                    df.set_value(i, f, new)
            
            
    if not auto_overwrite:
        try:
            out_file = path_exists(out_file)
        except:
            sys.exit(1)
            
    df.to_csv(out_file, sep=outsep, index=False)
    print('Written', out_file)


def path_exists(savefile):
    
    while os.path.exists(savefile):
        print('{} already exists. Would you like to overwrite it? '
              '[Y/n]'.format(savefile))
        ow = input()
        if ow.lower() == 'n':
            print('Please enter new file name: ')
            savefile = input()
        elif ow.lower() == 'y' or not ow:
            break
        elif ow.lower() != 'y':
            raise Exception('Invalid input. Aborting.')

    return savefile


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description=__doc__)
    
    parser.add_argument('input', help='file to check')
    parser.add_argument('-is', '--insep', help='input file separator. '
                        'Default is comma. Special characters should be '
                        'enclosed in quotation marks, e.g. "\\t"', default=',')
    parser.add_argument('-o', '--out', help='output file')
    parser.add_argument('-os', '--outsep', help='output file separator. '
                        'Default is comma. Special characters should be '
                        'enclosed in quotation marks, e.g. "\\t"', default=',')
    parser.add_argument('-f', '--field', help='field (or list of fields) in '
                        'which to look for whitespce characters. If not '
                        'supplied, all fields will be searched')
    parser.add_argument('-w', '--auto_overwrite', action='store_true',
                        help='if the given output file already exists, '
                        'overwrite it without prompt.')
    
    args = parser.parse_args()
    
    # if separators contain special characters, make sure they are correctly
    # represented
    separators = [args.insep, args.outsep]
    
    for n in range(len(separators)):
        if separators[n] is not None:
            separators[n] = decode(separators[n], 'unicode_escape')

    remove_chars(args.input, args.out, separators[0], separators[1], 
                 args.field, args.auto_overwrite)
