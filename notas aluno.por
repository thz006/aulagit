programa {
  funcao inicio() {
    //notas aluno
    real n1,n2,n3,media
    escreva("digite a primeira nota: ")
    leia(n1)
    escreva("digite a segunda nota: ")
    leia(n2)
    escreva("digite a terceira nota: ")
    leia(n3)
    escreva("Calculando média...")
    media=(n1+n2+n3)/3
    escreva("\nsua média é: ",media)
    se(media >= 7){
      escreva("\nVocê foi aprovado")
    }
    senao escreva("\nVocê foi reprovado, si fudeu kkkk")

  }
}
