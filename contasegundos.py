def main():
    seg = int(input("Por favor, entre com o número de segundos que deseja converter: "))
    dias = (seg//86400)
    seg = (seg%86400)
    horas = (seg//3600)
    seg = seg%3600
    minutos = seg//60
    seg = seg%60
    
    print(dias,"dias,",horas,"horas,",minutos,"minutos e",seg,"segundos.")
    
main()
