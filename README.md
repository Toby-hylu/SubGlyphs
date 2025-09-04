# SubGlyphs
The name 'SubGlyphs' stands for 'Stacked Universal Bopomofo Glyphs'. 

This project provides a prototype of a phonetic system with the features below: 
* Based on Bopomofo
* Mixed typeset with Han Character: Each syllable occupies the size of one Han Character, like Japanese Kana or Korean Hangul
* May be extanded for East Asian tonal languages

This system aims to solve the problem that in many East Asian languages, especially Sinitic languages, there are some words has the features below: 
* The word is a core word or a common word
* The word cannot be mapped to an original character, or the mapped character is rarely seen and difficult to write

It is mainly a LeTaX project, utilizing TikZ to create SubGlyph Symbols. I wrote the commands so that you can generate the glyphs from romanization systems. 

Currently, there are 6 subsystems provided, using "明" as an example: 

* Mandarin: `\ToSubGlyph{Hanpin}{m}{ing}{2}`
* Taiwanese: `\ToSubGlyph{Tailo}{b}{ing}{5}`
* Cantonese: `\ToSubGlyph{Jyutping}{m}{ing}{4}`
* Hakka (Xiian): `\ToSubGlyph{HagpinXiian}{m}{ang}{5}`
* Suzhounese: `\ToSubGlyph{WuphinSoutseu}{m}{in}{2}`
* Fuzhounese: `\ToSubGlyph{Yngping}{m}{ing}{5}`

Also, you may write your own .sty files for your language with Python. Please write your own .py file (or .json, if I have time to optimize the codes) as the examples provided. 

Note: I may have some mistakes on the subsystems given that I can only speak Mandarin and Taiwanese. Please inform me if you find any mistakes. 