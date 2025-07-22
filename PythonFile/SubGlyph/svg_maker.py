import subprocess
import os
from pathlib import Path
from .cleaner import clean_tmp_files

"""
Provides functions:
# --------------------------------------#------------------------------------- #
-- makeSingle                           # make single SubGlyph
-- makePar                              # make paragraph with SubGlyphs
-- makeSpan                             # onset X rime X tone SubGlyphs
# --------------------------------------#------------------------------------- #
"""
# --------------------------------------#------------------------------------- #
def _to_svg(                            # shared logic: generate .tex
  file_prefix : str                   , # name of .svg files
  content     : str                   , # content of the file
  tikz_env    : bool=False            , # set it True if there is no other text
): 
  tex_file = f"tmp/{file_prefix}.tex"
  pdf_file = f"tmp/{file_prefix}.pdf"
  svg_file = f"tmp/{file_prefix}.svg"
  subprocess.run([
    "touch", tex_file
  ])
  tikz_settings = '[tikz, border=0pt]' if tikz_env else ''
  with open(tex_file, 'w', encoding='utf-8') as f: 
    f.write( f"""\\documentclass{tikz_settings}{{standalone}}%
\\input{{../../LatexFile/premable/of_SingleGlyph.tex}}%
\\begin{{document}}
{content}
\end{{document}}
""")
  subprocess.run([
    "xelatex", "-output-directory=tmp", tex_file
  ])
  subprocess.run([
    "pdf2svg", pdf_file, svg_file
  ])
  clean_tmp_files(extra_set={'.pdf', '.tex'})
# --------------------------------------#------------------------------------- #
# --------------------------------------#------------------------------------- #
def makeSingle(                         # make single glyph
  system : str                        , # name of romanization system
  onset  : str                        , # name of onset in the system
  rime   : str                        , # name of rime in the system
  tone   : str                        , # number of tone in the system
): 
  _to_svg(
    file_prefix = f"{system.capitalize()}{onset}{rime}{tone}", 
    content = f"\\ToSubGlyph{{{system}}}{{{onset}}}{{{rime}}}{{{tone}}}", 
    tikz_env = True
  )
# --------------------------------------#------------------------------------- #
# --------------------------------------#------------------------------------- #
def makePar(                            # make paragraph from txt
  txt_path:str                        , # path to such txt
): 
  with open(txt_path, 'r', encoding='utf-8') as f: 
    content = f.read()
  _to_svg(
    file_prefix = f"SvgPar", 
    content=content
  )
# --------------------------------------#------------------------------------- #
# --------------------------------------#------------------------------------- #
def makeSpan(                           # make SubGlyphs of a syllable span
  system     : str                    , # name of system
  onset_list : list                   , # list of onset
  rime_list  : list                   , # list of rime
  tone_list  : list                   , # list of tone
): 
  for onset in onset_list: 
    for rime in rime_list: 
      for tone in tone_list: 
        makeSingle(system, onset, rime, tone)
# --------------------------------------#------------------------------------- #