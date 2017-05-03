#!/usr/local/bin/python

import argparse
import glob

def translate_erb(file, lang):
  print("Translating ERB {} to {}".format(file, lang))

def translate_jsx(file, lang):
  print("Translating JSX {} to {}".format(file, lang))

def translate_yaml(file, lang):
  print("Translating YAML {} to {}".format(file, lang))

def find_template_files():
  print("Finding original files")
  erb_files = []
  jsx_files = []
  yaml_files = []
  for filename in glob.iglob('**/*en.*', recursive=True):
    if filename.endswith(".erb"):
      erb_files.append(filename)
    elif filename.endswith(".jsx"):
      jsx_files.append(filename)
    elif filename.endswith(".yml"):
      yaml_files.append(filename)

  return erb_files, jsx_files, yaml_files

def main(lang):
  erb_files, jsx_files, yaml_files = find_template_files()
  for file in erb_files:
    translate_erb(file, lang)
  for file in jsx_files:
    translate_jsx(file, lang)
  for file in yaml_files:
    translate_yaml(file, lang)


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("lang", help="Language code to translate to e.g.")
  args = parser.parse_args()

  if args.lang:
    main(args.lang)
  else:
    print("Please pass the language you wish to translate to.")
