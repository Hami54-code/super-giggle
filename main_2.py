
import source_2

if __name__ == "__main__":

    # 相关参数
    U = 15
    Q = 4
    R = 12
    O = 8
    P = 4
    H = 2
    I = 5
    
    C = 5
    G = 7
    M = 3
    A = 2
    B = 7
    W = 12
    S = 2.5
    
    L = 6
    
    α = 0.6
    β = 0.2
    τ = 0.2
    γ = 0.4
    λ = 0.3
    θ = 0.5
    ρ = 0.3

    
    # 起始值
    x = 0.5
    y = 0.5
    z = 0.5
    
    # 迭代总数
    length = 25
    # 时间步长
    densy  = 0.05
    
    # 图片像素大小
    dpi = 80
    # 横轴和纵轴标注以及标题
    x_str = "Time"
    y_str = "Probability"
    title = ""
    label = ['x', 'y', 'z']
    # y轴的起始点
    y_label_start = -.1
    y_label_end   = 1.1
    # 字体大小
    fontsize = 16
    """
        如果是Mac : system = 'Mac'
    """
    system = 'Win'

    font = source_2.Select_system (system)

    track, t = source_2.math_dxdydz (x, y, z, U, Q, R, O, P, H, C, G, M, A, B, W, S, I,α, β, τ, γ, λ, θ, ρ, L, length, densy)  
    source_2.show_data (track, t, length, dpi, x_str, y_str, fontsize, title, label,y_label_start, y_label_end, font)
 
    
    