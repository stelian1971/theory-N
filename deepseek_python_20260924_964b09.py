from teoria_N import StructuraN, PredictorHadroni, PredictorNeutrini

# Structura
N = StructuraN()
print(N.spectru_pell())      # {1+sqrt(2), 1, 1-sqrt(2)}
print(N.urme(8))             # [3, 3, 7, 15, 35, 83, 199, 479]

# Hadroni
h = PredictorHadroni()
print(h.masa_proton())       # 0.938 GeV
print(h.masa_omega_minus())  # 1.6725 GeV

# Neutrini
nu = PredictorNeutrini()
print(nu.R_predicted())      # 33.28
print(nu.delta_CP())         # 1.207 rad