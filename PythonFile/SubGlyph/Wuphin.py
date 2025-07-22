# This is Wuphin, a Romanization of Suzhounese
from .generator import PhonemeMap

# --------------------------------------#------------------------------------- #
def SGWuphin(): 
  # ------------------------------------#------------------------------------- #
  OnsetMapWuphin = {                    # define onset map
    # Colloquail part
    ''    : ''    ,                     # zero consonant
    
    'p'   : 'pq'  ,                     # p   = voiceless labial plosive
    'ph'  : 'pa'  ,                     # ph  = aspirated labial plosive
    'b'   : 'pq,v',                     # b   = voiced labial plosive
    'm'   : 'pn'  ,                     # m   = labial nasal
    'f'   : 'pf'  ,                     # f   = voiceless labial fricative
    'v'   : 'pf,v',                     # v   = voiced labial fricative

    't'   : 'tq'  ,                     # t   = voiceless alveolar plosive
    'th'  : 'ta'  ,                     # th  = aspirated alveolar plosive
    'd'   : 'tq,v',                     # d   = voiced alveolar plosive
    'n'   : 'tn'  ,                     # n   = alveolar nasal
    'l'   : 'tl'  ,                     # l   = alveolar lateral approximant
    
    'ts'  : 'sq'  ,                     # ts  = voiceless alveolar affricate
    'tsh' : 'sa'  ,                     # tsh = aspirated alveolar affricate
    's'   : 'sf'  ,                     # s   = voiceless alveolar fricative
    'z'   : 'sf,v',                     # z   = voiced alveolar fricative
    
    'c'   : 'cq'  ,                     # c   = voiceless alveolo-palatal affricate
    'ch'  : 'ca'  ,                     # ch  = aspirated alveolo-palatal affricate
    'j'   : 'cq,v',                     # j   = voiced alveolo-palatal affricate
    'gn'  : 'cn'  ,                     # gn  = alveolo-palatal nasal
    'sh'  : 'cf'  ,                     # sh  = voiceless alveolo-palatal fricative
    
    'k'   : 'kq'  ,                     # k   = voiceless velar plosive
    'kh'  : 'ka'  ,                     # kh  = aspirated velar plosive
    'g'   : 'kq,v',                     # g   = voiced velar plosive
    'ng'  : 'kn'  ,                     # ng  = velar nasal
    
    'h'   : 'hf'  ,                     # h   = voiceless glottal fricative
    'gh'  : 'hf,v',                     # h   = voiced glottal fricative
    'y'   : 'hf,v',                     # h   = voiced glottal fricative
    'w'   : 'hf,v',                     # h   = voiced glottal fricative
  }
  # ------------------------------------#------------------------------------- #
  # ------------------------------------#------------------------------------- #
  RimeMapWuphin = {                     # define rime map
    'y'    : {'g': '' , 'n': 'ccxu'  }, # unrounded empty rime
    'yu'   : {'g': '' , 'n': 'ccxr'  }, # rounded empty rime

    'i'    : {'g': '' , 'n': '5'     }, # unrounded syllabic fricative
    'u'    : {'g': '' , 'n': 'ccbr'  }, # normal u
    'iu'   : {'g': '' , 'n': '8'     }, # rounded syllabic fricative

    'en'   : {'g': '' , 'n': 'ncen'  }, # en
    'in'   : {'g': 'i', 'n': 'ncen'  }, # i + en
    'uen'  : {'g': 'u', 'n': 'ncen'  }, # u + en
    'iun'  : {'g': 'y', 'n': 'ncen'  }, # y + en

    'eq'   : {'g': '' , 'n': 'mmcu'  }, # eq only in checked tone
    'iq'   : {'g': 'i', 'n': 'mmcu'  }, # i + eq
    'ueq'  : {'g': 'u', 'n': 'mmcu'  }, # u + eq
    'iuq'  : {'g': 'y', 'n': 'mmcu'  }, # eq

    'e'    : {'g': '' , 'n': 'cmfu'  }, # e
    'ie'   : {'g': '' , 'n': 'ccfu'  }, # ie -> i
    'ue'   : {'g': 'u', 'n': 'cmfu'  }, # u + e

    'an'   : {'g': '' , 'n': 'oofu,e'}, # nasalized open front vowel
    'ian'  : {'g': 'i', 'n': 'oofu,e'}, 
    'uan'  : {'g': 'u', 'n': 'oofu,e'},

    'aeq'  : {'g': '' , 'n': 'oofu'  }, # aeq, only in checked tone
    'iaeq' : {'g': 'i', 'n': 'oofu'  }, 
    'uaeq' : {'g': 'u', 'n': 'oofu'  }, 
    'iuaeq': {'g': 'y', 'n': 'oofu'  }, 

    'oe'   : {'g': '' , 'n': 'cmfr'  }, # oe
    'ioe'  : {'g': 'i', 'n': 'cmfr'  }, 
    'uoe'  : {'g': 'u', 'n': 'cmfr'  }, 

    'o'    : {'g': '' , 'n': 'cmbr'  }, # o
    'io'   : {'g': 'i', 'n': 'cmbr'  }, 

    'on'   : {'g': '' , 'n': 'ncong' }, # ong
    'ion'  : {'g': 'i', 'n': 'ncong' }, # i + ong

    'oq'   : {'g': '' , 'n': 'cmbr'  }, # o + q
    'ioq'  : {'g': 'i', 'n': 'cmbr'  }, 

    'a'    : {'g': '' , 'n': 'ombu'  }, # aa
    'ia'   : {'g': 'i', 'n': 'ombu'  },  
    'ua'   : {'g': 'u', 'n': 'ombu'  }, 

    'aon'  : {'g': '' , 'n': 'ombu,e'}, # aan
    'iaon' : {'g': 'i', 'n': 'ombu,e'},  
    'uaon' : {'g': 'u', 'n': 'ombu,e'}, 

    'aq'   : {'g': '' , 'n': 'ombu'  }, # aaq
    'iaq'  : {'g': 'i', 'n': 'ombu'  }, 

    'au'   : {'g': '' , 'n': 'omfu'  }, # au -> ae
    'iau'  : {'g': 'i', 'n': 'omfu'  },  

    'eu'   : {'g': '' , 'n': 'vcoi'  }, # eu
    'ieu'  : {'g': '' , 'n': 'ccfr'  }, # ieu -> y

    'ou'   : {'g': '' , 'n': 'vcou'  }, # ou

    'er'   : {'g': '' , 'n': 'mmxu'  }, # l
    'm'    : {'g': '' , 'n': 'm'     }, # m
    'n'    : {'g': '' , 'n': 'n'     }, # n
    'ng'   : {'g': '' , 'n': 'ng'    }, # ng
  }
  # ------------------------------------#------------------------------------- #
  # ------------------------------------#------------------------------------- #
  ToneMapWuphin = {                     # define tone map
    '1': ['p', 'i'],                    # Ping, yin
    '2': ['p', 'a'],                    # Ping, yang
    '3': ['s', 'i'],                    # Shang, yin
    '4': ['s', 'a'],                    # Shang, yang
    '5': ['q', 'i'],                    # Qu, yin
    '6': ['q', 'a'],                    # Qu, yang
    '7': ['r', 'i'],                    # Ru, yin
    '8': ['r', 'a'],                    # Ru, yang
  }
  # ------------------------------------#------------------------------------- #
  # ------------------------------------#------------------------------------- #
  RimeSpecialWuphin = {
    # ghi -> y, ghiu -> yu, ghu -> w
    'e'   : {
      'y' : {'g': '' , 'n': 'ccfu'  }, 
      'w' : {'g': 'u', 'n': 'cmfu'  }, 
    }, 
    'an'  : {
      'y' : {'g': 'i', 'n': 'oofu,e'}, 
      'w' : {'g': 'u', 'n': 'oofu,e'}, 
    }, 
    'aeq' : {
      'y' : {'g': 'i', 'n': 'oofu'  }, 
      'w' : {'g': 'u', 'n': 'oofu'  }, 
    }, 
    'oe'  : {
      'y' : {'g': 'i', 'n': 'cmfr'  },
      'w' : {'g': 'u', 'n': 'cmfr'  },
    }, 
    'o'   : {
      'y' : {'g': 'i', 'n': 'cmbr'  },
    }, 
    'on'  : {
      'y' : {'g': 'i', 'n': 'ncong' }, 
    }, 
    'oq'  : {
      'y' : {'g': 'i', 'n': 'cmbr'  }, 
    }, 
    'a'   : {
      'y' : {'g': 'i', 'n': 'ombu'  }, 
      'w' : {'g': 'u', 'n': 'ombu'  }, 
    }, 
    'aon' : {
      'y' : {'g': 'i', 'n': 'ombu'  }, 
      'w' : {'g': 'u', 'n': 'ombu'  }, 
    }, 
    'aq'  : {
      'y' : {'g': 'i', 'n': 'ombu'  }, 
    }, 
    'au'  : {
      'y' : {'g': '' , 'n': 'omfu'  }, 
    }, 
    'eu'  : {
      'y' : {'g': '' , 'n': 'ccfr'  }, 
    }, 
    'u'   : {
      'y' : {'g': '' , 'n': '8'     },
    }, 
    'un'  : {
      'y' : {'g': 'y', 'n': 'ncen'  }, 
    }, 
    'uq'  : {
      'y' : {'g': 'y', 'n': 'cccu'  }, 
    }, 
    'uaeq':{
      'y' : {'g': 'y', 'n': 'oofu'  }, 
    }, 
  }
  # ------------------------------------#------------------------------------- #
  # ------------------------------------#------------------------------------- #
  PM = PhonemeMap(
    system_name ='Wuphin', 
    OnsetMap    =OnsetMapWuphin, 
    RimeMap     =RimeMapWuphin, 
    ToneMap     =ToneMapWuphin, 
    RimeSpecial =RimeSpecialWuphin,
    variant_name='Soutseu',
  )
  PM.to_sty()
  # ------------------------------------#------------------------------------- #
# --------------------------------------#------------------------------------- #