programa {
  funcao inicio() {
    //canetas pre�o
    inteiro troco,dinheiro,custo,canetas,result
    escreva("digite o valor pago: ")
    leia(dinheiro)
    escreva("digite o n�mero de canetas compradas: ")
    leia(canetas)
    escreva("digite o troco recebido: ")
    leia(troco)
    custo=dinheiro-troco
    escreva(custo)
    result=custo/canetas
    escreva("calculando...")
    escreva("\no valor de cada caneta � de: ",result)

    
  }
}
