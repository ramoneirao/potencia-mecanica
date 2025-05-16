# Funções para calcular a potência mecânica

def gattinoniS(FR, Vt, Ppico, Pplato, PEEP):
    """
    Calcula a potência mecânica usando a fórmula de Gattinoni.

    Parâmetros:
    FR (float): Frequência respiratória (em ciclos por minuto).
    Vt (float): Volume corrente (em litros).
    Ppico (float): Pressão de pico (em cmH2O).
    Pplato (float): Pressão de platô (em cmH2O).
    PEEP (float): Pressão expiratória final positiva (em cmH2O).

    Retorna:
    float: Potência mecânica em watts.
    """
    return print(0.098 * FR * Vt * (Ppico - 0.5 * (PEEP - Pplato))) 
