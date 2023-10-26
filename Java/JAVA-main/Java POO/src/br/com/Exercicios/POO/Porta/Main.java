package br.com.Exercicios.POO.Porta;

public class Main {
    public static void main(String[] args) {
        Porta porta1 = new Porta();

        porta1.cor = "Marrom";
        porta1.dimensaoX = 30.0;
        porta1.dimensaoY = 280.0;
        porta1.dimensaoZ = 0.4;


        porta1.pinta("Preta");

        if (porta1.estaAberta()){
            System.out.println("Esta Aberta, portanto a irei fechar para não bater.");
            porta1.fecha();
        }else{
            System.out.println("Esta fechada!");
        }


    }
}