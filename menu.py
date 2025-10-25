from typing import Any, Callable


menuArt = """
                          ÕZo¿nZZN                                         
             ëÕNëZÕN     N¦› ›  › ›¿N     ë2¦¦››¿Õ NN¿››¦Õ ëZ¿¿oëë         
        ÕëZn›› › › ›N  ëÕ› › › › › › Õë2› › › › ›¦ZZ2 › ›eZe›  › ¿         
      Zë¿› ›  › › › Z ZN› › › › › › ›oÆ ›  › › n››Õe¦ › ›¦¿› › ›¦N         
      Në  › ›¿2o ››oN e¦› ›  eÕZ › › Æë › › ››oZëNZ2› ›  › › › ›Õ          
      ëo› › ë Ze ›››ÆZë› › ›onëZ ›  ›Në › ››NÕÕ   eZ›  › ›  › ››N          
     Õe›› › ›  › › ›¦NN› › ››22 › › ›ÕÆ› ›  oon¦ › o¦› › › › ›  ¦Õ         
     Ne› › › › ›  › ››Në› ›   ›  › ›ÆÆe¦ › › › › › ›2› › 2ë2› › ›¿         
     Õe¿ ›  ››Z2› ›  › ÕZZ¿ › › ›››2  eÕ› › › › › ››¦ › ›ZÆë›› › ›N        
      ëZ› ›  ¦Õëë› › › ›e NeÕe› ››ë   N2N› › › › ›2Æe¿›››Õ ëZ›  ¿¿›        
      NÕ› › ››Æ ëëNëZÕ2       2ë›      ëëëëëëëëZNN          NZeÕÕÕn        
      e2ëÕ                     ¿neëÕÕNëZ22ëëZeZN                           
        ë      2NÆÆÆÆÆÆÆë                                   ›¦¿ooo¦›¿2Õë   
        ¦    ›ÆÕ¦ë      NÆ ¦ÆÆ   ¦ÕÆÆÆÆZ            ÕÆÆÆÆÆÕ          2ë    
       Õ        ZÕ     2ÆneÆëÆn   2Õ   ÆÆ ZZeee¦   2Æ    nÆe        Z      
      Z        ¿ÆZoÕÆÆë  NÕ eÆ2  ›Æo›ÆÆÆ¿Æ2  ¦nZëe Æo   ëÆÆ        N       
      Õ        ÆÆ      2ÆÆëëÕÆN ¿ÆÆÆÆë¦ NÆ        ÆÆÆÆÆÆÆ¦        Õ        
      ¿       nÆe     ÆÆ    oÆÕ ¦Æë    ÕÆëÕNÕ    2ÆZëÕÆÆÆ›       Z         
     e        ÆÆ    oÆN     ›ÆN ëÆ    ZÆ›       ›ÆN   2ÆÆÆn     ¿          
     Z       ëÆe    ëZ       ÆÕ e2    ¿ÕÆÆÆÆÆÆo ÆÆ     ›ÆÆÆ2    Õ          
     Õ       ÆÕ                                ›Æn       ›     N           
     Z¦¦¿ZÆÆ¿¿¿¦¦¦›››                   ¿ ¿›   ¿¿¦         ¿¿¿2Æ       ÆÕÆÆ
      ÆonZÆÆ      ÆÆ2   ÆÆÆ      ÆÆëZn2noÆÆo   no¦¿Õ  Õe¿¦¦¦¦¦¦¦2   Nn¦oÆÆ 
    Õ¿¦oÆÆ      ÕnÆÆ    2oN  ÆZoZÆ No¦nÆÆ    Æ2¦¦¦¦¦oNZÕo¦¦o2¦¦¦ZÆÕ¿¦¦nNÆN 
  No¦¦ÆN      ë2¦eÆ    Æ¿¦Æ e¦eÆÆ Õ¦¦¦ë     Æ¿¦nÆNÆ¦¦ëÆÆ¿¦ZNÆ¿¦nÆn¦¦nÆÆ    
 ë¿¦oÆZ      Õo¦ÕÆ     Æ¦¦Æ2¦2Æ   Æ2¦¦¦¿eë No¦ZÆ   N¦¦ÆÆ¦¦N2¦¿ÕÆN¦¦¦NÕ     
N¦¦¦ëÆÕe2ëÆ Õo¦ZÆ      ë¦¿ÆÆo¦¦¦¿ëÆ ÕÆÕ¦¦¦Æe¦2Æ    Õ¦oÆe¦¦¦¦ëÆ   Æ¿¦¦¦¦Zë  
Z¦¦¦¦¦¦¦¦¦oN2¦oÆ       n¦oN  NÆN2¦¦e   n¦2Æn¦ëÕ   N¦¦NÆn¦o¦oÆ      ÆÆn¦¦ZÆ 
ÆÆÆÆÆÆNN¿¦ÕÆn¦oÆ       o¦ZÆ     ë¦oÆ  ë¦nÆNo¦N   Æ¿¦¿Æ o¦Æo¦Õ       Õo¦¦NÆ 
      Æ¿¦ëN 2¦¦¿eZZeNÆÆo¦ÕÆ   Õ¿¿ÕÆ Æ¿¦ZÆ  e¦nÆÆZ¦¦nÆ Æ¿eÆN¿oÆ     Õ¿¦¿ÆÆ  
    Õë¦¿ÆÕ  Æo¦¦¦¦¿oNÆÆ2¦Æ ÆÕe¿NÆ  Õ¦¿Æë   Æ¿¦¦¦¦¿NÆ  ÆNÆÆ Æ2ÆÆ  ëo¦¿ÕÆ    
  N2¦¿ëÆ     ÆÆÆÆÆÆÆ   ÕZÆ NÆÆÆ  ÆÕÆÆÆ      ÆÕZëÆÆ    ÆÆN   ÆNNÆÆÆnNÆN     
ÆNooÆÆ                 ÆÆÆ      NÆ                            Æ ÆÆN        
ÆÆÆÆ                                                                       
"""

#we can use these to make the output more user friendly and easier to read
bold = "\033[1m"
reset = "\033[0m"
red = "\033[31m"
green = "\033[92m"
blue = "\033[34m"
purple = "\033[35m"
cyan = "\033[36m"
underline = "\033[4m"

def _getValidInput(inputMessage: str, isValidConditional: Callable) -> Any:
    """Gets an input from the user based on the given input message. Checks if it's valid according to the provided conditional; if it's valid, return the value, if it's not valid, ask the user to reenter the input."""
    isValidInput = False
    inputValue = input(inputMessage).strip().lower()
    while not isValidInput:
        if isValidConditional(inputValue):
            isValidInput = True
        else:
            print(f"{bold}{red}That's not a valid option! Please try again below.{reset}")
            inputValue = input(inputMessage).strip().lower()
    return inputValue


def menu():
    """Brings up the main menu for the game. Asks users for game parameters before returning those parameters."""
    print(menuArt, "\n")
    print(f"{bold}{cyan}Welcome to Rock, Paper, Scissors! Please select your game options below.{reset}")

    rawDifficulty = _getValidInput(
        f"""
        Which AI difficulty would you like to play with? Indicate your choice by typing the number next to the option.
        {bold}(1) Random AI{reset}
        {bold}(2) Counter AI{reset}
        {bold}(3) Pattern AI{reset}

        Your choice: """,
        lambda x: x in ["1", "2", "3"],
    )
    if rawDifficulty == "1":
        difficulty = "random"
    elif rawDifficulty == "2":
        difficulty = "counter"
    else:
        difficulty = "pattern"

    numRounds = int(
        _getValidInput(
            "\nHow many rounds per tournament do you want? The options are 3, 5, and 7.\n\nYour choice: ",
            lambda x: x in ["3", "5", "7"],
        )
    )

    numTournaments = int(
        _getValidInput(
            "\nHow many tournaments do you want to play? You must play at least 1 tournament and no more than 10.\n\nYour choice: ",
            lambda x: x.isdecimal() and 0 < int(x) < 11,
        )
    )

    return numTournaments, numRounds, difficulty


if __name__ == "__main__":
    diff, rounds, tournaments = menu()
    print(f"Difficulty: {diff}\nNum Rounds: {rounds}\nNum Tournaments: {tournaments}")
