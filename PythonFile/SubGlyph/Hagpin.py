# This is Hagpin, a Romanization of Hakka
from .generator import PhonemeMap

# --------------------------------------#------------------------------------- #
def SGHagpin(): 
  # ------------------------------------#------------------------------------- #
  OnsetMapHagpin = {                     # define onset map
    # Colloquail part
    ''    : ''    ,                     # zero consonant
    
    'b'   : 'pq'  ,                     # b   = voiceless labial plosive
    'p'   : 'pa'  ,                     # p   = aspirated labial plosive
    'm'   : 'pn'  ,                     # m   = labial nasal
    'f'   : 'pf'  ,                     # f   = voiceless labial fricative
    'v'   : 'pf,v',                     # v   = voiced labial fricative

    'd'   : 'tq'  ,                     # d   = voiceless alveolar plosive
    't'   : 'ta'  ,                     # t   = aspirated alveolar plosive
    'n'   : 'tn'  ,                     # n   = alveolar nasal
    'l'   : 'tl'  ,                     # l   = alveolar lateral approximant
    
    'z'   : 'sq'  ,                     # z   = voiceless alveolar affricate
    'c'   : 'sa'  ,                     # c   = aspirated alveolar affricate
    's'   : 'sf'  ,                     # s   = voiceless alveolar fricative
    
    'j'   : 'cq'  ,                     # j   = voiceless alveolo-palatal affricate
    'q'   : 'ca'  ,                     # q   = aspirated alveolo-palatal affricate
    'x'   : 'cf'  ,                     # x   = voiceless alveolo-palatal fricative
    
    'g'   : 'kq'  ,                     # k   = voiceless velar plosive
    'k'   : 'ka'  ,                     # kh  = aspirated velar plosive
    'ng'  : 'kn'  ,                     # ng  = velar nasal 
    'h'   : 'hf'  ,                     # h   = voiceless velar fricative
  }
  # ------------------------------------#------------------------------------- #
  # ------------------------------------#------------------------------------- #
  RimeMapHagpin = {                       # define rime map
    'i'     : {'g': '' , 'n': 'ccfu', 'c': ''  }, 
    'im'    : {'g': '' , 'n': 'ccfu', 'c': 'm' },
    'ib'    : {'g': '' , 'n': 'ccfu', 'c': 'm' },
    'in'    : {'g': '' , 'n': 'ccfu', 'c': 'n' },
    'id'    : {'g': '' , 'n': 'ccfu', 'c': 'n' },
    'ing'   : {'g': '' , 'n': 'ccfu', 'c': 'ng'},
    'ig'    : {'g': '' , 'n': 'ccfu', 'c': 'ng'},
    
    'ui'    : {'g': 'u', 'n': 'ccfu', 'c': ''  },
    'uim'   : {'g': 'u', 'n': 'ccfu', 'c': 'm' },
    'uib'   : {'g': 'u', 'n': 'ccfu', 'c': 'm' },
    'uin'   : {'g': 'u', 'n': 'ccfu', 'c': 'n' },
    'uid'   : {'g': 'u', 'n': 'ccfu', 'c': 'n' },
    'uing'  : {'g': 'u', 'n': 'ccfu', 'c': 'ng'},
    'uig'   : {'g': 'u', 'n': 'ccfu', 'c': 'ng'},

    'u'     : {'g': '' , 'n': 'ccbr', 'c': ''  }, 
    'um'    : {'g': '' , 'n': 'ccbr', 'c': 'm' },
    'ub'    : {'g': '' , 'n': 'ccbr', 'c': 'm' },
    'un'    : {'g': '' , 'n': 'ccbr', 'c': 'n' },
    'ud'    : {'g': '' , 'n': 'ccbr', 'c': 'n' },
    'ung'   : {'g': '' , 'n': 'ccbr', 'c': 'ng'},
    'ug'    : {'g': '' , 'n': 'ccbr', 'c': 'ng'},

    'iu'    : {'g': 'i', 'n': 'ccbr', 'c': ''  }, 
    'ium'   : {'g': 'i', 'n': 'ccbr', 'c': 'm' },
    'iub'   : {'g': 'i', 'n': 'ccbr', 'c': 'm' },
    'iun'   : {'g': 'i', 'n': 'ccbr', 'c': 'n' },
    'iud'   : {'g': 'i', 'n': 'ccbr', 'c': 'n' },
    'iung'  : {'g': 'i', 'n': 'ccbr', 'c': 'ng'},
    'iug'   : {'g': 'i', 'n': 'ccbr', 'c': 'ng'},

    'ii'    : {'g': '' , 'n': 'cccu', 'c': ''  },
    'iim'   : {'g': '' , 'n': 'cccu', 'c': 'm' },
    'iib'   : {'g': '' , 'n': 'cccu', 'c': 'm' },
    'iin'   : {'g': '' , 'n': 'cccu', 'c': 'n' },
    'iid'   : {'g': '' , 'n': 'cccu', 'c': 'n' },
    'iing'  : {'g': '' , 'n': 'cccu', 'c': 'ng'},
    'iig'   : {'g': '' , 'n': 'cccu', 'c': 'ng'},

    'e'     : {'g': '' , 'n': 'omfu', 'c': ''  },
    'eu'    : {'g': '' , 'n': 'vceu', 'c': ''  },
    'em'    : {'g': '' , 'n': 'omfu', 'c': 'm' },
    'eb'    : {'g': '' , 'n': 'omfu', 'c': 'm' },
    'en'    : {'g': '' , 'n': 'omfu', 'c': 'n' },
    'ed'    : {'g': '' , 'n': 'omfu', 'c': 'n' },
    'eng'   : {'g': '' , 'n': 'omfu', 'c': 'ng'},
    'eg'    : {'g': '' , 'n': 'omfu', 'c': 'ng'},

    'ie'    : {'g': 'i', 'n': 'omfu', 'c': ''  },
    'ieu'   : {'g': 'i', 'n': 'vceu', 'c': ''  },
    'iem'   : {'g': 'i', 'n': 'omfu', 'c': 'm' },
    'ieb'   : {'g': 'i', 'n': 'omfu', 'c': 'm' },
    'ien'   : {'g': 'i', 'n': 'omfu', 'c': 'n' },
    'ied'   : {'g': 'i', 'n': 'omfu', 'c': 'n' },
    'ieng'  : {'g': 'i', 'n': 'omfu', 'c': 'ng'},
    'ieg'   : {'g': 'i', 'n': 'omfu', 'c': 'ng'},

    'ue'    : {'g': 'u', 'n': 'omfu', 'c': ''  },
    'uem'   : {'g': 'u', 'n': 'omfu', 'c': 'm' },
    'ueb'   : {'g': 'u', 'n': 'omfu', 'c': 'm' },
    'uen'   : {'g': 'u', 'n': 'omfu', 'c': 'n' },
    'ued'   : {'g': 'u', 'n': 'omfu', 'c': 'n' },
    'ueng'  : {'g': 'u', 'n': 'omfu', 'c': 'ng'},
    'ueg'   : {'g': 'u', 'n': 'omfu', 'c': 'ng'},

    'o'     : {'g': '' , 'n': 'cmbr', 'c': ''  }, 
    'oi'    : {'g': '' , 'n': 'vcoi', 'c': ''  },
    'om'    : {'g': '' , 'n': 'cmbr', 'c': 'm' },
    'ob'    : {'g': '' , 'n': 'cmbr', 'c': 'm' },
    'on'    : {'g': '' , 'n': 'cmbr', 'c': 'n' },
    'od'    : {'g': '' , 'n': 'cmbr', 'c': 'n' },
    'ong'   : {'g': '' , 'n': 'cmbr', 'c': 'ng'},
    'og'    : {'g': '' , 'n': 'cmbr', 'c': 'ng'},

    'io'    : {'g': 'i', 'n': 'cmbr', 'c': ''  }, 
    'ioi'   : {'g': 'i', 'n': 'vcoi', 'c': ''  },
    'iom'   : {'g': 'i', 'n': 'cmbr', 'c': 'm' },
    'iob'   : {'g': 'i', 'n': 'cmbr', 'c': 'm' },
    'ion'   : {'g': 'i', 'n': 'cmbr', 'c': 'n' },
    'iod'   : {'g': 'i', 'n': 'cmbr', 'c': 'n' },
    'iong'  : {'g': 'i', 'n': 'cmbr', 'c': 'ng'},
    'iog'   : {'g': 'i', 'n': 'cmbr', 'c': 'ng'},

    'a'     : {'g': '' , 'n': 'oofu', 'c': ''  },
    'ai'    : {'g': '' , 'n': 'vcai', 'c': ''  },
    'au'    : {'g': '' , 'n': 'vcau', 'c': ''  },
    'am'    : {'g': '' , 'n': 'oofu', 'c': 'm' },
    'ab'    : {'g': '' , 'n': 'oofu', 'c': 'm' },
    'an'    : {'g': '' , 'n': 'oofu', 'c': 'n' },
    'ad'    : {'g': '' , 'n': 'oofu', 'c': 'n' },
    'ang'   : {'g': '' , 'n': 'oofu', 'c': 'ng'},
    'ag'    : {'g': '' , 'n': 'oofu', 'c': 'ng'},

    'ia'    : {'g': 'i', 'n': 'oofu', 'c': ''  },
    'iau'   : {'g': 'i', 'n': 'vcau', 'c': ''  },
    'iam'   : {'g': 'i', 'n': 'oofu', 'c': 'm' },
    'iab'   : {'g': 'i', 'n': 'oofu', 'c': 'm' },
    'ian'   : {'g': 'i', 'n': 'oofu', 'c': 'n' },
    'iad'   : {'g': 'i', 'n': 'oofu', 'c': 'n' },
    'iang'  : {'g': 'i', 'n': 'oofu', 'c': 'ng'},
    'iag'   : {'g': 'i', 'n': 'oofu', 'c': 'ng'},

    'ua'    : {'g': 'u', 'n': 'oofu', 'c': ''  },
    'uai'   : {'g': 'u', 'n': 'vcai', 'c': ''  },
    'uam'   : {'g': 'u', 'n': 'oofu', 'c': 'm' },
    'uab'   : {'g': 'u', 'n': 'oofu', 'c': 'm' },
    'uan'   : {'g': 'u', 'n': 'oofu', 'c': 'n' },
    'uad'   : {'g': 'u', 'n': 'oofu', 'c': 'n' },
    'uang'  : {'g': 'u', 'n': 'oofu', 'c': 'ng'},
    'uag'   : {'g': 'u', 'n': 'oofu', 'c': 'ng'},

    'm'     : {'g': '' , 'n': 'm'   , 'c': ''  },
    'n'     : {'g': '' , 'n': 'n'   , 'c': ''  },
    'ng'    : {'g': '' , 'n': 'ng'  , 'c': ''  },
  }
  # ------------------------------------#------------------------------------- #
  # ------------------------------------#------------------------------------- #
  ToneMapHagpin = {                      # define tone map
    '1': ['p', 'i'],                    # Ping, yin
    '2': ['p', 'a'],                    # Ping, yang
    '3': ['s', 'i'],                    # Shang, yin
    '4': ['q', 'i'],                    # Qu, yin
    '5': ['r', 'i'],                    # Ru, yin
    '6': ['r', 'a'],                    # Ru, yang
  }
  # ------------------------------------#------------------------------------- #
  # ------------------------------------#------------------------------------- #
  PM = PhonemeMap(
    system_name  ='Hagpin', 
    OnsetMap     =OnsetMapHagpin, 
    RimeMap      =RimeMapHagpin, 
    ToneMap      =ToneMapHagpin, 
    variant_name ='Xiian'
  )
  PM.to_sty()
  # ------------------------------------#------------------------------------- #
# --------------------------------------#------------------------------------- #