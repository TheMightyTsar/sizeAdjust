P480X480 = {"480:480": 1,
            "1690:900": 1.875,
            "1920:1080": 2.25}

P1690X900 = {"480:480": 48 / 90,
             "1690:900": 1,
             "1920:1080": 108 / 90}

P1920X1080 = {"480:480": 48 / 108,
              "1690:900": 90 / 108,
              "1920:1080": 1}

ESCALADOS_INGAME = {"480:480": P480X480,
                    "1690:900": P1690X900,
                    "1920:1080": P1920X1080,
                    "Editable": None}
# [Deseado][Objetivo]
#### ahhhh modifcar, usar fullScreen(), eso modifica el tamano, usar width() y height()
### escalar los tamanos iniciales al fullscreen