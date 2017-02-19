class Trainer:
    def __init__(trainername, trainerpokemon, sign, pl):
        self.name = trainername
        self.pokemon = trainerpokemon
        self.signature = sign
        self.perfectlink = pl


label TrainerInfo:

    $ Red = Trainer("Red",["Charizard","Pikachu","Lapras","Snorlax","Blastoise","Venusaur"],"Charizard","Pikachu")
    $ Bianca = Trainer("Bianca",["Serperior","Mushama","Cinccino","Ribombee"], "")
    $ Blue = Trainer("Blue", ["Blastoise","Pidgeot","Arcanine","Umbreon","Gyarados","Kommo-o"],"Blastoise","Arcanine")
   
    return
