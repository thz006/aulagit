programa {
  funcao inicio() {
    cadeia dia,profe,trabalhar
    escreva("Bom Dia!!")
    escreva("\nque dia � hoje? ")
    leia(dia)
    escreva("Hoje � ",dia)
    se(dia == "segunda"){
    escreva("\nBora estudar!!")
    escreva("\nTemos muitos exerc�cios para hoje!!")
    
    }
    se(dia == "ter�a"){
      escreva("\nhoje n�o � dia de programar!!")
    }
    se(dia == "quarta"){
    escreva("\nhoje � dia de programar!!!")
    escreva("\nbora l�!!")

    }
    se(dia == "quinta"){
    escreva("\nquintou!!!")
    }
    se(dia == "sexta"){
    escreva("\nSEXTOUUU!!!!")
    escreva("\nhoje � dia de programar!!!")
    escreva("\nOBS: dia preferido da semana")
    }
    se(dia == "s�bado"){
    escreva("\nsabadouuu!!")
    escreva("\nBor� pra expo")
    }
    se(dia == "domingo"){
    escreva("\nHoje � dia de ficar de boaa")
    }
    escreva("\no professor � legal? ")
    leia(profe)
    se(profe == "sim")
    escreva("verdade man")
    se(profe == "n�o")
    escreva("mentira, ele � legal sim")
    escreva("\nHoje � dia de trabalhar? ")
    leia(trabalhar)
    se(trabalhar == "sim")
    escreva("que pena, bora l�!")
    senao escreva("Aeee, vou descan�ar!!")
  }
}
