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
    escreva("Calculando m�dia...")
    media=(n1+n2+n3)/3
    escreva("\nsua m�dia �: ",media)
    se(media >= 7){
      escreva("\nVoc� foi aprovado")
    }
    senao escreva("\nVoc� foi reprovado, si fudeu kkkk")

  }
}
