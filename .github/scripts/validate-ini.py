#!/usr/bin/env python3
"""Checks that the KDE INI-style theme files (colors, metadata.desktop, plasmarc) parse."""
import configparser
import pathlib
import sys

failures = []
for name in ('colors', 'metadata.desktop', 'plasmarc'):
	for path in pathlib.Path('.').rglob(name):
		parser = configparser.ConfigParser(strict=False, interpolation=None)
		try:
			parser.read_string(path.read_text(encoding='utf-8'))
		except Exception as error:
			failures.append(f'{path}: {error}')

if failures:
	print('\n'.join(failures))
	sys.exit(1)

print('All INI-style files parse cleanly.')
