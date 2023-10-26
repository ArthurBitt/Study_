package br.com.Exercicios.POO.Pessoa;

public class Pessoa {
    String nome;
    int idade;

    void fazAniversário(){
        int aniversario = idade+=1;
        this.idade = aniversario;
    }
}
