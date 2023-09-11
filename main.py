import tkinter
from tkinter import ttk
from categories import FILLINGNESS, FLAVOURS, METHODS, TEXTURES, TIMES
INGREDIENTS_PLACEHOLDER = ["egg","bacon","spam","sausage"]

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
HEADING_FONT_SIZE = 20
SUBHEADING_FONT_SIZE = 16
FONT = "Futura"

banner_location = "images/whatshouldicook-banner.png"

screen = tkinter.Tk()
screen.title("What Should I Cook?")
screen.config(height=SCREEN_HEIGHT,width=SCREEN_WIDTH,pady=20,padx=20,background="white")
screen.resizable(width=False,height=False)
screen.geometry(f'{int(SCREEN_WIDTH * 1.4)}x{SCREEN_HEIGHT}+0+0')

banner = tkinter.PhotoImage(file=banner_location)
logo = tkinter.Label(image=banner)
logo.grid(row=0, column=0, columnspan=3)

# ---------------------------- LEFT COLUMN ------------------------------- #
left_column_title = tkinter.Label(text="Filter",background="white",foreground="black",font=(FONT,HEADING_FONT_SIZE))
left_column_title.grid(row=1, column=0)

ingredient_title = tkinter.Label(text="Ingredient",background="white",foreground="black",font=(FONT,SUBHEADING_FONT_SIZE))
ingredient_title.grid(row=2, column=0)
ingredient = tkinter.StringVar()
ingredient_dropdown = tkinter.OptionMenu(screen, ingredient, *INGREDIENTS_PLACEHOLDER)
ingredient_dropdown.config(width=100,background="white",foreground="black",highlightbackground="white")
ingredient_dropdown.grid(row=3, column=0, pady=5)
separator1 = ttk.Separator(screen,orient='horizontal')
separator1.grid(row=4,column=0,ipadx=20,pady=10)

time_title = tkinter.Label(text="Time",background="white",foreground="black",font=(FONT,SUBHEADING_FONT_SIZE))
time_title.grid(row=5, column=0)
time_to_cook = tkinter.StringVar()
time_dropdown = tkinter.OptionMenu(screen, time_to_cook, *TIMES)
time_dropdown.config(width=100,background="white",foreground="black",highlightbackground="white")
time_dropdown.grid(row=6, column=0, pady=5)
separator2 = ttk.Separator(screen,orient='horizontal')
separator2.grid(row=7,column=0,ipadx=20,pady=10)

flavour_title = tkinter.Label(text="Flavour",background="white",foreground="black",font=(FONT,SUBHEADING_FONT_SIZE))
flavour_title.grid(row=8, column=0)
flavour = tkinter.StringVar()
flavour_dropdown = tkinter.OptionMenu(screen, flavour, *FLAVOURS)
flavour_dropdown.config(width=100,background="white",foreground="black",highlightbackground="white")
flavour_dropdown.grid(row=9, column=0, pady=5)
separator3 = ttk.Separator(screen,orient='horizontal')
separator3.grid(row=10,column=0,ipadx=20,pady=10)

texture_title = tkinter.Label(text="Texture",background="white",foreground="black",font=(FONT,SUBHEADING_FONT_SIZE))
texture_title.grid(row=11, column=0)
texture = tkinter.StringVar()
texture_dropdown = tkinter.OptionMenu(screen, texture, *TEXTURES)
texture_dropdown.config(width=100,background="white",foreground="black",highlightbackground="white")
texture_dropdown.grid(row=12, column=0, pady=5)
separator4 = ttk.Separator(screen,orient='horizontal')
separator4.grid(row=13,column=0,ipadx=20,pady=10)

method_title = tkinter.Label(text="Method",background="white",foreground="black",font=(FONT,SUBHEADING_FONT_SIZE))
method_title.grid(row=14, column=0)
method = tkinter.StringVar()
method_dropdown = tkinter.OptionMenu(screen, method, *METHODS)
method_dropdown.config(width=100,background="white",foreground="black",highlightbackground="white")
method_dropdown.grid(row=15, column=0, pady=5)
separator5 = ttk.Separator(screen,orient='horizontal')
separator5.grid(row=16,column=0,ipadx=20,pady=10)

filling_title = tkinter.Label(text="Fillingness",background="white",foreground="black",font=(FONT,SUBHEADING_FONT_SIZE))
filling_title.grid(row=17,column=0)
fillingness = tkinter.StringVar()
filling_dropdown = tkinter.OptionMenu(screen, fillingness, *FILLINGNESS)
filling_dropdown.config(width=100,background="white",foreground="black",highlightbackground="white")
filling_dropdown.grid(row=18, column=0, pady=5)
separator6 = ttk.Separator(screen,orient='horizontal')


# ---------------------------- RIGHT COLUMN ------------------------------- #
right_column_title = tkinter.Label(text="Recipes",background="white",foreground="black",font=(FONT,HEADING_FONT_SIZE),width=40)
right_column_title.grid(row=1, column=1)

add_recipe_button = tkinter.Button(text="+",highlightbackground="white")
add_recipe_button.grid(row=1,column=2)

recipe_frame = tkinter.Frame(background='black',width=100,pady=10)
recipe_frame.grid(row=2,column=1,columnspan=2,rowspan=18,sticky='nsew')
recipe_canvas = tkinter.Canvas(recipe_frame, bg='white',width=100)
recipe_canvas.pack()
# recipe_scrollbar = tkinter.Scrollbar(screen,width=10)
# # scrollbar.pack( side = "right", fill = "y" )
# recipes = tkinter.Listbox(screen, yscrollcommand=recipe_scrollbar.set,width=50,justify="left")
# for line in range(100):
#    recipes.insert(tkinter.END, "This is line number " + str(line))
# recipes.grid(row=2,column=1,columnspan=2)

screen.mainloop()



# TKINTER FONTS ('Academy Engraved LET', 'Al Bayan', 'Al Nile', 'Al Tarikh', 'American Typewriter', 'Andale Mono',
# 'Apple Braille', 'Apple Chancery', 'Apple Color Emoji', 'Apple SD Gothic Neo', 'Apple Symbols', 'AppleGothic',
# 'AppleMyungjo', 'Arial', 'Arial Black', 'Arial Hebrew', 'Arial Hebrew Scholar', 'Arial Narrow', 'Arial Rounded MT
# Bold', 'Arial Unicode MS', 'Avenir', 'Avenir Next', 'Avenir Next Condensed', 'Ayuthaya', 'Baghdad', 'Baka Too',
# 'Bangla MN', 'Bangla Sangam MN', 'Baskerville', 'Beirut', 'Big Caslon', 'Bodoni 72', 'Bodoni 72 Oldstyle',
# 'Bodoni 72 Smallcaps', 'Bodoni Ornaments', 'Bradley Hand', 'Brush Script MT', 'Chalkboard', 'Chalkboard SE',
# 'Chalkduster', 'Charter', 'Clarendon Wide', 'Clarendon Wide Medium', 'Clarendon Wide Stencil', 'Cochin',
# 'Comic Sans MS', 'Copperplate', 'Corsiva Hebrew', 'Courier New', 'Damascus', 'DecoType Naskh', 'Devanagari MT',
# 'Devanagari Sangam MN', 'Didot', 'DIN Alternate', 'DIN Condensed', 'Diwan Kufi', 'Diwan Thuluth', 'Euphemia UCAS',
# 'Farah', 'Farisi', 'Futura', 'Galvji', 'GB18030 Bitmap', 'Geeza Pro', 'Geneva', 'Georgia', 'Gill Sans',
# 'Grantha Sangam MN', 'Gujarati MT', 'Gujarati Sangam MN', 'Gurmukhi MN', 'Gurmukhi MT', 'Gurmukhi Sangam MN',
# 'Heiti SC', 'Heiti TC', 'Helvetica', 'Helvetica Neue', 'Herculanum', 'Hiragino Maru Gothic ProN', 'Hiragino Mincho
# ProN', 'Hiragino Sans', 'Hiragino Sans GB', 'Hoefler Text', 'Impact', 'InaiMathi', 'ITF Devanagari',
# 'ITF Devanagari Marathi', 'Josefin Sans', 'Kailasa', 'Kannada MN', 'Kannada Sangam MN', 'Kefa', 'Khmer MN',
# 'Khmer Sangam MN', 'Kohinoor Bangla', 'Kohinoor Devanagari', 'Kohinoor Gujarati', 'Kohinoor Telugu', 'Kokonor',
# 'Krungthep', 'KufiStandardGK', 'Lao MN', 'Lao Sangam MN', 'Lucida Grande', 'Luminari', 'Malayalam MN', 'Malayalam
# Sangam MN', 'Marker Felt', 'Marydale', 'MattB', 'Menlo', 'Microsoft Sans Serif', 'Mishafi', 'Mishafi Gold',
# 'Monaco', 'Mshtakan', 'Mukta Mahee', 'Muna', 'Myanmar MN', 'Myanmar Sangam MN', 'Nadeem', 'New Peninim MT',
# 'New Spirit', 'Noteworthy', 'Noto Nastaliq Urdu', 'Noto Sans Kannada', 'Noto Sans Myanmar', 'Noto Sans Oriya',
# 'Noto Serif Myanmar', 'Optima', 'Oriya MN', 'Oriya Sangam MN', 'P22 Stanyan', 'Palatino', 'Papyrus', 'Party LET',
# 'Phosphate', 'PingFang HK', 'PingFang SC', 'PingFang TC', 'Plantagenet Cherokee', 'PT Mono', 'PT Sans',
# 'PT Sans Caption', 'PT Sans Narrow', 'PT Serif', 'PT Serif Caption', 'Raanana', 'Rockwell', 'Sana', 'Sathu',
# 'Savoye LET', 'Shadows Into Light', 'Shree Devanagari 714', 'SignPainter', 'Silom', 'Sinhala MN', 'Sinhala Sangam
# MN', 'Skia', 'Snell Roundhand', 'Songti SC', 'Songti TC', 'STIX Two Math', 'STIX Two Text', 'STSong', 'Sukhumvit
# Set', 'Symbol', 'Tahoma', 'Tamil MN', 'Tamil Sangam MN', 'Telugu MN', 'Telugu Sangam MN', 'Thonburi', 'Times New
# Roman', 'Tornac', 'Trattatello', 'Trebuchet MS', 'Verdana', 'Waseem', 'Webdings', 'Wingdings', 'Wingdings 2',
# 'Wingdings 3', 'Wordy Diva', 'Zapf Dingbats', 'Zapfino')
