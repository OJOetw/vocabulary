import random

words_list = [("advent","出現"), ("swirling","旋轉"), ("erupt","爆發"), ("catalyst","催化劑")
              , ("abate","減弱"), ("grid","格子"), ("imminetn","即將發生"), ("fault","缺點") 
              , ("deliberate","深思熟慮 故意的"), ("incentivize","激勵"), ("devise","設計 想出"), ("conventional","傳統的")
              , ("foraging","採集"), ("residue","剩餘物"), ("catalog","目錄"), ("convention","習俗")
              , ("posit","提出"), ("prescriptivist","規範主義者"), ("overturn","推翻"), ("organically","自然地")
              , ("jargon","術語"), ("amenable","願意服從的")]


while True:
    word, meaning = random.choice(words_list)
    print(f"{word}")

    user_input = input("\n(翻譯)")
    if user_input.lower() == "q":
        print("拜拜~")
        break

    print(f"{meaning}")

    print("-" * 40)

    user_input = input("\n(單字)")
    if user_input.lower() == "q":
        print("拜拜")
        break
    
    
