def trans(inp):
    amh_list = ["ለሉሊላሌልሎሏ", "መሙሚማሜምሞሟ", "ሠሡሢሣሤሥሦሧ",
                "ረሩሪራሬርሮሯ", "ሰሱሲሳሴስሶሷ","ሸሹሺሻሼሽሾሿ",
                "ቀቁቂቃቄቅቆቋ", "በቡቢባቤብቦቧ", "ቨቩቪቫቬቭቮቯ",
                "ተቱቲታቴትቶቷ", "ቸቹቺቻቼችቾ ", "የዩዪያዬይዮ ",
                "ነኑኒናኔንኖኗ", "ኘኙኚኛኜኝኞኟ", "ከኩኪካኬክኮኳ",
                "ኸኹኺኻኼኽኾዃ",  "ወዉዊዋዌውዎ ", "ዘዙዚዛዜዝዞዟ",
                "ዠዡዢዣዤዥዦዧ", "ደዱዲዳዴድዶዷ ", "ጀጁጂጃጄጅጆ ",
                "ገጉጊጋጌግጎጓ", "ጠጡጢጣጤጥጦጧ", "ጨጩጪጫጬጭጮጯ",
                "ጸጹጺጻጼጽጾ ", "ጰጱጲጳጴጵጶጷ", "ፈፉፊፋፌፍፎፏ",
                "ፐፑፒፓፔፕፖፗ","ሀሁሂ ሄህሆኋ", "ሐሑሒ ሔሕሖሗ", "አኡኢ ኤእኦኧ"]  # list of amharic alphabet by there family

    cons_list = ['l', 'm', 's', 'r', 's', 'sh', 'q', 'b', 'v', 't', 'ch', 'y',  'n', 'ng', 'k', 'e',  'w', 'z',
                 'zh', 'd', 'j',  'g', 'x', 'c', 'ts', 'p', 'f', 'ph']  # list of consonant letter
    vow_list = ['e', 'u', 'i', 'a', 'ie', '', 'o', 'ua']  # list of vowel letter
    specons_list = ['h', 'h', '_']  # list of special consonant letter for ሀ አ ሐ family
    spevow_list = ['a', 'u', 'i', '_', 'e', '', 'o', 'ua']  # list of special vowel letter for ሀ አ ሐ family
    consVow_list = []  # list that pair consonant and vowel letter append
    for i in range(31):  # add empty list to cons_vow list for append pair consonant and vowel
        consVow_list.append([])
    for i in range(len(cons_list)):  # add pair consonant and vowel
        for j in range(len(vow_list)):
            cell = consVow_list[i]
            cell.append(f"{cons_list[i]}{vow_list[j]}")
    for i in range(len(specons_list)):  # add pair consonant and vowel for ha and a
        for j in range(len(spevow_list)):
            cell = consVow_list[i+28]
            cell.append(f"{specons_list[i]}{spevow_list[j]}")
    dict = {}  # empty dictionary append each amharic alphabet with there english value
    for i in range(len(amh_list)):
        for j in range(8):
            dict[amh_list[i][j]] = consVow_list[i][j]  # append amharic alphabet with there english value
    dict["/"] = "/"  # return itself if its space
    dict["."] = "."  # if it is full stop
    dict[","] = ","  # if it is comma
    dict["."] = "."  # if it is amharic full stop
    dict[","] = ","  # if it is amharic comma
    dict[","] = ","  # if it is another type of amharic comma
    result = []  # empty list that each alphabet value added
    for i in inp:  # find the value for each amharic word
        result.append(dict[i])
    return result

""" 


demo 
it will change ረቂቅ ቀሚስ ለበሰች to ["re","qi","q","qe","mi","s","le","be","se","ch"]  """
