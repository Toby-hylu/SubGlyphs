# This is Jyutping, a Romanization of Cantonese
from .generator import PhonemeMap

# --------------------------------------#------------------------------------- #
def SGJyutping(): 
  # ------------------------------------#------------------------------------- #
  OnsetMapJyutping = {                  # define onset map
    # Colloquail part
    ''    : ''    ,                     # zero consonant
    
    'b'   : 'pq'  ,                     # b   = voiceless labial plosive
    'p'   : 'pa'  ,                     # p   = aspirated labial plosive
    'm'   : 'pn'  ,                     # m   = labial nasal
    'f'   : 'pf'  ,                     # f   = voiceless labial fricative

    'd'   : 'tq'  ,                     # d   = voiceless alveolar plosive
    't'   : 'ta'  ,                     # t   = aspirated alveolar plosive
    'n'   : 'tn'  ,                     # n   = alveolar nasal
    'l'   : 'tl'  ,                     # l   = alveolar lateral approximant
    
    'z'   : 'sq'  ,                     # ts  = voiceless alveolar affricate
    'c'   : 'sa'  ,                     # tsh = aspirated alveolar affricate
    's'   : 'sf'  ,                     # s   = voiceless alveolar fricative
    
    'g'   : 'kq'  ,                     # k   = voiceless velar plosive
    'k'   : 'ka'  ,                     # kh  = aspirated velar plosive
    'ng'  : 'kn'  ,                     # ng  = velar nasal
    'h'   : 'hf'  ,                     # h   = voiceless glottal fricative

    'gw'  : 'wq'  ,                     # gw  = voiceless labio-velar plosive
    'kw'  : 'wa'  ,                     # kw  = aspirated labio-velar plosive

    'j'   : 'i'   ,                     # j   = palatal approximant
    'w'   : 'u'   ,                     # w   = labio-velar approximant
  }
  # ------------------------------------#------------------------------------- #
  # ------------------------------------#------------------------------------- #
  RimeMapJyutping = {                   # define rime map
    'm'     : {'n': 'm'   , 'c': ''  },
    'ng'    : {'n': 'ng'  , 'c': ''  },
    
    'i'     : {'n': 'ccfu', 'c': ''  },
    'iu'    : {'n': 'ccfu', 'c': 'u' },
    'im'    : {'n': 'ccfu', 'c': 'm' },
    'in'    : {'n': 'ccfu', 'c': 'n' },
    'ing'   : {'n': 'ccfu', 'c': 'ng'},
    'ip'    : {'n': 'ccfu', 'c': 'm' },
    'it'    : {'n': 'ccfu', 'c': 'n' },
    'ik'    : {'n': 'ccfu', 'c': 'ng'},

    'yu'    : {'n': 'ccfr', 'c': ''  },
    'yum'   : {'n': 'ccfr', 'c': 'm' },
    'yun'   : {'n': 'ccfr', 'c': 'n' },
    'yung'  : {'n': 'ccfr', 'c': 'ng'},
    'yup'   : {'n': 'ccfr', 'c': 'm' },
    'yut'   : {'n': 'ccfr', 'c': 'n' },
    'yuk'   : {'n': 'ccfr', 'c': 'ng'},
    
    'u'     : {'n': 'ccbr', 'c': ''  },
    'ui'    : {'n': 'ccbr', 'c': 'i' },
    'um'    : {'n': 'ccbr', 'c': 'm' },
    'un'    : {'n': 'ccbr', 'c': 'n' },
    'ung'   : {'n': 'ccbr', 'c': 'ng'},
    'up'    : {'n': 'ccbr', 'c': 'm' },
    'ut'    : {'n': 'ccbr', 'c': 'n' },
    'uk'    : {'n': 'ccbr', 'c': 'ng'},

    'e'     : {'n': 'omfu', 'c': ''  },
    'ei'    : {'n': 'omfu', 'c': 'i' },
    'eu'    : {'n': 'omfu', 'c': 'u' },
    'em'    : {'n': 'omfu', 'c': 'm' },
    'en'    : {'n': 'omfu', 'c': 'n' },
    'eng'   : {'n': 'omfu', 'c': 'ng'},
    'ep'    : {'n': 'omfu', 'c': 'm' },
    'et'    : {'n': 'omfu', 'c': 'n' },
    'ek'    : {'n': 'omfu', 'c': 'ng'},

    'eo'    : {'n': 'cmcr', 'c': ''  },
    'eoi'   : {'n': 'cmcr', 'c': 'i' },
    'eou'   : {'n': 'cmcr', 'c': 'u' },
    'eom'   : {'n': 'cmcr', 'c': 'm' },
    'eon'   : {'n': 'cmcr', 'c': 'n' },
    'eong'  : {'n': 'cmcr', 'c': 'ng'},
    'eop'   : {'n': 'cmcr', 'c': 'm' },
    'eot'   : {'n': 'cmcr', 'c': 'n' },
    'eok'   : {'n': 'cmcr', 'c': 'ng'},

    'oe'    : {'n': 'omfr', 'c': ''  },
    'oei'   : {'n': 'omfr', 'c': 'i' },
    'oeu'   : {'n': 'omfr', 'c': 'u' },
    'oem'   : {'n': 'omfr', 'c': 'm' },
    'oen'   : {'n': 'omfr', 'c': 'n' },
    'oeng'  : {'n': 'omfr', 'c': 'ng'},
    'oep'   : {'n': 'omfr', 'c': 'm' },
    'oet'   : {'n': 'omfr', 'c': 'n' },
    'oek'   : {'n': 'omfr', 'c': 'ng'},

    'o'     : {'n': 'cmbr', 'c': ''  },
    'oi'    : {'n': 'cmbr', 'c': 'i' },
    'ou'    : {'n': 'cmbr', 'c': 'u' },
    'om'    : {'n': 'cmbr', 'c': 'm' },
    'on'    : {'n': 'cmbr', 'c': 'n' },
    'ong'   : {'n': 'cmbr', 'c': 'ng'},
    'op'    : {'n': 'cmbr', 'c': 'm' },
    'ot'    : {'n': 'cmbr', 'c': 'n' },
    'ok'    : {'n': 'cmbr', 'c': 'ng'},

    'a'     : {'n': 'oscu', 'c': ''  },
    'ai'    : {'n': 'oscu', 'c': 'i' },
    'au'    : {'n': 'oscu', 'c': 'u' },
    'am'    : {'n': 'oscu', 'c': 'm' },
    'an'    : {'n': 'oscu', 'c': 'n' },
    'ang'   : {'n': 'oscu', 'c': 'ng'},
    'ap'    : {'n': 'oscu', 'c': 'm' },
    'at'    : {'n': 'oscu', 'c': 'n' },
    'ak'    : {'n': 'oscu', 'c': 'ng'},

    'aa'    : {'n': 'oofu', 'c': ''  },
    'aai'   : {'n': 'oofu', 'c': 'i' },
    'aau'   : {'n': 'oofu', 'c': 'u' },
    'aam'   : {'n': 'oofu', 'c': 'm' },
    'aan'   : {'n': 'oofu', 'c': 'n' },
    'aang'  : {'n': 'oofu', 'c': 'ng'},
    'aap'   : {'n': 'oofu', 'c': 'm' },
    'aat'   : {'n': 'oofu', 'c': 'n' },
    'aak'   : {'n': 'oofu', 'c': 'ng'},
  }
  # ------------------------------------#------------------------------------- #
  # ------------------------------------#------------------------------------- #
  ToneMapJyutping = {                   # define tone map
    '1': ['p', 'i'],                    # Ping, yin
    '2': ['s', 'i'],                    # Shang, yin
    '3': ['q', 'i'],                    # Qu, yin
    '4': ['p', 'a'],                    # Ping, yang
    '5': ['s', 'a'],                    # Shang, yang
    '6': ['q', 'a'],                    # Qu, yang
    '7': ['r', 'i'],                    # Ru, yin
    '8': ['r', 'z'],                    # Ru, extanded
    '9': ['r', 'a'],                    # Ru, yang
  }
  # ------------------------------------#------------------------------------- #
  # ------------------------------------#------------------------------------- #
  OnsetSpecialJyutping = {
    'j' : {                             # j+i or j+yu -> i or yu
      'i'   : '', 
      'iu'  : '', 
      'im'  : '', 
      'in'  : '', 
      'ing' : '', 
      'ip'  : '', 
      'it'  : '', 
      'ik'  : '', 
      'yu'  : '', 
      'yum' : '', 
      'yun' : '', 
      'yung': '', 
      'yup' : '', 
      'yut' : '', 
      'yuk' : '', 
    }, 
    'w' : {                             # w + u -> u
      'u'   : '', 
      'ui'  : '', 
      'um'  : '', 
      'un'  : '', 
      'ung' : '', 
      'up'  : '', 
      'ut'  : '', 
      'uk'  : '', 
    }, 
  }
  # ------------------------------------#------------------------------------- #
  # ------------------------------------#------------------------------------- #
  PM = PhonemeMap(
    system_name='Jyutping', 
    OnsetMap=OnsetMapJyutping, 
    RimeMap=RimeMapJyutping, 
    ToneMap=ToneMapJyutping, 
    OnsetSpecial=OnsetSpecialJyutping, 
  )
  PM.to_sty()
  # ------------------------------------#------------------------------------- #
# --------------------------------------#------------------------------------- #