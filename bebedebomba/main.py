import time
import sys

inicio = time.time()
tempo_limite = 5

while True:
    tempo_passado = time.time() - inicio
    
    try:
        if tempo_passado > tempo_limite:
            print("\nTempo esgotado. Tchau!")
            sys.exit()

        print("bebê tossindo")
        time.sleep(0.05)

    except KeyboardInterrupt:
        restante = int(tempo_limite - tempo_passado)
        print(f"\n[ERRO] BEBE VS BOMBA DE HIDROGENIO {restante}s.")
        continue

