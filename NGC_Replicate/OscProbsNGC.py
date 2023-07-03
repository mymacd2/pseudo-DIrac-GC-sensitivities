import numpy as np
import re
import matplotlib.pyplot as plt
import matplotlib



# Norms for the PMNS matrix squared:

u_e = [0, 0.674743, 0.302844, 0.0224125]
u_m = [0, 0.0946105, 0.360415, 0.544974]
u_t = [0, 0.230646, 0.33674,  0.432613]


# Effective distance traveled in 1oeV:
l_eff = 2.4685e20 * 5.06773093741 * 1e6

# Mass-difference squared (under assumption that all flavors have the same mass difference) in eV^2:
del_m2 = 0 

# Energy dist:
a = np.logspace(11, 13, num=2000)


# cos squared term:
osc = (np.cos((del_m2 * l_eff)/(4*a)))**2


# Define start and end flavor states:
ui = u_m
uf1 = u_e
uf2 = u_t
uf3 = u_m


prob1 = osc * ((ui[1]*uf1[1]) + (ui[2]*uf1[2]) + (ui[3]*uf1[3]))
prob2 = osc * ((ui[1]*uf2[1]) + (ui[2]*uf2[2]) + (ui[3]*uf2[3]))
prob3 = osc * ((ui[1]*uf3[1]) + (ui[2]*uf3[2]) + (ui[3]*uf3[3]))
prob4 = 1 - prob1 - prob2 - prob3

fig1, ax1 = plt.subplots()
µe, = ax1.plot(a, prob1)
µτ, = ax1.plot(a, prob2)
µµ, = ax1.plot(a, prob3)
µs, = ax1.plot(a, prob4)
ax1.set_xscale('log')
ax1.set_xticks([10**11, 10**12, 10**13])
ax1.set_xlabel(r"$E_{\nu}$ (eV)")
ax1.set_ylabel(r"$P(\nu_{e} \to \nu_{\alpha})$")
ax1.set_title(r"$\delta m^2 = 10^{-14}$ eV$^2$", loc="left")
ax1.set_title(r"$L_{eff} = 8$ kpc", loc="right")
ax1.legend([µe, µτ, µµ, µs], [r"$\nu_{e} \to \nu_{e}$", r"$\nu_{e} \to \nu_{\tau}$",r"$\nu_{e} \to \nu_{\mu}$",r"$\nu_{e} \to \nu_{s}$"])
plt.show()





