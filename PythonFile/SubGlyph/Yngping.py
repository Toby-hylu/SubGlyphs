# This is Yngping, a Romanization of Fuzhounese
from .generator import PhonemeMap

# --------------------------------------#------------------------------------- #
def SGYngping(): 
  # ------------------------------------#------------------------------------- #
  OnsetMapYngping = {                   # define onset map
    # Colloquail part
    ''    : ''    ,                     # zero consonant
    
    'b'   : 'pq'  ,                     # b   = voiceless labial plosive
    'p'   : 'pa'  ,                     # p   = aspirated labial plosive
    'm'   : 'pn'  ,                     # m   = labial nasal
                                        # m   = tone sandhi nasal case
    'w'   : 'pq,e',                     # w   = tone sandhi vowel case

    'd'   : 'tq'  ,                     # d   = voiceless alveolar plosive
    't'   : 'ta'  ,                     # t   = aspirated alveolar plosive
    's'   : 'sf'  ,                     # s   = voiceless alveolar fricative
    'n'   : 'tn'  ,                     # n   = alveolar nasal
                                        # m   = tone sandhi nasal case
    'l'   : 'tl'  ,                     # l   = alveolar lateral approximant
    'll'  : 'tl,e',                     # ll  = tone sandhi vowel case
    
    'z'   : 'sq'  ,                     # z   = voiceless alveolar affricate
    'c'   : 'sa'  ,                     # c   = aspirated alveolar affricate
    'nj'  : 'sq,e',                     # nj  = tone sandhi nasal case
    'j'   : 'sq,v',                     # j   = tone sandhi vowel case
    
    'g'   : 'kq'  ,                     # g   = voiceless velar plosive
    'k'   : 'ka'  ,                     # k   = aspirated velar plosive
    'ng'  : 'kn'  ,                     # ng  = velar nasal
                                        # ng  = tone sandhi nasal case
    'h'   : 'kf'  ,                     # h   = voiceless glottal fricative
    'hh'  : 'hq'  ,                     # hh  = tone sandhi vowel case
  }
  # ------------------------------------#------------------------------------- #
  # ------------------------------------#------------------------------------- #
  RimeMapYngping = {                    # define rime map
    # without tense - loose pair
    'a'     : {'g': '' , 'n': 'oofu' , 'c': ''  },
    'ah'    : {'g': '' , 'n': 'oofu' , 'c': ''  },
    'ai'    : {'g': '' , 'n': 'vcai' , 'c': ''  },
    'au'    : {'g': '' , 'n': 'vcau' , 'c': ''  },
    'ang'   : {'g': '' , 'n': 'oofu' , 'c': 'ng'},
    'ak'    : {'g': '' , 'n': 'oofu' , 'c': 'ng'},

    'ia'    : {'g': 'i', 'n': 'oofu' , 'c': ''  },
    'iah'   : {'g': 'i', 'n': 'oofu' , 'c': ''  },
    'iai'   : {'g': 'i', 'n': 'vcai' , 'c': ''  },
    'iau'   : {'g': 'i', 'n': 'vcau' , 'c': ''  },
    'iang'  : {'g': 'i', 'n': 'oofu' , 'c': 'ng'},
    'iak'   : {'g': 'i', 'n': 'oofu' , 'c': 'ng'},

    'ua'    : {'g': 'u', 'n': 'oofu' , 'c': ''  },
    'uah'   : {'g': 'u', 'n': 'oofu' , 'c': ''  },
    'uai'   : {'g': 'u', 'n': 'vcai' , 'c': ''  },
    'uau'   : {'g': 'u', 'n': 'vcau' , 'c': ''  },
    'uang'  : {'g': 'u', 'n': 'oofu' , 'c': 'ng'},
    'uak'   : {'g': 'u', 'n': 'oofu' , 'c': 'ng'},

    'ie'    : {'g': 'i', 'n': 'omfu' , 'c': ''  },
    'ieh'   : {'g': 'i', 'n': 'omfu' , 'c': ''  },
    'ieng'  : {'g': 'i', 'n': 'omfu' , 'c': 'ng'},
    'iek'   : {'g': 'i', 'n': 'omfu' , 'c': 'ng'},

    'uo'    : {'g': 'u', 'n': 'cmbr' , 'c': ''  },
    'uoh'   : {'g': 'u', 'n': 'cmbr' , 'c': ''  },
    'uong'  : {'g': 'u', 'n': 'cmbr' , 'c': 'ng'},
    'uok'   : {'g': 'u', 'n': 'cmbr' , 'c': 'ng'},

    'yo'    : {'g': 'y', 'n': 'cmbr' , 'c': ''  },
    'yoh'   : {'g': 'y', 'n': 'cmbr' , 'c': ''  },
    'yong'  : {'g': 'y', 'n': 'cmbr' , 'c': 'ng'},
    'yok'   : {'g': 'y', 'n': 'cmbr' , 'c': 'ng'},

    # with tense - loose pair
    # tense - loose pair o/oo
    'o'     : {'g': '' , 'n': 'cmbr' , 'c': ''  },
    'oh'    : {'g': '' , 'n': 'cmbr' , 'c': ''  },
    'oung'  : {'g': '' , 'n': 'vcou' , 'c': 'ng'},
    'ouk'   : {'g': '' , 'n': 'vcou' , 'c': 'ng'},

    'oo'    : {'g': '' , 'n': 'ombr' , 'c': ''  },
    'ooh'   : {'g': '' , 'n': 'ombr' , 'c': ''  },
    'ooung' : {'g': '' , 'n': 'vcoou', 'c': 'ng'},
    'oouk'  : {'g': '' , 'n': 'vcoou', 'c': 'ng'},

    # tense - loose pair eo/oo
    'eo'    : {'g': '' , 'n': 'cmfr' , 'c': ''  },
    'eoh'   : {'g': '' , 'n': 'cmfr' , 'c': ''  },
    'eoy'   : {'g': '' , 'n': 'vcoi' , 'c': ''  },
    'eoyng' : {'g': '' , 'n': 'vcoi' , 'c': 'ng'},
    'eoyk'  : {'g': '' , 'n': 'vcoi' , 'c': 'ng'},

#   'oo'    : {'g': '' , 'n': 'ombr' , 'c': ''  },
    'ooy'   : {'g': '' , 'n': 'vcooi', 'c': ''  },
    'ooyng' : {'g': '' , 'n': 'vcooi', 'c': 'ng'},
    'ooyk'  : {'g': '' , 'n': 'vcooi', 'c': 'ng'},

    # tense - loose pair e/a
    'e'     : {'g': '' , 'n': 'omfu', 'c': ''  }, 
    'eh'    : {'g': '' , 'n': 'omfu', 'c': ''  },
    'eu'    : {'g': '' , 'n': 'vceu', 'c': ''  },
    'eing'  : {'g': '' , 'n': 'vcei', 'c': 'ng'}, 
    'eik'   : {'g': '' , 'n': 'vcei', 'c': 'ng'}, 

#   'a'     : {'g': '' , 'n': 'oofu', 'c': ''  },
    'au'    : {'g': '' , 'n': 'vcau', 'c': ''  },
    'aing'  : {'g': '' , 'n': 'vcai', 'c': 'ng'},
    'aik'   : {'g': '' , 'n': 'vcai', 'c': 'ng'},

    # tense - loose pair i/ei
    'i'     : {'g': '' , 'n': 'ccfu', 'c': ''  }, 
    'ih'    : {'g': '' , 'n': 'ccfu', 'c': ''  },
    'iu'    : {'g': '' , 'n': 'vciu', 'c': ''  },
    'ing'   : {'g': '' , 'n': 'ccfu', 'c': 'ng'},
    'ik'    : {'g': '' , 'n': 'ccfu', 'c': 'ng'},

    'ei'    : {'g': '' , 'n': 'vcei', 'c': ''  },
    'eih'   : {'g': '' , 'n': 'vcei', 'c': ''  },
#   'eing'  : {'g': '' , 'n': 'vcei', 'c': 'ng'},
#   'eik'   : {'g': '' , 'n': 'vcei', 'c': 'ng'},

    # tense - loose pair u/ou
    'u'     : {'g': '' , 'n': 'ccbr', 'c': ''  }, 
    'uh'    : {'g': '' , 'n': 'ccbr', 'c': ''  },
    'ui'    : {'g': '' , 'n': 'vcui', 'c': ''  },
    'ung'   : {'g': '' , 'n': 'ccbr', 'c': 'ng'},
    'uk'    : {'g': '' , 'n': 'ccbr', 'c': 'ng'},

    'ou'    : {'g': '' , 'n': 'vcou', 'c': ''  }, 
    'ouh'   : {'g': '' , 'n': 'vcou', 'c': ''  },
#   'oung'  : {'g': '' , 'n': 'vcou', 'c': 'ng'},
#   'ouk'   : {'g': '' , 'n': 'vcou', 'c': 'ng'},

    # tense-loose pair y/eoy
    'y'     : {'g': '' , 'n': 'ccfr', 'c': ''  }, 
    'yh'    : {'g': '' , 'n': 'ccfr', 'c': ''  },
    'yng'   : {'g': '' , 'n': 'ccfr', 'c': 'ng'},
    'yk'    : {'g': '' , 'n': 'ccfr', 'c': 'ng'},

#   'eoy'   : {'g': '' , 'n': 'vcoi', 'c': ''  },
    'eoyh'  : {'g': '' , 'n': 'vcoi', 'c': ''  },
#   'eoyng' : {'g': '' , 'n': 'vcoi', 'c': 'ng'},
#   'eoyk'  : {'g': '' , 'n': 'vcoi', 'c': 'ng'},
  }
  # ------------------------------------#------------------------------------- #
  # ------------------------------------#------------------------------------- #
  ToneMapYngping = {                    # define tone map
    '1': ['p', 'i'],                    # Ping, yin
    '2': ['s', 'i'],                    # Shang, yin
    '3': ['q', 'i'],                    # Qu, yin
    '4': ['r', 'i'],                    # Ru, yin
    '5': ['p', 'a'],                    # Ping, yang
    '6': ['s', 'a'],                    # Shang, yang
    '7': ['q', 'a'],                    # Qu, yang
    '8': ['r', 'a'],                    # Ru, yang
    '0': ['p', 'z'],                    # Ping, extanded
  }
  # ------------------------------------#------------------------------------- #
  # ------------------------------------#------------------------------------- #
  PM = PhonemeMap(
    system_name='Yngping', 
    OnsetMap=OnsetMapYngping, 
    RimeMap=RimeMapYngping, 
    ToneMap=ToneMapYngping, 
  )
  PM.to_sty()
  # ------------------------------------#------------------------------------- #
# --------------------------------------#------------------------------------- #