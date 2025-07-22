# Package interface

# --------------------------------------#------------------------------------- #
from .Tailo    import SGTailo           # Taiwanese Lomaji
from .Hanpin   import SGHanpin          # Mandarin Pinyin
from .Hagpin   import SGHagpin          # Hakka Pinim
from .Jyutping import SGJyutping        # Cantonese ping
from .Yngping  import SGYngping         # Fuzhounese ping
from .Wuphin   import SGWuphin          # Suzhounese phin
# --------------------------------------#------------------------------------- #
from .svg_maker import makeSingle       # make svg of single SubGlyph
from .svg_maker import makePar          # make svg of paragraph 
from .svg_maker import makeSpan         # make syllable span of SubGlyphs
# --------------------------------------#------------------------------------- #