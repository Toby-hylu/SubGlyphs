# This is Tailo, a Romanization of Taiwanese
from .generator import PhonemeMap

# --------------------------------------#------------------------------------- #
def SGTailo(): 
  # ------------------------------------#------------------------------------- #
  OnsetMapTailo = {                     # define onset map
    # Colloquail part
    ''    : ''    ,                     # zero consonant
    
    'p'   : 'pq'  ,                     # p   = voiceless labial plosive
    'ph'  : 'pa'  ,                     # ph  = aspirated labial plosive
    'm'   : 'pn'  ,                     # m   = labial nasal
    'b'   : 'pq,v',                     # b   = voiced labial plosive

    't'   : 'tq'  ,                     # t   = voiceless alveolar plosive
    'th'  : 'ta'  ,                     # th  = aspirated alveolar plosive
    'n'   : 'tn'  ,                     # n   = alveolar nasal
    'l'   : 'tl'  ,                     # l   = alveolar lateral approximant
    
    'ts'  : 'sq'  ,                     # ts  = voiceless alveolar affricate
    'tsh' : 'sa'  ,                     # tsh = aspirated alveolar affricate
    's'   : 'sf'  ,                     # s   = voiceless alveolar fricative
    'j'   : 'sq,v',                     # j   = voiced alveolar affricate
    
    'tsi' : 'cq'  ,                     # tsi = voiceless alveolo-palatal affricate
    'tshi': 'ca'  ,                     # tshi= aspirated alveolo-palatal affricate
    'si'  : 'cf'  ,                     # si  = voiceless alveolo-palatal fricative
    'ji'  : 'cq,v',                     # ji  = voiced alveolo-palatal affricate
    
    'k'   : 'kq'  ,                     # k   = voiceless velar plosive
    'kh'  : 'ka'  ,                     # kh  = aspirated velar plosive
    'ng'  : 'kn'  ,                     # ng  = velar nasal
    'g'   : 'kq,v',                     # g   = voiced velar plosive
    
    'h'   : 'hf'  ,                     # h   = voiceless glottal fricative
  }
  # ------------------------------------#------------------------------------- #
  # ------------------------------------#------------------------------------- #
  RimeMapTailo = {                       # define rime map
    'i'     : {'g': '' , 'n': 'ccfu'  , 'c': ''  }, 
    'ih'    : {'g': '' , 'n': 'ccfu'  , 'c': ''  },
    'inn'   : {'g': '' , 'n': 'ccfu,e', 'c':''  },
    'innh'  : {'g': '' , 'n': 'ccfu,e', 'c':''  },

    'u'     : {'g': '' , 'n': 'ccbr'  , 'c': ''  }, 
    'uh'    : {'g': '' , 'n': 'ccbr'  , 'c': ''  },
    'unn'   : {'g': '' , 'n': 'ccbr,e', 'c':''  },
    'unnh'  : {'g': '' , 'n': 'ccbr,e', 'c':''  },

    'iu'    : {'g': 'i', 'n': 'ccbr'  , 'c': ''  }, 
    'iuh'   : {'g': 'i', 'n': 'ccbr'  , 'c': ''  },
    'iunn'  : {'g': 'i', 'n': 'ccbr,e', 'c':''  },
    'iunnh' : {'g': 'i', 'n': 'ccbr,e', 'c':''  },

    'ui'    : {'g': 'u', 'n': 'ccfu'  , 'c': ''  }, 
    'uih'   : {'g': 'u', 'n': 'ccfu'  , 'c': ''  },
    'uinn'  : {'g': 'u', 'n': 'ccfu,e', 'c':''  },
    'uinnh' : {'g': 'u', 'n': 'ccfu,e', 'c':''  },

    'e'     : {'g': '' , 'n': 'cmfu'  , 'c': ''  }, 
    'eh'    : {'g': '' , 'n': 'cmfu'  , 'c': ''  },
    'enn'   : {'g': '' , 'n': 'cmfu,e', 'c':''  },
    'ennh'  : {'g': '' , 'n': 'cmfu,e', 'c':''  },

    'o'     : {'g': '' , 'n': 'cmbr'  , 'c': ''  }, 
    'oh'    : {'g': '' , 'n': 'cmbr'  , 'c': ''  },
    'onn'   : {'g': '' , 'n': 'cmbr,e', 'c':''  },
    'onnh'  : {'g': '' , 'n': 'cmbr,e', 'c':''  },

    'io'    : {'g': 'i', 'n': 'cmbr'  , 'c': ''  }, 
    'ioh'   : {'g': 'i', 'n': 'cmbr'  , 'c': ''  },
    'ionn'  : {'g': 'i', 'n': 'cmbr,e', 'c':''  },
    'ionnh' : {'g': 'i', 'n': 'cmbr,e', 'c':''  }, 

    'ue'    : {'g': 'u', 'n': 'cmfu'  , 'c': ''  }, 
    'ueh'   : {'g': 'u', 'n': 'cmfu'  , 'c': ''  },
    'uenn'  : {'g': 'u', 'n': 'cmfu,e', 'c':''  }, 
    'uennh' : {'g': 'u', 'n': 'cmfu,e', 'c':''  },

    'a'     : {'g': '' , 'n': 'oofu'  , 'c': ''  }, 
    'ah'    : {'g': '' , 'n': 'oofu'  , 'c': ''  }, 
    'ann'   : {'g': '' , 'n': 'oofu,e', 'c':''  }, 
    'annh'  : {'g': '' , 'n': 'oofu,e', 'c':''  }, 
    
    'oo'    : {'g': '' , 'n': 'ombr'  , 'c': ''  },
    'ooh'   : {'g': '' , 'n': 'ombr'  , 'c': ''  },
    'oonn'  : {'g': '' , 'n': 'ombr,e', 'c':''  },
    'oonnh' : {'g': '' , 'n': 'ombr,e', 'c':''  },

    'ia'    : {'g': 'i', 'n': 'oofu'  , 'c': ''  }, 
    'iah'   : {'g': 'i', 'n': 'oofu'  , 'c': ''  }, 
    'iann'  : {'g': 'i', 'n': 'oofu,e', 'c':''  }, 
    'iannh' : {'g': 'i', 'n': 'oofu,e', 'c':''  }, 

    'ua'    : {'g': 'u', 'n': 'oofu'  , 'c': ''  }, 
    'uah'   : {'g': 'u', 'n': 'oofu'  , 'c': ''  }, 
    'uann'  : {'g': 'u', 'n': 'oofu,e', 'c':''  }, 
    'uannh' : {'g': 'u', 'n': 'oofu,e', 'c':''  }, 

    'ai'    : {'g': '' , 'n': 'vcai'  , 'c': ''  },
    'aih'   : {'g': '' , 'n': 'vcai'  , 'c': ''  },
    'ainn'  : {'g': '' , 'n': 'vcai,e', 'c':''  },
    'ainnh' : {'g': '' , 'n': 'vcai,e', 'c':''  },

    'au'    : {'g': '' , 'n': 'vcau'  , 'c': ''  },
    'auh'   : {'g': '' , 'n': 'vcau'  , 'c': ''  },
    'aunn'  : {'g': '' , 'n': 'vcau,e', 'c':''  },
    'aunnh' : {'g': '' , 'n': 'vcau,e', 'c':''  },

    'iau'   : {'g': 'i', 'n': 'vcau'  , 'c': ''  },
    'iauh'  : {'g': 'i', 'n': 'vcau'  , 'c': ''  },
    'iaunn' : {'g': 'i', 'n': 'vcau,e', 'c':''  },
    'iaunnh': {'g': 'i', 'n': 'vcau,e', 'c':''  },

    'uai'   : {'g': 'u', 'n': 'vcai'  , 'c': ''  },
    'uaih'  : {'g': 'u', 'n': 'vcai'  , 'c': ''  },
    'uainn' : {'g': 'u', 'n': 'vcai,e', 'c':''  },
    'uainnh': {'g': 'u', 'n': 'vcai,e', 'c':''  },

    'm'     : {'g': '' , 'n': 'm'     , 'c': ''  },
    'mh'    : {'g': '' , 'n': 'm'     , 'c': ''  },
    'ng'    : {'g': '' , 'n': 'ng'    , 'c': ''  },
    'ngh'   : {'g': '' , 'n': 'ng'    , 'c': ''  },
    
    # Literary part
    'im'    : {'g': '' , 'n': 'ccfu'  , 'c': 'm' },
    'in'    : {'g': '' , 'n': 'ccfu'  , 'c': 'n' },
    'ing'   : {'g': '' , 'n': 'ccfu'  , 'c': 'ng'},
    'ip'    : {'g': '' , 'n': 'ccfu'  , 'c': 'm' },
    'it'    : {'g': '' , 'n': 'ccfu'  , 'c': 'n' },
    'ik'    : {'g': '' , 'n': 'ccfu'  , 'c': 'ng'},
    
    'om'    : {'g': '' , 'n': 'cmbr'  , 'c': 'm' },
    'un'    : {'g': '' , 'n': 'ccbr'  , 'c': 'n' },
    'ong'   : {'g': '' , 'n': 'cmbr'  , 'c': 'ng'},
    'op'    : {'g': '' , 'n': 'cmbr'  , 'c': 'm' },
    'ut'    : {'g': '' , 'n': 'ccbr'  , 'c': 'n' },
    'ok'    : {'g': '' , 'n': 'cmbr'  , 'c': 'ng'},
    
    'iom'   : {'g': 'i', 'n': 'cmbr'  , 'c': 'm' },
    'iun'   : {'g': 'i', 'n': 'ccbr'  , 'c': 'n' },
    'iong'  : {'g': 'i', 'n': 'cmbr'  , 'c': 'ng'}, 
    'iop'   : {'g': 'i', 'n': 'cmbr'  , 'c': 'm' },
    'iut'   : {'g': 'i', 'n': 'ccbr'  , 'c': 'n' },
    'iok'   : {'g': 'i', 'n': 'cmbr'  , 'c': 'ng'}, 

    'am'    : {'g': '' , 'n': 'oofu'  , 'c': 'm' },
    'an'    : {'g': '' , 'n': 'oofu'  , 'c': 'n' },
    'ang'   : {'g': '' , 'n': 'oofu'  , 'c': 'ng'},
    'ap'    : {'g': '' , 'n': 'oofu'  , 'c': 'm' },
    'at'    : {'g': '' , 'n': 'oofu'  , 'c': 'n' },
    'ak'    : {'g': '' , 'n': 'oofu'  , 'c': 'ng'},

    'iam'   : {'g': 'i', 'n': 'oofu'  , 'c': 'm' },
    'ian'   : {'g': 'i', 'n': 'oofu'  , 'c': 'n' },
    'iang'  : {'g': 'i', 'n': 'oofu'  , 'c': 'ng'},
    'iap'   : {'g': 'i', 'n': 'oofu'  , 'c': 'm' },
    'iat'   : {'g': 'i', 'n': 'oofu'  , 'c': 'n' },
    'iak'   : {'g': 'i', 'n': 'oofu'  , 'c': 'ng'},

    'uam'   : {'g': 'u', 'n': 'oofu'  , 'c': 'm' },
    'uan'   : {'g': 'u', 'n': 'oofu'  , 'c': 'n' },
    'uang'  : {'g': 'u', 'n': 'oofu'  , 'c': 'ng'},
    'uap'   : {'g': 'u', 'n': 'oofu'  , 'c': 'm' },
    'uat'   : {'g': 'u', 'n': 'oofu'  , 'c': 'n' },
    'uak'   : {'g': 'u', 'n': 'oofu'  , 'c': 'ng'},
  }
  # ------------------------------------#------------------------------------- #
  # ------------------------------------#------------------------------------- #
  ToneMapTailo = {                      # define tone map
    '1': ['p', 'i'],                    # Ping, yin
    '2': ['s', 'i'],                    # Shang, yin
    '3': ['q', 'i'],                    # Qu, yin
    '4': ['r', 'i'],                    # Ru, yin
    '5': ['p', 'a'],                    # Ping, yang
    '6': ['s', 'a'],                    # Shang, yang
    '7': ['q', 'a'],                    # Qu, yang
    '8': ['r', 'a'],                    # Ru, yang
  }
  # ------------------------------------#------------------------------------- #
  # ------------------------------------#------------------------------------- #
  PM = PhonemeMap(
    system_name='Tailo', 
    OnsetMap=OnsetMapTailo, 
    RimeMap=RimeMapTailo, 
    ToneMap=ToneMapTailo, 
  )
  PM.to_sty()
  # ------------------------------------#------------------------------------- #
# --------------------------------------#------------------------------------- #