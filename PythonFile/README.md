A python package 'SubGlyph' is provided in this directory. 

The targets of this package are as below: 
  - Generate .sty required for other languages automatically
  - Generate .svg file for single SubGlyph or paragraphs with SubGlyphs

Before generating your .sty file, please refer to the following examples provided:
  - 'Hanpin'   : Hanyu Pinyin System
  - 'Tailo'    : Taiwanese Romanization System
  - 'Jyutping' : Linguistic Society of Hong Kong Cantonese Romanization Scheme
  - 'Hagpin'   : Taiwanese Hakka Romanization System
  - 'Wuphin'   : Suzhounese Romanization System
  - 'Yngping'  : Fuzhounese Romanization System

If you just want to generate your own SubGlyph, please use the functions in PythonFile/SubGlyph/svg_maker.py
  - makeSingle : make single SubGlyph.svg
  - makePar    : please create a .txt file with latex style, and parse it into makePar(), it will generate a .svg file with the contents
  - makeSpan   : generate ALL SubGlyphs from the onset list, rime list and tone list provided

To use it, please follow the steps below
  1. (Optional but useful): Analyze the romanization system of your language, as the examples given in LatexFile/Subsystems/
  2. Create your .py file under PythonFile/SubGlyph: Write the mapping rules of the onset, rime, tone and onset-rime coupling with the symbols defined in LatexFile/main/SubGlyphsDescription.pdf, as the given examples like Hanpin.py
  3. Modify run.py and run it for your .sty file
  4. LatexFile/package will be updated automatically once your .py works 
  5. The 'SubGlyph.sty' will also be updated automatically to require your new package
  6. Now you can directly the macro \ToSubGlyph{Yourlang}{onset}{rime}{tone} to generate your own subsystem in latex. Please typeset with xelatex for CJK symbols. 

