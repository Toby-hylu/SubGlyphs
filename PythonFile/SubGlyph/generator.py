# Provides class PhonemeMap
from pathlib import Path
# --------------------------------------#------------------------------------- #
"""
If the forms are incorrect, the latex .sty may not work correctly
Please define onset map in the form of: 
OnsetMap = {
  'b': 'pq',                            # voiceless labial plosive
  ...
}
Please define rime map in the form of: 
- roman_letter: {'g': glide, 'n': nucleus, 'e': coda_ext, 'c': coda_main}
- There MUST be 'n': nucleus, since every sinitic language has nucleus
- Please make sure that EVERY rime shares the same structure
-- since undefined and defined as empty are DIFFERENT in latex logic
'coda_ext' is for those with special diphthongs
- Please use it only when your language: 
-- 1. contains diphthons other than [a, e, o, oo] X [i, u, y] 
-- 2. the diphthongs can combine with consonant codas
-- 3. Suzhou numerals are not enough to describe those diphthongs, i.e. more than 9
-- This is because the typeset result may not be very the best if you use it
RimeMap  = {
  'a'    : {'g': '' , 'n': 'oofu' },    # deault: open front unrounded
  'ang'  : {'g': '' , 'n': 'ncang'},    # or {'', 'ncang', ''}
  'i'    : {'g': '' , 'n': 'ccfu' },    # default i
}
...
Please define tone map in the form of: 
ToneMap = {
  '1'  : ['p', 'i'],                    # p means Ping, i means Yin
  '2'  : ['p', 'a'],                    # p means Ping, a means Yang
  '3'  : ['s', 'i'],                    # s means Shang
  '4'  : ['q', 'i'],                    # q means Qu
  '5'  : ['p', 'z'],                    # p means Ping, z means Expanded
}
Please define special rule map in the form of: 
onset_special_rules = {
  'ts' : {                              # palatalization, for example
    'i': 'cq', 
    'y': 'cq', 
  }, 
    ...
} 
rime_special_rules = {
    'i'  : {                            # empty rime rules
      'z': {'g': '', 'n': 'ccxu'},      # i coupled with z
      'c': {'g': '', 'n': 'ccxu'},      # i coupled with c
      ...                               # and s, zh, ch, sh, r
    },
  }
}
"""
# --------------------------------------#------------------------------------- #
def get_command(                        # generate latex sty commands
  phType: str                         , # 'Onset', 'Nucleus', 'Glide', 'Coda', 'CodaExt'
  name:   str                         , # name of language
  roman1: str                         , # main roman letter
  code:   str                         , # the glyph code of the letter
  roman2: str=None                    , # coupled roman letter for special rules
):                                      # \newcommand{\...}{...}
  extrastr = f'@{roman2}' if roman2 is not None else ''
  commandstr = f'\\{phType}@{name}@{roman1}{extrastr}'
  return f'\\newcommand{{{commandstr}}}{{{code}}}%\n'
# --------------------------------------#------------------------------------- #
# --------------------------------------#------------------------------------- #
def get_tone_command(                   # tone commands, which contain numbers
  phType: str                         , # 'Toneclass' or 'Tonetype'
  name:   str                         , # name of language
  number: str                         , # tone number
  code:   str                         , # p,s,q,r or i,a,z
): 
  commandstr = f'{phType}@{name}@{number}'
  return f'\\expandafter\\newcommand\\csname {commandstr}\\endcsname{{{code}}}%\n'
# --------------------------------------#------------------------------------- #
# --------------------------------------#------------------------------------- #
def get_coda_interface(                 # coda / codaext interface command
  phType: str                         , # 'Coda' or 'CodaExt'
  name:   str                         , # name of language
  exist:  bool=False                  , # exist or not
): 
  commandstr = f'\\{phType}@{name}'
  if not exist: 
    return f'\\newcommand{{{commandstr}}}[1]{{}}%\n'
  result = f'\\newcommand{{{commandstr}}}[1]{{%\n'
  result += f'\t\\expandafter\\ifx\\csname {phType}@{name}@#1\\endcsname\\relax%\n'
  result += '\t\t?%\n'
  result += '\t\\else%\n'
  result += f'\t\t\\csname {phType}@{name}@#1\\endcsname%\n'
  result += '\t\\fi%\n'
  result += '}%\n'
  return result
# --------------------------------------#------------------------------------- #
# --------------------------------------#------------------------------------- #
def get_interface(                      # interface of onset, nucleus and glide
  phType: str                         , # 'Glide' ('Onset', 'Nucleus' if needed)
  name:   str                         , # name of language
  exist:  bool=False                  , # exist or not
): 
  commandstr = f'\\{phType}@{name}'
  if not exist: 
    return f'\\newcommand{{{commandstr}}}[2]{{}}%\n'
  result = f'\\newcommand{{{commandstr}}}[2]{{%\n'
  result += f'\t\\expandafter\\ifx\\csname {phType}@{name}@#1@#2\\endcsname\\relax%\n'
  result += f'\t\t\\expandafter\\ifx\\csname {phType}@{name}@#1\\endcsname\\relax%\n'
  result += '\t\t\t?%\n'
  result += '\t\t\\else%\n'
  result += f'\t\t\t\\csname {phType}@{name}@#1\\endcsname%\n'
  result += '\t\t\\fi%\n'
  result += '\t\\else%\n'
  result += f'\t\t\\csname {phType}@{name}@#1@#2\\endcsname%\n'
  result += '\t\\fi%\n'
  result += '}%\n'
  return result
# --------------------------------------#------------------------------------- #
# --------------------------------------#------------------------------------- #
def interface_update():                 # update the interface SubGlyph.sty
  interface_path = Path("../LatexFile/package/SubGlyph.sty")
  SG_sty_files = sorted(Path("../LatexFile/package").glob("SG*.sty"))
  require_syntax = [f'\\RequirePackage{{{f.stem}}}' for f in SG_sty_files]

  start_str = "% ======== AutoRequiredPackages START ======== %"
  end_str = "% ========= AutoRequiredPackages END ========= %"

  with interface_path.open() as f: 
    content = f.read()

    # split the file
    before, replaced, after = content.partition(start_str)
    _, _, after = after.partition(end_str)

    new_content = (
      before + 
      start_str + '\n' + 
      '\n'.join(require_syntax) + '\n' +
      end_str + 
      after
    )
    
  # update
  with interface_path.open('w') as f: 
    f.write(new_content)
# --------------------------------------#------------------------------------- #
# --------------------------------------#------------------------------------- #
class PhonemeMap:                       # Phoneme map
  # ------------------------------------#------------------------------------- #
  def __init__(
    self                              , #
    system_name  : str                , # name of system, Pinyin, Jyutping, etc.
    OnsetMap     : dict               , # onset map
    RimeMap      : dict               , # rime map
    ToneMap      : dict               , # tine map
    OnsetSpecial : dict=None          , # special rules of onset (coupled with rime)
    RimeSpecial  : dict=None          , # special rules of rime (coupled with onset)
    variant_name : str =None          , # name of variant, region, etc. 
  ): 
    self.system_name = system_name.capitalize()
    self.OnsetMap = OnsetMap
    self.RimeMap = RimeMap
    self.ToneMap = ToneMap
    self.OnsetSpecial = OnsetSpecial
    self.RimeSpecial = RimeSpecial
    self.variant_name = variant_name.capitalize() if variant_name is not None else ''
    self.name = f'{self.system_name}{self.variant_name}'
    self.filepath = f'../LatexFile/package/SG{self.name}.sty'
  # ------------------------------------#------------------------------------- #
  # ------------------------------------#------------------------------------- #
  def to_sty(self):                     # to latex command
    # Syllabic signs for glide, coda_ext and coda
    # They are optional, and behaviour in latex sty are different
    has_glide = False
    has_codaext = False
    has_coda = False
    
    # start of sty
    with open(self.filepath, 'w', encoding='utf-8') as f: 
      # write basic settings
      f.write(f'% Provides SubGlyph supporting package SG{self.name}\n')
      f.write(f'\\ProvidesPackage{{SG{self.name}}}%\n')
      f.write('\\RequirePackage{SGBasic}%\n')
      f.write('\n')
      
      f.write('\\makeatletter%\n')    # start of inner commands

      # onset commands
      f.write('% Onset\n')
      for roman, glyph_code in self.OnsetMap.items(): 
        f.write(get_command('Onset', self.name, roman, glyph_code))
      
      # rime commands
      f.write('% Rime\n')
      for roman, glyph_codes in self.RimeMap.items(): 
        if 'g' in glyph_codes: 
          has_glide = True
          f.write(get_command('Glide', self.name, roman, glyph_codes['g']))
        f.write(get_command('Nucleus', self.name, roman, glyph_codes['n']))
        if 'e' in glyph_codes: 
          has_codaext = True
          f.write(get_command('CodaExt', self.name, roman, glyph_codes['e']))
        if 'c' in glyph_codes: 
          has_coda = True
          f.write(get_command('Coda', self.name, roman, glyph_codes['c']))
      
      # tone commands
      f.write('% Tone\n')
      for number, glyph_codes in self.ToneMap.items(): 
        f.write(get_tone_command('Tonetype', self.name, number, glyph_codes[0]))
        f.write(get_tone_command('Toneclass', self.name, number, glyph_codes[1]))
      
      # onset special rules
      f.write('% Coupling rules\n')
      if self.OnsetSpecial is not None: 
        for roman1, rule_dict in self.OnsetSpecial.items(): 
          for roman2, glyph_code in rule_dict.items(): 
            f.write(get_command('Onset', self.name, roman1, glyph_code, roman2))
      if self.RimeSpecial is not None: 
        for roman1, rule_dict in self.RimeSpecial.items(): 
          for roman2, glyph_codes in rule_dict.items(): 
            if 'g' in glyph_codes: 
              has_glide = True
              f.write(get_command('Glide', self.name, roman1, glyph_codes['g'], roman2))
            f.write(get_command('Nucleus', self.name, roman1, glyph_codes['n'], roman2))
            if 'e' in glyph_codes: 
              has_codaext = True
              f.write(get_command('CodaExt', self.name, roman1, glyph_codes['e'], roman2))
            if 'c' in glyph_codes: 
              has_coda = True
              f.write(get_command('Coda', self.name, roman1, glyph_codes['c'], roman2))
      
      # interfaces of optional parts
      f.write('% Interface macros\n')
      f.write(get_interface('Glide', self.name, has_glide))
      f.write(get_coda_interface('CodaExt', self.name, has_codaext))
      f.write(get_coda_interface('Coda', self.name, has_coda))

      f.write('\\makeatother%\n')       # end of inner commands
      f.write('\\endinput')

    # update SubGlyph.sty
    interface_update()
  # ------------------------------------#------------------------------------- #
# --------------------------------------#------------------------------------- #