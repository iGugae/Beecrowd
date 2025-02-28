import math

def calcular_area(x,y):
    area = x * y   

    return area

def construcao(area,porcent):
    porcent = round(porcent/100, 2)
    percentual = math.floor(math.sqrt(math.floor(area / porcent)))

    return percentual

def main():    
    while True:
        try:
            A, B, C = input().split()
            casa_x = int(A)
            casa_y = int(B)
            porcentagem = int(C)
        
            area = calcular_area(casa_x,casa_y)
            lado = construcao(area,porcentagem)

            print(lado)

        except ValueError:
            break

if __name__ == "__main__":
    main()
