programa {
  funcao inicio() {
    cadeia dia,profe,trabalhar
    escreva("Bom Dia!!")
    escreva("\nque dia é hoje? ")
    leia(dia)
    escreva("Hoje é ",dia)
    se(dia == "segunda"){
    escreva("\nBora estudar!!")
    escreva("\nTemos muitos exercícios para hoje!!")
    
    }
    se(dia == "terça"){
      escreva("\nhoje não é dia de programar!!")
    }
    se(dia == "quarta"){
    escreva("\nhoje é dia de programar!!!")
    escreva("\nbora lá!!")

    }
    se(dia == "quinta"){
    escreva("\nquintou!!!")
    }
    se(dia == "sexta"){
    escreva("\nSEXTOUUU!!!!")
    escreva("\nhoje é dia de programar!!!")
    escreva("\nOBS: dia preferido da semana")
    }
    se(dia == "sábado"){
    escreva("\nsabadouuu!!")
    escreva("\nBorá pra expo")
    }
    se(dia == "domingo"){
    escreva("\nHoje é dia de ficar de boaa")
    }
    escreva("\no professor é legal? ")
    leia(profe)
    se(profe == "sim")
    escreva("verdade man")
    se(profe == "não")
    escreva("mentira, ele é legal sim")
    escreva("\nHoje é dia de trabalhar? ")
    leia(trabalhar)
    se(trabalhar == "sim")
    escreva("que pena, bora lá!")
    senao escreva("Aeee, vou descançar!!")
  }
}
