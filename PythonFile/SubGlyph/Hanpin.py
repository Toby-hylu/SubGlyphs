# This is Hanpin, a Romanization of Mandarin
from .generator import PhonemeMap

# --------------------------------------#------------------------------------- #
def SGHanpin(): 
  # ------------------------------------#------------------------------------- #
  OnsetMapHanpin = {                    # define onset map
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
    
    'g'   : 'kq'  ,                     # g   = voiceless velar plosive
    'k'   : 'ka'  ,                     # k   = aspirated velar plosive
    'h'   : 'kf'  ,                     # h   = voiceless velar fricative

    'j'   : 'cq'  ,                     # j   = voiceless alveolo-palatal affricate
    'q'   : 'ca'  ,                     # q   = aspirated alveolo-palatal affricate
    'x'   : 'cf'  ,                     # x   = voiceless alveolo-palatal fricative
    
    'zh'  : 'rq'  ,                     # zh  = voiceless retroflex affricate
    'ch'  : 'ra'  ,                     # ch  = aspirated retroflex affricate
    'sh'  : 'rf'  ,                     # sh  = voiceless retroflex fricative
    'r'   : 'rv'  ,                     # r   = voiced retroflex affricate
    
    'z'   : 'sq'  ,                     # z   = voiceless alveolar affricate
    'c'   : 'sa'  ,                     # c   = aspirated alveolar affricate
    's'   : 'sf'  ,                     # s   = voiceless alveolar fricative

  }
  # ------------------------------------#------------------------------------- #
  # ------------------------------------#------------------------------------- #
  RimeMapHanpin = {                     # define rime map
    'i'     : {'g': '' , 'n': 'ccfu' }, 
    'u'     : {'g': '' , 'n': 'ccbr' }, 
    'ü'     : {'g': '' , 'n': 'ccfr' }, 
    'v'     : {'g': '' , 'n': 'ccfr' }, 

    'yi'    : {'g': '' , 'n': 'ccfu' }, 
    'wu'    : {'g': '' , 'n': 'ccbr' },
    'yu'    : {'g': '' , 'n': 'ccfr' },  
    
    'a'     : {'g': '' , 'n': 'oofu' },
    'ai'    : {'g': '' , 'n': 'vcai' },
    'ao'    : {'g': '' , 'n': 'vcau' }, 
    'an'    : {'g': '' , 'n': 'ncan' },
    'ang'   : {'g': '' , 'n': 'ncang'},
    
    'ia'    : {'g': 'i', 'n': 'oofu' },
    'iai'   : {'g': 'i', 'n': 'vcai' },
    'iao'   : {'g': 'i', 'n': 'vcau' }, 
    'ian'   : {'g': 'i', 'n': 'ncan' },
    'iang'  : {'g': 'i', 'n': 'ncang'},

    'ya'    : {'g': 'i', 'n': 'oofu' },
    'yai'   : {'g': 'i', 'n': 'vcai' },
    'yao'   : {'g': 'i', 'n': 'vcau' }, 
    'yan'   : {'g': 'i', 'n': 'ncan' },
    'yang'  : {'g': 'i', 'n': 'ncang'},

    'ua'    : {'g': 'u', 'n': 'oofu' },
    'uai'   : {'g': 'u', 'n': 'vcai' },
    'uan'   : {'g': 'u', 'n': 'ncan' },
    'uang'  : {'g': 'u', 'n': 'ncang'}, 

    'wa'    : {'g': 'u', 'n': 'oofu' },
    'wai'   : {'g': 'u', 'n': 'vcai' },
    'wan'   : {'g': 'u', 'n': 'ncan' },
    'wang'  : {'g': 'u', 'n': 'ncang'},

    'yuan'  : {'g': 'y', 'n': 'ncan' },

    'o'     : {'g': '' , 'n': 'cmbr' },
    'ou'    : {'g': '' , 'n': 'vcou' }, 

    'uo'    : {'g': 'u', 'n': 'cmbr' },

    'wo'    : {'g': 'u', 'n': 'cmbr' },

    'iu'    : {'g': 'i', 'n': 'vcou' },

    'you'   : {'g': 'i', 'n': 'vcou' },

    'e'     : {'g': '' , 'n': 'cmbu' }, 
    'ee'    : {'g': '' , 'n': 'omfu' }, 
    'ei'    : {'g': '' , 'n': 'vcei' },
    'en'    : {'g': '' , 'n': 'ncen' },
    'eng'   : {'g': '' , 'n': 'nceng'},

    'ie'    : {'g': 'i', 'n': 'omfu' }, 
    'in'    : {'g': 'i', 'n': 'ncen' },
    'ing'   : {'g': 'i', 'n': 'nceng'},
    
    'ye'    : {'g': 'i', 'n': 'omfu' }, 
    'yin'   : {'g': 'i', 'n': 'ncen' },
    'ying'  : {'g': 'i', 'n': 'nceng'},

    'ui'    : {'g': 'u', 'n': 'vcei' },
    'un'    : {'g': 'u', 'n': 'ncen' },
    'ong'   : {'g': 'u', 'n': 'nceng'},

    'wei'   : {'g': 'u', 'n': 'vcei' },
    'wen'   : {'g': 'u', 'n': 'ncen' },
    'weng'  : {'g': 'u', 'n': 'nceng'},

    'ue'    : {'g': 'y', 'n': 'omfu' }, 
    'iong'  : {'g': 'y', 'n': 'nceng'},

    'yue'   : {'g': 'y', 'n': 'omfu' },
    'yun'   : {'g': 'y', 'n': 'ncen' },
    'yong'  : {'g': 'y', 'n': 'nceng'},

    'er'    : {'g': '' , 'n': 'mmxu' },
  }
  # ------------------------------------#------------------------------------- #
  # ------------------------------------#------------------------------------- #
  RimeSpecialHanpin = {
    'i'     : {
      'zh'  : {'g': '' , 'n': 'ccxu' }, 
      'ch'  : {'g': '' , 'n': 'ccxu' }, 
      'sh'  : {'g': '' , 'n': 'ccxu' }, 
      'r'   : {'g': '' , 'n': 'ccxu' }, 
      'z'   : {'g': '' , 'n': 'ccxu' }, 
      'c'   : {'g': '' , 'n': 'ccxu' }, 
      's'   : {'g': '' , 'n': 'ccxu' }, 
    }, 
    'u'     : {
      'j'   : {'g': '' , 'n': 'ccfr' }, 
      'q'   : {'g': '' , 'n': 'ccfr' }, 
      'x'   : {'g': '' , 'n': 'ccfr' }, 
    },
    'uan'   : {
      'j'   : {'g': 'y', 'n': 'ncan' },
      'q'   : {'g': 'y', 'n': 'ncan' },
      'x'   : {'g': 'y', 'n': 'ncan' },
    }, 
    'un'   : {
      'j'   : {'g': 'y', 'n': 'ncen' },
      'q'   : {'g': 'y', 'n': 'ncen' },
      'x'   : {'g': 'y', 'n': 'ncen' },
    }, 
  }
  # ------------------------------------#------------------------------------- #
  # ------------------------------------#------------------------------------- #
  ToneMapHanpin = {                     # define tone map
    '1': ['p', 'i'],                    # Ping, yin
    '2': ['p', 'a'],                    # Ping, yang
    '3': ['s', 'i'],                    # Shang, yin
    '4': ['q', 'i'],                    # Qu, yin
    '5': ['p', 'z'],                    # Ping, extanded
  }
  # ------------------------------------#------------------------------------- #
  # ------------------------------------#------------------------------------- #
  PM = PhonemeMap(
    system_name='Hanpin', 
    OnsetMap=OnsetMapHanpin, 
    RimeMap=RimeMapHanpin, 
    ToneMap=ToneMapHanpin, 
    RimeSpecial=RimeSpecialHanpin,
  )
  PM.to_sty()
  # ------------------------------------#------------------------------------- #
# --------------------------------------#------------------------------------- #