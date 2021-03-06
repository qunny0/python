#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Knight
# Date: 2015-09-23 15:16:03
#

import csv
import time
import codecs
import os

kAuthor = "Knight"

kNumberType = "number"

kBoolType = "bool"
kBoolTypeFalse = 'false'
kBoolTypeTrue = 'true'

kStringType = "string"

kTargetLuaFilePath = '../../src/app/db/%s.lua'

fieldnames = []
fieldTypes = []
fieldDesc = []

strLuaFileComment = (	'-- \n'
						'-- Author: %s\n'
						'-- Date: %s\n'
						'-- \n'
						'-- This file is automatically generated.\n' 
						'-- DO NOT manually modify!!!\n-- \n\n'
				 	)

strLuaGetDataFormat = (	'\n\nfunction %sTable:getDataById(id)\n'
						'\tfor i,v in ipairs(%sTable) do\n'
						'\t\tif v.id == id then\n'
						'\t\t\treturn v\n'
						'\t\tend\n'
						'\tend\n'
						'\treturn nil\n'
						'end\n'
					)

strLuaReturnTable = '\n\nreturn %sTable'

def csv2lua(filepath, filename):
	csvfile = file(filepath, 'rb')
	reader = csv.reader(csvfile)

	fieldnames = reader.next()
	fieldTypes = reader.next()
	fieldDesc = reader.next()

	luapath = kTargetLuaFilePath % (filename)
	output = codecs.open(luapath, 'w+', 'utf-8')

	# create file comment
	now = time.strftime('%Y-%m-%d %H:%M:%S')
	fileComment = strLuaFileComment % (kAuthor, now)
	output.write(fileComment)

	# lua table define  -- local [filename]Table = {
	format = 'local %sTable = { \n'
	outputData = format % (filename)
	output.write(outputData)

	# lua table data  -- format
	format = '\t{\n'
	for index in range(0,len(fieldnames)):
		format = format + '\t\t' + fieldnames[index] + ' = '
		fieldtype = fieldTypes[index].lower()
		if fieldtype == kStringType:
			format = format + '\"%s\"'
		elif fieldtype == kNumberType or fieldtype == kBoolType :
			format = format + '%s'
		else:
			assert False, '!!!!!' + filename + '.csv file format error!!!!!'

		format = format + ',\n'
	format = format + '\t},\n'

	# lua table data -- values
	values = ()
	for line in reader:

		if line == '':
			continue 

		lineList = line
		for index in range(0, len(line)):
			value = lineList[index].lower()
			if fieldTypes[index].lower() == kBoolType:
				if value == kBoolTypeFalse or value == '0' or value == '':
					lineList[index] = kBoolTypeFalse
				else :
					lineList[index] = kBoolTypeTrue

		values = tuple(lineList)
		outputData = format % values
		output.write(outputData.decode('gb2312'))

	# lua table define -- }
	outputData = '}\n'
	output.write(unicode(outputData))

	# lua function getDataById(id)
	outputData = strLuaGetDataFormat % (filename, filename)
	output.write(outputData)

	# lua return table
	outputData = strLuaReturnTable % (filename)
	output.write(outputData)

	output.close()


def traversal_dir(dir):
	for parent, dirnames, filenames in os.walk(dir):
		for filename in filenames:
			# name, sufix = os.path.splitext(filename)[1][1:]
			name, ext = os.path.splitext(filename)
			ext = ext[1:]
			if ext == 'csv':
				fullpath = os.path.join(parent, filename)
				print(parent + '/' + filename)
				csv2lua(fullpath, name)


if __name__ == '__main__':
	traversal_dir('./')