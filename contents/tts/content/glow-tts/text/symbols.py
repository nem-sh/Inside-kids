""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details. '''
from text import cmudict

korean_jaso_code = list(range(0x1100, 0x1113)) + list(range(0x1161, 0x1176)) + list(range(0x11a8, 0x11c3))
korean_jaso = list(chr(c) for c in korean_jaso_code)

_punctuation = ' .!?'
_eos = '~'
_letters = korean_jaso

# Export all symbols:
symbols = list(_punctuation) + list(_letters) + list(_eos)
