programa {
  funcao inicio() {
    //estoque empresa //estoque=sant + ent- sd
    inteiro estoq,sant,ent,sd
    escreva("Bem Vindo ao calculador de estoque")
    escreva("\ndigite o estoque do final do mês anterior: ")
    leia(sant)
    escreva("digite a quantidade que foi comprada no mês atual: ")
    leia(ent)
    escreva("digite a quantidade que foi vendida no mês atual: ")
    leia(sd)
    escreva("calculando...")
    estoq=sant+ent-sd
    escreva("\n o estoque atual desse produto é de: ",estoq," unidades")

  }
}
