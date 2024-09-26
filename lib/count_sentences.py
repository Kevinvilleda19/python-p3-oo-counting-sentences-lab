#!/usr/bin/env python3
import re

class MyString:
  def __init__(self,value = ''):
    self.value = value

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    return self.value.endswith(".")

  def is_question(self):
    return self.value.endswith("?")

  def is_exclamation(self):
    return self.value.endswith("!")

  def count_sentences(self):
      sentences = re.split(r'[.!?]+\s*', self.value)

        # Filter out empty sentences (like trailing spaces)
      non_empty_sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

        # Return the count of non-empty sentences
      return len(non_empty_sentences)
