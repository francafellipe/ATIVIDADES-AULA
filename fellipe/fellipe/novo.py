import a

a.jogo(a.jogador(), a.computador())

"================================"

from a import jogo

jogo(a.jogador(), a.computador())

"================================"

from a import (jogador, computador)

a.jogo(jogador(), computador())

from a import *

jogo(jogador)

import a as game
