import random


while True:

  print("1.Random English")
  print("2.Random Espanol")
  print("3.Random Rest")
  print("4.Rest")
  print("5.太陽系の構造と天体")
  print("6.地球の形と内部構造")
  print("7.鉱石と岩石")
  print("8.火山と変成岩")
  print("9.地震と断層")
  print("10.プレートテクトニクス")


  choice = input("\nenter 1, 2, 3, 4, 5: ")

  if choice == "1":
      vocab_list = [
        ("Deposit", "存款／押金 - n./v."),
        ("Coincide", "同時發生／一致 - v."),
        ("Attest", "證明／作證 - v."),
        ("Displace", "取代／移開／使離開 - v."),
        ("Deem", "認為／視為 - v."),
        ("Cultivations", "耕作／培養 - n. (plural)"),
        ("Exceedingly", "極其／非常 - adv."),
        ("Curtail", "削減／限制 - v."),
        ("Creeping", "漸進的／爬行中的 - adj./v."),
        ("Soak up", "吸收／沉浸 - phr.v."),
        ("Terminate", "終止／結束 - v."),
        ("Mitigate", "減輕／緩和 - v."),
        ("Extent", "程度／範圍 - n."),
        ("Flare", "爆發／閃光 - n./v."),
        ("Waxing", "漸盈的（月亮） - adj./v."),
        ("Waning", "漸虧的（月亮） - adj./v."),
        ("Advent", "出現／到來 - n."),
        ("Undulate", "波動／起伏 - v."),
        ("Erupt", "噴發／爆發 - v."),
        ("Catalyst", "催化劑／促進因素 - n."),
        ("Crippling", "癱瘓性的／嚴重損害的 - adj."),
        ("Fault", "錯誤／斷層／缺陷 - n./v."),
        ("Deliberate", "故意的／慎重的 - adj./v."),
        ("Strain", "壓力／拉力／拉傷 - n./v."),
        ("Devise", "設計／想出 - v."),
        ("Incentivize", "激勵／提供誘因 - v."),
        ("Conventional", "傳統的／慣例的 - adj."),
        ("Catalog", "目錄／編目 - n./v."),
        ("Mandate", "命令／授權／強制 - n./v."),
        ("Posit", "假設／提出 - v."),
        ("Adopt", "採用／收養／接受 - v."),
        ("Amenable", "願意接受的／可被影響的 - adj."),
        ("Strife", "衝突／紛爭 - n."),
        ("Clump", "一叢／成團 - n./v."),
        ("Municipal", "市政的／地方政府的 - adj."),
        ("Placement", "放置／安排／配置 - n."),
        ("Resurgence", "復甦／再起 - n."),
        ("Zoning", "土地分區／分區規劃 - n."),
        ("Dizzying", "令人目眩的／令人困惑的 - adj."),
        ("Redemption", "贖回／救贖 - n."),
        ("Petrified", "嚇呆的／石化的 - adj."),
        ("Mundanity", "平凡／日常 - n."),
        ("Depict", "描繪／描述 - v."),
        ("Vertigo", "暈眩 - n."),
        ("Subversive", "顛覆性的／顛覆者 - adj./n."),
        ("Focal", "焦點的 - adj."),
        ("Dub", "稱呼／配音 - v."),
        ("Instill", "灌輸／逐漸培養 - v."),
        ("Suspenseful", "充滿懸念的 - adj."),
        ("Captivate", "吸引／迷住 - v."),
        ("Thereby", "因此／從而 - adv."),
        ("Conceptual", "概念性的 - adj."),
        ("Trivial", "瑣碎的／不重要的 - adj."),
        ("Narrative", "敘事／故事 - n./adj."),
        ("Shear", "剪切／切斷 - v./n."),
        ("Consistent", "一致的／穩定的 - adj."),
        ("Converge", "匯聚／趨同 - v."),
        ("Coordinate", "協調／座標 - v./n."),
        ("Prerequisite", "先決條件 - n./adj."),
        ("Disturbance", "擾動／干擾 - n."),
        ("Intensified", "加劇的／增強的 - adj./v."),
        ("Negligible", "可忽略的／微不足道的 - adj."),
        ("Destructive", "具破壞性的 - adj."),
        ("Transformative", "有變革性的 - adj."),
        ("Dissipate", "消散／驅散 - v."),
        ("Propel", "推進／驅動 - v."),
        ("Detrimental", "有害的 - adj."),
        ("Condense", "凝結／濃縮 - v."),
        ("Amass", "積累／聚集 - v."),
        ("Dwindle", "減少／縮小 - v.")]



      while True:
          for vocab, meaning in vocab_list:
            #vocab, meaning = random.choice(vocab_list)
            print(f"{vocab}")

            user_input = input("\n(翻譯)")
            
            if user_input.lower() == "q":
                print("bye~")
                break

            print(f"{meaning}")

            print("-" * 40)

            user_input = input("\n(單字)")
            
            if user_input.lower() == "q":
                print("bye")
                time.sleep(1)
                break

  if choice == "2":
      vocab_list = [
    ("Exude", "滲出／散發出 - v."),
    ("Ensnare", "誘捕／使落入陷阱 - v."),
    ("Entrap", "設陷阱／困住 - v."),
    ("Hoax", "惡作劇／騙局 - n./v."),
    ("Nourishment", "營養／養分 - n."),
    ("Arthropods", "節肢動物 - n."),
    ("Carnivorous", "食肉的 - adj."),
    ("Photosynthesis", "光合作用 - n."),
    ("Reliance", "依賴／信賴 - n."),
    ("Sundew", "毛氈苔（食蟲植物） - n."),
    ("Passively", "被動地 - adv."),
    ("Lure", "引誘／誘惑 - v./n."),
    ("Insectivorous", "食蟲的 - adj."),
    ("Slippery", "滑的／難以捉摸的 - adj."),
    ("Cupped", "杯狀的 - adj."),
    ("Piercing", "刺穿的／尖銳的 - adj."),
    ("Throne", "王座／寶座 - n."),
    ("Enzymatic", "酵素的／酶的 - adj."),
    ("Seduce", "誘惑／引誘 - v."),
    ("Slick", "滑的／聰明的 - adj."),
    ("Decomposed", "分解的／腐爛的 - adj./v."),
    ("Decay", "腐爛／衰退 - n./v."),
    ("Feces", "糞便／排泄物 - n."),
    ("Carcass", "動物屍體 - n."),
    ("Ardent", "熱情的／熱心的 - adj."),
    ("Botany", "植物學 - n."),
    ("Inclusive", "包容的／包含一切的 - adj."),
    ("Seeming", "表面上的 - adj."),
    ("Unsuspecting", "毫無戒心的 - adj."),
    ("Intruder", "入侵者／闖入者 - n."),
    ("Twig", "小樹枝 - n."),
    ("Bogs", "沼澤 - n."),
    ("Subsist", "勉強生存／維持生活 - v."),
    ("Drawn", "被吸引的／拉出的 - adj./v."),
    ("Entice", "引誘／誘惑 - v."),
    ("Imprison", "監禁／困住 - v."),
    ("Interlock", "互相扣住／連接 - v.")
]

     
      while True:
          for vocab, meaning in vocab_list:
            #vocab, meaning = random.choice(vocab_list)
            print(f"{vocab}")

            user_input = input("\n(翻譯)")
            
            if user_input.lower() == "q":
                print("bye~")
                break

            print(f"{meaning}")

            print("-" * 40)

            user_input = input("\n(單字)")
            
            if user_input.lower() == "q":
                print("bye")
                time.sleep(1)
                break

        

    
  if choice == "3":
    word_list = [("太陽", "Sun"),
                 ("惑星", "planet"),
                 ("津波", "tsunami"),
                 ("火山", "volcano"),
                 ("石油", "oil"),
                 ("岩石", "rock"),
                 ("地球", "Earth"),
                 ("地震", "earthquake"),
                 ("CO2", "carbon dioxide"),
                 ("地球温暖化", "global warming"),
                 ("熔岩", "lava")
                 ]
    
    while True:
      word, meaning = random.choice(word_list)
      print(f"{word}")
      user_input = input("\n(↓)")

      if user_input.lower() == "q":
        print("bye~")
        time.sleep(1)
        break

      print(f"{meaning}")

      print("-"*40)

      user_input = input("")
      if user_input.lower() == "q":
        print("bye~")
        time.sleep(1)
        break

  if choice == "4":
    word_list = [("太陽", "Sun"),
                 ("惑星", "planet"),
                 ("津波", "tsunami"),
                 ("火山", "volcano"),
                 ("石油", "oil"),
                 ("岩石", "rock"),
                 ("地球", "Earth"),
                 ("地震", "earthquake"),
                 ("CO2", "carbon dioxide"),
                 ("地球温暖化", "global warming"),
                 ("熔岩", "lava")
                 ]
    while True:
      for word, meaning in word_list:
        print(f"{word}")
        user_input = input("\n(↓)")
        if user_input.lower() == "q":
          print("bye~")
          time.sleep(1)
          break
        print(f"{meaning}")
        print("-"*40)
        user_input = input("")
        

  if choice == "5":
    word_list =[
    ("AU（天文単位）とは", ""),
    ("彗星の源はどこか", ""),
    ("地球型惑星とは何か", ""),
    ("木星型惑星とは何か", ""),
    ("木星の大赤斑, 組成、木星の衛星数", ""),
    ("エウロパとは何か", ""),
    ("**EKBO天体とは何か", ""),
    ("冥王星とカロンの関係", ""),
    ("**惑星の定義とは何か", ""),
    ("準惑星とは何か", ""),
    ("球形ではない天体とは何か", ""),
    ("EKBとは何か", "12"),
    ("課題：なぜ冥王星は準惑星になったか？事情と原因を説明して", "s")]

    back_to_menu = False
    while True:
      
      for word, meaning in word_list:
        print(f"{word}")
        user_input = input("\n(↓)")
        if user_input.lower() == "q":
          print("bye~")
          time.sleep(1)
          back_to_menu = True
          break
        print(f"{meaning}")
        print("-"*40)
        user_input = input("")
      if back_to_menu:
        break
       #我試著想跳回主選單 但好像辦不太到

        
  if choice == "6":
    word_list =[
    ("地球の形は", ""),
    ("平均半径は", ""),
    ("赤道半径→極半径よりも？", ""),
    ("遠心力が最大のところは", ""),
    ("扁平率とは", ""),
    ("大きく三区分は（英語）（比率）", ""),
    ("内部構造を知る方法", ""),
    ("P波は", ""),
    ("S波は", ""),
    ("外核は？波", ""),
    ("シャドーゾーンとは", ""),
    ("リンスフェアーと？", ""),
    ("大陸地殻は海洋地殻より", ""),
    ("マントルの上に、何が漂っている？", ""),
    ("マントル→（？）岩", ""),
    ("**上部マントル", ""),
    ("下部マントル", ""),
    ("地核は", ""),
    ("課題：地球とゆで卵（殻付き、黄身は一個とする）の内部構造、外形を比較し、共通点と相違点を述べてください。略図も書きましょう。", "")
]

    while True:
      for word, meaning in word_list:
        print(f"{word}")
        user_input = input("\n(↓)")
        if user_input.lower() == "q":
          print("bye~")
          time.sleep(1)
          break
        print(f"{meaning}")
        print("-"*40)
        user_input = input("") 

  if choice == "7":
    word_list =[
    ("**鉱物の英語", ""),
    ("鉱物の定義", ""),
    ("結晶の英語", ""),
    ("**結晶の定義", ""),
    ("**鉱物とは", ""),
    ("ガラスとは", ""),
    ("硬度とは、順番", ""),
    ("造岩鉱物とは", ""),
    ("**造岩鉱物の多くは？", ""),
    ("宝石は？", ""),
    ("固溶体からできる", ""),
    ("カンラン石の構造とイオン半径は入れ替わりやすい？", ""),
    ("マグマの溶けた部分の温度は", ""),
    ("溶岩とは？", ""),
    ("火山岩とは", ""),
    ("深成岩とは、地下何km？", ""),
    ("宝石と鉱石は", ""),
    ("キンバライト噴火", ""),
    ("課題：「結晶」と「ガラス」の違いは？マグマから形成される場合、その違いが生じる要因は？具体的な例を", ""),
    ("**課題；鉱物と鉱石の違い", "")
]

    while True:
      for word, meaning in word_list:
        print(f"{word}")
        user_input = input("\n(↓)")
        if user_input.lower() == "q":
          print("bye~")
          time.sleep(1)
          break
        print(f"{meaning}")
        print("-"*40)
        user_input = input("") 


  if choice == "8":
    word_list =[
    ("**火山とは", ""),
    ("火山フロントより、海溝側に？", ""),
    ("世界の火山の分布", ""),
    ("海嶺とは", ""),
    ("**火山の種類と分布", ""),
    ("**島弧", ""),("海溝とトラフの違い",""),
    ("マグマとは、温度は", ""),
    ("複成火山とは", ""),
    ("単成火山とは", ""),
    ("火山灰　火山弾　火砕流", ""),
    ("マグマと変成岩とは", ""),
    ("日本の主な変成岩は", ""),
    ("課題：プリント", "")
]

    while True:
      for word, meaning in word_list:
        print(f"{word}")
        user_input = input("\n(↓)")
        if user_input.lower() == "q":
          print("bye~")
          time.sleep(1)
          break
        print(f"{meaning}")
        print("-"*40)
        user_input = input("")     

  if choice == "9":
    word_list =[
    ("地震とは", ""),
    ("**マグニチュードとは", ""),
    ("マグニチュード１の違いはエネルギー？倍", ""),
    ("震度とは", ""),
    ("地震の原因とは、種類？", ""),
    ("活断層とは", ""),
    ("正断層、逆断層とは", ""),
    ("三つのタイプは？", ""),
    ("地震予測は？", ""),
    ("空白域とは", ""),
    ("トレンチ調査とは", ""),
    ("数字は？年代測定", ""),
    ("**津波とは", ""),
    ("地震の連動の例", ""),
    ("津波の痕跡とは英語とは", ""),
    ("液状化とは？間隙水？", ""),
    ("課題：プリント", "")
]

    while True:
      for word, meaning in word_list:
        print(f"{word}")
        user_input = input("\n(↓)")
        if user_input.lower() == "q":
          print("bye~")
          time.sleep(1)
          break
        print(f"{meaning}")
        print("-"*40)
        user_input = input("")          

  if choice == "10":
    word_list =[
    ("**プレートテクトニクス理論とは", ""),
    ("大陸移動説の根拠とは", ""),
    ("大陸移動説の復活の原因は", ""),
    ("海洋底拡大説", ""),
    ("海洋底の年代を調べる方法？", ""),
    ("海嶺軸から左右対称の？を示す", ""),
    ("**どんな境界は海嶺？衝突境界は？すれ違う境界とは", ""),
    ("海嶺の特徴　三つ", ""),
    ("沈み込み帯の特徴　五つ", ""),
    ("火山フロントとは", ""),
    ("日本の活火山の数は", ""),
    ("課題：プリント", "")
]

    while True:
      for word, meaning in word_list:
        print(f"{word}")
        user_input = input("\n(↓)")
        if user_input.lower() == "q":
          print("bye~")
          time.sleep(1)
          break
        print(f"{meaning}")
        print("-"*40)
        user_input = input("")
