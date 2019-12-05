#!/usr/bin/env python3
import zipfile
import argparse
import os

parser = argparse.ArgumentParser(description='Bruteforce the password of a zip file.')
parser.add_argument('zipfile',type=str)
parser.add_argument('wordlist',type=str)

args = parser.parse_args()
zip_file_name = os.path.abspath(os.path.realpath(args.zipfile))
wordlist_name = os.path.abspath(os.path.realpath(args.wordlist))

with zipfile.ZipFile(zip_file_name,'r') as zip_file:
    with open(wordlist_name,'r') as wordlist:
        for line in wordlist:
            try :
                password_bytes = line.rstrip('\n').encode('utf-8')
                zip_file.extractall(pwd=password_bytes)
                print('success')
                try :
                    zip_file.extractall()
                    print('zip is unencrypted');
                except:
                    print( 'password is {}'.format(line.rstrip('\n')) )
                break
            except:
                pass
        else:
            print('fail, no password matched')
