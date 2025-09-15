# Gerenciamento de Instâncias AWS EC2 com Python

Este repositório serve como um material de apoio para a automação do ciclo de vida de instâncias EC2 na AWS usando **Python** e a biblioteca **Boto3**.


---

## 🚀 Como Usar

### 1. Pré-requisitos

Antes de começar, certifique-se de ter os seguintes itens:

* **Conta da AWS com permissões:** É essencial ter um usuário IAM com acesso programático e permissões para gerenciar instâncias EC2.
* **AWS CLI configurado:** Instale e configure a AWS CLI em sua máquina para que o Boto3 possa encontrar suas credenciais.
    ```bash
    aws configure
    ```
* **Python instalado:** Certifique-se de ter o Python 3.x em sua máquina.
* **Chave EC2:** Você precisará de uma chave de par (`.pem`) para criar instâncias. Se ainda não tiver uma, crie-a no console da AWS.

### 2. Configuração do Projeto

1.  **Clone este repositório** para a sua máquina local.
    ```bash
    git clone [https://github.com/hsin91/AWS-EC2-Management-with-Python.git](https://github.com/hsin91/AWS-EC2-Management-with-Python.git)
    cd AWS-EC2-Management-with-Python
    ```
2.  **Instale a dependência Boto3:**
    ```bash
    pip install -r requirements.txt
    ```

### 3. Usando o Script

O script principal, `gerenciar_ec2.py`, contém funções para gerenciar o ciclo de vida das instâncias. Você pode usá-las descomentando a função desejada na seção `if __name__ == "__main__":`.

**⚠️ Importante:**
* **`AMI_ID`:** Substitua o `ami-053b0d53c279acc91` por uma AMI válida na sua região.
* **`KEY_NAME`:** Substitua `nome-da-sua-chave` pelo nome da sua chave EC2.
* **IDs de Instância:** Para parar ou terminar uma instância, você deve substituir o ID de exemplo (`i-0123456789abcdef0`) pelo ID da sua instância.

---

### Funções Disponíveis:

* **`criar_instancia()`:** Cria e inicia uma nova instância EC2.
* **`listar_instancias()`:** Exibe o ID e o estado de todas as suas instâncias.
* **`parar_instancia()`:** Põe uma instância em estado de parada.
* **`terminar_instancia()`:** Exclui permanentemente uma instância (não pode ser revertido).

---

Espero que este material seja útil para os seus estudos e projetos futuros!
