programa {
  funcao inicio() {
    //canetas preço
    inteiro troco,dinheiro,custo,canetas,result
    escreva("digite o valor pago: ")
    leia(dinheiro)
    escreva("digite o número de canetas compradas: ")
    leia(canetas)
    escreva("digite o troco recebido: ")
    leia(troco)
    custo=dinheiro-troco
    escreva(custo)
    result=custo/canetas
    escreva("calculando...")
    escreva("\no valor de cada caneta é de: ",result)

    
  }
}
