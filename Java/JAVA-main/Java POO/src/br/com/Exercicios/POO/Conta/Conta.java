package br.com.Exercicios.POO.Conta;
import java.util.Random;
public class Conta {

        //Variáveis Atributos
    String nomeTitular;
    int numConta;
    int numAgencia;
    double saldo = 0;
    Data dataAbertura;
    private static int  quantContas;
    private int identificador;

    public Conta(Data dataAbertura, String nomeTitular, int numeroConta, int numeroAgencia){
        Random rand = new Random();

        this.dataAbertura = dataAbertura;
        this.nomeTitular = nomeTitular;
        this.numConta = numeroAgencia;
        this.numAgencia = numeroAgencia;
        Conta.quantContas += 1;
        this.identificador = rand.nextInt();

    }
//getters e setters da classe
public int getIdentificador(){
        return this.identificador;
    }
public double getSaldo(){
        return this.saldo;
    }

public void setNomeTitular(String nomeTitular){
    this.nomeTitular = nomeTitular;

}

public static int getQuantContas() {
    return Conta.quantContas;
}

public double getRendimento(){
        double rendimento = this.saldo * 0.1;
        this.saldo += rendimento;
        return this.saldo;
    }




    //Métodos da Classe
    public double saca(double valor){
        this.saldo -= valor;
        return this.saldo;
    }

    public double deposita(double valor){
        this.saldo += valor;
        return this.saldo;
    }


    String recuperaDadosParaImpressao() {
        String dadosImpressos = String.format("""
                ********************************
                    Titular:          %s
                    Conta:            %d
                    Agência:          %d
                    Saldo:            %.2f
                    Data Abertura:    %s
                ********************************                       
                """, nomeTitular, numConta, numAgencia, saldo, Data.recuperaData());
        return dadosImpressos;

    }

}
