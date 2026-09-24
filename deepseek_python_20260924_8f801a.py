"""
Exemplu complet de utilizare a pachetului teoria_N.
"""

from teoria_N import StructuraN, PredictorHadroni, PredictorNeutrini


def main():
    print()
    print("=" * 70)
    print("  TEORIA N — EXEMPLU COMPLET")
    print("=" * 70)
    print()

    # =========================================================
    # 1. Structura
    # =========================================================
    print("1. STRUCTURA N")
    print("-" * 70)
    N = StructuraN()

    print(f"Spectrul Pell: {N.spectru_pell()}")
    print(f"Urmele: {N.urme(8)}")
    print()

    constante = N.constante()
    print("Constante structurale:")
    for k, v in constante.items():
        print(f"  {k}: {v}")
    print()

    # =========================================================
    # 2. Hadroni
    # =========================================================
    print("2. PREDICTOR HADRONI")
    print("-" * 70)
    h = PredictorHadroni()
    h.raport()
    print()

    # =========================================================
    # 3. Neutrini
    # =========================================================
    print("3. PREDICTOR NEUTRINI")
    print("-" * 70)
    nu = PredictorNeutrini()
    nu.raport()
    print()

    print("=" * 70)
    print("N = {A, F, N} cu not N = N")
    print("Structura fundamentului.")
    print("=" * 70)


if __name__ == "__main__":
    main()