import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


import motion

from mpl_toolkits.mplot3d import Axes3D

def Select_system (system):
    if system == 'Win':
        font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)    
    elif system == 'Mac':
        font=FontProperties(fname='/System/Library/Fonts/PingFang.ttc',size=14)
    return font


def function (zz, t, U, Q, R, O, P, H, C, G, M, A, B, W, S, I, α, β, τ, γ, λ, θ, ρ, L):
    x, y, z = zz
    return np.array([x*(1 - x) * (y*((1-λ)*(U-Q) - (1-ρ)*R - (1+λ)*O + P + H) + θ*O*z + y*z*(θ*(I+P) - (1+θ)*ρ*R) - α*B),           
                     y*(1 - y) * (x*((1-ρ)*R - (1-γ)*C - (G - M) - β*L) + θ*(G-M)*z + x*z*((θ+β)*A - (1-θ)*(1-ρ)*τ*R - (1+θ)*γ*C) - (1-α)*B),            
                     z*(1 - z) * (x*y*(θ*(W-P) - (θ+β)*A - θ*(1-ρ)*τ*R + ρ*R + γ*C) - θ*O*x - θ*(G-M)*y + θ*(G-M+O+P-W) - S)])
    
def math_dxdydz (x, y, z, U, Q, R, O, P, H, C, G, M, A, B, W, S, I,α, β, τ, γ, λ, θ, ρ, L,length, densy):
    t = np.arange(0, length, densy)
    track = motion.motden(function, x, y, z, t, U, Q, R, O, P, H, C, G, M, A, B, W, S, I,α, β, τ, γ, λ, θ, ρ, L)
        
    return track, t

def show_data (track, t, length, dpi, x_str, y_str, fontsize, title, label,y_label_start, y_label_end, font):
    
    plt.figure (figsize = (8, 6),dpi = dpi)
    
    marker = ['-', '--', '-.', '*', '-']


    plt.plot (t, track[:, 0], marker[0], label =  label[0])
    plt.plot (t, track[:, 1], marker[1], label =  label[1])
    plt.plot (t, track[:, 2], marker[2], label =  label[2])

    
    
    plt.xlim(0, length, 0.05)
    plt.ylim (y_label_start, y_label_end)
   # plt.legend(prop =font, numpoints=0.5)
    plt.legend(prop =font)
    leg = plt.gca().get_legend()
    ltext = leg.get_texts()
    plt.setp(ltext, fontsize=16)
    
    
    plt.xlabel(x_str, fontproperties=font, fontsize = fontsize)
    plt.ylabel(y_str, fontproperties=font, fontsize = fontsize)
    plt.title (title, fontproperties=font, fontsize = fontsize)
    plt.grid ()
    plt.show()     