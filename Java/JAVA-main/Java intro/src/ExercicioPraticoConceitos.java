import java.util.Scanner;

public class ExercicioPraticoConceitos {
    public static void main(String[] args) {
        int i = 0;
        int menu = 0;
        double saldo = 2500;
        double valor = 0;
        String token;
        String inicializar;
        Scanner sc = new Scanner(System.in);

        System.out.println("Deseja iniciar a aplicação S/N: ");
        inicializar = sc.nextLine().toUpperCase();
        while (inicializar.equals("S")){

            if (i != 4){

                System.out.println("Insira seu Token de acesso com 3 dígitos: [xxx] ");
                token = sc.nextLine();


                if (token.equals("abc")) {
                    System.out.println("""
                                                                
                            Token digitado corretamente!
                                                                
                            ...carregando aplicação
                                                                
                            """);

                    while (i != 4) {
                        System.out.println(String.format("""
                                                    
                                                    
                                *****************DADOS CLIENTE ****************
                                Cliente                     Arthur Bittencourt
                                Tipo da Conta               Conta Corrente
                                Saldo Disponível            %.2f    
                                ************************************************ 
                                                    
                                                    
                                """,saldo));


                        System.out.println("""
                                                        
                                                        
                                ********* MENU **********
                                1- Consultar Saldo
                                2- Depositar
                                3- Transferir
                                4- Sair
                                *************************
                                                        
                                                        
                                """);
                        i = sc.nextInt();
                            switch (i) {
                                case 1:
                                    System.out.println("...Consultando Saldo");
                                    System.out.println(String.format("%.2f", saldo));
                                    break;
                                case 2:
                                    System.out.println("valor a depositar: ");
                                    valor = sc.nextDouble();
                                    saldo += valor;
                                    System.out.println(String.format("Seu saldo atual é %.2f", saldo));
                                    break;
                                case 3:
                                    System.out.println("Valor da transferência: ");
                                    valor = sc.nextDouble();
                                    saldo -= valor;
                                    System.out.println(String.format("Seu saldo atual é %.2f", saldo));
                                    break;

                                case 4:
                                    System.out.println("...encerrando a aplicação ");
                                    break;

                                default:
                                    System.out.println("...opção inválida");
                                    break;

                            }//fim switch
                    }//fim while programa
                } else {
                    System.out.println("""
                            Token inválido
                            Reinicie a aplicação para uma nova tentativa de acesso
                                                                    
                            """);
                    break;
                }
            }else{
                break;
            }//fim validação entrada e saída
        }//fim while inicialização
    }//fim main
}//fim classe








