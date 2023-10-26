package br.com.Exercicios.POO.Pessoa;

public class Main {
    public static void main(String[] args) {
        Pessoa p1 = new Pessoa();

        p1.idade = 20;
        p1.fazAniversário();
        p1.fazAniversário();
        p1.fazAniversário();

        System.out.println(p1.idade);

    }
}