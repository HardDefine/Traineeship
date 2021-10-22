from os import readlink
from behave import *

@given(u'There is an empty text file available to us')
def create_text_file(context):
   context.filename = "empty_file.txt"
   bestand = open(context.filename, "wt")
   bestand.close()


@when(u'I open this file')
def create_text_file(context):
   context.document = open(context.filename, "at")



@when(u'I write the following table in it')
def step_impl(context):
   mijn_bestand = context.document
   for row in context.table:
      course = row["course"]
      participant = row["participants"]
      mijn_bestand.write(course + '\t' + participant + '\n')
   mijn_bestand.close()


@then(u'This file has 3 lines in it')
def step_impl(context):
    file = open(context.filename, 'rt')
    a = file.readlines()
    assert len(a) == 3



@given(u'The text file has been opened')
def step_impl(context):
   context.filename = 'secondFile.txt'
   file = open(context.filename, 'at')
   file.close()

@then(u'I write the values {one}, {two} and {three}')
def step_impl(context, one, two, three):
   context.file = open(context.filename, 'at')
   regel = one + '\t' + two + '\t' + three + '\n'
   context.file.write(regel)


@then(u'I close the file')
def step_impl(context):
    t = context.file
    t.close()
