#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self.value = value

  @property
  def value(self):
    """The value property""" 
    return self._value

  @value.setter
  def value(self, value):
    """The value property must be a string."""
    if isinstance (value, str):
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    return self._value.endswith(".")

  def is_question(self):
    return self._value.endswith("?")

  def is_exclamation(self):
    return self._value.endswith("!")

  def count_sentences(self):    
    sentences = [s.strip() for s in self._value.replace("!", ".").replace("?", ".").split(".") if s.strip()]
    return len(sentences)
    
    
