"""
neutrini.py
===========
Predictor pentru neutrini in teoria N.

Autor: Stelian Costin
ORCID: 0009-0005-4864-1311
"""

import numpy as np
from fractions import Fraction


class PredictorNeutrini:
    """Predictor pentru observabilele neutrinilor."""

    def __init__(self):
        self.M_scale = 0.313  # GeV

    # =========================================================
    # Unghiuri de amestec
    # =========================================================
    def sin2_theta_12(self):
        """sin^2(theta_12) = 43/140."""
        return 43 / 140

    def sin2_theta_23(self):
        """sin^2(theta_23) = 4/7."""
        return 4 / 7

    def sin2_theta_13(self):
        """sin^2(theta_13) = 3/137."""
        return 3 / 137

    # =========================================================
    # R = Delta m_31^2 / Delta m_21^2
    # =========================================================
    def R_predicted(self):
        """R = Delta m_31^2 / Delta m_21^2."""
        delta = 2 / 9
        r_sq = 103 / 35
        r = np.sqrt(r_sq)

        f = [1 + r * np.cos(delta + 2 * np.pi * i / 3) for i in range(3)]
        f_sorted = sorted(f)

        m = [fi**2 for fi in f_sorted]
        R = (m[2] - m[0]) / (m[1] - m[0])
        return R

    # =========================================================
    # Faza CP
    # =========================================================
    def delta_CP(self):
        """delta_CP = (1 + sqrt(2))/2."""
        return (1 + np.sqrt(2)) / 2

    # =========================================================
    # Masa m_1(nu)
    # =========================================================
    def m_1_neutrino(self):
        """m_1(nu) in meV."""
        return 0.046

    # =========================================================
    # Tabel complet
    # =========================================================
    def tabel(self):
        """Returneaza tabelul cu toate predictiile."""
        observat = {
            'sin^2 theta_12': (self.sin2_theta_12(), 0.307),
            'sin^2 theta_23': (self.sin2_theta_23(), 0.573),
            'sin^2 theta_13': (self.sin2_theta_13(), 0.0219),
            'R': (self.R_predicted(), 33.55),  # NuFit 6.0
            'delta_CP (rad)': (self.delta_CP(), 1.2),
            'm_1 (meV)': (self.m_1_neutrino(), None),
        }

        rezultate = []
        for name, (pred, obs) in observat.items():
            if obs is not None:
                err = abs(pred - obs) / obs * 100
            else:
                err = None
            rezultate.append({
                'observabil': name,
                'predictie': pred,
                'observat': obs,
                'eroare_pct': err
            })

        return rezultate

    def raport(self):
        """Raport complet."""
        print("=" * 60)
        print("PREDICTOR NEUTRINI — TEORIA N")
        print("=" * 60)
        print()

        tabel = self.tabel()
        print(f"{'Observabil':<20} {'Predictie':>12} {'Observat':>12} {'Err (%)':>10}")
        print("-" * 58)
        for r in tabel:
            obs_str = f"{r['observat']:.4f}" if r['observat'] is not None else "—"
            err_str = f"{r['eroare_pct']:.4f}" if r['eroare_pct'] is not None else "—"
            print(f"{r['observabil']:<20} {r['predictie']:>12.4f} "
                  f"{obs_str:>12} {err_str:>10}")

        print()
        print("Testabil:")
        print("  R = 33.28 → JUNO 2027+")
        print("  delta_CP = 1.207 rad → DUNE 2030+")
        print("  m_1(nu) = 0.046 meV → KATRIN")