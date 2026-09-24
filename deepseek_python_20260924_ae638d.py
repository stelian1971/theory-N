"""
hadroni.py
==========
Predictor pentru mase hadronice in teoria N.

Autor: Stelian Costin
ORCID: 0009-0005-4864-1311
"""

import numpy as np
from fractions import Fraction


class PredictorHadroni:
    """Predictor pentru masele hadronilor."""

    def __init__(self, M_scale=0.313):
        self.M_scale = M_scale  # GeV

    # =========================================================
    # 13 mase de baza
    # =========================================================
    def masa(self, hadron):
        """Returneaza masa unui hadron (in GeV)."""
        coeficienti = {
            'pi': Fraction(4, 9),
            'K': Fraction(11, 7),
            'eta': Fraction(7, 4),
            'rho': Fraction(5, 2),
            'omega': Fraction(5, 2),
            'phi': Fraction(13, 4),
            'p': Fraction(3, 1),
            'n': Fraction(3, 1) + Fraction(1, 35),
            'Lambda': Fraction(3, 1) + Fraction(4, 7),
            'Sigma': Fraction(3, 1) + Fraction(4, 5),
            'Xi': Fraction(4, 1) + Fraction(1, 5),
            'Delta': Fraction(4, 1) - Fraction(1, 16),
            'Omega': None,  # formula speciala
        }

        if hadron == 'Omega':
            return self.masa_omega_minus()

        if hadron not in coeficienti:
            raise ValueError(f"Hadron necunoscut: {hadron}")

        coef = coeficienti[hadron]
        if coef is None:
            return None
        return float(coef) * self.M_scale

    def masa_proton(self):
        """Masa protonului."""
        return 3.0 * self.M_scale

    def masa_neutron(self):
        """Masa neutronului."""
        return (3.0 + 1/35) * self.M_scale

    def masa_omega_minus(self):
        """Masa barionului Omega- (sss)."""
        Tr_M = 3
        Tr_M2 = 7
        Tr_M6 = 199
        AF = 2
        coef = Tr_M + Tr_M2 / Tr_M + AF / Tr_M6
        return coef * self.M_scale

    # =========================================================
    # Toate cele 13 mase
    # =========================================================
    def tabel_13_mase(self):
        """Returneaza tabelul cu 13 mase si erorile."""
        observat = {
            'pi': 0.1396, 'K': 0.4937, 'eta': 0.5479,
            'rho': 0.7753, 'omega': 0.7827, 'phi': 1.0195,
            'p': 0.9383, 'n': 0.9396, 'Lambda': 1.1157,
            'Sigma': 1.1894, 'Xi': 1.3149, 'Delta': 1.2320,
            'Omega': 1.6724,
        }

        rezultate = []
        for hadron, obs in observat.items():
            pred = self.masa(hadron)
            err = abs(pred - obs) / obs * 100
            rezultate.append({
                'hadron': hadron,
                'predictie': pred,
                'observat': obs,
                'eroare_pct': err
            })

        return rezultate

    # =========================================================
    # 4 molecule barion+mezon
    # =========================================================
    def masa_molecula(self, m_barion, m_mezon):
        """Masa unei molecule barion+mezon."""
        E_binding = -self.M_scale / (2 * np.pi)
        return m_barion + m_mezon + E_binding

    def tabel_molecule(self):
        """Returneaza tabelul cu 4 molecule."""
        m_N = self.masa_proton()
        m_rho = self.masa('rho')
        m_Delta = self.masa('Delta')

        molecule = [
            ('N(1650)', 1.650, m_N, m_rho),
            ('N(1675)', 1.675, m_N, m_rho),
            ('N(1680)', 1.680, m_N, m_rho),
            ('Delta(1950)', 1.950, m_Delta, m_rho),
        ]

        rezultate = []
        for nume, obs, m_B, m_M in molecule:
            pred = self.masa_molecula(m_B, m_M)
            err = abs(pred - obs) / obs * 100
            rezultate.append({
                'nume': nume,
                'predictie': pred,
                'observat': obs,
                'eroare_pct': err
            })

        return rezultate

    # =========================================================
    # Statistici
    # =========================================================
    def statistici(self):
        """Returneaza statisticile complete."""
        tabel = self.tabel_13_mase()
        erori = [r['eroare_pct'] for r in tabel]

        return {
            'nr_hadroni': len(tabel),
            'eroare_medie': np.mean(erori),
            'eroare_max': np.max(erori),
            'eroare_min': np.min(erori),
        }

    def raport(self):
        """Raport complet."""
        print("=" * 60)
        print("PREDICTOR HADRONI — TEORIA N")
        print("=" * 60)
        print()

        tabel = self.tabel_13_mase()
        print(f"{'Hadron':<10} {'Predictie':>12} {'Observat':>12} {'Err (%)':>10}")
        print("-" * 48)
        for r in tabel:
            print(f"{r['hadron']:<10} {r['predictie']:>12.4f} "
                  f"{r['observat']:>12.4f} {r['eroare_pct']:>9.3f}")

        stats = self.statistici()
        print()
        print(f"Eroare medie: {stats['eroare_medie']:.3f}%")
        print(f"Eroare maxima: {stats['eroare_max']:.3f}%")