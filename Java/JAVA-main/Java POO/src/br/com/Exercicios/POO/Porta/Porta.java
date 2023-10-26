package br.com.Exercicios.POO.Porta;

public class Porta {
    boolean aberta = true;
    String cor;
    double dimensaoX;
    double dimensaoY;
    double dimensaoZ;

    void fecha(){
        this.aberta = false;
        System.out.println("Porta fechada!");
    }

    void pinta(String cor){
        String novaCor = cor;
        this.cor = novaCor;
        System.out.println(String.format("A porta foi pintada da cor %s",this.cor));
    }

    boolean estaAberta(){

        if (aberta == true){
            return true;

        }else{
            return false;
        }
    }

}